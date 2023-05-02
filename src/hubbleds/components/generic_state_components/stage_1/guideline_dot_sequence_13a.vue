<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :can-advance="(state) => state.meas_two_made"
    :state="state"
  >
      <!-- :can-advance="(state) => state.meas_two_made" -->
    <template #before-next>
      Measure wavelength
    </template>
    <div>
      <p>
       Remeasure the wavelength of the spectral line keeping in mind what you learned from the dot plots. 
        <!-- {{ state.meas_two_made ? 'You have measured the wavelength of the spectral line.' : '' }} -->
      </p>
    </div>
  </scaffold-alert>
</template>




<script>
module.exports = {
 props: ['state']
}
</script>
