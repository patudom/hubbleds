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
      Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-tape-measure</v-icon></v-btn> in toolbar
    </template>

    <div
      class="mb-4"
    >
      <p>
        The distance estimate for your galaxy has been entered into the table.
      </p>
      <p>
        Click the <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-tape-measure</v-icon></v-btn> icon in the table toolbar to calculate distances for the remaining galaxies.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
