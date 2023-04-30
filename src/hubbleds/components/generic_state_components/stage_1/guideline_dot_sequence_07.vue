<template>
  <scaffold-alert
    title-text="Consensus"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        With a wisdom of crowds approach, we hope to see <strong>consensus</strong> in everyone's measurements.
      </p>
      <p>
        <strong>consensus</strong>: measurements tend to cluster around a single value.
      </p>
      <p>
        <strong>no consensus</strong>: measurements are scattered across a range of values or clustered around more than one value.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
