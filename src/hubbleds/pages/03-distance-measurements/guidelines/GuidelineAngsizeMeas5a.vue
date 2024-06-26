<template>
  <scaffold-alert
    title-text="Angular Size Measurement"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Click <span class="inline-guideline-button tutorial">MEASUREMENT DOS AND DONTS</span> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Given that there was not consensus on the angular size measurements for the galaxy, click <span class="inline-guideline-button tutorial">MEASUREMENT DOS AND DONTS</span> for tips on how to ensure the most accurate results.
      </p>
    </div>
  </scaffold-alert>
</template>


