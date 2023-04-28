<template>
  <scaffold-alert
    title-text="Consensus"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        The first thing to check is whether there is <strong>consensus</strong> in everyone's measurements.
      </p>
      <p>
        If there is consensus, the measurements will tend to cluster around a single value.
      </p>
      <p>
        If there is not consensus, the measurements will be scattered across a range of values or clustered around more than one value.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
