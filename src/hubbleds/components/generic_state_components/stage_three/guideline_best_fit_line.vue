<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Best Fit Line"
    @back="state.marker = 'tre_lin2'"
    @next="state.marker = 'age_uni1'"
    :can-advance="(state) => state.best_fit_clicked"
    :state="state"
  >
    <template #before-next>
      Click <v-icon>mdi-chart-timeline-variant</v-icon> to show best fit.
    </template>

    <div class="mb-4">
      <p>
        Depending on how messy your dataset is, it may be tricky to draw a trendline. We can use a formula to calculate the <strong>best-fit line</strong>, no matter how messy your data are. A best-fit-line minimizes the total distance between all the data points and the line. Let’s see how the calculated best-fit line compares with your trend line.
      </p>
      <p>
        Click on <v-icon>mdi-chart-timeline-variant</v-icon> in the Toolbar to display the best fit line.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
