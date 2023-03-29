<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Meet the Spectrum Viewer"
    :can-advance="(state) => state.spec_tutorial_opened"
    :state="state"
    @back="() => {
      state.marker_backward = 1;
      state.spectrum_tool_visible = 0;
    }"
    @next="() => { state.marker_forward = 1; }"
  >

    <template #before-next>
      Click the <strong>SPECTRUM TUTORIAL</strong> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        The <b>spectrum</b> of light measured from the example galaxy is shown in the Spectrum Viewer.
      </p>
      <p>
        (If you scroll up to the Cosmic Sky Viewer, you will see the example galaxy displayed there too.)
      </p>
    </div>
    <div
      v-if="!(state.spec_tutorial_opened || state.marker == 'spe_tut1')"
    >    
      <p>
        Click the <strong>SPECTRUM TUTORIAL</strong> button to learn what spectra can tell us about galaxies.
      </p>
    </div>
    <div
      class="mb-4"
      v-if="state.spec_tutorial_opened || state.marker == 'spe_tut1'"
    >
      <p>
        You can reopen the <strong>SPECTRUM TUTORIAL</strong> any time you need a refresher about spectra.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
