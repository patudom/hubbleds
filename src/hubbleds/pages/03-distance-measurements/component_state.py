from solara import Reactive
import enum
from ...decorators import computed_property
from ...marker_base import MarkerBase
import dataclasses
from ...component_state_base import BaseComponentState


ELEMENT_REST = {
    'H-α': 6562.79,
    'Mg-I': 5176.7
}


class Marker(enum.Enum, MarkerBase):
    ang_siz1 = enum.auto()	
    cho_row1 = enum.auto()	
    ang_siz2 = enum.auto()	
    ang_siz2b = enum.auto()	
    ang_siz3 = enum.auto()	
    ang_siz4 = enum.auto()	
    ang_siz5 = enum.auto()	
    est_dis1 = enum.auto()	
    est_dis2 = enum.auto()	
    cho_row2 = enum.auto()	
    est_dis3 = enum.auto()	
    est_dis4 = enum.auto()	
    dot_seq1 = enum.auto()	
    dot_seq2 = enum.auto()	
    dot_seq3 = enum.auto()	
    dot_seq4 = enum.auto()	
    dot_seq4a = enum.auto()	
    ang_siz5a  = enum.auto()	
    # ang_siz6  = enum.auto() We skipped this in the voila version
    dot_seq5  = enum.auto()	
    dot_seq5a = enum.auto()	
    dot_seq5b = enum.auto()	
    dot_seq5c = enum.auto()	
    dot_seq6  = enum.auto()	
    dot_seq7 = enum.auto()	
    rep_rem1 = enum.auto()	
    fil_rem1 = enum.auto()


@dataclasses.dataclass
class ComponentState(BaseComponentState):
    current_step: Reactive[Marker] = dataclasses.field(
        default=Reactive(Marker.ang_siz1)
    )
    dosdonts_tutorial_opened: Reactive[bool] = dataclasses.field(
        default=Reactive(False)
    )
    selected_galaxy: Reactive[dict] = dataclasses.field(default=Reactive({}))
    selected_example_galaxy: Reactive[dict] = dataclasses.field(default=Reactive({}))
    show_ruler: Reactive[bool] = dataclasses.field(default=Reactive(False))

    def setup(self):
        pass

    @computed_property
    def dot_seq5_gate(self):
        return (
            bool(self.dosdonts_tutorial_opened.value)
        )
