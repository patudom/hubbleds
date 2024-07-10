<template>
  <scaffold-alert
    title-text="Multiple Choice Example"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
  
    <template #before-next>
      Choose a response
    </template>
    
   <div class="mb-4">
    
      <h1 class="test-page"> This is a test page Marker 2 </h1>
      <p> Are you feeling luck today? </p>
    
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Well are you?"
        :tag="state_view.free_response.tag"
        :initial-response="state_view.free_response.response"
        :intialized="state_view.free_response.initialized"
        @fr-emit="fr_callback($event)"
        ></free-response>
      
    </div>
    
  </scaffold-alert>
</template>

<script>
</script>

<style>
h1.test-page {
  color: rgb(0, 255, 30);
}
</style>