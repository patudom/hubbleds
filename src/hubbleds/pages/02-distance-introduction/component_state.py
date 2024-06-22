from solara import Reactive
from dataclasses import dataclass, field


@dataclass
class DistanceSlideshow:
    step_dist: Reactive[int] = field(default=Reactive(0))
    max_step_completed: Reactive[int] = field(default=Reactive(0))
    complete: Reactive[bool] = field(default=Reactive(False))


@dataclass
class ComponentState:
    distance_slideshow_state: DistanceSlideshow = field(
        default_factory=DistanceSlideshow
    )