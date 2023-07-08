<template>
  <scaffold-alert
    title-text="Select Best Value"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
    <p>
      Now that you’ve identified your most likely value for the age of the universe, 
      we need to acknowledge that it’s not the only possible value. 
      Other values that were measured by your classmates are also possible, 
      so we want to specify a likely range of age values.
    </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
