<template>
  <scaffold-alert
    title-text="Most Likely Value"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Click the switches to display each quantity as a vertical line in the histogram. 
      </p>
      <p>
        Click <v-icon>mdi-help-circle-outline</v-icon> to learn more about each quantity.
      </p>
    </div>
  </scaffold-alert>
</template>

