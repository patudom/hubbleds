from solara import Reactive
import solara
import enum
from ...marker_base import MarkerBase
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


class Marker(MarkerBase, enum.Enum):
    exp_dat1 = enum.auto()
    tre_dat1 = enum.auto()
    tre_dat2 = enum.auto()
    tre_dat3 = enum.auto()
    rel_vel1 = enum.auto()
    hub_exp1 = enum.auto()
    tre_lin1 = enum.auto()
    tre_lin2 = enum.auto()
    bes_fit1 = enum.auto()
    age_uni1 = enum.auto()
    hyp_gal1 = enum.auto()
    age_rac1 = enum.auto()
    age_uni2 = enum.auto()
    age_uni3 = enum.auto()
    age_uni4 = enum.auto()
    you_age1 = enum.auto()
    sho_est1 = enum.auto()
    sho_est2 = enum.auto()


@dataclasses.dataclass
class HubbleSlideshowState:
    step: Reactive[int] = dataclasses.field(default=Reactive(0))
    max_step_completed: Reactive[int] = dataclasses.field(default=Reactive(0))

@dataclasses.dataclass
class ComponentState:
    current_step: Reactive[Marker] = dataclasses.field(
        default=Reactive(Marker.exp_dat1)
    )
    hubble_slideshow_dialog: Reactive[bool] = dataclasses.field(default=Reactive(False))
    hubble_slideshow_finished: Reactive[bool] = dataclasses.field(
        default=Reactive(False)
    )
    hubble_slideshow_state: HubbleSlideshowState = dataclasses.field(
        default_factory=HubbleSlideshowState
    )

    def setup(self):
        pass

    def is_current_step(self, step: Marker):
        return self.current_step.value == step

    def can_transition(self, step: Marker = None, next=False, prev=False):
        if next:
            if self.current_step.value is Marker.last():
                return False  # FIX once we sort out transitions between stages
            step = Marker.next(self.current_step.value)
        elif prev:
            if self.current_step.value is Marker.first():
                return False  # FIX once we sort out transitions between stages
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
    def tre_lin1_gate(self):
        return (
            bool(self.hubble_slideshow_finished.value)
        )
