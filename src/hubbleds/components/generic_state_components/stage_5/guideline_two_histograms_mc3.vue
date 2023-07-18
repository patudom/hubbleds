<!-- this state.marker = 'two_his2' -->
<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Student Histogram vs. Class Histogram"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
    :can-advance="(state) => state.two_hist3_response"
    :state="state"
  >
    <div
      class="mb-4"
    >
      Now try comparing the inner 50%, 68%, and 95% ranges between the two histograms. (Clicking a radio button will display the same percentage range on both histograms.)
      <v-container
        class="px-0"
        fluid
      >
        <p>What do you notice about the relationship between the histograms? </p>
        <mc-radiogroup
          :radio-options="[
            'The inner percentage ranges are all smaller for the All Students histogram than the All Classes histogram.',
            'The inner percentage ranges are all larger for the All Students histogram than the All Classes histogram.',
            'Some of the inner percentage ranges are smaller for the All Students than the All classes histogram and some are larger.'
          ]"
          :feedbacks="[
            'Not quite. Look at the inner percentage ranges reported for each histogram. Try again.',
            'That’s right. The student histogram consistently has a larger inner percentage range.',
            'Not quite. Look at the inner percentage ranges reported for each histogram. Try again.',
          ]"
          :correct-answers="[1]"
          :wrong-answers='[0,2]'
          @select="(state) => { if (state.correct) { $emit('ready'); } }"
          score-tag="histogram-percent-range"
        >
        </mc-radiogroup>
      </v-container>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
