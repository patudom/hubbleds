<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Select Your Galaxies"
    @back="() => { state.marker = 'mee_gui1'; }"
    @next="() => {
      if (state.gals_total == 0) {
        state.marker = 'sel_gal2';
      } else if (state.gals_total > 0) {
        state.marker = 'sel_gal3';
      } 
    }"
  >
    <div
      class="mb-4"
    >
      <p>
        This is a view of the cosmic sky, like the one you explored in the introduction. This view shows a more modern data set from the Sloan Digital Sky Survey (SDSS), which has collected imaging and spectral data for millions of galaxies. 
      </p>
      <p>
        This Data Story will focus on a nearby subset of spiral galaxies.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
