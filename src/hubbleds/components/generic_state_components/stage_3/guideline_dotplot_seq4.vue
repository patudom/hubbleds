<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Measurement Comparison"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
    :can-advance="(state) => true"
    :state="state"
  >
    <template #before-next>
      nothing
    </template>

    <div
      class="mb-4"
    >
      <p>
        We now show the distribution of angular size measurements for this galaxy. Click on different locations on the graph of distanes to see where they are on the angular size measurement plot. 
      </p>
      <p>
        What relationship do you see between the angular size and distance measurements?
      </p>
      <mc-radiogroup 
          :radio-options="[
            'A large distance corresponds to a small angular size',
            'A small distance corresponds to a large angular size',
            'There is no relation between distance and the measured angular size',
            ]"
            :feedbacks="[
            'Correct! If two objects have the same size, the one at a larger distance will have a smaller angular size.',
            'Not quite. Look again at the graphs and check two different distance values. Which one has the larger angular size?',
            'Not quite. Look again at the graphs and check two different distance values. Which one has the larger angular size?',
            ]" 
          :correct-answers="[0]"
          :neutral-answers="[1,2]"
          :selected-callback="(opt) => { if (opt.correct) { console.log('correct'); } }"
          score-tag="ang_meas_dist_relation">

          </mc-radiogroup>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
