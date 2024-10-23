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
        You can click on any velocity in the dot plot to display the corresponding wavelength in the spectrum viewer, and vice versa.
      </p>
      <p>
        If you zoom in on either plot, the other will zoom in to the corresponding range.
      </p>
      <p>
        See if you can identify features in the spectrum viewer that correspond to outliers and other velocity measurements.
      </p>      
    </div>
  </scaffold-alert>
</template>
