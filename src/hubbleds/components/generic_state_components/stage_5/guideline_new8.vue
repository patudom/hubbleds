<template>
  <scaffold-alert
    title-text="Select Best Value"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
    <p>
      How did your best estimate and range of values change going from 
      student by student results (each with 5 galaxies) to 
      class by class results (each with ~50-100+ galaxies)?
      
    </p>
    
    <p>
      Are your answers different?
     <mc-radiogroup
          :radio-options="[
            'Class range is narrower than student range',
            'Class range is wider than student range',
            'Class range is the same as student range',
          ]"
          :feedbacks="[]"
          :incorrect-answers="[]"
          :correct-answers="[]"
          :neutral-answers="[0,1,2]"
          @select="(status) => { if (status.correct) { allowAdvancing(); } }"
          score-tag="unc-range-change"
        >
        </mc-radiogroup>
        <v-row>
        <v-col>
          What do you think led to the change?

          <free-response
            outlined
            auto-grow
            rows="2"
            label="My Reasoning"
            tag="unc-range-change-reasoning"
          ></free-response>
        </v-col>
      </v-row>
    </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
