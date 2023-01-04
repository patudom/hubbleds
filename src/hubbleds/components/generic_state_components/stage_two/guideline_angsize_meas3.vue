<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Angular Size Measurement"
    @back="state.marker = 'ang_siz2b'"
    @next="state.marker = 'ang_siz4'"
    :can-advance="(state) => state.ruler_clicked_total > 0"
    :state="state"
  >
    <template #before-next>
      Click the <v-icon>mdi-ruler</v-icon> icon.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Zoom in or out so your entire galaxy is framed within the viewer.
      </p>    
      <p>
        Click the <v-icon>mdi-ruler</v-icon> icon to activate the angular size measuring tool.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
