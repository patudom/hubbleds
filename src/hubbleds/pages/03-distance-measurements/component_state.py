from solara import Reactive
import solara
import enum
from ...decorators import computed_property
import dataclasses
from cosmicds.utils import API_URL
from ...state import GLOBAL_STATE
from ...data_models.student import example_data, StudentMeasurement, SpectrumData
from contextlib import closing
from io import BytesIO
from astropy.io import fits


ELEMENT_REST = {
    'H-α': 6562.79,
    'Mg-I': 5176.7
}


class Marker(enum.Enum):
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
    ang_siz6  = enum.auto()
    dot_seq5  = enum.auto()	
    dot_seq5a = enum.auto()	
    dot_seq5b = enum.auto()	
    dot_seq5c = enum.auto()	
    dot_seq6  = enum.auto()	
    dot_seq7 = enum.auto()	
    rep_rem1 = enum.auto()	
    fil_rem1 = enum.auto()	

    @staticmethod
    def next(step):
        return Marker(step.value + 1)

    @staticmethod
    def previous(step):
        return Marker(step.value - 1)


@dataclasses.dataclass
class ComponentState:
    current_step: Reactive[Marker] = dataclasses.field(
        default=Reactive(Marker.ang_siz1)
    )
    dosdonts_tutorial_opened: Reactive[bool] = dataclasses.field(
        default=Reactive(False)
    )

    def is_current_step(self, step: Marker):
        return self.current_step.value == step

    def can_transition(self, step: Marker = None, next=False, prev=False):
        if next:
            step = Marker.next(self.current_step.value)
        elif prev:
            step = Marker.previous(self.current_step.value)

        if hasattr(self, f"{step.name}_gate"):
            return getattr(
                self,
                f"{step.name}_gate",
            )().value

        print(f"No gate exists for step {step.name}, allowing anyway.")
        return True

    def transition_to(self, step: Marker, force=False):
        if self.can_transition(step) or force:
            self.current_step.set(step)
        else:
            print(
                f"Conditions not met to transition from "
                f"{self.current_step.value.name} to {step.name}."
            )

    def transition_next(self):
        next_marker = Marker.next(self.current_step.value)
        self.transition_to(next_marker)

    def transition_previous(self):
        previous_marker = Marker.previous(self.current_step.value)
        self.transition_to(previous_marker, force=True)

    @computed_property
    def ang_siz6_gate(self):
        return (
            bool(self.dosdonts_tutorial_opened.value)
        )