<template>
  <scaffold-alert
    header-text="Best Fit Line"
    @back="
      state.marker = 'tre_lin2c';
    "
    @next="
      state.marker = 'you_age1c';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Now let's look at the best-fit line for your class's data and see how that compares with your trend line.
      </p>
      <p>
        Click on <v-icon>mdi-chart-timeline-variant</v-icon> in the Toolbar to display the best fit line.
      </p>
    </div>
  </scaffold-alert>
</template>
