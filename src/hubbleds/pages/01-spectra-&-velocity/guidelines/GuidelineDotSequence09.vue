<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div>
      <p>
        To make sure everyone is making the best measurements, use the measuring tool to compare which spectrum features match the velocity bins.
        
      </p>
      <p>
        (Notice we zoomed in to the corresponding wavelength range in the spectrum viewer below.)
      </p>
    </div>
  </scaffold-alert>
</template>
