<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Trend Lines"
    @back="state.marker = 'tre_lin1'"
    @next="state.marker = 'bes_fit1'"
    :can-advance="(state) => state.trend_line_drawn"
    :state="state"
  >
    <template #before-next>
      Draw a trend line.
    </template>

    <div
      class="mb-4"
    >
    <p>
        Even when data are messy, it is possible to explore relationships between the quantities being graphed. Scientists do this by fitting a <strong>model</strong> to the data. 
      </p>
      <p>
        Since we saw a trend in the larger class data set, let's start with a trend line. A <strong>trend line</strong> follows the observed trend in the graphed data.
      </p>
      <p>
        Click <v-icon>mdi-message-draw</v-icon> in the Toolbar to activate the drawing tool and try drawing a trend line through your data points.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>


