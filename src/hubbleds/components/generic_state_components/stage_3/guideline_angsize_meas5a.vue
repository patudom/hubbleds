<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Angular Size Measurement"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
    :can-advance="(state) => state.dos_donts_opened"
    :state="state"
  >
    <template #before-next>
      Click <span style="background-color: #02838f; border-radius: 5px; padding: 3px; color:white!important;">MEASUREMENT DOS AND DONTS</span> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        You may adjust your measurement by clicking on the ends of the green line and moving them to a new location.
      </p>
      <p>
        Click <span style="background-color: #02838f; border-radius: 5px; padding: 3px; color:white!important;">MEASUREMENT DOS AND DONTS</span> for tips on how to ensure the most accurate results.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
