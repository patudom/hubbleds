<template>
  <scaffold-alert
    title-text="Explore Your Data"
    next-text="graph"
    @next="next_callback()"
    :can-advance="can_advance"
    :allow-back="false"
  >
    <div
      class="mb-4"
    >
      <p>
        Now, you have a table of velocity and distance data for your galaxies, like Hubble did.
      </p>
      <p>
        Hubble graphed his data with velocity on the y-axis and distance on the x-axis. Let’s do the same with your data and see what it looks like.
      </p>
    </div>

  </scaffold-alert>
</template>