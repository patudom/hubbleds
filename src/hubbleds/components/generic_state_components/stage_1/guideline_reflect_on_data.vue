<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Reflect on Your Data"
    :can-advance="(state) => state.reflection_complete"
    :state="state"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
  >

    <template #before-next>
      Click <span style="background-color: #DD2C00; border-radius: 5px; padding: 3px; color:white!important;">REFLECT</span> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        As scientists do, let’s examine what conclusions you might draw from your data.
      </p>
      <p>
        Click the <span style="background-color: #DD2C00; border-radius: 5px; padding: 3px; color:white!important;">REFLECT</span> button to complete the reflection sequence before moving on.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
