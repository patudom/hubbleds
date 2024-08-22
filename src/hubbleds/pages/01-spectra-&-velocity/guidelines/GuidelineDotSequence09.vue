<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div>
      <p>
        If your velocity measurement does not <em>reasonably</em> aggree with the concensus, use the Spectrum Viewer to remeasure the spectral line for your galaxy.
      </p>
      <p> The velocity in the table and the dot plot will automatically update to reflect your new measurement. </p>
      <!-- <p>
        (Notice we zoomed in to the corresponding wavelength range in the spectrum viewer below.)
      </p> -->
    </div>
  </scaffold-alert>
</template>
