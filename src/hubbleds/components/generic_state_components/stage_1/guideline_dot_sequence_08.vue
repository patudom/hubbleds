<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :can-advance="(state) => state.dot_zoomed"
    :state="state"
  >
    <template #before-next>
      Zoom in
    </template>
    <div>
      <p>
        Click and drag across the cluster of velocity measurements to zoom in.
      </p>
      <span style="color:#1DE9B6!important">After user zooms in, autoadvance to next guideline</span>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
