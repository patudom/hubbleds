<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Measurement Comparison"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
    :can-advance="(state) => true"
    :state="state"
  >

    <div
      class="mb-4"
    >
      <p>
        Click on the galaxy in the second row of the example galaxy table and then take a second measurement considering what you learned in the <span style="background-color: #02838f; border-radius: 5px; padding: 3px; color:white!important;">MEASUREMENT DOS AND DONTS</span>
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
