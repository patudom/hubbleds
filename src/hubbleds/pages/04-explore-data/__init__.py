import numpy as np
import solara
from solara.toestand import Ref

from hubbleds.state import LOCAL_STATE, GLOBAL_STATE
from .component_state import COMPONENT_STATE, Marker
from hubbleds.remote import LOCAL_API

from cosmicds.logger import setup_logger

logger = setup_logger("STAGE 4")


@solara.component
def Page():
    loaded_component_state = solara.use_reactive(False)

    async def _load_component_state():
        # Load stored component state from database, measurement data is
        # considered higher-level and is loaded when the story starts
        LOCAL_API.get_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)

        # TODO: What else to we need to do here?
        logger.info("Finished loading component state for stage 4.")
        loaded_component_state.set(True)

    solara.lab.use_task(_load_component_state)

    async def _write_local_global_states():
        # Listen for changes in the states and write them to the database
        LOCAL_API.put_story_state(GLOBAL_STATE, LOCAL_STATE)

        logger.info("Wrote state to database.")

    solara.lab.use_task(_write_local_global_states, dependencies=[GLOBAL_STATE.value, LOCAL_STATE.value])

    async def _write_component_state():
        if not loaded_component_state.value:
            return

        # Listen for changes in the states and write them to the database
        LOCAL_API.put_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)

        logger.info("Wrote component state to database.")

    solara.lab.use_task(_write_component_state, dependencies=[COMPONENT_STATE.value])

    class_plot_data = solara.use_reactive([])
    async def _load_class_data():
        class_measurements = LOCAL_API.get_class_measurements(GLOBAL_STATE, LOCAL_STATE)
        measurements = Ref(LOCAL_STATE.fields.class_measurements)
        student_ids = Ref(LOCAL_STATE.fields.stage_4_class_data_students)
        if class_measurements and not student_ids:
            ids = [id for id in np.unique([m.student_id for m in class_measurements])]
            student_ids.set(ids)
        measurements.set(class_measurements)

        class_data_points = [m for m in class_measurements if m.student_id in student_ids.value] 
        class_plot_data.set(class_data_points)

    solara.lab.use_task(_load_class_data)

