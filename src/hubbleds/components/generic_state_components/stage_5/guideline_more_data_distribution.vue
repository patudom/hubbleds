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
        When you have random uncertainties in your measurement, the data points that are the most inaccurate (outliers) matter more when you have a small number of measurements. This is because most data points will tend to cluster closer to their expected true values. However, there is a chance you could measure an outlier.
      </p>
      <p>
        If you have <strong>3 close-to-accurate</strong> data points and <strong>2 outliers</strong>, the overall result will be more inaccurate than if you have, say, <strong>98 close-to-accurate</strong> data points and <strong>2 outliers</strong>.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
