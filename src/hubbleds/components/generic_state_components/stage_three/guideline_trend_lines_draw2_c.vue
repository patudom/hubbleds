<template>
  <scaffold-alert
    header-text="Trend Lines"
    @back="
      state.marker = 'con_int2';
    "
    @next="
      state.marker = 'bes_fit1c';
    "
  >
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
