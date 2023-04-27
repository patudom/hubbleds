<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Second Measurement Comparison"
    @back="state.marker = 'dot_seq5'"
    @next="state.marker = 'dot_seq6'"
    :state="state"
    >
    <div class="mb-4">
      <p>
        Your angular size and distance measurements are now entered in the table.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
