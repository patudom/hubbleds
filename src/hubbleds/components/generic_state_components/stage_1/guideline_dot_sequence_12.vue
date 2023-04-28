<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <span style="color:#1DE9B6!important">Create same choice card and parallel behavior from Stage 3 tutorial to end</span>
      
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
