import dataclasses
from hubbleds.decorators import computed_property
from solara import Reactive
import enum

from hubbleds.state import LOCAL_STATE
from hubbleds.marker_base import MarkerBase

__all__ = ["Marker", "ComponentState"]

class Marker(enum.Enum, MarkerBase):
    ran_var1 = enum.auto()
    fin_cla1 = enum.auto()
    cla_res1 = enum.auto()
    rel_age1 = enum.auto()
    cla_age1 = enum.auto()
    cla_age2 = enum.auto()
    cla_age3 = enum.auto()
    cla_age4 = enum.auto()
    lea_unc1 = enum.auto()
    mos_lik1 = enum.auto()
    age_dis1 = enum.auto()
    mos_lik2 = enum.auto()
    mos_lik3 = enum.auto()
    mos_lik4 = enum.auto()
    con_int1 = enum.auto()
    con_int2 = enum.auto()
    con_int3 = enum.auto()

    cla_dat1 = enum.auto()
    tre_lin2c = enum.auto()
    bes_fit1c = enum.auto()
    you_age1c = enum.auto()
    cla_res1c = enum.auto()
    cla_age1c = enum.auto()
    age_dis1c = enum.auto()
    con_int2c = enum.auto()
    
    two_his1 = enum.auto()
    two_his2 = enum.auto()
    two_his3 = enum.auto()
    two_his4 = enum.auto()
    two_his5 = enum.auto()
    mor_dat1 = enum.auto()


@dataclasses.dataclass
class UncertaintyState:
    step: Reactive[int] = dataclasses.field(default=Reactive(0))

@dataclasses.dataclass
class MMMState:
    step: Reactive[int] = dataclasses.field(default=Reactive(0))
    length: Reactive[int] = dataclasses.field(default=Reactive(3))
    titles: Reactive[list] = dataclasses.field(
        default=Reactive(
            [
                "Mean",
                "Median",
                "Mode",
            ]
        )
    )


@dataclasses.dataclass
class AgeCalcState:
    hint1_dialog: Reactive[bool] = dataclasses.field(default=Reactive(False))
    hint2_dialog: Reactive[bool] = dataclasses.field(default=Reactive(False))
    hint3_dialog: Reactive[bool] = dataclasses.field(default=Reactive(False))
    best_guess: Reactive[int] = dataclasses.field(default=Reactive(0))
    low_guess: Reactive[int] = dataclasses.field(default=Reactive(0))
    high_guess: Reactive[int] = dataclasses.field(default=Reactive(0))
    short_one: Reactive[str] = dataclasses.field(default=Reactive("dummy shortcoming 1"))
    short_two: Reactive[str] = dataclasses.field(default=Reactive("dummy shortcoming 2"))
    short_other: Reactive[str] = dataclasses.field(default=Reactive("dummy shortcoming other"))


@dataclasses.dataclass
class ComponentState:
    current_step: Reactive[Marker] = dataclasses.field(default=Reactive(Marker.ran_var1))
    student_low_age: Reactive[int] = dataclasses.field(default=Reactive(0))
    student_high_age: Reactive[int] = dataclasses.field(default=Reactive(0))
    class_low_age: Reactive[int] = dataclasses.field(default=Reactive(0))
    class_high_age: Reactive[int] = dataclasses.field(default=Reactive(0))
    uncertainty_state: UncertaintyState = dataclasses.field(default_factory=UncertaintyState)
    uncertainty_slideshow_finished: Reactive[bool] = dataclasses.field(
        default=Reactive(False)
    )
    mmm_state: MMMState = dataclasses.field(default_factory=MMMState)
    age_calc_state: AgeCalcState = dataclasses.field(default_factory=AgeCalcState)

    def is_current_step(self, step: Marker):
        return self.current_step.value == step

    def can_transition(self, step: Marker=None, next=False, prev=False):
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
    def mos_lik1_gate(self):
        return (
            bool(self.uncertainty_slideshow_finished.value)
        )
