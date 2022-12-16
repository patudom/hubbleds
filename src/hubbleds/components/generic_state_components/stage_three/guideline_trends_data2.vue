<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Trends in the Data"
    @back="state.marker = 'tre_dat1'"
    @next="state.marker = 'tre_dat3'"
    :can-advance="(state) => state.class_layer_toggled > 0"
    :state="state"
  >
    <template #before-next>
      Click <v-icon>mdi-google-classroom</v-icon> in Toolbar.
    </template>

    <div
      class="mb-4"
    >
      <p>
        It can be difficult to notice a trend with so few data points.
      </p>
      <p>
        Since everyone in your class also measured 5 galaxies, let's look at a dataset that combines everyone's measurements.
      </p>
      <p>
        Click <v-icon>mdi-google-classroom</v-icon> to display measurements from your entire class.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
