<!-- # multiple choice -->
<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      <div v-if="!state_view.mc_completed">
        Choose a response.
      </div>
      <div v-else>
        Enter a response.
      </div>
    </template>

    <div
      class="mb-4"
    >
      <p>Whose age estimate are you more inclined to believe?</p>
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Our age estimate',
            'Hubble\'s age estimate'
          ]"
          :feedbacks="['Interesting! Why do you choose that?','Interesting! Why do you choose that?']"
          :correct-answers="[]"
          :neutral-answers='[0,1]'
          :score-tag="state_view.score_tag"
          @mc-emit="mc_callback($event)"
          :initialization="state_view.mc_score"
        >
        </mc-radiogroup>
      </v-container>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Why?"
        :tag="state_view.free_response.tag"
        :initial-response="state_view.free_response.response"
        :initialized="state_view.free_response.initialized"
        @fr-emit="fr_callback($event)"
        v-if="state_view.mc_completed"
      ></free-response>
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
