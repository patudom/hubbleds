from solara import Reactive
import solara
import enum
from ...utils import HUBBLE_ROUTE_PATH
from ...decorators import computed_property
import dataclasses
from cosmicds.utils import API_URL
from ...state import GLOBAL_STATE
from ...data_models.student import example_data, StudentMeasurement, SpectrumData
from contextlib import closing
from io import BytesIO
from astropy.io import fits


class Marker(enum.Enum):
    mee_gui1 = enum.auto()
    sel_gal1 = enum.auto()
    sel_gal2 = enum.auto()
    not_gal_tab = enum.auto()
    sel_gal3 = enum.auto()
    sel_gal4 = enum.auto()
    cho_row1 = enum.auto()
    mee_spe1 = enum.auto()
    spe_tut1 = enum.auto()
    res_wave1 = enum.auto()

    @staticmethod
    def next(step):
        return Marker(step.value + 1)

    @staticmethod
    def previous(step):
        return Marker(step.value - 1)


@dataclasses.dataclass
class ComponentState:
    current_step: Reactive[Marker] = dataclasses.field(
        default=Reactive(Marker.mee_gui1)
    )
    total_galaxies: Reactive[int] = dataclasses.field(default=Reactive(0))
    selected_galaxy: Reactive[dict] = dataclasses.field(default=Reactive({}))
    show_example_galaxy: Reactive[bool] = dataclasses.field(default=Reactive(False))
    selected_example_galaxy: Reactive[dict] = dataclasses.field(default=Reactive({}))
    spectrum_tutorial_opened: Reactive[bool] = dataclasses.field(default=Reactive(bool))

    def __post_init__(self):
        self._galaxy_data = None
        self._example_galaxy_data = None

        self._load_galaxies()
        self._load_example_galaxy()

    def setup(self):
        # Set up a forced transition. I don't think this should occur this way,
        #  but this works best without altering the guidelines too much.
        def _on_total_galaxies_changed(*args):
            if self.total_galaxies.value == 1:
                self.transition_to(Marker.not_gal_tab)

        self.total_galaxies.subscribe_change(_on_total_galaxies_changed)

        def _on_example_galaxy_selected(*args):
            self.transition_to(Marker.mee_spe1)

        self.selected_example_galaxy.subscribe(_on_example_galaxy_selected)

    def is_current_step(self, step: Marker):
        return self.current_step.value == step

    def can_transition(self, step: Marker = None, next=False, prev=False):
        if next:
            step = Marker.next(self.current_step.value)
        elif prev:
            step = Marker.previous(self.current_step.value)

        return getattr(self, f"{step.name}_gate")().value

    def transition_to(self, step: Marker, force=False):
        if self.can_transition(step) or force:
            self.current_step.set(step)
        else:
            print(
                f"Conditions not met to transition from "
                f"{self.current_step.value.name} to {step.name}."
            )

    def transition_next(self):
        next_marker = Marker.next(self.current_step.value)
        self.transition_to(next_marker)

    def transition_previous(self):
        previous_marker = Marker.previous(self.current_step.value)
        self.transition_to(previous_marker)

    @computed_property
    def mee_gui1_gate(self):
        return (
            self.current_step.value == Marker.mee_gui1
            and self.total_galaxies.value == 0
            and not self.selected_galaxy.value
        )

    @computed_property
    def sel_gal1_gate(self):
        return self.total_galaxies.value == 0 and not self.selected_galaxy.value

    @computed_property
    def sel_gal2_gate(self):
        return self.total_galaxies.value == 0 and not self.selected_galaxy.value

    @computed_property
    def not_gal_tab_gate(self):
        return self.total_galaxies.value == 1

    @computed_property
    def sel_gal3_gate(self):
        return self.total_galaxies.value == 1

    @computed_property
    def sel_gal4_gate(self):
        return self.total_galaxies.value == 5

    @computed_property
    def cho_row1_gate(self):
        return self.total_galaxies.value == 5

    @computed_property
    def mee_spe1_gate(self):
        return bool(self.selected_example_galaxy.value)

    @computed_property
    def spe_tut1_gate(self):
        return bool(self.selected_example_galaxy.value)

    @computed_property
    def res_wave1_gate(self):
        return bool(self.selected_example_galaxy.value)

    @property
    def galaxy_data(self):
        return self._galaxy_data

    @property
    def example_galaxy_data(self):
        return self._example_galaxy_data

    def _load_galaxies(self):
        if self._galaxy_data is None:
            galaxies = GLOBAL_STATE.request_session.get(
                f"{API_URL}/{HUBBLE_ROUTE_PATH}/galaxies?types=Sp"
            ).json()

            self._galaxy_data = {k: [x[k] for x in galaxies] for k in galaxies[0]}
            self._galaxy_data["name"] = [
                x[: -len(".fits")] for x in self._galaxy_data["name"]
            ]

        return self._galaxy_data

    def _load_example_galaxy(self):
        if self._example_galaxy_data is None:
            example_galaxy_data = GLOBAL_STATE.request_session.get(
                f"{API_URL}/{HUBBLE_ROUTE_PATH}/sample-galaxy"
            ).json()

            self._example_galaxy_data = {
                k: example_galaxy_data[k] for k in example_galaxy_data
            }
            self._example_galaxy_data["id"] = str(self._example_galaxy_data["id"])
            self._example_galaxy_data["name"] = example_galaxy_data["name"].replace(
                ".fits", ""
            )

            # Load the spectrum associated with the example data
            spec_data = self._load_spectrum_data(self._example_galaxy_data)
            self._example_galaxy_data["spectrum"] = spec_data

            # Explicitly add the example galaxy to the example measurements
            example_data.measurements.append(
                StudentMeasurement(**self.example_galaxy_data)
            )

        return self._example_galaxy_data

    @staticmethod
    def _load_spectrum_data(gal_info):
        file_name = f"{gal_info['name']}.fits"
        gal_type = gal_info["type"]

        type_folders = {"Sp": "spiral", "E": "elliptical", "Ir": "irregular"}
        folder = type_folders[gal_type]
        url = f"{API_URL}/{HUBBLE_ROUTE_PATH}/spectra/{folder}/{file_name}"
        response = GLOBAL_STATE.request_session.get(url)

        with closing(BytesIO(response.content)) as f:
            f.name = gal_info["name"]

            with fits.open(f) as hdulist:
                data = hdulist["COADD"].data if "COADD" in hdulist else None

        if data is None:
            print("No extension named 'COADD' in spectrum fits file.")
            return

        spec_data = dict(
            name=gal_info["name"],
            wave=10 ** data["loglam"],
            flux=data["flux"],
            ivar=data["ivar"],
        )

        return spec_data
