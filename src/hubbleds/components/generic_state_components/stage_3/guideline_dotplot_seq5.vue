<template>
  <scaffold-alert
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
        You can now remeasure the example galaxy using what you've learned and see how your answer changes.
      </p>
      <p>
        Or move on to measure the sizes for your 5 galaxies. 
      </p>
      
      <p>
      <v-btn 
        block color="accent"
        class="black--text"
        elevation="2"
        @click="() => {
          state.marker = 'dot_seq5a'
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
          state.marker = 'rep_rem1'
        }"
      >
         <strong>Move on to my galaxies</strong>
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
