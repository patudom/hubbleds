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
      Perhaps even more important than the range of ages is <b>how those ages are distributed</b>. If most of the measurements are bunched closely together, that gives us more confidence than
      if they are spread across a large range of values or are bunched around multiple values. As with the dot plots you saw earlier, more <b>consensus</b> in measurements generally gives us more <b>confidence</b> in a result.
      <v-container
        class="px-0"
        fluid
      >
        <p>How would you describe the distribution of age measurements for these histograms?</p>
        <mc-radiogroup
          :radio-options="[
            'The distribution for the student and class age measurements look similar to each other.',
            'The distribution for the student measurements are more concentrated around a central value than the class measurements.',
            'The distribution for the class measurements are more concentrated around a central value than the student measurements.'
          ]"
          :feedbacks="[
            'Not quite. One histogram looks more like a spike, while the other looks more like a bell. Which is which?',
            'Not quite. One histogram looks more like a spike, while the other looks more like a bell. Which is which?',
            'That\'s right. The student histogram looks more like a bell, while the class histogram looks more like a spike, so there is more consensus within the class age measurements.',
          ]"
          :correct-answers="[2]"
          :wrong-answers='[0,1]'
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
}
</script>
