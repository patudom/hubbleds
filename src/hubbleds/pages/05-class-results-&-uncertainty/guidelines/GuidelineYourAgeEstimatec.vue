<!-- this state.marker = 'you_age1' -->
<template>
  <scaffold-alert
    title-text="Your Age Estimate"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        How did your drawn trend line compare with your class's best fit line? Were they closer together than the lines for your own five galaxies?
      </p>
      <p>
        The fit line is labeled with your class's age estimate. How does it compare with the most likely age and confidence interval you identified earlier? Notice whether the best fit age is within the bounds you chose: <StudentResponse class="StudentResponses">{{ state_view.low_guess }}</StudentResponse> to <StudentResponse class="StudentResponses">{{ state_view.high_guess }}</StudentResponse>&nbsp;Gyr, with a most likely value of <StudentResponse class="StudentResponses">{{ state_view.best_guess }}</StudentResponse>&nbsp;Gyr.
      </p>
    </div>
  </scaffold-alert>
</template>

