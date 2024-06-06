<template>
  <scaffold-alert
    title-text="Velocity Calculation"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-run-fast</v-icon></v-btn> button
    </template>

    <div
        class="mb-4"
    >
      <p>
        Since you've already seen how to use the Doppler equation, click the
        <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-run-fast</v-icon></v-btn>
        icon in the table header to have the velocities of your galaxies calculated.
      </p>
    </div>
  </scaffold-alert>
</template>


<style>

.JaxEquation .MathJax {
  margin: 16px auto !important;
}

</style>
