<template>
  <scaffold-alert
    title-text="Velocity and Wavelength"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Move your mouse left and right in the velocity dot plot. 
      </p>
      <p>
        Notice that the marker in the spectrum viewer moves to the corresponding wavelengths.
      </p>
      <p>
        See if you can identify features in the spectrum viewer that correspond to outliers and other velocity measurements.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
