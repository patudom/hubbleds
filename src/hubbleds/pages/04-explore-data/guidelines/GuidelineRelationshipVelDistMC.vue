<template>
  <scaffold-alert
    title-text="Relationship Between Velocity and Distance"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="question_completed && can_advance"
  >
    <template #next-content>
      Choose a response.
    </template>

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
          @select="(status) => { if (status.correct) { question_completed = true; } }"
          :score-tag="state_view.score_tag"
          @mc-emit="mc_callback($event)"
          :initialization="state_view.mc_score"
        >
        </mc-radiogroup>
      </v-container>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  
  data() {
    return {
      question_completed: false,
    };
  },
};
</script>