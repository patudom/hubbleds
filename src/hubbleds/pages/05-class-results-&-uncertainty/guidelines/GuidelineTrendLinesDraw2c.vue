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
        First, draw a trend line for your class's data set.
      </p>
      <p>
        Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-message-draw</v-icon></v-btn> in the Toolbar to activate the drawing tool and try drawing a trend line through your class's data points.
      </p>
    </div>
  </scaffold-alert>
</template>
