from solara.toestand import Ref

from cosmicds.state import GLOBAL_STATE
from hubbleds.remote import LOCAL_API
from hubbleds.state import LOCAL_STATE, StudentMeasurement


def fill_velocities():
    dummy_measurements = LOCAL_API.get_dummy_data()
    measurements = []
    for measurement in dummy_measurements:
        measurements.append(StudentMeasurement(student_id=GLOBAL_STATE.value.student.id,
                                               obs_wave_value=measurement.obs_wave_value,
                                               galaxy=measurement.galaxy,
                                               velocity_value=measurement.velocity_value))
    Ref(LOCAL_STATE.fields.measurements).set(measurements)


def fill_thetas():
    dummy_measurements = LOCAL_API.get_dummy_data()
    measurements = []
    for measurement in dummy_measurements:
        measurements.append(StudentMeasurement(student_id=GLOBAL_STATE.value.student.id,
                                               obs_wave_value=measurement.obs_wave_value,
                                               velocity_value=measurement.velocity_value,
                                               ang_size_value=measurement.ang_size_value,
                                               galaxy=measurement.galaxy))
    Ref(LOCAL_STATE.fields.measurements).set(measurements)


def fill_data_points():
    dummy_measurements = LOCAL_API.get_dummy_data()
    for measurement in dummy_measurements:
        measurement.student_id = GLOBAL_STATE.value.student.id
    Ref(LOCAL_STATE.fields.measurements).set(dummy_measurements)
