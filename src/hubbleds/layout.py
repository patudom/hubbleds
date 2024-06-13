from cosmicds.layout import BaseLayout
from cosmicds.state import GLOBAL_STATE
import solara
from cosmicds.components import MathJaxSupport
from .data_models.student import student_data, StudentMeasurement
from .remote import DatabaseAPI


@solara.component
def Layout(children=[]):

    with BaseLayout(
        children=children, story_name="hubbles_law", story_title="Hubble's Law"
    ):
        # Mount external javascript libraries
        def _load_math_jax():
            MathJaxSupport()

        solara.use_memo(_load_math_jax, dependencies=[])

        # Load student data measurements
        def _load_student_measurements():
            stored_measurements = DatabaseAPI.get_measurements()
            student_data.measurements = stored_measurements

        solara.use_memo(
            _load_student_measurements, dependencies=[GLOBAL_STATE.student.id.value]
        )
