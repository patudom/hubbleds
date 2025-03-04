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
        Notice that the Dot Plot has been set to show the velocity range that corresponds to the Spectrum Viewer's wavelength range.
      </p>
    </div>
  </scaffold-alert>
</template>
