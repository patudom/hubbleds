<!-- this state.marker = 'two_his1' -->
<template>
  <scaffold-alert
    header-text="Student Histogram vs. Class Histogram"
    @back="
      state.marker = 'con_int2c';
    "
    @next="
      state.marker = 'tru_age1';
    "
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
