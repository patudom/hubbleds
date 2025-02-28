<template>
  <scaffold-alert
    title-text="Check Measurement"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <template #before-next>
      Choose a response
    </template>
    <div>
      <div style="display: flex; justify-content: center;">
        <v-btn color="secondary" @click="zoom_to_range()" class="mb-6 mt-2">zoom to optimal range</v-btn>
      </div>
      <p>
        Based on this graph do you think there is <strong>consensus</strong> on the velocity of this galaxy?
      </p>
      <mc-radiogroup 
          :radio-options="[
            'Yes',
            'No',
            'I am not sure',
            ]"
            :feedbacks="[
            'Try again. Make sure you zoom in to where most of the data points are and see if they are clustered around more than one velocity value.',
            'Yes. When we exclude outliers and zoom into the central data tower, we see that measurements are clustered around more than one velocity value.',
            'Consider only the range of values that excludes outliers. If measurements are clustered around a single velocity value, there is consensus. If they are clustered around multiple values, there is not consensus.'
            ]" 
          :correct-answers="[1]"
          :neutral-answers="[0, 2]"
          :score-tag="state_view.score_tag"
          @mc-emit="mc_callback($event)"
          :initialization="state_view.mc_score"
          >
          </mc-radiogroup>
    </div>
  </scaffold-alert>
</template>
