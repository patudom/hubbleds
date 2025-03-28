import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate
from ...utils import IMAGE_BASE_URL
from typing import Callable


@solara.component_vue("SpectrumSlideshow.vue")
def SpectrumSlideshow(
    step: int = 0,
    length: int = 11,
    dialog: bool = False,
    opened: bool = False,
    image_location: str = f"{IMAGE_BASE_URL}/stage_one_spectrum",
    event_dialog_opened_callback: Callable = None,
    show_team_interface: bool = False,
):
    pass
