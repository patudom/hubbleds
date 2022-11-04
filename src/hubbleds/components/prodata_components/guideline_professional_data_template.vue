<!-- # multiple choice -->
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
      Professional Data
    </h3>
    <div
      class="mb-4"
    >
      {{ TEXT }}
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            // option 1,
            // option 2,
            // option 3,
          ]"
          :feedbacks="[
            // feedback 1,
            // feedback 2,
            // feedback 3,
          ]"
          :correct-answers="[]"
          :neutral-answers='[0,1,2]'
          :selected-callback="(option) => { if (option.correct || option.neutral) { can_advance = true };  }"
          score-tag="pro-datN"
        >
        </mc-radiogroup>
      </v-container>
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
              () => {
                state.marker = 'back_marker';
              }
            "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!can_advance"
      >
        <div
          style="font-size: 16px;"
        >
          Choose a response.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="can_advance"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
              () => {
                state.marker = 'pro_dat_next';
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
