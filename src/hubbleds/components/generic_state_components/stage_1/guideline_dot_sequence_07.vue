<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :can-advance="(state) => state.dot_zoom_activated"
    :state="state"
  >
    <template #before-next>
      Click <span style="color:#1DE9B6!important">magnifying glass icon</span>
    </template>
    <div>
      <p>
        Let's take a closer look at the cluster of measurements to the right of the graph. Click <span style="color:#1DE9B6!important">insert magnifying glass icon here</span> to activate the zoom tool.
      </p>
      <span style="color:#1DE9B6!important">After zoom tool is activated, autoadvance to next guideline</span>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
