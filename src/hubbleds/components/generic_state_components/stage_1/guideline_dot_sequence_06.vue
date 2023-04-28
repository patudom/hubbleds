<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Let's now focus on the part of the dot plot that includes most of the data. (In other words, we will ignore outliers).
      </p>
      <p>
        As you did in the tutorial, use (zoom tool icon) to zoom in around the main cluster of data.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
