<template>
  <scaffold-alert
    title-text="Second Measurement Comparison"
    @back="state.marker = 'dot_seq6a'"
    @next="state.marker = 'rep_rem1'"
    :can-advance="(state) => state.dot_seq6_q"
    :state="state"
    >
      <template #before-next>
        Choose a response
      </template>
    
    <div class="mb-4">
      <p>
        Now, in the upper graph we show you the distribution of first measurements as you saw earlier in this stage.
      </p>
      <p>
        In the lower graph, we show you the distribution of second measurements, with yours marked in blue.
      </p>
      <p>
        Based on these two histograms, which set of measurments shows better concensus on the the distance to the galaxy?
      </p>
      <mc-radiogroup
        :radio-options="[
          'The first set of measurements',
          'The second set of measurements',
          'I am not sure',
          ]"
        :feedbacks="[
          'Not quite! In which histogram is the data more clustered around a single value?',
          'Correct! The second set of measurements cluster around one common value',
          'Consider where the measurements cluster around a single common value.'
          ]"
        :correct-answers="[1]"
        :wrong-answers="[0]"
        :neutral-answers="[2]"
        @select="(opt) => { if (opt.correct) { console.log('correct'); $emit('ready') } }"
        score-tag="ange_meas_concensus_2">
      </mc-radiogroup>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
