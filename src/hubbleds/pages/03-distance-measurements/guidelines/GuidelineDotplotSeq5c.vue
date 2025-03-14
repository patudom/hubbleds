<template>
  <scaffold-alert
    title-text="Second Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    >
    <div class="mb-4">
      <p>
        Note: If your new angular size measurement is larger than the "consensus", that does not mean your new measurement is wrong. It could mean, for example, that many students did not adjust the brightness of the galaxy when making their original measurement and may have missed the fainter parts of the galaxy, thereby underestimating the angular size and overestimating the distance. 
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
