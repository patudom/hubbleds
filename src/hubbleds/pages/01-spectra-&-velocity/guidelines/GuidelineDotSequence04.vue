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
        Your measured wavelength is marked in orange-red on the spectrum viewer.
      </p>
      <p>
        Notice that the Dot Plot has be set to show the velocity range 
          that corresponds to the Spectrum Viewer's wavelength range.
      </p>
      <p>
        As seen in the Dot Plot Tutorial, because we are looking 
          at a larger range than before, the dots are stacked in to fewer, taller towers. 
      </p>
    </div>
  </scaffold-alert>
</template>
