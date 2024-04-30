<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Choose a Row"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
  <template #before-next>
      Select the example galaxy from your table.
    </template>  
  <div class="mb-4">
      <p>
      For the moment, we have replaced the galaxies in your table with the example galaxy.
      </p>
      <p>
      Click the row containing the example galaxy to select it.
      </p>
    </div>
  </scaffold-alert>
</template>
