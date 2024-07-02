from cosmicds.layout import BaseLayout
from .state import GLOBAL_STATE, LOCAL_STATE
import solara
from solara.lab import Ref
from cosmicds.components import MathJaxSupport, PlotlySupport
from hubbleds.state import StudentMeasurement
from hubbleds.remote import LOCAL_API
from cosmicds.logger import setup_logger
import asyncio

logger = setup_logger("LAYOUT")


@solara.component
def Layout(children=[]):
    def _mount_external():
        logger.info("Mounted external libraries.")
        MathJaxSupport()
        PlotlySupport()

    solara.use_memo(_mount_external)

    student_id = Ref(GLOBAL_STATE.fields.student.id)
    loaded_states = solara.use_reactive(False)

    async def _load_local_state():
        if not GLOBAL_STATE.value.student.id:
            logger.warning("Failed to load measurements: no student was found.")
            return

        logger.info(
            "Loading story stage and measurements for user `%s`.",
            GLOBAL_STATE.value.student.id,
        )

        # Retrieve the student's app and local states
        LOCAL_API.get_story_state(GLOBAL_STATE, LOCAL_STATE)

        # Load in the student's measurements
        measurements = LOCAL_API.get_measurements(GLOBAL_STATE, LOCAL_STATE)
        sample_measurements = LOCAL_API.get_sample_measurements(
            GLOBAL_STATE, LOCAL_STATE
        )

        logger.info("Finished loading state.")
        loaded_states.set(True)

    solara.lab.use_task(_load_local_state, dependencies=[student_id.value])
    # solara.use_memo(_load_local_state, dependencies=[student_id.value])

    async def _write_local_global_states():
        if not loaded_states.value:
            return

        # Listen for changes in the states and write them to the database
        LOCAL_API.put_story_state(GLOBAL_STATE, LOCAL_STATE)

        # Be sure to write the measurement data separately since it's stored
        #  in another location in the database
        LOCAL_API.put_measurements(GLOBAL_STATE, LOCAL_STATE)
        LOCAL_API.put_sample_measurements(GLOBAL_STATE, LOCAL_STATE)

        logger.info("Wrote state to database.")

    solara.lab.use_task(
        _write_local_global_states, dependencies=[GLOBAL_STATE.value, LOCAL_STATE.value]
    )

    with BaseLayout(
        children=children,
        story_name=LOCAL_STATE.value.story_id,
        story_title=LOCAL_STATE.value.title,
    ):
        pass
