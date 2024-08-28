<template>
  <scaffold-alert
    next-text="stage 2"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
  <template #before-next>
      Remeasure the wavelength.
    </template>
    <div>
      <p>Great work! You have completed Stage 1. Proceed to Stage 2.</p>
    </div>
    <v-card
      v-if="state_view.has_bad_velocities || state_view.has_multiple_bad_velocities"
      color="warning"
      >
      <v-card-text>
        <strong>Warning:</strong>You seem to have some bad measurements. Please review your measurements and try again. If you don't see an issue, ask your teacher for help.
      </v-card-text>
    </v-card>
  </scaffold-alert>
</template>
