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
      When thinking about the range of ages that are most plausible based on your and your classmates’ measurements, it is helpful to visualize the data in a different way.
    </p>
    <p>
      This is a histogram which displays the distribution of your classmates' age estimates for the universe. The range of age values is shown on the x-axis, and the number of students who measured that value for the age of the universe is shown on the y-axis.
    </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
