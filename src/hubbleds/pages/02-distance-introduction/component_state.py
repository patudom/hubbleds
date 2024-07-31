import solara
import enum
from pydantic import BaseModel
from cosmicds.state import BaseState
from hubbleds.base_marker import BaseMarker 
from hubbleds.base_component_state import BaseComponentState

class Marker(enum.Enum, BaseMarker):
    mea_dis1 = enum.auto()

class DistanceSlideshow(BaseModel):
    step: int = 0
    max_step_completed: int = 0

class ComponentState(BaseComponentState, BaseState):
    current_step: Marker = Marker.mea_dis1
    stage_id: str = "distance_introduction"
    distance_slideshow_state: DistanceSlideshow = DistanceSlideshow()

COMPONENT_STATE = solara.reactive(ComponentState())