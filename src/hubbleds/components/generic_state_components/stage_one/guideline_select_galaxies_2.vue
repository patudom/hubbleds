<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Select Your Galaxies"
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
        If it looks good to you, add it to your galaxy collection.
      </p>
      <p>
        If you’d rather look for another galaxy, reset the view and choose a different green dot.
      </p>
    </div>
    
    <v-divider
      class="my-4"
    >
    </v-divider>

    <v-row
      align="center"
      no-gutters
    >
      <v-col>
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'sel_gal1'
          "
        >
          back
        </v-btn>
      </v-col>
      <v-spacer></v-spacer>
      <v-col
        v-if="state.gals_total < 5 && state.gals_total > 0"
        cols="6"
        class="shrink"
      >
        <div
          style="font-size: 16px;"
        >
          Select {{ 5 - state.gals_total }} <span v-if="state.gals_total > 0">more</span> <span v-if="state.gals_total < 4">galaxies</span><span v-if="state.gals_total == 4">galaxy</span>.
        </div>
      </v-col>
      <v-col
        v-if="state.gals_total == 0 && !state.gal_selected"
        cols="6"
        class="shrink"
      >
        <div
          style="font-size: 16px; border-left: solid 3px #FFD740; padding-left: 10px; color: #FFF8E1;"
        >
          <strong style="color: white;">Click</strong> on any green dot.
        </div>
      </v-col>
      <v-col
        v-if="state.gals_total == 0 && state.gal_selected"
        cols="6"
        class="shrink"
      >
        <div
          style="font-size: 16px; border-left: solid 3px #FFD740; padding-left: 10px; color: #FFF8E1;"
        >
          <strong style="color: white;">Click</strong> <v-btn icon dark x-small disabled
            class="mx-1 black--text" elevation="2" style="background-color: #00E676;"><v-icon style="color:black!important;">mdi-plus</v-icon></v-btn> to add galaxy or <v-btn icon dark x-small disabled
            class="mx-1 black--text" elevation="2" style="background-color: #00E676;"><v-icon style="color:black!important;">mdi-cached</v-icon></v-btn> to choose another
        </div>
      </v-col>
    </v-row>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
