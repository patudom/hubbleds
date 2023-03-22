<template>
  <scaffold-alert
    title-text="Velocity Calculation"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        Now, you will use the observed wavelength of the H-alpha spectral line to determine the galaxy's velocity, using the <strong>Doppler Equation</strong>.

      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
