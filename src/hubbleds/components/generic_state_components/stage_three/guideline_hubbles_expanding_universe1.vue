<template>
  <scaffold-alert
    header-text="Hubble's Expanding Universe"
    @back="
      state.marker = 'rel_vel1';
    "
    @next="
      state.marker = 'hub_exp2';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        The relationship between your galaxies’ velocity and distance is the same as what Hubble found: galaxies at a greater distance away are moving away from us at a higher velocity.
      </p>
    </div>
  </scaffold-alert>
</template>
