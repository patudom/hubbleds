<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Introducing the Guidelines"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
    back-text="Stage 0"
  >
    <template #before-next>
      Viewer loading
    </template>
    <div
      class="mb-4"
    >
      <p>
        <b>These orange boxes will guide you as you move through the story.</b>
      </p>
      <p>
        The information in the boxes will suggest what you should focus on, or what you should do next.
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
