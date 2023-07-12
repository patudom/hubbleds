<template>
  <scaffold-alert
    title-text="Select Best Value"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
    <p>
      When identifying the “most likely value” for a measurement, it is helpful to consider 3 particular values that can be identified based on a group of measurements.
    </p>
    Check the different boxes for Mean, Median, and Mode to see where these values lie on your class’s histogram of age measurements.
    <p>
    Click the ? for more information about each quantity.
    </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
