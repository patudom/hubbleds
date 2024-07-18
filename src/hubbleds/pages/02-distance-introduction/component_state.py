import solara
from pydantic import BaseModel
from cosmicds.state import BaseState
from hubbleds.base_component_state import BaseComponentState

class DistanceSlideshow(BaseModel):
    step: int = 0
    max_step_completed: int = 0
    complete: bool = False

class ComponentState(BaseComponentState, BaseState):
    stage_id: str = "distance_introduction"
    distance_slideshow_state: DistanceSlideshow = DistanceSlideshow()

COMPONENT_STATE = solara.reactive(ComponentState())