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
        Click on a velocity to mark the corresponding wavelength in the spectrum viewer below.
      </p>
      <p>
        See if you can identify features in the spectrum viewer that correspond to outliers or to the larger cluster of velocity measurements.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
