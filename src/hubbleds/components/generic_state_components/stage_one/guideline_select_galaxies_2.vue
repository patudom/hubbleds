<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Select Your Galaxies"
    @back="() => { state.marker = 'sel_gal1'; }"
    :can-advance="(_state) => false"
    :state="state"
  >

    <template #before-next>
      <div>
        <div
          v-if="state.gals_total < 5 && state.gals_total > 0"
          style="font-size: 16px;"
        >
          Select {{ 5 - state.gals_total }} <span v-if="state.gals_total > 0">more</span> <span v-if="state.gals_total < 4">galaxies</span><span v-if="state.gals_total == 4">galaxy</span>.
        </div>
        <div
          v-if="state.gals_total == 0 && !state.gal_selected"
          style="font-size: 16px;"
        >
          Click on any green dot.
        </div>
        <div
          v-if="state.gals_total == 0 && state.gal_selected"
          style="font-size: 16px;"
        >
          Click <v-icon>mdi-plus</v-icon> to add galaxy or <v-icon>mdi-cached</v-icon> to choose another
        </div>
      </div>
    </template>

    <div
      v-if="state.gals_total == 0 && !state.gal_selected"
      class="mb-4"
    >
      <p>
        The green dots in the Cosmic Sky Viewer mark the locations of galaxies you can collect data for. 
      </p>
      <p>
        Pan around the sky and click on one of these dots to select that galaxy.
      </p>
    </div>
    <div
      v-if="state.gals_total < 5 && state.gal_selected"
    >
      <p>
        What do you think of this galaxy?
      </p>
      <p>
        If it looks good to you, click the <v-icon>mdi-plus</v-icon> button to add it to your galaxy collection.
      </p>
      <p>
        If you’d rather look for another galaxy, click the <v-icon>mdi-cached</v-icon> button to reset the view and choose a different green dot.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
