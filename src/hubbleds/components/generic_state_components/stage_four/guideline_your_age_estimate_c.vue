<!-- this state.marker = 'you_age1' -->
<template>
  <scaffold-alert
    title-text="Your Age Estimate"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        How did your drawn trend line compare with your class's best fit line? Were they closer together than the lines for your own five galaxies?
      </p>
      <p>
        The fit line is labeled with your class's age estimate. How does it compare with the "best guess" age and confidence intervals you identified earlier? Notice whether the best fit age is within the bounds you chose: <StudentResponse class="pa-1 StudentResponses">{{ state.age_calc_state.low_guess }}</StudentResponse> to <StudentResponse class="pa-1 StudentResponses">{{ state.age_calc_state.high_guess }}</StudentResponse> Gyr, with a best guess of <StudentResponse class="pa-1 StudentResponses">{{ state.age_calc_state.best_guess }}</StudentResponse> Gyr.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
