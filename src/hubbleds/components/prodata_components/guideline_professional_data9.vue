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
        Why do you think scientists' measurement of the age of the universe has changed with time?
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
              'Scientists can\'t really know what the age of the universe is.',
              'Scientists measure different ages because the universe is always getting older.',
              'The measured age of the universe can change based on new and better data.'
          ]"
          :feedbacks="[
            'It is possible to measure the age of the universe, though it can be difficult to do so.',
            'The universe is always getting older, but scientists measure the age of the universe on scales of billions of years, far greater than time between recent measurements.',
            'Correct! Improved data and technology allow scientists to measure the age of the universe more precisely and with less bias.'
          ]"
          :correct-answers="[2]"
          :neutral-answers='[0,1]'
          :selected-callback="(state) => { $emit('ready'); }"
          score-tag="pro-dat9"
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
                state.marker = 'pro_dat8';
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
                state.prodata_response = false;
                state.marker = 'pro_dat10';
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
