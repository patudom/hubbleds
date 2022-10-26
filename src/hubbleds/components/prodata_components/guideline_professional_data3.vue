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
        First, let's look at Edwin Hubble's data from 1929.
      </p>
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
            "Are you sure",
            "Are you sure",
            "Are you sure",
          ]'
          :correct-answers="[]"
          :neutral-answers='[0,1,2]'
          :selected-callback="(state) => { $emit('ready'); }"
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
        v-if="!state.prodata_response"
      >
        <div
          style="font-size: 16px;"
        >
          Choose a response.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.prodata_response"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
              () => {
                state.marker = 'pro_dat4';
                state.prodata_response = false;
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>