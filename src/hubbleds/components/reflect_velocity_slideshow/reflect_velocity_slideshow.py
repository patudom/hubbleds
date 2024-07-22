import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate

@solara.component_vue("ReflectVelocitySlideshow.vue")
def ReflectVelocitySlideshow(
    # Variables we are not storing in state
    length,
    titles,
    interact_steps,
    require_responses,

    # State variables
    dialog,
    step,
    max_step_completed,
    reflection_complete,
    state_view,

    # Event handlers
    event_set_dialog,
    event_mc_callback,
    event_set_step,
    event_set_max_step_completed,
    event_on_reflection_complete,
):
    pass
