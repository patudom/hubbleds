<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Measurement Comparison"
    @back="state.marker_backward = 1"
    @next= "() => { 
      if (can_advance === 1) { state.marker = 'dop_seq6' }
        else if (can_advance === 2) { state.marker = 'rep_rem1' }
         }"
    :can-advance="can_advance > 2"
    :state="state"
  >

    <div
      class="mb-4"
    >
      <p>
        You may now either make a second measurement on the example galaxy using what you've learned and see how your answer changes, or you may move on to meauring the sizes for your 5 galaxies. 
      </p>
      
      <p>
      <v-btn block color="secondary" @click="() => {can_advance = 1; state.marker = 'dot_seq6'}">
         Make second measurement
      </v-btn>
    </p><p>
      <v-btn block color="secondary" @click="() => {can_advance = 2; state.marker = 'rep_rem1' }">
         Continue to my galaxies
      </v-btn>
    </p>
      
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state'],

  data: () => ({
    can_advance: false,
  }),
}
</script>
