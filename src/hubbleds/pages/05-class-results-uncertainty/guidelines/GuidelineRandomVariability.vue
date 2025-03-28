<template>
  <scaffold-alert
    title-text="Random Variability"
    @back="back_callback()"
    @next="next_callback()"
    back-text="Stage 4"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Due to the shortcomings you just considered, your age estimate may or may not reflect the "true" age of the universe, especially since you have a small sample of only 5 galaxies. It might help to explore data from your class and others who have completed this Data Story.  
      </p>
    </div>
  </scaffold-alert>
</template>
