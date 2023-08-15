<template>
  <scaffold-alert
    title-text="Classmates' Data"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        Now let’s look at age estimates of the universe from other classes who have already completed this data story.
      </p>
      <p>
        Your class's graph is highlighted in blue.
      </p>
      <p>
        Use the slider to scan through the age estimates that each participating class measured. 
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
