
import solara

from pydantic import field_validator

from cosmicds.state import BaseState
from hubbleds.base_marker import BaseMarker 
from hubbleds.base_component_state import BaseComponentState
from hubbleds.state import LOCAL_STATE

import enum
from typing import Any, cast


class Marker(enum.Enum, BaseMarker):
    mark1 = enum.auto()
    mark2 = enum.auto()
    mark3 = enum.auto()
    mark4 = enum.auto()
    
class ComponentState(BaseState, BaseComponentState):
    current_step: Marker = Marker.mark1
    stage_id: str = "test_page"
    
    button_clicked: bool = False
    
    @field_validator("current_step", mode="before")
    def convert_int_to_enum(cls, v: Any) -> Marker:
        if isinstance(v, int):
            return Marker(v)
        return v
    
    @property
    def mark2_gate(self) -> bool:
        return self.button_clicked
    
    @property
    def mark3_gate(self) -> bool:
        return LOCAL_STATE.value.question_completed("mc-2")
    


    
COMPONENT_STATE = solara.reactive(ComponentState())