import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate
from ...utils import IMAGE_BASE_URL


@solara.component_vue("SpectrumSlideshow.vue")
def SpectrumSlideshow(
    step=0,
    length=11,
    dialog=False,
    opened=False,
    image_location=f"{IMAGE_BASE_URL}/stage_one_spectrum",
    event_on_dialog_opened=None,
):
    pass
