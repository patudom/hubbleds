<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Second Measurement Comparison"
    @back="state.marker = 'dot_seq6'"
    @next="state.marker = 'rep_rem1'"
    :state="state"
    >
    <div class="mb-4">
      <p>
        With improved consensus in the distance measurements, you are ready to measure your five galaxies.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
