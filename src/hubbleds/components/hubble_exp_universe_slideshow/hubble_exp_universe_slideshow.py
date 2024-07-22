from reacton.ipyvuetify import Any
from solara import component_vue
from typing import Callable, List

from ...utils import IMAGE_BASE_URL

@component_vue("HubbleExpUniverseSlideshow.vue")
def HubbleExpUniverseSlideshow(
    race_viewer: Any,
    layer_viewer: Any,
    dialog: bool = False,
    step: int = 0,
    max_step_completed: int = 0,
    length: int = 4,
    interact_steps: List[int] = [1],
    titles: List[str] = [
        "Hubble's Discovery",
        "A Running Race",
        "Runner's Velocities vs. Distances",
        "Age of the Universe"
    ],
    image_location: str = f"{IMAGE_BASE_URL}/stage_three",
    state_view: Any = None,
    event_set_dialog: Callable | None = None,
    event_set_step: Callable | None = None,
    event_set_max_step_completed: Callable | None = None,
    event_mc_callback: Callable | None = None,
    event_on_slideshow_finished: Callable | None = None,

):
    pass
