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
        Now that you know your observed galaxies are moving away from us, let's figure out <strong>how fast</strong> they are moving.
      </p>
      <p>
        Light from <strong>faster</strong> galaxies experiences a <strong>larger change</strong> in observed wavelength.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
