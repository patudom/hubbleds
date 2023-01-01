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
      Relationship Between Velocity and Distance
    </h3>
    <div
      class="mb-4"
    >
      <p>
        How would you describe the trend (or relationship) between the velocities and distances for your class's galaxies?
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <p>The trend is:</p>
        <mc-radiogroup
          :radio-options="[
            'The velocities of galaxies are generally the same across all distances.',
            'Galaxies that are at a greater distance from us tend to have larger velocities.',
            'Galaxies that are at a greater distance from us tend to have smaller velocities.',
            'The velocities of galaxies appear to be random across all distances.'
          ]"
          :feedbacks="[
            'This would be true if the data points formed a horizontal line across the graph. Try again.',
            'Yes. Your graph has an upward trend. In general, galaxies that are closer to us are moving away at lower speeds, and galaxies that are farther away are moving away at higher speeds.',
            'This would be true if the data points had a downward trend on the graph. Try again.',
            'Even if your class\'s dataset is very messy, you should observe a trend that is not random. Try again.'
          ]"
          :correct-answers="[1]"
          :neutral-answers='[0,2,3]'
          @select="(state) => { if (state.correct) { $emit('ready'); } }"
          score-tag="galaxy-trend"
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
      <v-col>
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'tre_dat3'
          "
        >
          back
        </v-btn>
      </v-col>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.relvel_response"
      >
        <div
          style="font-size: 16px;"
        >
          Choose a response.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.relvel_response"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'hub_exp1'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
