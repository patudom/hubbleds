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
    Now let's consider more modern data from 2001. 
      This data is from a team known as the HST Key Project,led by astronomer Wendy Freedman, 
      which used data from the Hubble Space Telescope to measure a quantity known as the Hubble Constant
      (which is the inverse of the age value you calculatad).
      
    <p> whose data has the least amount of random uncertainty?</p>
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Our class',
            'Edwin Hubble',
            'HST Key Project'
          ]"
          :feedbacks="[
            'Seems unlikely',
            'Seems unlikely',
            'Correct! The HST Key Project data has the least amount of random uncertainty.'
          ]"
          :correct-answers="[2]"
          :neutral-answers='[0,1]'
          :selected-callback="(state) => { $emit('ready'); }"
          score-tag="pro-dat5"
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
                state.marker = 'pro_dat4';
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
                state.marker = 'pro_dat6';
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
