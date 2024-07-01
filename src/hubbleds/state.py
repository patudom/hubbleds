from pydantic import BaseModel, computed_field, field_validator
from solara import Reactive
from cosmicds.state import BaseState, GLOBAL_STATE
from typing import Optional
import solara
import datetime
from functools import cached_property
from astropy.table import Table
from pydantic import Field

ELEMENT_REST = {"H-α": 6562.79, "Mg-I": 5176.7}


class SpectrumData(BaseModel):
    name: str
    wave: list[float]
    flux: list[float]
    ivar: list[float]


class GalaxyData(BaseModel):
    id: int
    name: str
    ra: float
    decl: float
    z: float
    type: str
    element: str

    @cached_property
    def spectrum(self):
        from hubbleds.remote import LOCAL_API

        return LOCAL_API.load_spectrum_data(self, LOCAL_STATE)

    @cached_property
    def spectrum_as_data_frame(self):
        from hubbleds.remote import LOCAL_API

        spec_data = LOCAL_API.load_spectrum_data(self, LOCAL_STATE)

        return Table({"wave": spec_data.wave, "flux": spec_data.flux}).to_pandas()


class StudentMeasurement(BaseModel):
    student_id: int
    rest_wave_unit: str = "angstrom"
    obs_wave_value: float | None = None
    obs_wave_unit: str = "angstrom"
    velocity_value: float | None = None
    velocity_unit: str = "km/s"
    ang_size_value: float | None = None
    ang_size_unit: str = "arcsecond"
    est_dist_value: float | None = None
    est_dist_unit: str = "Mpc"
    measurement_number: str | None = None
    brightness: float = 0
    galaxy: Optional[GalaxyData] = None

    @computed_field
    @property
    def galaxy_id(self) -> int:
        return self.galaxy.id

    @computed_field
    @property
    def rest_wave_value(self) -> float:
        return round(ELEMENT_REST[self.galaxy.element])

    @computed_field
    @property
    def last_modified(self) -> str:
        return f"{datetime.datetime.now(datetime.UTC)}"


class MCScore(BaseModel):
    tag: str = ""


class LocalState(BaseState):
    debug_mode: bool = False
    title: str = "Hubble's law"
    story_id: str = "hubbles_law"
    measurements: list[StudentMeasurement] = []
    example_measurements: list[StudentMeasurement] = []
    calculations: dict = {}
    validation_failure_counts: dict = {}
    has_best_fit_galaxy: bool = False
    enough_students_ready: bool = False
    class_data_students: list = []
    class_data_info: dict = {}
    mc_scoring: dict[str, MCScore] = {}
    show_snackbar: bool = False
    snackbar_message: str = ""

    @cached_property
    def galaxies(self) -> list[GalaxyData]:
        from hubbleds.remote import LOCAL_API

        return LOCAL_API.get_galaxies(LOCAL_STATE)

    def get_measurement(self, galaxy_id: int) -> StudentMeasurement | None:
        return next((x for x in self.measurements if x.galaxy_id == galaxy_id), None)

    def get_example_measurement(self, galaxy_id: int) -> StudentMeasurement | None:
        return next(
            (x for x in self.example_measurements if x.galaxy_id == galaxy_id), None
        )

    def get_measurement_index(self, galaxy_id: int) -> int | None:
        return next(
            (i for i, x in enumerate(self.measurements) if x.galaxy_id == galaxy_id),
            None,
        )

    def get_example_measurement_index(self, galaxy_id: int) -> int | None:
        return next(
            (
                i
                for i, x in enumerate(self.example_measurements)
                if x.galaxy_id == galaxy_id
            ),
            None,
        )


LOCAL_STATE = solara.reactive(LocalState())
