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
      Hubble's Expanding Universe
    </h3>
    <div
      class="mb-4"
    >
      <p>
        The relationship between your galaxies’ velocity and distance is the same as what Hubble found: galaxies at a greater distance away are moving away from us at a higher velocity.
      </p>
      <p>
       Click the <strong>HUBBLE's DISCOVERY</strong> button to learn what was significant about this result.
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
            state.marker = 'rel_vel1'
          "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.hubble_dialog_opened"
      >
        <div
          style="font-size: 16px;"
        >
          Click the <strong>HUBBLE'S DISCOVERY</strong> button.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.hubble_dialog_opened"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'hub_exp2'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
