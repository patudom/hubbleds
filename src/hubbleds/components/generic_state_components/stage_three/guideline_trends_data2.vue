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
      Trends in the Data
    </h3>
    <div
      class="mb-4"
    >
      <p>
        It can be difficult to notice a trend with so few data points.
      </p>
      <p>
        Since everyone in your class also measured 5 galaxies, let's look at a dataset that combines everyone's measurements.
      </p>
      <p>
        Click <v-icon>mdi-google-classroom</v-icon> to display measurements from your entire class.
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
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'tre_dat1'
          "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="state.class_layer_toggled==0"
      >
        <div
          style="font-size: 16px;"
        >
          Click <v-icon>mdi-google-classroom</v-icon> in Toolbar.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.class_layer_toggled>0"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'tre_dat3'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
