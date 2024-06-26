import solara.toestand
from solara import Reactive
import enum

from ...component_state_base import BaseComponentState
from ...marker_base import MarkerBase
from ...utils import HUBBLE_ROUTE_PATH
from ...decorators import computed_property
import dataclasses
from cosmicds.utils import API_URL
from ...state import GLOBAL_STATE
from ...data_models.student import example_data, StudentMeasurement, SpectrumData
from contextlib import closing
from io import BytesIO
from astropy.io import fits
from ...remote import DatabaseAPI, ELEMENT_REST


class Marker(enum.Enum, MarkerBase):
    mee_gui1 = enum.auto()
    sel_gal1 = enum.auto()
    sel_gal2 = enum.auto()
    not_gal_tab = enum.auto()
    sel_gal3 = enum.auto()
    sel_gal4 = enum.auto()
    cho_row1 = enum.auto()
    mee_spe1 = enum.auto()
    # spe_tut1 = enum.auto()  # This step doesn't seem to do anything?
    res_wav1 = enum.auto()
    obs_wav1 = enum.auto()
    obs_wav2 = enum.auto()
    dop_cal0 = enum.auto()
    dop_cal2 = enum.auto()
    dop_cal4 = enum.auto()
    dop_cal5 = enum.auto()
    che_mea1 = enum.auto()
    int_dot1 = enum.auto()
    dot_seq1 = enum.auto()
    dot_seq2 = enum.auto()
    dot_seq3 = enum.auto()
    dot_seq4 = enum.auto()
    dot_seq5 = enum.auto()
    dot_seq6 = enum.auto()
    dot_seq7 = enum.auto()
    dot_seq8 = enum.auto()
    dot_seq9 = enum.auto()
    dot_seq10 = enum.auto()
    dot_seq11 = enum.auto()
    dot_seq12 = enum.auto()
    dot_seq13 = enum.auto()
    dot_seq13a = enum.auto()
    dot_seq14 = enum.auto()
    rem_gal1 = enum.auto()
    ref_dat1 = enum.auto()
    dop_cal6 = enum.auto()
    ref_vel1 = enum.auto()
    end_sta1 = enum.auto()
    nxt_stg = enum.auto()


@dataclasses.dataclass
class DopplerCalculation:
    step: Reactive[int] = dataclasses.field(default=Reactive(0))
    length: Reactive[int] = dataclasses.field(default=Reactive(6))
    current_title: Reactive[str] = dataclasses.field(
        default=Reactive("Doppler Calculation")
    )
    failed_validation_4: Reactive[bool] = dataclasses.field(default=Reactive(False))
    failed_validation_5: Reactive[bool] = dataclasses.field(default=Reactive(False))
    interact_steps_5: Reactive[list] = dataclasses.field(default=Reactive([3, 4]))
    max_step_completed_5: Reactive[int] = dataclasses.field(default=Reactive(0))
    student_c: Reactive[int] = dataclasses.field(default=Reactive(0))
    student_vel_calc: Reactive[bool] = dataclasses.field(default=Reactive(False))
    complete: Reactive[bool] = dataclasses.field(default=Reactive(False))
    titles: Reactive[list] = dataclasses.field(
        default=Reactive(
            [
                "Doppler Calculation",
                "Doppler Calculation",
                "Doppler Calculation",
                "Reflect on Your Result",
                "Enter Speed of Light",
                "Your Galaxy's Velocity",
            ]
        )
    )
    mj_inputs: Reactive[list] = dataclasses.field(default=Reactive([]))


@dataclasses.dataclass
class DotPlotTutorialState:
    step: Reactive[int] = dataclasses.field(default=Reactive(0))
    length: Reactive[int] = dataclasses.field(default=Reactive(4))
    max_step_completed: Reactive[int] = dataclasses.field(default=Reactive(0))
    current_title: Reactive[str] = dataclasses.field(default=Reactive(""))


