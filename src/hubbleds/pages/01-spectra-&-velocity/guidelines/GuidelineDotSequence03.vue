<template>
  <scaffold-alert
    title-text="Velocity and Wavelength"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div>
      <p>
        Whether or not your point is an outlier, it can be helpful to know how the measured velocities correspond to the measured wavelengths in the spectrum.
      </p>
    </div>
  </scaffold-alert>
</template>
