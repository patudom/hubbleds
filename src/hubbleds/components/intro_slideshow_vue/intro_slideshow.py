
import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate

@solara.component_vue("introSlideshow.vue")
def IntroSlideshowVue (
    step,
    length,
    titles,
    image_location,
    event_set_step,
    event_slideshow_finished,
    debug,
):
    pass