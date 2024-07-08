<template>
  <!-- We will need to update the can-advance condition to switch from false to true when the angular size is measured, but I don't know how to wire that up, so leaving this for later -->
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
    <template #before-next>
        Remeasure galaxy angular size
    </template>
    <div class="mb-4">
      <p>
        Remeasure the galaxy angular size, keeping the dos and don'ts in mind. 
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
