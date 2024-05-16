<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div>
      <p>
        You might have noticed that there is a trio of lines near the H-&#945; marker. And you might have wondered which of them you should have measured. The tallest one? The middle one?
      </p>

      <v-btn
      block
      color="deep-orange darken-2"
      @click="
        learn_more = !learn_more
      "
      >
        What causes these lines?
      </v-btn>
      <v-alert
        class="mt-4 trend-alert"
        v-if="learn_more"
        dense
        color="info darken-1"
      >
        Many galaxies have this trio of lines. The H-&#945; line is the one in the middle that corresponds to the marker. The emission lines to the left and right are cause by nitrogen in the galaxy.
      </v-alert>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  data: () => ({
      learn_more: false,
  })
}
</script>
