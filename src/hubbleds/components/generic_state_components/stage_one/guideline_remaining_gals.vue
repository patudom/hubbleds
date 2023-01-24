<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :can-advance="(state) => state.obswaves_total >= 5"
    :title-text="state.obswaves_total < 5 ? 'Repeat for Remaining Galaxies' : 'Nice Work'
    "
    :state="state"
  >
    <template #before-next>
      Measure wavelength<span v-if="state.obswaves_total < 4">s</span> for {{ 5 - state.obswaves_total }} more <span v-if="state.obswaves_total < 4">galaxies</span><span v-if="state.obswaves_total == 4">galaxy</span>.
    </template>

    <div
      class="mb-4"
      v-if="state.obswaves_total < 5"
    >
      <p>
        Your measurement of the line’s observed wavelength is now recorded in the table for your selected galaxy.
      </p>
      <p>
        Go through each of the remaining galaxies in your table and repeat these measurements, until you have recorded rest and observed wavelengths for each of your galaxies.
      </p>
    </div>
    <div
      class="mb-4"
      v-if="state.obswaves_total >= 5"
    >
      <p>
        You have measured the spectral line wavelengths for all of your galaxies.
      </p>
      <p>
        You can continue to refine your measurements, or, if you are satisfied with your measurements, you can move on.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
