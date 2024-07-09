<template>
  <scaffold-alert
    title-text="Simple Guideline Example"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <h3 class="test-page"> This is a test page Marker 1 </h3>
    <div class="mb-4">
      <p> My first guideline just shows some text </p>
    </div>
  </scaffold-alert>
</template>

<script>
</script>

<style>
h3.test-page {
  color: rgb(0, 255, 30);
}
</style>