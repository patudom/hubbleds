<!-- this state.marker = 'mor_dat1' -->
<template>
  <scaffold-alert
    title-text="More Data and Narrow Distributions"
    next-text="stage 6"
    @next="next_callback()"
    @back="back_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        In general, using a smaller number of data points to measure a quantity will result in larger uncertainties than if you use a larger number of data points.
      </p>
      <p> 
        This is because outliers matter less in a large data set. Say one person measures the age of the universe with 5 galaxies and another uses 100 galaxies. Now imagine both have 2 galaxies that are outliers. The small data set would only have 3 "typical" galaxies to balance out the outliers, while the large data set would have 98.
      </p>
    </div>
    <v-btn
          block
          color="deep-orange darken-2"
          @click="
            define_outlier = !define_outlier
          "
        >
          What is an outlier?
        </v-btn>
        <v-alert
          class="mt-4 trend-alert"
          v-if="define_outlier"
          dense
          color="info darken-1"
        >
          An outlier is an unusual data point that lies significantly far away from the other data points. 
        </v-alert>
  </scaffold-alert>
</template>

<script>
module.exports = {
  data() {
    return {
      define_outlier: false,
    };
  },
}
</script>
