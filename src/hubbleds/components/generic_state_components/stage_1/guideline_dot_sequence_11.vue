<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        We have zoomed in to the corresponding range of the spectrum viewer.
      </p>
      <p>
        When you measured the line earlier, you may have noticed that there is actually a trio of lines here. And you might have wondered which of them is the one you should have measured. The tallest one? The middle one?
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
        Many galaxies have this trio of lines. The H-alpha line is the one in the middle that corresponds to the marker. The emission lines to the left and right are cause by nitrogen in the galaxy.
      </v-alert>
    </div>
  </scaffold-alert>
</template>



<script>
module.exports = {
  props: ['state'],

  data: () => ({
      learn_more: false,
  })
}
</script>