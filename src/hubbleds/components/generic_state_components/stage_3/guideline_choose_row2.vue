<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Choose a Galaxy"
    @back="state.marker = 'est_dis2'"
    @next="state.marker = 'est_dis3'"
    :can-advance="(state) => state.galaxy_selected"
    :state="state"
  >
    <template #before-next>
      Select example galaxy from table.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Select the example galaxy to estimate its distance.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
