<!-- # multiple choice -->
<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
        Enter your responses.
    </template>
    <div
      class="mb-4"
    >
      Reflect a bit on what this tells you.
      <v-container
        class="px-0"
        fluid
      >
      
        <p> What did astronomers in the early 1920's believe about the universe before Edwin Hubble's discovery?</p>
        <free-response
          outlined
          auto-grow
          rows="2"
          label="Reflection #1"
          :tag="state_view.free_response_a.tag"
          :initial-response="state_view.free_response_a.response"
          :initialized="state_view.free_response_a.initialized"
          @fr-emit="fr_callback($event)"
        ></free-response>
        
        <p>What age of the universe can be obtained from Edwin Hubble's data (in Gyr)?</p>
        <free-response
          outlined
          auto-grow
          rows="2"
          label="Age from Edwin Hubble"
          type="float"
          :tag="state_view.free_response_b.tag"
          :initial-response="state_view.free_response_b.response"
          :initialized="state_view.free_response_b.initialized"
          @fr-emit="fr_callback($event)"
        ></free-response>
        
        <p>What age of the universe can be obtained from the HST Key project's data (in Gyr)?</p>
        <free-response
          outlined
          auto-grow
          rows="2"
          label="Age from HST Key Project"
          type="float"
          :tag="state_view.free_response_c.tag"
          :initial-response="state_view.free_response_c.response"
          :initialized="state_view.free_response_c.initialized"
          @fr-emit="fr_callback($event)"
        ></free-response>
      </v-container>
    </div>
  </scaffold-alert>
</template>

<script setup>

</script>
