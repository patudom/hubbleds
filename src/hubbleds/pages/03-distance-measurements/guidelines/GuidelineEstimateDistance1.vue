<template>
  <scaffold-alert
    title-text="Estimate Distance"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        Now that you have an angular size measurement for the example galaxy, let’s estimate how far away it is.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
