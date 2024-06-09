from pydantic import BaseModel
from typing import Optional, List


class SpectrumData(BaseModel):
    name: str
    wave: list[float]
    flux: list[float]
    ivar: list[float]


class GalaxyData(BaseModel):
    id: Optional[int]
    name: Optional[str]
    ra: Optional[float]
    decl: Optional[float]
    z: Optional[float]
    type: Optional[str]
    element: Optional[str]
    spectrum: Optional[SpectrumData] = None
    angular_size: Optional[int] = None
    distance: Optional[float] = None
    measurement_number: Optional[int] = 1


class StudentMeasurement(BaseModel):
    ang_size: Optional[float] = 0
    est_dist: Optional[float] = 0
    rest_wave: Optional[float] = 0.0
    obs_wave: Optional[float] = 0.0
    velocity: Optional[float] = 0.0
    galaxy: Optional[GalaxyData] = None


class StudentData(BaseModel):
    measurements: Optional[List[StudentMeasurement]]

    def update(self, id_: str, data: dict):
        idx = next(
            iter(i for i, x in enumerate(self.measurements) if x.id == id_), None
        )

        if idx is None:
            print(f"No data with id {id_} found.")
            return

        self.measurements[idx] = StudentMeasurement(
            **{**self.measurements[idx].dict(), **data}
        )

    def get_by_id(self, id_: str, exclude=None, asdict=False):
        idx = next(
            iter(i for i, x in enumerate(self.measurements) if x.id == id_), None
        )

        print(f"Found spectral data with id {id_} at index {idx}.")

        if idx is None:
            print(f"No data with id {id_} found.")
            return None if not asdict else {}

        return self.measurements[idx] if not asdict else self.measurements[idx].model_dump()


student_data = StudentData(measurements=[])
example_data = StudentData(measurements=[])
