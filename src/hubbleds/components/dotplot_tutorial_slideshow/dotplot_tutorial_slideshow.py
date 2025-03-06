import solara
from typing import Callable, Any


@solara.component_vue("DotplotTutorialSlideshow.vue")
def DotplotTutorialSlideshow(
    dialog: bool,
    step: int,
    length: int,
    max_step_completed: int,
    dotplot_viewer: Any,
    event_tutorial_finished: Callable,
    event_show_dialog: Callable,
    event_set_step: Callable,
):
    pass
