<template>
  <scaffold-alert
    title-text="Check Measurement"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :can-advance="(state) => state.dot_seq2_q"
    :state="state"
  >
    <template #before-next>
      Choose a response
    </template>
    <div>
      <p>
        Based on this graph do you think there is <it>concensus</it> on the velocity of this galaxy?
      </p>
      <mc-radiogroup 
          :radio-options="[
            'Yes',
            'No',
            'I am not sure',
            ]"
            :feedbacks="[
            'Yes, most of the measurements appear in a cluster towards the right of the graph. Note, though, that they span a large range in velocity values.',
            'This case could go either way. Most of the measurements appear in a cluster towards the right of the graph, but they span a very large range in velocity values.',
            'Yeah, sometimes it is hard to tell. Most of the measurements appear in a cluster towards the right of the graph, but they span a large range in velocity values.'
            ]" 
          :neutral-answers="[0,1,2]"
          @select="(opt) => { if (opt.correct || opt.neutral) { console.log('correct'); $emit('ready'); } }"
          score-tag="vel_meas_concensus">
            >
          </mc-radiogroup>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
