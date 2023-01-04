<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Table Data"
    @back="() => { state.marker = 'sel_gal1'; }"
    @next="() => { state.marker = 'sel_gal3'; }"
  >
    <div
      class="mb-4"
    >
      <p>
        Notice that your My Galaxies table now has a row for your selected galaxy, and the marker on your galaxy has changed from green to yellow.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
