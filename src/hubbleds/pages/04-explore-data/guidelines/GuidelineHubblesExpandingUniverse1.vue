<template>
  <scaffold-alert
    title-text="Hubble's Expanding Universe"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :state="state"
  >
    <template #before-next>
      Click <span class="inline-guideline-button tutorial">HUBBLE'S DISCOVERY</span> button.
    </template>
    
    <div
      class="mb-4"
    >
      <p>
        The relationship between your galaxies’ velocity and distance is the same as what Hubble found: galaxies at a greater distance away are moving away from us at a higher velocity.
      </p>
      <p>
       Click the <span class="inline-guideline-button tutorial">HUBBLE'S DISCOVERY</span> button to learn what was significant about this result.
      </p>
    </div>
  </scaffold-alert>
</template>


