from collections import defaultdict
from datetime import datetime
from io import BytesIO
from pathlib import Path
# from fsspec import Callback
import requests

import ipyvuetify as v
import numpy as np
from astropy.io import fits
from cosmicds.phases import Story
from cosmicds.registries import story_registry
from cosmicds.utils import API_URL, RepeatedTimer
from echo import DictCallbackProperty, CallbackProperty
from echo.callback_container import CallbackContainer
from glue.core import Data
from glue.core.component import CategoricalComponent, Component
from glue.core.data_factories.fits import fits_reader
from glue.core.subset import CategorySubsetState

from .data_management import BEST_FIT_SUBSET_LABEL, CLASS_DATA_LABEL, CLASS_SUMMARY_LABEL, SDSS_DATA_LABEL, STATE_TO_MEAS, STATE_TO_SUMM, \
    STUDENT_DATA_LABEL, STUDENT_MEASUREMENTS_LABEL, BEST_FIT_GALAXY_NAME
from .utils import H_ALPHA_REST_LAMBDA, HUBBLE_ROUTE_PATH, age_in_gyr_simple, fit_line

from .data_management import EXAMPLE_GALAXY_DATA, EXAMPLE_GALAXY_MEASUREMENTS, EXAMPLE_GALAXY_STUDENT_DATA, EXAMPLE_GALAXY_SEED_DATA
from .utils import MG_REST_LAMBDA

