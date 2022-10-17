<template>
  <scaffold-alert
    header-text="Your Age Estimate"
    @back="
      state.marker = 'age_uni4';
    "
    @next="
      state.marker = 'sho_est1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Congratulations! &#127881 You have made your very own estimate of the age of the universe.
      </p>
      <p>
        We will now label your best-fit line with your age estimate.
      </p>
      <p>
        Next, we need to think about how reliable your estimate is.
      </p>
    </div>
  </scaffold-alert>
</template>
