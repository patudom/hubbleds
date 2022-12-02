<template>
  <v-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
  >
    <h3
      class="mb-4"
    >
      Observed Wavelength
    </h3>
    <div
      class="mb-4"
    >
      <p
        v-if=!state.zoom_tool_activated>  
        To improve the precision in your measurement, zoom in to the wavelength range around the {{ state.galaxy.element }} line using the <v-icon>mdi-select-search</v-icon> icon in the toolbar.
      </p>
      <p
        v-if=state.zoom_tool_activated>  
        If you accidentally zoomed in too far or in the wrong spot, you can click <v-icon>mdi-cached</v-icon> to reset the view to the full range of wavelengths.
      </p>
      <p>
        <strong>Tip:</strong> You can re-measure the wavelength as many times as you like. 
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
            state.marker = 'obs_wav1';
          "
        >
          back
        </v-btn>
      </v-col>
      <v-spacer></v-spacer>
      
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.zoom_tool_activated"
      >
        <div
          style="font-size: 16px;"
        >
          Click <v-icon>mdi-select-search</v-icon> to activate tool. Click and drag across the red <strong>{{ state.galaxy.element }} </strong> marker to zoom in.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.zoom_tool_activated"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'rep_rem1';
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>