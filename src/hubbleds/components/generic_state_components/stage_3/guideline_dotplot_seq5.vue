<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Measurement Comparison"
    @back="state.marker_backward = 1"
    :can-advance="(state) => false"
    :state="state"
  >
    <template #next-content>
    </template>

    <div
      class="mb-4"
    >
      <p>
        You may now either make a second measurement on the example galaxy using what you've learned and see how your answer changes, or you may move on to meauring the sizes for your 5 galaxies. 
      </p>
      
      <p>
      <v-btn 
        block color="accent"
        class="black--text"
        elevation="2"
        @click="() => {
          state.show_ruler = true;
          state.marker = 'dot_seq6a'
        }"
      >
         <strong>Make second measurement</strong>
      </v-btn>
    </p><p>
      <v-btn 
        block color="accent"
        class="black--text"
        elevation="2"
        @click="() => {
          state.show_ruler = true;
          state.marker = 'rep_rem1'
        }"
      >
         <strong>Continue to my galaxies</strong>
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
