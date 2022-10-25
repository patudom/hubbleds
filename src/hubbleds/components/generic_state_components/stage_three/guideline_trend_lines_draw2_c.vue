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
        Now that you've drawn what conclusions you can from looking at individual students' measurements, let's turn back to your whole class's dataset.
      </p>
      <p>
        Is it easier to identify a trend in the larger dataset?
      </p>
      <p>
        Click <v-icon>mdi-message-draw</v-icon> in the Toolbar to activate the drawing tool and try drawing a trend line through your class's data points.
      </p>
    </div>
  </scaffold-alert>
</template>
