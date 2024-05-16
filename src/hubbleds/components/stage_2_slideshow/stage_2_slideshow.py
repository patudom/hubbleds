import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate

@solara.component_vue("stage_2_slideshow.vue")
def Stage2Slideshow (
    step,
    length,
    titles,
    max_step_completed,
    interact_steps,
    stage_2_complete,
    show_team_interface,
    distance_const,
    image_location,
):
    pass