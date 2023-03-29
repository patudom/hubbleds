<!-- this state.marker = 'two_his1' -->
<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Student Histogram vs. Class Histogram"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
    :state="state"
  >
    <div
      class="mb-4"
    >
      <p>
        Everyone who participated in this data story followed the same procedure, measuring velocities and distances to galaxies, but they obtained different age values for the universe, given in these histograms. The student histogram tells you <strong>how many students</strong> obtained a particular age value, and the class histogram tells you <strong>how many classes</strong> obtained a particular age value.
      </p>
      <p>
        The student values are in the top graph and the class values are in the bottom graph.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
