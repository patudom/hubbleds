<template>
  <scaffold-alert
    title-text="Velocity Calculation"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Now, you will use the observed wavelength of the H-&alpha; spectral line to determine the galaxy's velocity, using the <strong>Doppler Equation</strong>.

      </p>
    </div>
  </scaffold-alert>
</template>
