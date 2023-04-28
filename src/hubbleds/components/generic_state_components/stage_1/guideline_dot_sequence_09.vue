<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        You should see that the tall towers of dots have split into smaller towers across smaller velocity bins. If not, zoom in closer by clicking and dragging again, or click <span style="color:#1DE9B6!important">reset icon</span> to reset the view and try again.
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
