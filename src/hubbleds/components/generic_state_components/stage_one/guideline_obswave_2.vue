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
    <p>
        <strong>Tips:</strong> You can re-measure the wavelength as many times as you like. 
      </p>
      <p>  
        If you want even more precision in your measurement, zoom in to a specific wavelength range in the viewer using the <v-icon>mdi-select-search</v-icon> icon in the toolbar.
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
        v-if="!state.zoom_tool_used"
      >
        <div
          style="font-size: 16px;"
        >
          Zoom in around the red <strong>{{ state.galaxy.element }} </strong> marker.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.zoom_tool_used"
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
