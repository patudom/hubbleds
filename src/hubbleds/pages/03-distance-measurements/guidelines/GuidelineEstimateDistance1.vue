<template>
  <scaffold-alert
    title-text="Estimate Distance"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Now that you have an angular size measurement for the example galaxy, let’s estimate how far away it is.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>

