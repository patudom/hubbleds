<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Rest Wavelength"
    :state="state"
    @back="() => { state.marker = 'mee_spe1'; }"
    @next="() => { state.marker = 'obs_wav1'; }"
  >

    <template #next-content>
      Click the <v-icon>mdi-lambda</v-icon> button.
    </template>

    <div
      class="mb-4"
    >
      <p
        v-if="!state.lambda_on"      
      >
        Your galaxy spectrum has {{ state.galaxy.element == 'Mg-I' ? 'a' : 'an' }} {{ state.galaxy.element }} {{ state.galaxy.element == 'Mg-I' ? 'absorption' : 'emission' }} line marked by a red vertical rectangle on the graph.
      </p>
      <p
        v-if="!state.lambda_used"
      >
        The known <strong>rest wavelength</strong> for the line is recorded in your table.
      </p>
      <p
        v-if="!state.lambda_on"
      >
        Click the <v-icon>mdi-lambda</v-icon> icon in the Spectrum Viewer toolbar to display the line's rest wavelength on the graph.
      </p>
      <p
        v-if="state.lambda_on"
      >
        The rest wavelength of your line appears in the graph as a vertical dotted line.
      </p>
      <p
        v-if="state.lambda_on"
      >
        You can click the <v-icon>mdi-lambda</v-icon> icon again to toggle the rest wavelength back off.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
