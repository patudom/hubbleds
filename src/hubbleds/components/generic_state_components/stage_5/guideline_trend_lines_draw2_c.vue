<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Trend Lines"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
    :can-advance="(state) => state.class_trend_line_drawn"
    :state="state"
  >
    <template #before-next>
      Click <v-icon>mdi-message-draw</v-icon> and draw a trend line.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Now that you've drawn what conclusions you can from looking at individual students' measurements, let's turn back to your whole class's dataset.
      </p>
      <p>
        Click <v-icon>mdi-message-draw</v-icon> in the Toolbar to activate the drawing tool and try drawing a trend line through your class's data points.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
