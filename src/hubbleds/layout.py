from cosmicds.layout import BaseLayout
from .state import GLOBAL_STATE, LOCAL_STATE
import solara
from solara.lab import Ref
from cosmicds.components import MathJaxSupport, PlotlySupport
from hubbleds.remote import LOCAL_API
from cosmicds.logger import setup_logger

logger = setup_logger("LAYOUT")


@solara.component
def Layout(children=[]):
    def _mount_external():
        logger.info("Mounted external libraries.")
        MathJaxSupport()
        PlotlySupport()

    solara.use_memo(_mount_external)

    student_id = Ref(GLOBAL_STATE.fields.student.id)

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

    solara.lab.use_task(_load_local_state, dependencies=[student_id.value])
    # solara.use_memo(_load_local_state, dependencies=[student_id.value])

    with BaseLayout(
        children=children,
        story_name=LOCAL_STATE.value.story_id,
        story_title=LOCAL_STATE.value.title,
    ):
        pass
