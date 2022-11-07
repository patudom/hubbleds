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
      Edwin Hubble's own data from 1929 is shown in purple. (Your class's data is shown in teal).
    </p>

    <p>
      Does your class's age estimate agree with Hubble's age estimate? It might help to display the best fit lines.
    </p>

    <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Yes',
            'No',
            'I\'m not sure',
          ]"
          :feedbacks="['Remember, the slope of the line is related to the age measurement from this data. Are the slopes the same?','Correct. The best fit lines for our data and Edwin Hubble\'s data have very different slopes.','The slope of the line is related to the age measurement from this data. Are the slopes the same?']"
          :incorrect-answers="[0]"
          :correct-answers="[1]"
          :neutral-answers="[2]"
          :selected-callback="(status) => { if (status.correct) { can_advance = true; } }"
          score-tag="pro-dat1"
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
                state.marker = 'pro_dat0';
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
               advance('pro_dat2');
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
