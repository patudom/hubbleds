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
    <template #before-next>
      nothing
    </template>

    <div
      class="mb-4"
    >
      <p>
        Let's see how your measurement compares with a random subset of measured values from others who have completed this Data Story.
      </p>
      <p>
        This dot plot shows the distrubution of distances measured.
      </p> 
      <p>
        The red dot shows your measurement. 
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
