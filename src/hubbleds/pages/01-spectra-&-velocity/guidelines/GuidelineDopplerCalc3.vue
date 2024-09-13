<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Select a Galaxy"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <template #before-next>
      Select a galaxy from your table.
    </template>
    
    <div class="mb-4">
      <p>
        Click on a row in your table to select one of the galaxies.
      </p>
      <p>
        You will calculate the velocity for this galaxy using the Doppler equation.
      </p>
    </div>
  </scaffold-alert>
</template>


<style>

.JaxEquation .MathJax {
  margin: 0 auto 16px !important;
}

</style>
