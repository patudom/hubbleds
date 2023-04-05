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

# Sample measurements
MEASUREMENT_NUMBER_COMPONENT = "measurement_number"

# Summaries
CLASS_ID_COMPONENT = "class_id"
AGE_COMPONENT = "age"

def reverse(d):
    return { v : k for k, v in d.items() }

MEAS_TO_STATE = {
    MEASWAVE_COMPONENT: "obs_wave_value",
    RESTWAVE_COMPONENT: "rest_wave_value",
    VELOCITY_COMPONENT: "velocity_value",
    DISTANCE_COMPONENT: "est_dist_value",
    NAME_COMPONENT: "galaxy_name",
    STUDENT_ID_COMPONENT: "student_id",
    ANGULAR_SIZE_COMPONENT : "ang_size_value"
}

STATE_TO_MEAS = reverse(MEAS_TO_STATE)

SUMM_TO_STATE = {
    "H0": "hubble_fit_value",
    "age": "age_value"
}

STATE_TO_SUMM = reverse(SUMM_TO_STATE)

UNITS_TO_STATE = {
    "rest_wave_unit": "angstrom",
    "obs_wave_unit": "angstrom",
    "est_dist_unit": "Mpc",
    "velocity_unit": "km / s",
    "ang_size_unit": "arcsecond"
}
