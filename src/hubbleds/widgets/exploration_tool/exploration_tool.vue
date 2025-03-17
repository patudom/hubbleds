<template>
  <v-card
    color="info"
    :class="highlighted ? 'pa-1' : ''"
    v-intersect.once="(entries, observer, isIntersecting) => {
      const root = entries[0].target;
      const element = root.querySelector('iframe');
      if (element) {
        element.src = element.src.replace('/api/kernels', '');
      }
    }"
  >
    <v-toolbar
      height="40px"
      dense
      dark
      class="text-uppercase toolbar"
    >
      <v-toolbar-title>Cosmic Sky Viewer</v-toolbar-title>
      <v-spacer></v-spacer>          
      <div class="text-center">
        <v-dialog v-model="dialog" width="600">
          <template v-slot:activator="{ on, attrs }">
            <v-btn 
              icon
              right
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-information-outline</v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              Data Tool and Imagery credits
            </v-card-title>
            <v-card-text>
              <p>
                This WorldWideTelescope tool displays the Digitized Sky Survey which combines all-sky photographic surveys from the Palomar and UK Schmidt telescopes.
              </p>
            </v-card-text>
            <v-card-actions>
               <v-spacer></v-spacer>
              <v-btn
                text
                @click="dialog = false"
              >
                Close
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </v-toolbar>
    <div id="exploration-root" style="position: relative;">
      <v-overlay absolute opacity="1" v-show="!wwt_ready">
        <v-progress-circular
          indeterminate
          color="primary"
          size="100"
        ></v-progress-circular>
      </v-overlay>
      <jupyter-widget
        :widget="widget"
        id="exploration-widget"
      />
    </div>
  </v-card>
</template>

<style scoped>
#exploration-widget .p-Widget, #exploration-widget .p-Widget iframe {
  height: 350px !important;
  width: 100% !important;
}
</style>
<script setup lang="ts">
</script>