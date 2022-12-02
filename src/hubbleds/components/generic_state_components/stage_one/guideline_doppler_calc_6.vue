<template>
  <v-alert
      class="mb-4 mx-auto"
      color="info"
      elevation="6"
      max-width="800"
  >
    <h3
        class="mb-4"
    >
      Velocity Calculation
    </h3>
    <div
        v-if="state.velocities_total < 5"
        v-intersect="(entries, _observer, intersecting) => {
        if (!intersecting) return;
        const targets = entries.filter(entry => entry.isIntersecting).map(entry => entry.target);
        MathJax.typesetPromise(targets);            
      }"
        class="mb-4"
    >
      <p>
        Notice your calculated velocity is now entered in the table.
      </p>
      <div
          class="JaxEquation"
      >
        $$ v = {{ state.student_vel.toFixed(0).toLocaleString() }} \text{ km/s}$$
      </div>
      <p>
        Now that you know how to use the Doppler equation, click the
        <v-icon>mdi-run-fast</v-icon>
        icon in the table header to have the velocities of the remaining galaxies calculated as well.
      </p>
    </div>
    <div
        v-if="state.velocities_total === 5"
        class="mb-4"
    >
      Great work! You have completed Stage 1. Proceed to Stage 2.
    </div>
    <v-divider
        class="my-4"
    >
    </v-divider>

    <v-row
        align="center"
        no-gutters
    >
      <v-col>
        <v-btn
            class="black--text"
            color="accent"
            elevation="2"
            @click="
            state.marker = 'dop_cal3';
          "
        >
          back
        </v-btn>
      </v-col>
      <v-spacer></v-spacer>

      <v-col
          v-if="state.velocities_total < 5"
          class="shrink"
          cols="4"
      >
        <div
            style="font-size: 16px;"
        >
          Click the
          <v-icon>mdi-run-fast</v-icon>
          icon.
        </div>
      </v-col>
      <v-col
          v-if="state.velocities_total === 5"
          class="shrink"
      >
        <v-btn
            class="black--text"
            color="accent"
            elevation="2"
            @click="state.completed = true"
        >
          stage 2
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>


<style>

.JaxEquation .MathJax {
  margin: 16px auto !important;
}

</style>

<script>
module.exports = {
  props: ['state']
}
</script>