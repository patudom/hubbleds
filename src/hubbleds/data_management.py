STUDENT_MEASUREMENTS_LABEL = "student_measurements"
STUDENT_DATA_LABEL = "student_data"
CLASS_DATA_LABEL = "class_data"
ALL_DATA_LABEL = "all_measurements"
CLASS_SUMMARY_LABEL = "class_summary_data"
ALL_STUDENT_SUMMARIES_LABEL = "all_student_summaries"
ALL_CLASS_SUMMARIES_LABEL = "all_class_summaries"
SDSS_DATA_LABEL = "SDSS_all_sample_filtered"
SPECTRUM_DATA_LABEL = "spectrum_data"
HUBBLE_1929_DATA_LABEL = "Hubble 1929-Table 1"
HUBBLE_KEY_DATA_LABEL = "HSTkey2001"

BEST_FIT_SUBSET_LABEL = "best_fit_subset"
BEST_FIT_GALAXY_NAME = "Best Fit Galaxy"

EXAMPLE_GALAXY_SEED_DATA = "example_galaxy_seed_data"
EXAMPLE_GALAXY_DATA = "example_galaxy"
EXAMPLE_GALAXY_MEASUREMENTS = "example_galaxy_data"
EXAMPLE_GALAXY_STUDENT_DATA = "example_galaxy_student_data"


### Data Components

# Measurements
MEASWAVE_COMPONENT = "measwave"
RESTWAVE_COMPONENT = "restwave"
VELOCITY_COMPONENT = "velocity"
DISTANCE_COMPONENT = "distance"
ANGULAR_SIZE_COMPONENT = "angular_size"
NAME_COMPONENT = "name"
STUDENT_ID_COMPONENT = "student_id"
ELEMENT_COMPONENT = "element"
RA_COMPONENT = "ra"
DEC_COMPONENT = "decl"
Z_COMPONENT = "z"
GALTYPE_COMPONENT = "type"

# Sample measurements
SAMPLE_ID_COMPONENT = "id"
MEASUREMENT_NUMBER_COMPONENT = "measurement_number"

# Summaries
CLASS_ID_COMPONENT = "class_id"
AGE_COMPONENT = "age"
H0_COMPONENT = "H0"


### Database keys

# Measurements
DB_MEASWAVE_KEY = "obs_wave_value"
DB_RESTWAVE_KEY = "rest_wave_value"
DB_VELOCITY_KEY = "velocity_value"
DB_DISTANCE_KEY = "est_dist_value"
DB_ANGSIZE_KEY = "ang_size_value"
DB_RA_KEY = "ra"
DB_DEC_KEY = "decl"
DB_NAME_KEY = "name"
DB_Z_KEY = "z"
DB_GALTYPE_KEY = "type"
DB_ELEMENT_KEY = "element"
DB_STUDENT_ID_KEY = "student_id"
DB_LAST_MODIFIED_KEY = "last_modified"

DB_MEASNUM_KEY = "measurement_number"

DB_GALNAME_KEY = "galaxy_name"

DB_RESTWAVE_UNIT_KEY = "rest_wave_unit"
DB_MEASWAVE_UNIT_KEY = "obs_wave_unit"
DB_DISTANCE_UNIT_KEY = "est_dist_unit"
DB_VELOCITY_UNIT_KEY = "velocity_unit"
DB_ANGSIZE_UNIT_KEY = "ang_size_unit"

DB_MEASUREMENT_KEYS = [
    DB_MEASWAVE_KEY,
    DB_RESTWAVE_KEY,
    DB_VELOCITY_KEY,
    DB_DISTANCE_KEY,
    DB_ANGSIZE_KEY,
    DB_RA_KEY,
    DB_DEC_KEY,
    DB_NAME_KEY,
    DB_Z_KEY,
    DB_GALTYPE_KEY,
    DB_ELEMENT_KEY,
    DB_STUDENT_ID_KEY,
    DB_LAST_MODIFIED_KEY
]

# Summaries
DB_H0_KEY = "hubble_fit_value"
DB_AGE_KEY = "age"

DB_SUMMARY_KEYS = [
    DB_H0_KEY,
    DB_AGE_KEY
]

def reverse(d):
    return { v : k for k, v in d.items() }

MEAS_TO_STATE = {
    MEASWAVE_COMPONENT: DB_MEASWAVE_KEY,
    RESTWAVE_COMPONENT: DB_RESTWAVE_KEY,
    VELOCITY_COMPONENT: DB_VELOCITY_KEY,
    DISTANCE_COMPONENT: DB_DISTANCE_KEY,
    NAME_COMPONENT: DB_GALNAME_KEY,
    STUDENT_ID_COMPONENT: DB_STUDENT_ID_KEY,
    ANGULAR_SIZE_COMPONENT : DB_ANGSIZE_KEY
}

STATE_TO_MEAS = reverse(MEAS_TO_STATE)

SUMM_TO_STATE = {
    H0_COMPONENT: DB_H0_KEY,
    AGE_COMPONENT: DB_AGE_KEY
}

STATE_TO_SUMM = reverse(SUMM_TO_STATE)

UNITS_TO_STATE = {
    DB_RESTWAVE_UNIT_KEY: "angstrom",
    DB_MEASWAVE_KEY: "angstrom",
    DB_DISTANCE_UNIT_KEY: "Mpc",
    DB_VELOCITY_UNIT_KEY: "km / s",
    DB_ANGSIZE_UNIT_KEY: "arcsecond"
}
