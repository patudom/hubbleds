<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Earlier, it might have seemed like there was consensus in our measurements, but now that we are zoomed in, notice that the velocities are actually clustered around multiple values.
      </p>
      <p>
        Click on different velocity values to see which features in the spectrum viewer they are connected to.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>