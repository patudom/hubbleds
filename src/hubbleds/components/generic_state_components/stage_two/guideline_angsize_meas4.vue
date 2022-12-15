<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Angular Size Measurement"
    @back="state.marker = 'ang_siz3'"
    @next="state.marker = 'ang_siz5'"
    :can-advance="(state) => state.n_meas > 0"
    :state="state"
  >
    <template #before-next>
      Measure angular size of galaxy
    </template>

    <div
      class="mb-4"
    >
      <p>
        Click on one edge of your galaxy to mark the ruler's starting point.
      </p>
      <p>
        With the button held down, drag to the other edge of your galaxy and release the button.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
