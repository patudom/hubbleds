<template>
  <scaffold-alert
    title-text="Angular Size Measurement"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        If necessary, click and drag the ends of the measurement tool to make a second measurment for the example galaxy
      </p>
      <p>
        <!-- The table will update to display your most recent angular size (distance) measurement. -->
      </p>
    </div>
  </scaffold-alert>
</template>
