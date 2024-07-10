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
      <p> Which option will you choose? </p>
      
      {{ state_view.score_tag }}
      {{ state_view.mc_score }}
    
      <mc-radiogroup
        :radio-options="[
          'This option',
          'The correct option',
          'This one is wrong',
        ]"
        :feedbacks="[
          'Why not the correct option?',
          'Good choice',
          'What a contrarian choice!',
        ]"
        :correct-answers="[1]"  
        :neutral-answers="[0]"
        :score-tag="state_view.score_tag"
        @mc-emit="mc_callback($event)"
        :initialization="state_view.mc_score"
        
      >
      </mc-radiogroup>
      
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