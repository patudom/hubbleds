<template>
  <v-card
    id="waiting-screen"
    elevation="6"
  >
    <v-toolbar
      ref="toolbar"
      color="warning"
      dense
      dark
    >
      <v-toolbar-title
        class="text-h6 text-uppercase font-weight-regular"
      >
        Take a quick break
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <speech-synthesizer
        ref="synth"
        :root="$el"
        :selectors="['div.v-toolbar__title.text-h6', 'div.v-card__text.black--text', 'h3', 'p']"
      />
    </v-toolbar>
    <v-card-text>
      <v-container>
        <v-row>
          <p>You and your classmates will be comparing your measurements in the next section, but we need to wait a few moments for more of them to catch up.</p>
          <p>While you wait, you can explore the same sky viewer you saw in the introduction.</p>
          <p>This screen will autoadvance when enough classmates are ready to proceed.</p>
          <iframe
            allowfullscreen
            allow="accelerometer; clipboard-write; gyroscope"
            class="wwt-iframe"
            title="WorldWide Telescope"
            :src="`https://web.wwtassets.org/research/latest/?origin=${window.location.origin}`"
          >
            <p>ERROR: cannot display AAS WorldWide Telescope research app!</p>
          </iframe>
        </v-row>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
module.exports = {
  mounted() {
    const iframe = this.$el.querySelector(".wwt-iframe");

    /**
     * For now, I'm using the research app because we can't include script tags
     * in templates, and requirejs was giving some issues when I tried loading
     * the WWT SDK programmatically.
     * TODO: Figure this out!
     */

    // The app needs some time to be ready to accept messages
    setTimeout(() => {
      iframe.contentWindow.postMessage({
        event: "modify_settings",
        target: "app",
        settings: [["hideAllChrome", true]]
      }, "https://web.wwtassets.org/");
    }, 1000);
  }
}
</script>

<style scoped>
.wwt-iframe {
  width: 100% !important;
  height: 500px !important;
}
</style>
