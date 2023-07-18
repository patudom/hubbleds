<template>
  <scaffold-alert
    title-text="Class Age Distribution"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        Here is a histogram of the class by class age measurements.
      </p>
      <p>
        Explore the mean, median, and mode and the different percentage ranges for the All Classes dataset. 
      </p>
    </div>
  </scaffold-alert>
</template>

<style>
  .JaxEquation .MathJax {
    margin: 3px auto !important;
  }
</style>

<script>
module.exports = {
  props: ['state']
}
</script>
