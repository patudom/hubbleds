import solara
from typing import Callable


@solara.component_vue("ReflectVelocitySlideshow.vue")
def ReflectVelocitySlideshow(
    step: int = 0,
    length: int = 8,
    dialog: bool = False,
    max_step_completed: int = 0,
    interact_steps: list[int] = [2, 3, 4, 5, 6],
    button_text: str = "Reflect",
    close_text: str = "Done",
    require_responses: bool = True,
    reflection_complete: bool = False,
    event_on_reflection_completed: Callable = lambda: None,
):
    pass
