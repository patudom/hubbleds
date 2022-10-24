<template>
  <scaffold-alert
    header-text="Best Fit Line"
    @back="
      state.marker = 'tre_lin2c';
    "
    @next="
      state.marker = 'age_uni1c';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Depending on how messy your dataset is, it may be tricky to draw a trendline. We can use a formula to calculate the <strong>best-fit line</strong>, no matter how messy your data are. A best-fit-line minimizes the total distance between all the data points and the line. Let’s see how the calculated best-fit line compares with your trend line.
      </p>
      <p>
        Click on <v-icon>mdi-chart-timeline-variant</v-icon> in the Toolbar to display the best fit line.
      </p>
    </div>
  </scaffold-alert>
</template>
