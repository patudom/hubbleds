<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
       This bottom dot plot shows second measurements. Zoom in to see if there is more consensus in the second measurements than for the first measurements above.
      </p>
    </div>
  </scaffold-alert>
</template>




<script>
module.exports = {
 props: ['state']
}
</script>
