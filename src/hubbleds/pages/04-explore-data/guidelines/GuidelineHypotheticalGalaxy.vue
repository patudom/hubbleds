<template>
  <scaffold-alert
    title-text="A Hypothetical Galaxy"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        This "best fit galaxy" is a hypothetical galaxy that lies on your best fit line. You can use its distance and velocity to estimate the age of the universe given by the best fit line to your galaxy data. (Any galaxy that lies on this line would give you the same age estimate.)
      </p>
      <!-- we have two values state_view.hypgal_distance and state_view.hypgal_velocity. display these nicely, not as an equation -->
      <v-card color="alert" class="mb-4">
        <v-card-text style="font-weight: bold; color: blue;">
          Your best fit galaxy is at<br>
          Distance: {{ state_view.hypgal_distance }} Mpc<br>
          Velocity: {{ state_view.hypgal_velocity }} km/s
        </v-card-text>
      </v-card>
      
        Now let's look at the equation that can tell us the age of universe.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>