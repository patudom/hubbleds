<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :can-advance="(state) => false"
    :state="state"
  >
    <template #next-content>
    </template>
    <div>
      <p>
        You can now remeasure the example galaxy using what you've learned and see how your answer changes.
      </p>
      <p>
        Or move on to measure the spectral lines for your 5 galaxies. 
      </p>

      <v-btn 
        block color="accent"
        class="black--text"
        elevation="2"
        @click="() => {
          state.marker = 'dot_seq13'
        }"
      >
         <strong>Remeasure example</strong>
      </v-btn>
    </p><p>
      <v-btn 
        block color="accent"
        class="black--text"
        elevation="2"
        @click="() => {
          state.show_ruler = true;
          state.marker = 'rem_gal1'
        }"
      >
         <strong>Move on to my galaxies</strong>
      </v-btn>
      
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
