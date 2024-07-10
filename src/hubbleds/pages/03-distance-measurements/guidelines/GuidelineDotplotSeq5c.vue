<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Second Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    >
    <div class="mb-4">
      <p>
        Your angular size and distance measurements are now entered in the table.
      </p>
      <p>
        Click and drag the ends of the green measurement line if you want to make adjustments.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
