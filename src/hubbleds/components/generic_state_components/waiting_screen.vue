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
        Waiting Screen
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
          <p>Very few of your classmates have finished taking their data, so let's wait for them to catch up.</p>
          <p>While you do, feel free to explore the sky using WorldWide Telescope!</p>
          <iframe
            allowfullscreen
            allow="accelerometer; clipboard-write; gyroscope"
            class="wwt-iframe"
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

    // The app needs some time to be ready to accept messages
    setTimeout(() => {
      console.log("About to post!");
      iframe.contentWindow.postMessage({
        event: "modify_settings",
        target: "app",
        settings: [["hideAllChrome", true]]
      }, "https://web.wwtassets.org/");
    }, 1000);
  }
}
</script>

