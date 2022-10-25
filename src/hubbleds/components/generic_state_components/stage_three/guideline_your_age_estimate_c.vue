<template>
  <scaffold-alert
    header-text="Your Age Estimate"
    @back="
      state.marker = 'bes_fit1c';
    "
    @next="
      state.marker = 'cla_res1c';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Notice your best-fit line is now labeled with the age estimate based on your whole class's dataset.
      </p>
      <p>
        You can compare this way of estimating the age of the universe from your class's dataset with the "best guess" and confidence intervals you identified earlier. Notice whether the best fit age is within the bounds you chose.
      </p>
    </div>
  </scaffold-alert>
</template>
