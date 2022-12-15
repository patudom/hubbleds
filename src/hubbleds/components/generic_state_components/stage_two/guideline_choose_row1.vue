<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Choose a Galaxy"
    @back="state.marker = 'ang_siz1'"
    @next="state.marker = 'ang_siz2'"
    :can-advance="(state) => state.galaxy_selected"
    :state="state"
  >
    <template #before-next>
      Select a galaxy from your table.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Click a row in your table to choose one of your galaxies.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
