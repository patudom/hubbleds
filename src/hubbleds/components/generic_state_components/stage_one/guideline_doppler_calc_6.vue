<template>
  <scaffold-alert
      class="mb-4 mx-auto"
      color="info"
      elevation="6"
      max-width="800"
      header-text="Velocity Calculation"
      :can-advance="(state) => state.velocities_total === 5"
      next-text="stage 2"
      :state="state"
      @back="() => { state.marker = 'dop_cal3'; }"
      @next="() => { state.completed = true; }"
  >
    <template #next-content>
      Click the <v-icon>mdi-run-fast</v-icon> icon.
    </template>

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
      <p>Great work! You have completed Stage 1. Proceed to Stage 2.</p>
    </div>
  </scaffold-alert>
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
