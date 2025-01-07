<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
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
        This dot plot shows the distribution of distances measured.
      </p> 
      <p>
        The {{ state_view.color }} dot shows your measurement. 
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
