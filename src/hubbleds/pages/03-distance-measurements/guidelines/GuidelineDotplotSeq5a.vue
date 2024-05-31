<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Second Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    >
    <template #before-next>
        Select second measurement row
    </template>
    <div class="mb-4">
      <p>
        Click on the new row labeled <b>second</b> to remeasure the galaxy angular size.
      </p>
    </div>
  </scaffold-alert>
</template>

