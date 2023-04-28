<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Without consensus, it helps to check again what wavelength measurements correspond with the different clusters of velocity measurements.
      </p>
      <p>
        Click on the velocity values to mark their corresponding wavelength in the spectrum viewer. (We have zoomed in to the corresponding wavelength range.)
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>