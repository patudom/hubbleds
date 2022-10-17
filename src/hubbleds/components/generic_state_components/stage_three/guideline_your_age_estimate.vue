<template>
  <scaffold-alert
    header-text="Your Age Estimate"
    @back="
      state.marker = 'age_uni3';
    "
    @next="
      state.marker = 'sho_ref1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Congratulations! &#127881 You have made your very own estimate of the age of the universe.
      </p>
      <p>
        Now we need to think about how reliable your estimate is.
      </p>
    </div>
  </scaffold-alert>
</template>
