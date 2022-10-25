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
        .add questions about how it relates to your confidence interval values..
      </p>
    </div>
  </scaffold-alert>
</template>
