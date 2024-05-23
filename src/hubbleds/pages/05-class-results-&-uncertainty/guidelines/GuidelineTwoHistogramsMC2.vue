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
      <v-container
        class="px-0"
        fluid
      >
        <p>In comparing the All Students and All Classes histogram, which spans a larger range of ages?</p>
        <mc-radiogroup
          :radio-options="[
            'The histogram of student measurements.',
            'The histogram of class measurements.',
            'The student and class histograms are the same.'
          ]"
          :feedbacks="[
            'That’s right. The student histogram has a larger range.',
            'Not quite. Look at the x-axis for each histogram. Where does the range of values start and end for each histogram? Try again.',
            'Not quite. Look at the x-axis for each histogram. Where does the range of values start and end for each histogram? Try again.'
          ]"
          :correct-answers="[0]"
          :wrong-answers='[1,2]'
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