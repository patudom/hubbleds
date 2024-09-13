<template>
  <scaffold-alert
    title-text="Dot plots"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <template #before-next>
      Click <span class="inline-guideline-button tutorial">DOT PLOT TUTORIAL</span> button.
    </template>

    <div>
      <p>
        This is a <b>dot plot</b> of velocity measurements for you and a randomly chosen subset of others who have completed the Hubble Data Story.
      </p>
      <p>
        Your measurement is shown as an orange-red dot. <b>You may need to press <v-icon>cached</v-icon> on the Dotplot Viewer to see your data point.</b>
      </p>
      <!-- <p><strong style="font-size:2em">You might need to refresh to see your data point</strong></p> TODO -->
      <p>
        Click the <span class="inline-guideline-button tutorial">DOT PLOT TUTORIAL</span> button to learn about interpreting dot plots.
      </p>
    </div>
  </scaffold-alert>
</template>
