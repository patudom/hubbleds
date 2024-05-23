<!-- this state.marker = 'two_his2' -->
<template>
  <scaffold-alert

    title-text="Student Histogram vs. Class Histogram"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="question_completed && can_advance"
  >
    <template #before-next>
      Choose a response.
    </template>
    <div
      class="mb-4"
    >
      Now try comparing the inner 50%, 68%, and 95% confidence ranges between the two histograms. (The switches will display the same percentage range on both histograms.)
      <v-container
        class="px-0"
        fluid
      >
        <p>What do you notice about the relationship between the histograms? </p>
        <mc-radiogroup
          :radio-options="[
            'All confidence ranges are narrower for the students than the classes.',
            'All confidence ranges are broader for the students than the classes.',
            'Some of the confidence ranges are narrower for the students and some are broader.'
          ]"
          :feedbacks="[
            'Not quite. Look at the percentage confidence ranges reported for each histogram. Try again.',
            'That’s right. The student histogram consistently has a larger confidence range for all percentages.',
            'Not quite. Look at the percentage confidence ranges reported for each histogram. Try again.',
          ]"
          :correct-answers="[1]"
          :wrong-answers='[0,2]'
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
