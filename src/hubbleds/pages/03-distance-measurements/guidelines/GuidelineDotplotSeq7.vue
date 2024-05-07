<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Second Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    >
    <div class="mb-4">
      <p>
        With improved consensus in the distance measurements, you are ready to measure your five galaxies.
      </p>
    </div>
  </scaffold-alert>
</template>

