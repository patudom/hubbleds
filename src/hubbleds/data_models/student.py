from pydantic import BaseModel
from typing import Optional, List


class StudentMeasurement(BaseModel):
    id: Optional[str]
    name: Optional[str]
    ra: Optional[float]
    decl: Optional[float]
    z: Optional[float]
    type: Optional[str]
    element: Optional[str]
    rest_wave: Optional[float] = 0.0
    measured_wave: Optional[float] = 0.0
    velocity: Optional[float] = 0.0


class StudentData(BaseModel):
    measurements: Optional[List[StudentMeasurement]]


student_data = StudentData(measurements=[])
example_data = StudentData(measurements=[])
