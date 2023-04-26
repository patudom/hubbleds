<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Second Measurement Comparison"
    @back="state.marker = 'dot_seq5'"
    @next="state.marker = 'dot_seq5b'"
    :can-advance="(state) => state.exgal_second_row_selected"
    :state="state"
    >
    <template #before-next>
        Select second measurement row
    </template>
    <div class="mb-4">
      <p>
        Click on the new row labeled <strong>second</strong> to remeasure the galaxy angular size.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
