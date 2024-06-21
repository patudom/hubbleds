<!-- this state.marker = 'lea_unc1' -->
<template>
  <scaffold-alert
    title-text="Learn About Uncertainty"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
   
    <template #before-next>
      Click <span class="inline-guideline-button tutorial">UNCERTAINTY TUTORIAL</span> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Before we go further, let's explore in more detail <b>why</b> different students may have obtained different age values for the universe.
      </p>
      <p>
        Scientists explain this using a concept called <b>uncertainty</b>. Click the <span class="inline-guideline-button tutorial">UNCERTAINTY TUTORIAL</span> button to learn about this important concept for interpreting data.
      </p>
    </div>
  </scaffold-alert>
</template>

