import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate
from ...utils import IMAGE_BASE_URL


@solara.component_vue("ReflectVelocitySlideshow.vue")
def ReflectVelocitySlideshow(
    step=0,
    length=8,
    dialog=False,
    max_step_completed=0,
    interact_steps=[2, 3, 4, 5, 6],
    button_text="Reflect",
    close_text="Done",
    require_responses=True,
    reflection_complete=False,
    event_on_reflection_completed=lambda: None,
):
    pass
