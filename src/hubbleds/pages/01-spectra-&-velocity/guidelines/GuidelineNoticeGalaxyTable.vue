<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Table Data"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Notice that your table now has a row for your selected galaxy, and the marker on your galaxy has changed from green to yellow.
      </p>
    </div>
  </scaffold-alert>
</template>
