<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Observed Wavelength"
    @back="() => { state.marker = 'obs_wav1'; }"
    @next="() => { state.marker = 'rep_rem1'; }"
    :can-advance="(state) => state.zoom_tool_activated"
    :state="state"
  >
    <template #next-content>
      Click <v-icon>mdi-select-search</v-icon> to activate tool. Click and drag across the red <strong>{{ state.galaxy.element }} </strong> marker to zoom in.
    </template>

    <div
      class="mb-4"
    >
      <p
        v-if=!state.zoom_tool_activated>  
        To improve the precision in your measurement, zoom in to the wavelength range around the {{ state.galaxy.element }} line using the <v-icon>mdi-select-search</v-icon> icon in the toolbar.
      </p>
      <p
        v-if=state.zoom_tool_activated>  
        If you accidentally zoomed in too far or in the wrong spot, you can click <v-icon>mdi-cached</v-icon> to reset the view to the full range of wavelengths.
      </p>
      <p>
        <strong>Tip:</strong> You can re-measure the wavelength as many times as you like. 
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
