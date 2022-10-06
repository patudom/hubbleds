<template>
  <scaffold-alert
    header-text="Trend Lines"
    @back="
      state.marker = 'tre_dat1';
    "
    @next="
      state.marker = 'tre_lin1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Since everyone in your class also measured 5 galaxies, let's look at a dataset that combines everyone's measurements.
      </p>
      <p>
        Click <v-icon>mdi-google-classroom</v-icon> to display measurements from your entire class.
      </p>
    </div>
  </scaffold-alert>
</template>
