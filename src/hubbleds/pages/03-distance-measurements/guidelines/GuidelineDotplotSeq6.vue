<template>
  <scaffold-alert
    title-text="Second Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="question_completed && can_advance"
    >
      <template #before-next>
        Choose a response
      </template>
    
    <div class="mb-4">
      <p>
        In the upper graph we show the distribution of first measurements as you saw earlier.
      </p>
      <p>
        In the lower graph, we show the distribution of second distance measurements. Yours are again marked in red-orange.
      </p>
      <p>
        Based on these two histograms, which set of measurements shows better consensus on the distance to the galaxy?
      </p>
      <mc-radiogroup
        :radio-options="[
          'The first set of measurements',
          'The second set of measurements',
          'I am not sure',
          ]"
        :feedbacks="[
          'Not quite. Consider which dot plot has measurements that cluster around fewer common values.',
          'Correct. The second set of measurements clusters around fewer common values',
          'Consider which dot plot has measurements that cluster around fewer common values.'
          ]"
        :correct-answers="[1]"
        :neutral-answers="[0, 2]"
        @select="(status) => { if (status.correct) { question_completed = true; } }"
        :score-tag="state_view.score_tag"
        @mc-emit="mc_callback($event)"
        :initialization="state_view.mc_score"
      >
      </mc-radiogroup>
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