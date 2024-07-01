<template>
  <scaffold-alert
    title-text="Trends in the Data"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Choose a response.
    </template>

    <div>
      <p>
        The graph here shows the velocities of your galaxies plotted vs. their distances.  
      </p>
      <p>
        Do you see any sort of trend in your data? Is there a relationship between the velocities and distances of the galaxies?
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
          :score-tag="state_view.score_tag"
          @mc-emit="mc_callback($event)"
          :initialization="state_view.mc_score"
        >
        </mc-radiogroup>
        <v-btn
          block
          color="deep-orange darken-2"
          @click="
            define_trend = !define_trend
          "
        >
          What is a trend?
        </v-btn>
        <v-alert
          class="mt-4 trend-alert"
          v-if="define_trend"
          dense
          color="info darken-1"
        >
          A trend is a pattern in data (for example, an upward line <v-icon>mdi-arrow-top-right-bottom-left-bold</v-icon> or downward line <v-icon>mdi-arrow-top-left-bottom-right-bold</v-icon>). 
        </v-alert>
      </v-container>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  
  data() {
    return {
      define_trend: false,
    };
  },
};
</script>