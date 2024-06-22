from cosmicds.layout import BaseLayout
from .state import GLOBAL_STATE, LOCAL_STATE
import solara
from cosmicds.components import MathJaxSupport, PlotlySupport
from hubbleds.data_models.student import StudentMeasurement
from hubbleds.pages.remote import DatabaseAPI


@solara.lab.task
async def _load_student_measurements():
    print("Loading student measurements...")
    stored_measurements = DatabaseAPI.get_measurements()
    LOCAL_STATE.student_data.value.measurements = stored_measurements

    stored_example_measurements = DatabaseAPI.get_measurements(samples=True)

    return stored_measurements, stored_example_measurements


@solara.component
def Layout(children=[]):
    # Mount external javascript libraries
    def _mount_external():
        MathJaxSupport()
        PlotlySupport()

    solara.use_memo(_mount_external)

    # Generate a task to load user galaxy measurements in the background
    GLOBAL_STATE.student.id.subscribe_change(
        lambda *arg: _load_student_measurements()
    )

    if _load_student_measurements.finished:
        stored_measurements, stored_example_measurements = (
            _load_student_measurements.value
        )

        if len(stored_example_measurements) > 0:
            LOCAL_STATE.example_data.value.measurements = stored_example_measurements
        else:
            print("No stored sample measurements; creating new one...")
            LOCAL_STATE.example_data.value.measurements = [
                StudentMeasurement(**DatabaseAPI.get_sample_galaxy())
            ]
            DatabaseAPI.put_measurements(True)

    with BaseLayout(
        children=children,
        global_state=GLOBAL_STATE,
        story_name="hubbles_law",
        story_title="Hubble's Law",
    ):
        pass
