<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div>
      <p>
        Let's focus on the part of the dot plot that includes most of the data and ignore outliers.
      </p>
      <p>
        As you did in the tutorial, use <v-icon>mdi-select-search</v-icon> to zoom in around the main tower of data.
      </p>
      <v-btn color="secondary" @click="zoom_to_range()">zoom to optimal range</v-btn> 
    </div>
  </scaffold-alert>
</template>
