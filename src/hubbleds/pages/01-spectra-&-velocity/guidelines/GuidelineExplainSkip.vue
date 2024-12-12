<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Skipped Content"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div
      class="mb-4"
    >
      <p>
        Notice your calculated velocity is now in the table.
      </p>
      <p>
        <span style="font-weight:bold">SKIPPED CONTENT:</span> Shortened DEMO version skips a sequence where students compare their velocity measurement with that of their peers using a dot plot, to help them evaluate whether they have accurately measured the observed wavelength of the example galaxy.
      </p>
    </div>
  </scaffold-alert>
</template>
