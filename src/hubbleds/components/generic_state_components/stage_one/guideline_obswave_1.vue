<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Observed Wavelength"
    :can-advance="(state) => state.obswaves_total >= 1"
    @back="() => { state.marker = 'res_wav1'; }"
    @next="() => { state.marker = 'obs_wav2'; }"
    :state="state"
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
        Align the measuring tool to the <strong>{{ state.galaxy.element }} (observed)</strong> marker and click. This records the <strong>observed wavelength</strong> in your table.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
