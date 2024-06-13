from cosmicds.layout import BaseLayout
from cosmicds.state import GLOBAL_STATE
import solara
from cosmicds.components import MathJaxSupport, PlotlySupport
from .data_models.student import student_data, StudentMeasurement, example_data
from .remote import DatabaseAPI


@solara.component
def Layout(children=[]):

    with BaseLayout(
        children=children, story_name="hubbles_law", story_title="Hubble's Law"
    ):
        # Mount external javascript libraries
        def _load_math_jax():
            MathJaxSupport()
            PlotlySupport()

        solara.use_memo(_load_math_jax, dependencies=[])

        # Load student data measurements
        def _load_student_measurements():
            stored_measurements = DatabaseAPI.get_measurements()
            student_data.measurements = stored_measurements

            stored_example_measurements = DatabaseAPI.get_measurements(samples=True)

            if len(stored_example_measurements) > 0:
                example_data.measurements = stored_example_measurements
            else:
                print("No stored sample measurements; creating new one...")
                example_data.measurements = [StudentMeasurement(
                    **DatabaseAPI.get_sample_galaxy()
                )]
                DatabaseAPI.put_measurements(True)

        solara.use_memo(
            _load_student_measurements, dependencies=[GLOBAL_STATE.student.id.value]
        )
