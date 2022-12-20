<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Distances Complete"
    @back="state.marker = 'fil_rem1'"
    @next="state.stage_two_complete = true;"
  >
    <div
      class="mb-4"
    >
      <p>
        You are ready to move on to the next stage.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
