import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate
from ...utils import IMAGE_BASE_URL


@solara.component_vue("AngsizeDosDontsSlideshow.vue")
def AngsizeDosDontsSlideshow(
    step=0,
    length=8,
    dialog=False,
    opened=False,
    currentTitle="Measurement Dos and Don'ts",
    image_location=f"{IMAGE_BASE_URL}/stage_two_dos_donts",
    event_on_dialog_opened=None,
):
    pass
