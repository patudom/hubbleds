<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Choose a Galaxy"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Select example galaxy from table.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Click on the row with the example galaxy to select it.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
