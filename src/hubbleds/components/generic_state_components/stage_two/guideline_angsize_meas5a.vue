<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Angular Size Measurement"
    @back="state.marker = 'ang_siz5'"
    @next="state.marker = 'ang_siz6'"
    :can-advance="(state) => state.dos_donts_opened"
    :state="state"
  >
    <template #before-next>
      Click the <strong>MEASUREMENT DOS AND DONTS</strong> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        You may adjust your measurement by clicking on the ends of the green line and moving them to a new location.
      </p>
      <p>
        Click <strong>MEASUREMENT DOS AND DONTS</strong> for tips on how to ensure the most accurate results.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
