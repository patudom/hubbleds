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
        Do you see any sort of trend in your data? Is there a relationship between the velocity and distance of the galaxies?
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Yes, I see a trend.',
            'No, I don\'t see a trend.',
            'I can\'t tell if there\'s a trend.',
          ]"
          :feedbacks="[
            'Interesting, but it might help to look at more data before deciding for sure.',
            'Yeah, it can be hard with so few data points. Let\'s see what happens if we add more data.',
            'Yeah, it can be hard with so few data points. Let\'s see what happens if we add more data.',
          ]"
          :correct-answers="[]"
          :neutral-answers='[0,1,2]'
          :selected-callback="(state) => { $emit('ready'); }"
        >
        </mc-radiogroup>
        <v-btn
          plain
          color="info"
          @click="
            define_trend = true
          "
        >
          What's a trend?
        </v-btn>
        <v-divider
          class="my-4"
          v-if="define_trend"
        >
        </v-divider>
        <v-alert
          v-if="define_trend"
          dense
          color="info darken-1"
        >
          A trend is a pattern in data that resembles an upward <v-icon>mdi-arrow-top-right-bottom-left-bold</v-icon> or downward <v-icon>mdi-arrow-top-left-bottom-right-bold</v-icon> line. 
        </v-alert>
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
                state.marker = 'exp_dat1';
                define_trend = false;
              }
            "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.trend_response"
      >
        <div
          style="font-size: 16px;"
        >
          Choose a response.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.trend_response"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
              () => {
                state.marker = 'tre_dat2';
                define_trend = false;
                state.trend_response = false;
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
