<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Choose a Galaxy"
    @back="state.marker = 'est_dis2'"
    @next="state.marker = 'est_dis3'"
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
        Click on a row to choose a galaxy whose distance we will estimate.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
