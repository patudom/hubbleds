<template>
  <scaffold-alert
    title-text="Trend Lines"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-message-draw</v-icon></v-btn> and draw a trend line.
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
        Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-message-draw</v-icon></v-btn>  in the Toolbar to activate the drawing tool and try drawing a trend line through your data points.
      </p>
    </div>
  </scaffold-alert>
</template>
