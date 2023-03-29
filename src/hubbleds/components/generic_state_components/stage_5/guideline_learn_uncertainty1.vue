<!-- this state.marker = 'lea_unc1' -->
<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Learn About Uncertainty"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
    :can-advance="(state) => state.uncertainty_dialog_complete"
    :state="state"
  >
   
    <template #before-next>
      Click the <strong>UNCERTAINTY TUTORIAL</strong> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Before we go further, let's explore some reasons <strong>why</strong> different students and different classes may have obtained different age values for the universe.
      </p>
      <p>
        We can explain this using a concept called <strong>uncertainty</strong>. Click the <strong>UNCERTAINTY TUTORIAL</strong> button to learn about this important concept for interpreting data.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
