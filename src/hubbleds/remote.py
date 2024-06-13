from cosmicds.utils import API_URL
from cosmicds.state import GLOBAL_STATE
from .utils import HUBBLE_ROUTE_PATH
from .data_models.student import student_data, StudentMeasurement
from contextlib import closing
from io import BytesIO
from astropy.io import fits
from .state import LOCAL_STATE
import datetime


class DatabaseAPI:
    @staticmethod
    def get_measurements():
        url = f"{API_URL}/{HUBBLE_ROUTE_PATH}/measurements/{GLOBAL_STATE.student.id.value}"
        r = GLOBAL_STATE.request_session.get(url)
        res_json = r.json()

        measurements = []

        for measurement in res_json["measurements"]:
            meas_dict = {}

            for k, v in measurement.items():
                if not (k.endswith("_value") or k == "galaxy"):
                    continue

                meas_dict[k.replace("_value", "")] = v

                if k != "galaxy":
                    continue

                gal_dict = {}

                for gk, gv in v.items():
                    if gk in ["galaxy_id", "id"]:
                        gk = "id"
                        gv = str(gv)

                    gal_dict[gk] = gv

                # TODO: This is duplicated with the `_load_spectrum` from the
                #  component state -- revisit and unify!
                gal_type = gal_dict["type"]
                gal_name = gal_dict["name"]
                folder = {"Sp": "spiral", "E": "elliptical", "Ir": "irregular"}.get(
                    gal_type
                )

                response = GLOBAL_STATE.request_session.get(
                    f"{API_URL}/{HUBBLE_ROUTE_PATH}/spectra/{folder}/{gal_name}"
                )

                with closing(BytesIO(response.content)) as f:
                    f.name = gal_name

                    with fits.open(f) as hdulist:
                        data = hdulist["COADD"].data if "COADD" in hdulist else None

                if data is None:
                    print("No extension named 'COADD' in spectrum fits file.")
                    return

                spec_data = dict(
                    name=gal_name,
                    wave=10 ** data["loglam"],
                    flux=data["flux"],
                    ivar=data["ivar"],
                )

                gal_dict["spectrum"] = spec_data

                meas_dict[k] = gal_dict

            measurement = StudentMeasurement(**meas_dict)
            measurements.append(measurement)

            # NOTE: FOR DELETING DB MEASUREMENTS
            # url = f"{API_URL}/{HUBBLE_ROUTE_PATH}/measurement/{GLOBAL_STATE.student.id.value}/{measurement.galaxy.id}"
            # r = GLOBAL_STATE.request_session.delete(url)
            # print(r)

        return measurements

    @staticmethod
    def put_measurements():
        url = f"{API_URL}/{HUBBLE_ROUTE_PATH}/submit-measurement/"

        for measurement in student_data.measurements:
            sub_dict = {
                "student_id": GLOBAL_STATE.student.id.value,
                "galaxy_id": int(measurement.galaxy.id),
                "rest_wave_value": measurement.rest_wave,
                "rest_wave_unit": "angstrom",
                "obs_wave_value": measurement.obs_wave,
                "obs_wave_unit": "angstrom",
                "velocity_value": measurement.velocity,
                "velocity_unit": "km / s",
                "ang_size_value": measurement.ang_size,
                "ang_size_unit": "arcsecond",
                "est_dist_value": measurement.est_dist,
                "est_dist_unit": "Mpc",
                "brightness": 1,
                "last_modified": f"{datetime.datetime.now(datetime.UTC)}",
                "galaxy": {
                    "id": measurement.galaxy.id,
                    "ra": measurement.galaxy.ra,
                    "decl": measurement.galaxy.decl,
                    "z": measurement.galaxy.z,
                    "type": measurement.galaxy.type,
                    "name": measurement.galaxy.name,
                    "element": measurement.galaxy.element,
                },
            }

            r = GLOBAL_STATE.request_session.put(url, json=sub_dict)

    @staticmethod
    def get_story_state(component_state):
        r = GLOBAL_STATE.request_session.get(
            f"{API_URL}/story-state/{GLOBAL_STATE.student.id.value}/hubbles_law"
        )
        res_json = r.json()

        app_state = res_json["state"]["app"]
        story_state = res_json["state"]["story"]
        stage_state = res_json["state"]["stage"][f"{component_state.stage_name.value}"]

        # NOTE: the way the loading from a dict works, solara with trigger
        #  the reactive variables one after another, as there are loaded from
        #  the database. It is possible that `current_step` will be set early,
        #  and that some other event will cause it to revert to an early step.
        #  To avoid this, remove `current_step` and re-add it as the last one.
        stage_step = stage_state.pop("current_step")
        stage_state.update(
            {"current_step": component_state.current_step.value.__class__(stage_step)}
        )

        GLOBAL_STATE.from_dict(app_state)
        LOCAL_STATE.from_dict(story_state)
        component_state.from_dict(stage_state)

    @staticmethod
    def put_story_state(component_state):
        comp_state_dict = component_state.as_dict()
        comp_state_dict.update(
            {"current_step": component_state.current_step.value.value}
        )

        state = {
            "app": GLOBAL_STATE.as_dict(),
            "story": LOCAL_STATE.as_dict(),
            "stage": {f"{component_state.stage_name.value}": comp_state_dict},
        }

        r = GLOBAL_STATE.request_session.put(
            f"{API_URL}/story-state/{GLOBAL_STATE.student.id.value}/hubbles_law",
            json=state,
        )
