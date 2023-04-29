<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        It may have been tempting to choose the tallest line present, but you should always choose the line that aligns with the marker.
      </p>
    </div>
  </scaffold-alert>
</template>




<script>
module.exports = {
 props: ['state']
}
</script>