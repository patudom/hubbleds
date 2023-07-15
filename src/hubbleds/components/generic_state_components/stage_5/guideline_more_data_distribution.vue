<!-- this state.marker = 'mor_dat1' -->
<template>
  <scaffold-alert
    title-text="More Data and Narrow Distributions"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        In general, using a smaller number of data points (say, 5 galaxies) to measure a quantity will result in larger uncertainties than if you use a larger number of data points (say, 100 galaxies).
      </p>
      <p>
        When there are random uncertainties in a measurement, most data points will tend to cluster closer to their expected true values, but a smaller number of data points (called <strong>outliers</strong>) will randomly be further away from the true value. 
      </p>
      <p> 
        When you have a large number of data points contributing to your measurement, outliers will matter less. Imagine you have <strong>3 close-to-accurate</strong> data points and <strong>2 outliers</strong>. The overall result will be more inaccurate than if you have, say, <strong>98 close-to-accurate</strong> data points and <strong>2 outliers</strong>.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
