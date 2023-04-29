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
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
