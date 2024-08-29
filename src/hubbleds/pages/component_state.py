import solara
import enum
from pydantic import BaseModel
from cosmicds.state import BaseState
from hubbleds.base_marker import BaseMarker 
from hubbleds.base_component_state import BaseComponentState

class Marker(enum.Enum, BaseMarker):
    int_sli1 = enum.auto()

class IntroSlideshow(BaseModel):
    step: int = 0

class ComponentState(BaseComponentState, BaseState):
    current_step: Marker = Marker.int_sli1
    stage_id: str = "introduction"
    intro_slideshow_state: IntroSlideshow = IntroSlideshow()

COMPONENT_STATE = solara.reactive(ComponentState())