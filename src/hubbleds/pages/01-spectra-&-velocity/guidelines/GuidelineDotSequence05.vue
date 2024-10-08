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
        See if you can identify features in the spectrum viewer that correspond to outliers and other velocity measurements.
      </p>
      <p>
        You can zoom in on either plot to see more detail, or click on either plot to bring up a green line which shows the corresponding velocity and wavelength on their respective graphs.
      </p>
      <p>
        As you did in the tutorial, use <v-icon>mdi-select-search</v-icon> to zoom in around the main tower of data.
      </p>
      
    </div>
  </scaffold-alert>
</template>
