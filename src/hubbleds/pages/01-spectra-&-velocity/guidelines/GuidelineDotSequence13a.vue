<template>
  <scaffold-alert
      @back="back_callback()"
      @next="next_callback()"
      :can-advance="can_advance"
  >
      <!-- :can-advance="(state) => state.meas_two_made" -->
    <template #before-next>
      Measure wavelength
    </template>
    <div>
      <p>
       Remeasure the wavelength of the spectral line keeping in mind what you learned from the dot plots. 
        <!-- {{ state.meas_two_made ? 'You have measured the wavelength of the spectral line.' : '' }} -->
      </p>
    </div>
  </scaffold-alert>
</template>