@story_registry(name="hubbles_law")
class HubblesLaw(Story):
    title = CallbackProperty("Hubble's Law")
    measurements = DictCallbackProperty({})
    calculations = DictCallbackProperty({})
    validation_failure_counts = DictCallbackProperty({})
    has_best_fit_galaxy = CallbackProperty(False)

    measurement_keys = [
        "obs_wave_value",
        "rest_wave_value",
        "velocity_value",
        "est_dist_value",
        "ang_size_value",
        "ra",
        "decl",
        "name",
        "z",
        "type",
        "element",
        "student_id",
        "last_modified"
    ]
    summary_keys = [
        "hubble_fit_value",
        "age_value"
    ]
    name_ext = ".fits"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._set_theme()

        self._on_timer_cbs = CallbackContainer()

        self.add_callback('has_best_fit_galaxy', self.update_student_data)

        # Load data needed for Hubble's Law
        data_dir = Path(__file__).parent / "data"
        output_dir = data_dir / "hubble_simulation" / "output"

        # Load some simulated measurements as summary data
        self.app.load_data([
            f"{dataset}.csv" for dataset in (
                data_dir / "galaxy_data",
                data_dir / "Hubble 1929-Table 1",
                data_dir / "HSTkey2001",
                data_dir / "dummy_student_data",
                output_dir / "HubbleData_ClassSample",
                output_dir / "HubbleData_All",
                output_dir / "HubbleSummary_ClassSample",
                output_dir / "HubbleSummary_Students",
                output_dir / "HubbleSummary_Classes",
            )
        ])

        # Load in the galaxy data
        galaxies = requests.get(f"{API_URL}/{HUBBLE_ROUTE_PATH}/galaxies?types=Sp").json()
        galaxies_dict = { k : [x[k] for x in galaxies] for k in galaxies[0] }
        galaxies_dict["name"] = [x[:-len(self.name_ext)] for x in galaxies_dict["name"]]
        self.data_collection.append(Data(
            label=SDSS_DATA_LABEL,
            **galaxies_dict
        ))

        # Load in the overall data
        all_json = requests.get(f"{API_URL}/{HUBBLE_ROUTE_PATH}/all-data").json()
        all_measurements = all_json["measurements"]
        for measurement in all_measurements:
            measurement.update(measurement["galaxy"])
        all_student_summaries = all_json["studentData"]
        all_class_summaries = all_json["classData"]
        all_data = Data(
            label="all_measurements",
            **{ STATE_TO_MEAS.get(k, k) : [x[k] for x in all_measurements] for k in all_measurements[0] }
        )
        HubblesLaw.prune_none(all_data)
        self.data_collection.append(all_data)

        all_student_summ_data = self.data_from_summaries(all_student_summaries, label="all_student_summaries", id_key="student_id")
        all_class_summ_data = self.data_from_summaries(all_class_summaries, label="all_class_summaries", id_key="class_id")
        self.data_collection.append(all_student_summ_data)
        self.data_collection.append(all_class_summ_data)
        for comp in ['age', 'H0']:
            self.app.add_link(all_student_summ_data, comp, all_class_summ_data, comp)

        # Compose empty data containers to be populated by user
        self.student_cols = ["name", "ra", "decl", "z", "type", "measwave",
                         "restwave", "student_id", "velocity", "distance",
                         "element", "angular_size"]
        self.categorical_cols = ['name', 'element', 'type']
        student_measurements = Data(label=STUDENT_MEASUREMENTS_LABEL)
        class_data = Data(label=CLASS_DATA_LABEL)
        student_data = Data(label=STUDENT_DATA_LABEL)
        for col in self.student_cols:
            categorical = col in self.categorical_cols
            ctype = CategoricalComponent if categorical else Component
            meas_comp = ctype(np.array([]))
            data = ['X'] if categorical else [0]
            student_data_comp = ctype(np.array(data))
            class_data_comp = ctype(np.array(data))
            student_measurements.add_component(meas_comp, col)
            student_data.add_component(student_data_comp, col)
            class_data.add_component(class_data_comp, col)

        self.data_collection.append(student_measurements)
        self.data_collection.append(student_data)
        self.data_collection.append(class_data)
        for comp in ['distance', 'velocity', 'student_id']:
            self.app.add_link(student_measurements, comp, student_data, comp)
            self.app.add_link(student_measurements, comp, class_data, comp)

        class_summary_cols = ["student_id", "H0", "age"]
        class_summary_data = Data(label=CLASS_SUMMARY_LABEL)
        for col in class_summary_cols:
            component = Component(np.array([0]))
            class_summary_data.add_component(component, col)
        self.data_collection.append(class_summary_data)
        
        # create example galaxy data sets
        # example_galaxy_measurements
        # example_galaxy_student_data
        # SINGLE_GALAXY_SEED_DATA
        example_galaxy_meas = self.setup_example_galaxy()
        for comp in ['distance', 'velocity', 'student_id']:
            self.app.add_link(student_measurements, comp, example_galaxy_meas, comp)
            self.app.add_link(student_measurements, comp, example_galaxy_meas, comp)
        # Make all data writeable
        for data in self.data_collection:
            HubblesLaw.make_data_writeable(data)

        self.class_last_modified = None
        self.class_data_timer = RepeatedTimer(5, self._on_timer)
        self.class_data_timer.start()

    def _on_timer(self):
        self.fetch_class_data()
        for cb in self._on_timer_cbs:
            cb()

    def _set_theme(self):
        v.theme.dark = True
        v.theme.themes.dark.primary = 'colors.blue.darken4'   # Overall theme & header bars
        v.theme.themes.light.primary = 'colors.blue.darken3'
        v.theme.themes.dark.secondary = 'colors.cyan.darken3'    # Headers on dialogs & buttons that pop up dialogs
        v.theme.themes.light.secondary = 'colors.cyan.darken4'
        v.theme.themes.dark.accent = 'colors.amber.accent3'   # Next/Back buttons
        v.theme.themes.light.accent = 'colors.amber.accent2'
        v.theme.themes.dark.error = 'colors.pink.lighten1'  # Team insider buttons that will not appear for user
        v.theme.themes.light.error = 'colors.indigo.lighten2'
        v.theme.themes.dark.info = 'colors.deepOrange.darken4'  # Instruction scaffolds & viewer highlights
        v.theme.themes.light.info = 'colors.deepOrange.lighten1'
        v.theme.themes.dark.success = 'colors.green.accent3'   # Actions and interactions
        v.theme.themes.light.success = 'colors.green.accent3'
        v.theme.themes.dark.warning = 'colors.deepOrange.accent4' # Unallocated (maybe viewer highlights?)
        v.theme.themes.light.warning = 'colors.deepOrange.accent4'
        #Alt Palette 1:  Y:FFBE0B, O:FB5607, Pi:FF006E, Pu:8338EC, Bl:3A86FF, LiBl:619EFF


    def load_spectrum_data(self, name, gal_type):
        if not name.endswith(self.name_ext):
            filename = name + self.name_ext
        else:
            filename = name
            name = name[:-len(self.name_ext)]

        # Don't load data that we've already loaded
        dc = self.data_collection
        if name not in dc:
            data_name = name + '[COADD]'
            type_folders = { "Sp" : "spiral", "E" : "elliptical", "Ir" : "irregular" }
            folder = type_folders[gal_type]
            url = f"{API_URL}/{HUBBLE_ROUTE_PATH}/spectra/{folder}/{filename}"
            response = requests.get(url)
            f = BytesIO(response.content)
            f.name = name
            hdulist = fits.open(f)
            data = next((d for d in fits_reader(hdulist) if d.label == data_name), None)
            if data is None:
                return
            data.label = name
            dc.append(data)
            data['lambda'] = 10 ** data['loglam']
            HubblesLaw.make_data_writeable(data)
        return dc[name]

    def _best_fit_galaxy(self, measurements):
        distances = measurements["distance"]
        velocities = measurements["velocity"]
        line = fit_line(distances, velocities)
        if line is None:
            return None

        dmin = min(distances)
        dmax = max(distances)
        d = round(0.5 * (dmin + dmax))
        v = round(line.slope.value * d)
        return {
            "name": BEST_FIT_GALAXY_NAME,
            "distance": d,
            "velocity": v,
            "ra": 0, "decl": 0,
            "type": "Sp",
            "measwave": 0,
            "restwave": H_ALPHA_REST_LAMBDA,
            "z": 0, "angular_size": 0,
            "element": "H-α",
            "student_id": self.student_user["id"],
            "last_modified": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def setup_example_galaxy(self):
        """
        Load in the example galaxy data and seed data for the example galaxy
        Create empty Data for student measurements of example galaxy
        """
        # Load in the galaxy data
        example_galaxy_data = requests.get(f"{API_URL}/{HUBBLE_ROUTE_PATH}/sample-galaxy").json()
        example_galaxy_data = { k : [example_galaxy_data[k]] for k in example_galaxy_data }
        example_galaxy_data['galaxy_id'] = [name.replace('.fits','') for name in example_galaxy_data['name']]
        self.data_collection.append(Data(label=EXAMPLE_GALAXY_DATA, **example_galaxy_data))
        
        # load the seed data for the example galaxy to populate
        # parse the json into a dictionary of arrays
        # create glue Data object [each dictionary item becomes a component]
        example_galaxy_seed_data = requests.get(f"{API_URL}/{HUBBLE_ROUTE_PATH}/sample-measurements").json()
        example_galaxy_seed_data = {k: np.array([record[k] for record in example_galaxy_seed_data]) for k in example_galaxy_seed_data[0]}
        good = example_galaxy_seed_data['velocity_value'] != None
        example_galaxy_seed_data = {k: np.array(v)[good] for k,v in example_galaxy_seed_data.items()}
        for k in ['velocity_value']: #, 'ang_size_value','obs_wave_value','rest_wave_value','est_dist_value']:
            example_galaxy_seed_data[k] = np.array(example_galaxy_seed_data[k], dtype = type(example_galaxy_seed_data[k][0]))
        example_galaxy_seed_data = Data(label=EXAMPLE_GALAXY_SEED_DATA, **example_galaxy_seed_data)
        
        self.data_collection.append(example_galaxy_seed_data)
        
        
        # Create empty Data for student measurements of example galaxy
        single_gal_student_cols = ["id", "name", "ra", "decl", "z", "type", "measwave",
                        "restwave", "student_id", "velocity", "distance",
                        "element", "angular_size", "measurement_number"]
        # empty_record = {x: np.array([], dtype='float64') for x in single_gal_student_cols}
        empty_record = {x : ['X'] if x in ['id', 'element', 'type', 'name', 'measurement_number'] else [0] 
                for x in single_gal_student_cols}
        for col in ['name', 'element', 'type','ra','decl','z']:
            empty_record[col] = example_galaxy_data[col]
        empty_record['restwave'] = [H_ALPHA_REST_LAMBDA] if ('H' in example_galaxy_data['element'][0]) else [MG_REST_LAMBDA]
        empty_record['measurement_number'] = ['first']
        empty_record['measurement_number'] = np.asarray(empty_record['measurement_number'], dtype = ('<U6'))
        example_galaxy_measurements = Data(
            label=EXAMPLE_GALAXY_MEASUREMENTS,
            **empty_record)

        
        # categorical_cols = ['id', 'element', 'type', 'name', 'measurement_number']
        # example_galaxy_measurements = Data(label=EXAMPLE_GALAXY_MEASUREMENTS)
        # example_galaxy_student_data = Data(label=EXAMPLE_GALAXY_STUDENT_DATA)
        # for col in single_gal_student_cols:
        #     categorical = col in categorical_cols
        #     ctype = CategoricalComponent if categorical else Component
        #     meas_comp = ctype(np.array([]))
        #     data = ['X'] if categorical else [0]
        #     student_data_comp = ctype(np.array(data))
        #     # class_data_comp = ctype(np.array(data))
        #     example_galaxy_measurements.add_component(meas_comp, col)
        #     example_galaxy_student_data.add_component(student_data_comp, col)
        #     # example_galaxy_class_data.add_component(class_data_comp, col)
        
        # example_galaxy_measurements.append(empty_record)
        # self.data_collection.append(example_galaxy_student_data)
        self.data_collection.append(example_galaxy_measurements)

        self.app.add_link(example_galaxy_seed_data, 'student_id', example_galaxy_measurements, 'student_id')
        self.app.add_link(example_galaxy_seed_data, 'est_dist_value', example_galaxy_measurements, 'distance')
        self.app.add_link(example_galaxy_seed_data, 'velocity_value', example_galaxy_measurements, 'velocity')
        self.app.add_link(example_galaxy_seed_data, 'measurement_number', example_galaxy_measurements, 'measurement_number')
        self.app.add_link(example_galaxy_seed_data, 'ang_size_value', example_galaxy_measurements, 'angular_size')
        
        return example_galaxy_measurements


    def update_data(self, label, new_data):
        dc = self.data_collection
        if label in dc:
            data = dc[label]
            data.update_values_from_data(new_data)
            data.label = label
        else:
            main_comps = [x.label for x in new_data.main_components]
            components = { col: list(new_data[col]) for col in main_comps }
            data = Data(label=label, **components)
            HubblesLaw.make_data_writeable(data) 
            dc.append(data)

    def update_student_data(self, *args):
        dc = self.data_collection
        meas_data = dc[STUDENT_MEASUREMENTS_LABEL]
        df = meas_data.to_dataframe()
        df = df[df['distance'].notna() & \
                df['velocity'].notna() & \
                df['angular_size'].notna()]
        df["name"] = df["name"].astype(np.dtype(str))
        main_components = [x.label for x in meas_data.main_components]
        components = { col: list(df[col]) for col in main_components }
        if not all(len(v) > 0 for v in components.values()):
            return

        # Add the best-fit galaxy, if appropriate
        if self.has_best_fit_galaxy:
            bfg = self._best_fit_galaxy(components)
            for col, data in components.items():
                data.append(bfg.get(col, None))

        new_data = Data(label=STUDENT_DATA_LABEL)
        for col, data in components.items():
            categorical = col in self.categorical_cols
            ctype = CategoricalComponent if categorical else Component
            comp = ctype(np.array(data))
            new_data.add_component(comp, col)
        
        student_data = dc[STUDENT_DATA_LABEL]
        student_data.update_values_from_data(new_data)
        HubblesLaw.make_data_writeable(student_data)

        # Make sure that the best-fit galaxy subset is correct
        if self.has_best_fit_galaxy:
            c = student_data.get_component("name")
            indices = np.where(c.labels == bfg["name"])[0]
            codes = c.codes[indices]
            subset_state = CategorySubsetState(student_data.id["name"], codes)
            subset = next((s for s in student_data.subsets if s.label == BEST_FIT_SUBSET_LABEL), None)
            if subset is not None:
                subset.subset_state = subset_state
            else:
                student_data.new_subset(label=BEST_FIT_SUBSET_LABEL,
                                                 subset=subset_state,
                                                 color="blue",
                                                 alpha=1,
                                                 markersize=10)
                

    @staticmethod
    def prune_none(data):
        keep = set()
        for i in range(data.size):
            if all(data[comp][i] is not None for comp in data.main_components):
                keep.add(i)

        pruned_components = { comp.label: [data[comp][x] for x in keep] for comp in data.main_components }
        pruned = Data(label=data.label, **pruned_components)
        data.update_values_from_data(pruned)

    @staticmethod
    def make_data_writeable(data):
        for comp in data.main_components:
            data[comp.label].setflags(write=True)

    def galaxy_info(self, galaxy_ids):
        sdss = self.data_collection[SDSS_DATA_LABEL]
        indices = [i for i in range(sdss.size) if sdss['id'][i] in galaxy_ids]
        components = [x for x in sdss.main_components if x.label != 'id']
        return { sdss['id'][index]: { comp.label: sdss[comp][index] for comp in components } for index in indices }

    def data_from_measurements(self, measurements):
        for measurement in measurements:
            measurement.update(measurement.get("galaxy", {}))
        components = { STATE_TO_MEAS.get(k, k) : [measurement.get(k, None) for measurement in measurements] for k in self.measurement_keys }

        for i, name in enumerate(components["name"]):
            if name.endswith(self.name_ext):
                components["name"][i] = name[:-len(self.name_ext)]
        return Data(**components)

    def data_from_summaries(self, summaries, id_key=None, label=None):
        components = { STATE_TO_SUMM.get(k, k) : [summary.get(k, None) for summary in summaries] for k in self.summary_keys }
        if id_key is not None:
            ids = [summary.get(id_key, None) for summary in summaries]
            ids = [x for x in ids if x is not None]
            components.update({ id_key: ids})

        data = Data(**components)
        if label is not None:
            data.label = label
        return data

    def fetch_measurements(self, url):
        response = requests.get(url)
        res_json = response.json()
        return res_json["measurements"]

    def fetch_measurement_data_and_update(self, url, label, prune_none=False, make_writeable=False, check_update=None, callbacks=None):
        measurements = self.fetch_measurements(url)
        need_update = check_update is None or check_update(measurements)
        if not need_update:
            return None
        new_data = self.data_from_measurements(measurements)
        new_data.label = label
        if prune_none:
            HubblesLaw.prune_none(new_data)
        data = self.data_collection[label]
        data.update_values_from_data(new_data)
        if make_writeable:
            HubblesLaw.make_data_writeable(data)

        if callbacks is not None:
            for cb in callbacks:
                cb()

        return new_data

    def update_summary_data(self, measurements, summ_label, id_field):
        dists = defaultdict(list)
        vels = defaultdict(list)
        d = measurements["distance"]
        v = measurements["velocity"]
        components = {}
        ids = set()
        for i in range(measurements.size):
            id_num = measurements[id_field][i]
            ids.add(id_num)
            dists[id_num].append(d[i])
            vels[id_num].append(v[i])
        
        hubbles = []
        ages = []
        for id_num in ids:
            d = dists[id_num]
            v = vels[id_num]
            line = fit_line(d, v)
            h0 = line.slope.value
            hubbles.append(h0)
            ages.append(age_in_gyr_simple(h0))

        components = dict(hubble=hubbles, age=ages)
        components[id_field] = list(ids)
        new_data = Data(label=summ_label, **components)

        data = self.data_collection[summ_label]
        data.update_values_from_data(new_data)

    def fetch_student_data(self):
        student_meas_url = f"{API_URL}/{HUBBLE_ROUTE_PATH}/measurements/{self.student_user['id']}"
        self.fetch_measurement_data_and_update(student_meas_url, STUDENT_MEASUREMENTS_LABEL, make_writeable=True)
        self.update_student_data()

    def on_timer(self, cb):
        self._on_timer_cbs.append(cb)

    def fetch_class_data(self):
        #print("Fetching class data")
        def check_update(measurements):
            #print(sorted([[x["student_id"], x["last_modified"]] for x in measurements], key=lambda x: x[1], reverse=True)[0])
            last_modified = max([datetime.fromisoformat(x["last_modified"][:-1]) for x in measurements], default=None)
            #print(self.class_last_modified)
            #print(last_modified)
            # if not (self.class_last_modified is None or last_modified is None):
            #     print(last_modified > self.class_last_modified)
            need_update = self.class_last_modified is None or last_modified is None or last_modified > self.class_last_modified
            if need_update:
                self.class_last_modified = last_modified
            #print("Do we need an update? ", need_update)
            return need_update
        class_data_url = f"{API_URL}/{HUBBLE_ROUTE_PATH}/stage-3-data/{self.student_user['id']}/{self.classroom['id']}"
        updated = self.fetch_measurement_data_and_update(class_data_url, CLASS_DATA_LABEL, prune_none=True, check_update=check_update)
        if updated is not None:
            self.update_summary_data(updated, CLASS_SUMMARY_LABEL, "student_id")

    def setup_for_student(self, app_state):
        super().setup_for_student(app_state)
        if self.student_user["id"] in range(2989, 3018):
            print("Warning! You are using the ID of a beta test student.")
            app_state.update_db = False
        self.fetch_student_data()
        self.fetch_class_data()
