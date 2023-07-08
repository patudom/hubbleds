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
      When scientists make a measurement of an unknown quantity, they report the value that they think is most likely based on their measurements, and they report something called a confidence interval which gives lower and upper bounds on the most plausible range of measurement values.
    </p>
    <p>
      We'll guide you through how to do this for your class's measurements.
    </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
