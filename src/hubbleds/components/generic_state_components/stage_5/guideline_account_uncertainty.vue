<!-- this state.marker = 'acc_unc1' -->
<template>
  <scaffold-alert
    title-text="Accounting for Uncertainty"
    next-text="stage 6"
    @back="state.marker_backward = 1"
    @next="() => {$emit('stage_complete');}"
  >
    <div
      class="mb-4"
    >
      <p>
        Coming back to systematic uncertainty, if you have any bias in your methods or assumptions, that means your whole range of measured ages is slightly too high or too low.
      </p>
      <p>
        Figuring out and accounting for all the sources of uncertainty is usually the most difficult and most important task in a scientific experiment. Given that our time is limited, let’s just say that our results may have systematic uncertainty and leave it at that.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
