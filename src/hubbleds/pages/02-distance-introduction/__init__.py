
import solara

from hubbleds.components import Stage2Slideshow
from hubbleds.state import LOCAL_STATE, GLOBAL_STATE 
from .component_state import COMPONENT_STATE
from hubbleds.remote import LOCAL_API
from ...utils import IMAGE_BASE_URL, DISTANCE_CONSTANT

from cosmicds.logger import setup_logger

logger = setup_logger("STAGE 2")

@solara.component
def Page():
    loaded_component_state = solara.use_reactive(False)

    async def _load_component_state():
        # Load stored component state from database, measurement data is
        # considered higher-level and is loaded when the story starts
        LOCAL_API.get_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)

        # TODO: What else to we need to do here?
        logger.info("Finished loading component state for stage 2.")
        loaded_component_state.set(True)

    solara.lab.use_task(_load_component_state)

    async def _write_component_state():
        if not loaded_component_state.value:
            return

        # Listen for changes in the states and write them to the database
        LOCAL_API.put_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)

        logger.info("Wrote component state for stage 2 to database.")

    logger.info("Trying to write component state for stage 2.")
    solara.lab.use_task(_write_component_state, dependencies=[COMPONENT_STATE.value])

    Stage2Slideshow(
        step = COMPONENT_STATE.value.distance_slideshow_state.step,
        max_step_completed = COMPONENT_STATE.value.distance_slideshow_state.max_step_completed,
        event_on_slideshow_finished=lambda _: COMPONENT_STATE.value.complete.set(True),
        length = 13,
        titles = [
            "1920's Astronomy",
            "1920's Astronomy",
            "How can we know how far away something is?",
            "How can we know how far away something is?",
            "How can we know how far away something is?",
            "How can we know how far away something is?",
            "Galaxy Distances",
            "Galaxy Distances",
            "Galaxy Distances",
            "Galaxy Distances",
            "Galaxy Distances",
            "Galaxy Distances",
            "Galaxy Distances"
        ],
        interact_steps=[7,9],
        distance_const=DISTANCE_CONSTANT,
        image_location=f"{IMAGE_BASE_URL}/stage_two_intro",
        debug = LOCAL_STATE.value.debug_mode,
    )
