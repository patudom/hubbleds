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
      <p>Interesting that they are not the same. Whose age estimate are you more inclined to believe?</p>
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Out age estimate',
            'Hubble\'s age estimate'
          ]"
          :feedbacks="['','']"
          :correct-answers="[]"
          :neutral-answers='[0,1]'
          :selected-callback="(state) => { $emit('ready'); }"
          score-tag="pro-dat4"
        >
        </mc-radiogroup>
      </v-container>
      <p> Why did you choose that?</p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Why?"
        tag="prodata-free-4"
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
                state.marker = 'pro_dat3';
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
                state.marker = 'pro_dat5';
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
