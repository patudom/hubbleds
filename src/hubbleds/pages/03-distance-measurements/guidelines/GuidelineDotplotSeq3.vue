<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      nothing
    </template>

    <div
      class="mb-4"
    >
      <p>
        It looks like there is some disagreement about the distance to the galaxy. It might help to look at the angular size measurements that were used to obtain the distances. 
      </p>
    </div>
  </scaffold-alert>
</template>

