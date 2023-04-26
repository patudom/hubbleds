<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Second Measurement Comparison"
    @back="state.marker = 'dot_seq5'"
    @next="state.marker = 'dot_seq6'"
    :can-advance="(state) => state.exgal_second_row_selected"
    :state="state"
    >
    <div class="mb-4">
      <p>
        Click on the second row with the <it>second</it> and make your second measurement considering the tips we've given on making accurate measurements. 
      </p>
      
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
