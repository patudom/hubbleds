<template>
  <scaffold-alert
      @back="back_callback()"
      @next="next_callback()"
      :can-advance="can_advance"
  >
    <template #next-content>
    </template>
    <div>
      <!-- <p>
        You can now remeasure the example galaxy using what you've learned and see how your answer changes.
      </p>
      <p>
        Or move on to measure the spectral lines for your 5 galaxies.
      </p> -->
      <p>
        You can move on to measure the spectral lines for your 5 galaxies. 
      </p>
      <p>
        Try to take as accurate measurements as possible.
      </p>

      <!-- <v-btn
          block color="accent"
          class="black--text"
          elevation="2"
          @click="() => {
          remeasure_example_galaxy()
        }"
      >
        <strong>Remeasure example</strong>
      </v-btn>
      <p></p>
      <v-btn
          block color="accent"
          class="black--text"
          elevation="2"
          @click="() => {
          continue_to_galaxies()
        }"
      >
        <strong>Move on to my galaxies</strong>
      </v-btn> -->

    </div>
  </scaffold-alert>
</template>
