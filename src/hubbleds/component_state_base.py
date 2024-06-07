import dataclasses

from solara import Reactive

from hubbleds.marker_base import MarkerBase


class BaseComponentState:

   current_step: Reactive[MarkerBase] = dataclasses.field()

   def is_current_step(self, step):
       return self.current_step.value.value == step.value

   def can_transition(self, step: MarkerBase = None, next=False, prev=False):
       current_step = self.current_step.value
       if next:
           if current_step is current_step.last():
               return False  # TODO: Fix once we sort out transitions between stages
           step = current_step.next(current_step)
       elif prev:
           if current_step is current_step.first():
               return False  # TODO: Fix once we sort out transitions between stages
           step = current_step.previous(current_step)

       if hasattr(self, f"{step.name}_gate"):
           return getattr(
               self,
               f"{step.name}_gate",
           )().value

       print(f"No gate exists for step {step.name}, allowing anyway.")
       return True

   def transition_to(self, step: MarkerBase, force=False):
       if self.can_transition(step) or force:
           self.current_step.set(step)
       else:
           print(
               f"Conditions not met to transition from "
               f"{self.current_step.value.name} to {step.name}."
           )

   def transition_next(self):
       next_marker = self.current_step.value.next(self.current_step.value)
       self.transition_to(next_marker)

   def transition_previous(self):
       previous_marker = self.current_step.value.previous(self.current_step.value)
       self.transition_to(previous_marker, force=True)

   def current_step_between(self, start, end=None):
       end = end or self.current_step.value.last()
       return self.current_step.value.is_between(self.current_step.value, start, end)
   
   def current_step_this_or_before(self, end):
       return self.current_step.value.is_this_or_before(self.current_step.value, end)
   
   def current_step_this_or_after(self, start):
       return self.current_step.value.is_this_or_after(self.current_step.value, start)

