<template>
  <scaffold-alert
    title-text="Best Fit Line"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-chart-timeline-variant</v-icon></v-btn> to show best fit.
    </template>

    <div class="mb-4">
      <p>
        Depending on how messy your dataset is, it may be tricky to draw a trendline. We can use a formula to calculate the <strong>best-fit line</strong>, no matter how messy your data are. A best-fit-line minimizes the total distance between all the data points and the line. Let’s see how the calculated best-fit line compares with your trend line.
      </p>
      <p>
        Click on <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-chart-timeline-variant</v-icon></v-btn> in the Toolbar to display the best fit line.
      </p>
    </div>
  </scaffold-alert>
</template>
