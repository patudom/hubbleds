<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Angular Size Measurement"
    @back="state.marker = 'ang_siz4'"
    @next="state.marker = 'ang_siz5a'"
  >
    <div
      class="mb-4"
    >
      <p>
        Notice your galaxy’s angular size is now displayed in the table.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
