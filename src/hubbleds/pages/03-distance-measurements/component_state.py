from solara import Reactive
import enum
from ...decorators import computed_property
from ...marker_base import MarkerBase
from dataclasses import dataclass, field
from ...base_component_state import BaseComponentState
from hubbleds.pages.state import LOCAL_STATE


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
    est_dis3 = enum.auto()	
    est_dis4 = enum.auto()	
    dot_seq1 = enum.auto()	
    dot_seq2 = enum.auto() # MC ang_meas_consensus
    dot_seq3 = enum.auto()	
    dot_seq4 = enum.auto()	
    dot_seq4a = enum.auto()	 # MC ang_meas_dist_relation
    ang_siz5a  = enum.auto()	
    # ang_siz6  = enum.auto() We skipped this in the voila version
    dot_seq5  = enum.auto()	
    dot_seq5a = enum.auto()	
    dot_seq5b = enum.auto()	
    dot_seq5c = enum.auto()	
    dot_seq6  = enum.auto()	# MC ang_meas_consensus_2
    dot_seq7 = enum.auto()	
    rep_rem1 = enum.auto()	
    fil_rem1 = enum.auto()


@dataclass
class ComponentState(BaseComponentState):

    current_step: Reactive[Marker] = field(
        default=Reactive(Marker.ang_siz1)
    )
    example_angular_sizes_total: Reactive[int] = field(default=Reactive(0))
    angular_sizes_total: Reactive[int] = field(default=Reactive(0))
    dosdonts_tutorial_opened: Reactive[bool] = field(
        default=Reactive(False)
    )
    selected_galaxy: Reactive[dict] = field(default=Reactive({}))
    selected_example_galaxy: Reactive[dict] = field(default=Reactive({}))
    show_ruler: Reactive[bool] = field(default=Reactive(False))
    meas_theta: Reactive[float] = field(default=Reactive(0.0))
    ruler_click_count: Reactive[int] = field(default=Reactive(0))
    n_meas: Reactive[int] = field(default=Reactive(0))

    def setup(self):
        def _on_example_galaxy_selected(*args):
            if self.is_current_step(Marker.cho_row1):
                self.transition_to(Marker.ang_siz2)

        self.selected_example_galaxy.subscribe(_on_example_galaxy_selected)

        def _on_ruler_clicked_first_time(*args):
            if self.is_current_step(Marker.ang_siz3) and self.ruler_click_count.value == 1:
                self.transition_to(Marker.ang_siz4)

        self.ruler_click_count.subscribe(_on_ruler_clicked_first_time)

        def _on_measurement_added(*args):
            if self.is_current_step(Marker.ang_siz4) and self.n_meas.value == 1:
                self.transition_to(Marker.ang_siz5)

        self.n_meas.subscribe(_on_measurement_added)
    
    @computed_property
    def ang_siz2_gate(self):
        return bool(self.selected_example_galaxy.value)
    
    @computed_property
    def ang_siz4_gate(self):
        return self.ruler_click_count.value == 1
    
    @computed_property
    def ang_siz5_gate(self):
        return self.n_meas.value > 0

    @computed_property
    def dot_seq3_gate(self):
        return LOCAL_STATE.question_completed("ang_meas_consensus")
    
    @computed_property
    def ang_siz5a_gate(self):
        return LOCAL_STATE.question_completed("ang_meas_dist_relation")
    
    @computed_property
    def dot_seq7_gate(self):
        return LOCAL_STATE.question_completed("ang_meas_consensus_2")
    
    @computed_property
    def dot_seq5_gate(self):
        return (
            bool(self.dosdonts_tutorial_opened.value)
        )
    