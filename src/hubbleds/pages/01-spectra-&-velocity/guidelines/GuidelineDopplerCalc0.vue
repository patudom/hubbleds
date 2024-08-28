<template>
  <scaffold-alert
    title-text="Velocity Calculation"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div
      class="mb-4"
    >
      <p>
        Now, you will use the observed wavelength of the H-&alpha; spectral line to determine the galaxy's velocity, using the <b>Doppler Equation</b>.

      </p>
    </div>
  </scaffold-alert>
</template>
