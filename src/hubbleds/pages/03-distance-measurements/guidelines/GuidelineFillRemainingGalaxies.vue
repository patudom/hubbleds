<template>
  <scaffold-alert
    title-text="Estimate Distance"
    next-text="stage 4"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-tape-measure</v-icon></v-btn> in toolbar
    </template>

    <div
      v-if="state.distances_total < 5"
      class="mb-4"
    >
      <p>
        Now we can use the same distance equation from earlier.
      </p>
      <p>
        Click the <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-tape-measure</v-icon></v-btn> icon in the table toolbar to auto-calculate distances for the remaining galaxies.
      </p>
    </div>
    <div
        v-if="state.distances_total === 5"
        class="mb-4"
    >
      <p>Distances have been entered in the table. Proceed to Stage 4.</p>
    </div>
  </scaffold-alert>
</template>
