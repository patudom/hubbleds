<template>
  <scaffold-alert
    title-text="Consensus"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div>
      <p>
        With a wisdom of crowds approach, we hope to see <b>consensus</b> in everyone's measurements.
      </p>
      <p>
        <b>consensus</b>: measurements tend to cluster around a single value.
      </p>
      <p>
        <b>no consensus</b>: measurements are scattered across a range of values or clustered around more than one value.
      </p>
    </div>
  </scaffold-alert>
</template>
