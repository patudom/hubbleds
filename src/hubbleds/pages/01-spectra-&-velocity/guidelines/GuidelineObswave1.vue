<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Observed Wavelength"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <template #before-next>
      Measure the observed wavelength.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Hover your mouse in the Spectrum Viewer. A vertical measuring tool identifies the wavelength as you move the tool left and right.
      </p>
      <p>
        Align the measuring tool to the <b><span style="color:#ff665e; background-color: white; border-radius : 5px; padding: 3px">{{ state_view.selected_example_galaxy.element }} (observed)</span></b> marker and click. This records the <b>observed wavelength</b> (&lambda;<sub>obs</sub>) in your table.
      </p>
    </div>
  </scaffold-alert>
</template>
