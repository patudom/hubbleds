<template>
  <scaffold-alert
    title-text="Relationship Between Age and Slope"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Choose a response.
    </template>
    
    <div
      class="mb-4"
    >
      <p>
        After scanning through your classmates' Hubble graphs, how would you describe the relationship between the slope of the best-fit line and the age of the universe estimated from that dataset?
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <p>The relationship is:</p>
        <mc-radiogroup
          :radio-options="[
            'The data sets that have a steeper slope give a lower estimate for the age of the universe.',
            'The data sets that have a steeper slope give a higher estimate for the age of the universe.',
            'There is no relationship between the slope in a data set and the estimate for the age of the universe.'
          ]"
          :feedbacks="[
            'Yes. Notice that when you drag the slider toward the left (lower age), the slope of the graphed data gets larger (steeper).',
            'Try again. When you drag the slider toward the left (lower age), does the slope of the graphed data get steeper or shallower?',
            'Try again. Drag the slider slowly toward the left (lower age) and observe what happens to the slope of the graphed data. Then drag the slider to the right (higher age) and observe what happens to the slope.'
          ]"
          :correct-answers="[0]"
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
    };
  },
};
</script>