@dataclasses.dataclass
class ComponentState(BaseComponentState):
    current_step: Reactive[Marker] = dataclasses.field(
        default=Reactive(Marker.mee_gui1)
    )
    stage_name: Reactive[str] = dataclasses.field(
        default=Reactive("spectra_&_velocity")
    )
    database_changes: Reactive[int] = dataclasses.field(default=Reactive(0))
    total_galaxies: Reactive[int] = dataclasses.field(default=Reactive(0))
    selected_galaxy: Reactive[str] = dataclasses.field(default=Reactive(""))
    selected_galaxies: Reactive[list] = dataclasses.field(default=Reactive([]))
    show_example_galaxy: Reactive[bool] = dataclasses.field(default=Reactive(False))
    selected_example_galaxy: Reactive[str] = dataclasses.field(default=Reactive(""))
    spectrum_tutorial_opened: Reactive[bool] = dataclasses.field(
        default=Reactive(False)
    )
    lambda_on: Reactive[bool] = dataclasses.field(default=Reactive(False))
    lambda_used: Reactive[bool] = dataclasses.field(default=Reactive(False))
    spectrum_clicked: Reactive[bool] = dataclasses.field(default=Reactive(False))
    zoom_tool_activated: Reactive[bool] = dataclasses.field(default=Reactive(False))
    doppler_calc_reached: Reactive[bool] = dataclasses.field(default=Reactive(False))
    lambda_obs: Reactive[float] = dataclasses.field(default=Reactive(0.0))
    lambda_rest: Reactive[float] = dataclasses.field(default=Reactive(0.0))
    doppler_calc_dialog: Reactive[bool] = dataclasses.field(default=Reactive(False))
    doppler_calc_state: DopplerCalculation = dataclasses.field(
        default_factory=DopplerCalculation
    )
    student_vel: Reactive[float] = dataclasses.field(default=Reactive(0))
    dotplot_tutorial_dialog: Reactive[bool] = dataclasses.field(default=Reactive(False))
    dotplot_tutorial_state: DotPlotTutorialState = dataclasses.field(
        default_factory=DotPlotTutorialState
    )
    dotplot_tutorial_finished: Reactive[bool] = dataclasses.field(
        default=Reactive(False)
    )

    has_bad_velocities: Reactive[bool] = dataclasses.field(default=Reactive(False))
    has_multiple_bad_velocities: Reactive[bool] = dataclasses.field(
        default=Reactive(False)
    )
    obswaves_total: Reactive[int] = dataclasses.field(default=Reactive(0))
    velocities_total: Reactive[int] = dataclasses.field(default=Reactive(0))
    reflection_complete: Reactive[bool] = dataclasses.field(default=Reactive(False))

    def __post_init__(self):
        self._galaxy_data = None
        self._example_galaxy_data = None

        self._load_galaxies()

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

    @computed_property
    def mee_gui1_gate(self):
        return (
            self.current_step.value == Marker.mee_gui1
            and self.total_galaxies.value == 0
            and not self.selected_galaxy.value
        )

    @computed_property
    def not_gal_tab_gate(self):
        return self.total_galaxies.value == 1

    @computed_property
    def sel_gal3_gate(self):
        return self.total_galaxies.value >= 1

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
        return (
            bool(self.selected_example_galaxy.value)
            and self.spectrum_tutorial_opened.value
        )

    @computed_property
    def res_wav1_gate(self):
        return (
            bool(self.selected_example_galaxy.value)
            and self.spectrum_tutorial_opened.value
        )

    @computed_property
    def obs_wav1_gate(self):
        return self.lambda_used.value

    @computed_property
    def obs_wav2_gate(self):
        return self.spectrum_clicked.value

    @computed_property
    def obs_wav2_gate(self):
        return self.spectrum_clicked.value

    @computed_property
    def dop_cal0_gate(self):
        return self.zoom_tool_activated.value

    @computed_property
    def che_mea1_gate(self):
        return self.doppler_calc_state.student_vel_calc.value

    @computed_property
    def dot_seq1_gate(self):
        return self.dotplot_tutorial_finished.value

    @computed_property
    def ref_dat1_gate(self):
        return self.obswaves_total.value >= 5

    @computed_property
    def dop_cal6_gate(self):
        return self.reflection_complete.value

    @computed_property
    def ref_vel1_gate(self):
        return self.velocities_total.value >= 5

    @computed_property
    def nxt_stg_gate(self):
        return not (self.has_bad_velocities.value or self.has_multiple_bad_velocities)

    @property
    def galaxy_data(self):
        return self._galaxy_data

    def _load_galaxies(self):
        if self._galaxy_data is None:
            galaxies = GLOBAL_STATE.request_session.get(
                f"{API_URL}/{HUBBLE_ROUTE_PATH}/galaxies?types=Sp"
            ).json()

            self._galaxy_data = {k: [x[k] for x in galaxies] for k in galaxies[0]}
            self._galaxy_data["name"] = [
                x[: -len(".fits")] for x in self._galaxy_data["name"]
            ]
            self._galaxy_data["rest_wave"] = [
                round(ELEMENT_REST[x["element"]]) for x in galaxies
            ]

        return self._galaxy_data

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
