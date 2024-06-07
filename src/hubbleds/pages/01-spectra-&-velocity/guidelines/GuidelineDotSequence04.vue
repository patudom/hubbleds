<template>
  <scaffold-alert
    title-text="Velocity and Wavelength"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div>
      <p>
        Your measured wavelength is marked in orange-red on the spectrum viewer.
      </p>
    </div>
  </scaffold-alert>
</template>
