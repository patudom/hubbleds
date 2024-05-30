import dataclasses
from typing import Generic, Type, TypeVar

from solara import Reactive

from hubbleds.marker_base import MarkerBase


MB = TypeVar('MB', bound=MarkerBase)


class BaseComponentState:

   current_step: Reactive[MB] = dataclasses.field()

   def is_current_step(self, step):
       return self.current_step.value.value == step.value

   def can_transition(self, step: M = None, next=False, prev=False):
       if next:
           step = M.next(self.current_step.value)
       elif prev:
           step = M.previous(self.current_step.value)

       if hasattr(self, f"{step.name}_gate"):
           return getattr(
               self,
               f"{step.name}_gate",
           )().value

       print(f"No gate exists for step {step.name}, allowing anyway.")
       return True

   def transition_to(self, step: M, force=False):
       if self.can_transition(step) or force:
           self.current_step.set(step)
       else:
           print(
               f"Conditions not met to transition from "
               f"{self.current_step.value.name} to {step.name}."
           )

   def transition_next(self):
       next_marker = M.next(self.current_step.value)
       self.transition_to(next_marker)

   def transition_previous(self):
       previous_marker = M.previous(self.current_step.value)
       self.transition_to(previous_marker, force=True)

   def current_step_between(self, start, end=None):
       end = end or M.last()
       return M.is_between(self.current_step.value, start, end)

