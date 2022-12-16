<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    :header-text="state.angsizes_total < 5 ? 'Repeat for Remaining Galaxies' : 'Nice Work'
    "
    @back="state.marker = 'ang_siz6'"
    @next="state.marker = 'est_dis1'"
    :can-advance="(state) => state.angsizes_total >= 5"
    :state="state"
  >
    <template #before-next>
      Measure angular size<span v-if="state.angsizes_total < 4">s</span> for {{ 5 - state.angsizes_total }} more <span v-if="state.angsizes_total < 4">galaxies</span><span v-if="state.angsizes_total == 4">galaxy</span>.
    </template>

    <div
      class="mb-4"
      v-if="state.angsizes_total < 5"
    >
      <p>
        Repeat the angular size measurements for each of the remaining galaxies in your table.
      </p>
    </div>
    <div
      class="mb-4"
      v-if="state.angsizes_total >= 5"
    >
      <p>
        You have measured the angular size for all of your galaxies.
      </p>
      <p>
        You can continue to refine your measurements, or, if you are satisfied with your measurements, you can move on.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
