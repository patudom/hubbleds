<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        To make sure everyone is making the best measurements, use the measuring tool to compare which spectrum features match the velocity bins.
        
      </p>
      <p>
        (Notice we zoomed in to the corresponding wavelength range in the spectrum viewer below.)
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>