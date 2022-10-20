<template>
  <v-container
    class="py-0"
  >
    <v-row
      justify="center"
    >
      <v-col cols="12">
        <c-intro-slideshow />
      </v-col>
    </v-row>
  </v-container>
</template>

<style>

.v-container .v-card__text {
  font-size: 18px !important;
  line-height: 1.5 !important;
}

.v-alert .v-input--radio-group+.v-alert, .v-dialog .v-input--radio-group+.v-alert {
  background-color: #000b !important;
}

</style>