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
      <p>
        Whose data set has more random uncertainty?
      </p>
      
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Our class\'s dataset',
            'Edwin Hubble\'s dataset',
            'It\'s hard to tell',
          ]"
          :feedbacks='[
            "Yes. We can see how much more our data deviates from the best fit line.",
            "It can be hard to tell. One thing to consider is how far off your data is from the best fit line",
            "It can be hard to tell. One thing to consider is how far off your data is from the best fit line",
          ]'
          :correct-answers="[0]"
          :neutral-answers='[1,2]'
          :selected-callback="(status) => { if (status.correct) { can_advance = true; } }"
          score-tag="pro-dat3"
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
                state.marker = 'pro_dat2';
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
                advance('pro_dat4');
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
