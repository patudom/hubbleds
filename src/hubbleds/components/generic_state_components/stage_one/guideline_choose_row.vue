<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Choose a Row"
    @back="() => state.marker = 'sel_gal3'"
    @next="() => state.marker = 'mee_spe1'"
    next-text="Select a galaxy from your table."
    :can-advance="() => state.spec_viewer_reached"
    :state="state"
  >
    <div class="mb-4">
      <p>
      Let's look at the light spectrum for one of your galaxies.
      </p>
      <p>
      Click on a row in your table to choose that galaxy.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
