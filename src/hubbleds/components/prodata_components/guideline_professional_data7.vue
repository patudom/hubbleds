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
      Whose age estiamte are you more inclinded to believe?
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="['Our age estimate', 'Hubble team\'s age estimate']"
          :feedbacks="['Interesting! Why do you choose that?','Interesting! Why do you choose that?']"
          :correct-answers="[0,1]"
          :neutral-answers='[]'
          :selected-callback="(state) => { $emit('ready'); }"
          score-tag="pro-dat7"
        >
        </mc-radiogroup>
      </v-container>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Why?"
        tag="prodata-free-7"
        v-if='state.prodata_response'
      ></free-response>
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
                state.marker = 'pro_dat6';
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
                state.marker = 'pro_dat8';
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
