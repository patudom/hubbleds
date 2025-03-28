<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Angular Size Measurements"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    back-text="Stage 2"
  >
    <template #before-next>
      Viewer loading
    </template>
    <div
      class="mb-4"
    >
      <p>
        This is the same sky viewer you used in Stage 1, now with added functionality to measure angular sizes.
      </p>
      <p>
        The light blue vertical line on the left tells you the <b>angular size</b> of the patch of sky being displayed.
      </p>
      <p>
        Like last time, we will all measure the same example galaxy first.
      </p>
      <p>
        Use left Stage Navigation to return to earlier stages.
        (If closed, open navigation with <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #172c4d; border-radius: 5px;"><v-icon style="color:white!important;">mdi-menu</v-icon></v-btn> above)
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
</script>