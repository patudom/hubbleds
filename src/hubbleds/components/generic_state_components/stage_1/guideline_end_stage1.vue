<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.stage_1_complete = true; }"
    next-text="stage 2"
    :state="state"
  >
    <div>
      <p>Great work! You have completed Stage 1. Proceed to Stage 2.</p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>