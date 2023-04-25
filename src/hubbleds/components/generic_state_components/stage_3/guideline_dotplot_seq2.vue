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
        Based on this graph do you think there is <it>concensus</it> on the distance to this galaxy?
      </p>
      <mc-radiogroup 
          :radio-options="[
            'Yes',
            'No',
            'I am not sure',
            ]"
            :feedbacks="[
            'Not quite! Consider where the measurements cluster around a single common value.',
            'Correct! The measurements cluster around two common values, so there is no concensus.',
            'Consider where the measurements cluster around a single common value.'
            ]" 
          :correct-answers="[1]"
          :neutral-answers="[2]"
          :selected-callback="(opt) => { if (opt.correct) { console.log('correct'); } }"
          score-tag="ange_meas_concensus">
            >
          </mc-radiogroup>
          
          <v-btn
          block
          color="deep-orange darken-2"
          @click="
            define_concensus = !define_concensus
          "
        >
          What is <it>concensus</it>?
        </v-btn>
        <v-alert
          class="mt-4 trend-alert"
          v-if="define_concensus"
          dense
          color="info darken-1"
        >
        A set of measurements shows consensus when all of the measurements tend to cluster around a single rather than multiple values
        </v-alert>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state'],

  data: () => ({
      define_concensus: false,
  })
}
</script>
