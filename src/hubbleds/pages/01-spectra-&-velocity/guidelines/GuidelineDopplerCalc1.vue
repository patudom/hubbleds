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
        You will use the Doppler equation to calculate the velocity for just one of your galaxies, so you get a feel for how it works.
      </p>
      <p>
        After that, we’ll fill in velocities for the rest of your galaxies for you.
      </p>
    </div>
  </scaffold-alert>
</template>
