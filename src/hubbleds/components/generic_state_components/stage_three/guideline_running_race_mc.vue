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
      A Running Race
    </h3>
    <div
      class="mb-4"
    >
      <p>
        To understand Hubble’s thinking about this, let’s use the following situation as a model: Imagine runners in the middle of a race, where the runners are running at different speeds.
      </p>
      <p>
        In this diagram, runner A is running with a velocity of 4 km per hour and has run a distance of 12 km, while runner C is running faster with a velocity of 10 km per hour and has gone a distance of 30 km.
      </p>
      <p>
        Can you figure out how long ago the race started — the “age” of the race? (Assume each runner has maintained a consistent speed for the entire race).
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <p>The race began:</p>
        <mc-radiogroup
          :radio-options="[
            '1/3 of an hour ago',
            '3 hours ago',
            '12 hours ago',
            '75 hours ago'
          ]"
          :feedbacks="[
            'Recorded. You think it started 1/3 of an hour ago.',
            'Recorded. You think it started 3 hours ago.',
            'Recorded. You think it started 12 hours ago.',
            'Recorded. You think it started 75 hours ago.'
          ]"
          :correct-answers="[1]"
          :neutral-answers='[0,2,3]'
          :selected-callback="(state) => { $emit('ready'); }"
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
            state.marker = 'hub_exp2'
          "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.race_response"
      >
        <div
          style="font-size: 16px;"
        >
          Answer the question above.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.race_response"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'run_vel1'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
