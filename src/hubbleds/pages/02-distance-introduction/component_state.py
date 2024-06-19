from solara import Reactive
import dataclasses


@dataclasses.dataclass
class DistanceSlideshow:
    step_dist: Reactive[int] = dataclasses.field(default=Reactive(0))
    max_step_completed: Reactive[int] = dataclasses.field(default=Reactive(0)) 
    complete: Reactive[bool] = dataclasses.field(default=Reactive(False))


@dataclasses.dataclass
class ComponentState:
    distance_slideshow_state: DistanceSlideshow = dataclasses.field(
        default_factory=DistanceSlideshow
    )