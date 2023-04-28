<template>
  <scaffold-alert
    title-text="Velocity and Wavelength"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Your measured wavelength is marked in orange-red on the spectrum viewer.
      </p>
      <span style="color:#1DE9B6!important">
        <strong>This guidline is where wavelength marker should turn on in viewer.</strong>
      </span>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
