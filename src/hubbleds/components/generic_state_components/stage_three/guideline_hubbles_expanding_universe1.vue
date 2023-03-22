<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Hubble's Expanding Universe"
    @back="state.marker = 'rel_vel1'"
    @next="state.marker = 'tre_lin1'"
    :can-advance="(state) => state.hubble_dialog_opened"
    :state="state"
  >
    <template #before-next>
      Click the <strong>HUBBLE'S DISCOVERY</strong> button.
    </template>
    
    <div
      class="mb-4"
    >
      <p>
        The relationship between your galaxies’ velocity and distance is the same as what Hubble found: galaxies at a greater distance away are moving away from us at a higher velocity.
      </p>
      <p>
       Click the <strong>HUBBLE'S DISCOVERY</strong> button to learn what was significant about this result.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
