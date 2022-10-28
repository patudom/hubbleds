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
      <p>Whose age estimate are you more inclined to believe?</p>
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Our age estimate',
            'Hubble\'s age estimate'
          ]"
          :feedbacks="['Interesting! Why do you choose that?','Interesting! Why do you choose that?']"
          :correct-answers="[0,1]"
          :neutral-answers='[]'
          :selected-callback="(state) => { if (state.correct) { can_advance = true; } }"
          score-tag="pro-dat4"
        >
        </mc-radiogroup>
      </v-container>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Why?"
        tag="prodata-free-4"
        v-if='can_advance'
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
                advance('pro_dat5');
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
