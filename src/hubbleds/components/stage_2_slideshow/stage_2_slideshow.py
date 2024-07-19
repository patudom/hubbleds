import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate

@solara.component_vue("Stage2Slideshow.vue")
def Stage2Slideshow (
    step,
    max_step_completed,
    length,
    titles,
    interact_steps,
    distance_const,
    image_location,
    debug,
    event_set_step,
    event_set_max_step_completed,
    event_mc_callback,
    state_view,
    event_slideshow_finished,
):
    pass
