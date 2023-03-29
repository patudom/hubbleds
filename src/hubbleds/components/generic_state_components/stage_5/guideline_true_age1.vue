<!-- this state.marker = 'tru_age1' -->
<template>
  <scaffold-alert
    title-text="Which Value Is the True Age?"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        There is only one universe that we live in, so our universe only has one age. Our job as scientists is to figure out if the <strong>true age</strong> of the universe is included within the ranges shown within these histograms, and if so, which value within the range is the true age.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
