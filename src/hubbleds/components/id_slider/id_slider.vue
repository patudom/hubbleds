<template>
  <v-slider
    v-model="selected"
    :step="step"
    :min="vmin"
    :max="vmax"
    ticks
    thumb-label="always"
  >
    <template v-slot:thumb-label="">
      {{ thumb_value }}
    </template>
  </v-slider>
</template>
