<template>
  <scaffold-alert
    title-text="Angular Size Measurement"
    @back="
      state.marker = 'cho_row1';
    "
    @next="
      state.marker = 'ang_siz2b';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Your galaxy now appears in the sky viewer. (You may need to wait a few moments for the full-resolution image to load.)
      </p>
      <p>
        If you zoom towards or away from your galaxy, notice that the angular scale (marked by the light blue line on the left) changes.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
