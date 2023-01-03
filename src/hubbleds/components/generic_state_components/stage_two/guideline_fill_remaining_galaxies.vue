<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Estimate Distance"
    @back="state.marker = 'est_dis4'"
    @next="state.marker = 'two_com1'"
    :can-advance="(state) => state.distances_total == 5"
    :state="state"
  >
    <template #before-next>
      Click <v-icon>mdi-tape-measure</v-icon> in toolbar
    </template>

    <div
      class="mb-4"
    >
      <p>
        The distance estimate for your galaxy has been entered into the table.
      </p>
      <p>
        Click the <v-icon>mdi-tape-measure</v-icon> icon in the table toolbar to calculate distances for the remaining galaxies.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
