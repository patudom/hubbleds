<template>
  <v-slider
    v-model="selected"
    :step="step"
    :min="vmin"
    :max="vmax"
    :color="color"
    :thumb-color="color"
    ticks
    :tick-labels="tick_labels"
    thumb-label="always"
  >
    <template v-slot:thumb-label="">
      {{ thumb_value }}
    </template>
  </v-slider>
</template>
