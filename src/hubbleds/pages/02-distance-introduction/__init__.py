import solara
from cosmicds import load_custom_vue_components

from ...components import Stage2Slideshow

from hubbleds.pages.state import LOCAL_STATE
from .component_state import ComponentState
from ...utils import IMAGE_BASE_URL, DISTANCE_CONSTANT


component_state = ComponentState()

@solara.component
def Page():
    load_custom_vue_components()

    Stage2Slideshow(
        step = component_state.distance_slideshow_state.step_dist.value,
        max_step_completed = component_state.distance_slideshow_state.max_step_completed.value,
        event_on_slideshow_finished=lambda *args: component_state.distance_slideshow_state.complete.set(
                            True
                        ),
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
        debug = LOCAL_STATE.debug_mode.value,
    )    
