<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div>
      <p>
        If your velocity measurement does not <em>reasonably</em> agree with the concensus, use the Spectrum Viewer to remeasure the spectral line for your galaxy.
      </p>
      <p> The velocity in the table and the dot plot will automatically update to reflect your new measurement here.</p>
      <p>
        (The database will retain your original measurement.)
      </p>
    </div>
  </scaffold-alert>
</template>
