<template>
  <scaffold-alert
    title-text="Simple Guideline Example"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <h3 class="test-page"> Guideline 4 </h3>
    <div class="mb-4">
      <p> Test end stage guideline </p>
      <p> 
        can_advance is {{ can_advance }} 
        because end of stage checks are not implemented
      </p>
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