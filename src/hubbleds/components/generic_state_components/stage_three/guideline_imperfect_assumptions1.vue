<!-- this state.marker = 'imp_ass1' -->
<template>
  <scaffold-alert
    header-text="Our Assumptions are Imperfect"
    @back="
      state.marker = 'imp_met1';
    "
    @next="
      state.marker = 'imp_mea1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        We assumed that all galaxies are the same size as our own galaxy, the Milky Way. This is not a correct assumption, as galaxies have a large amount of natural variability in their sizes. This is likely the biggest source of “messiness” in our results.
      </p>
    </div>
  </scaffold-alert>
</template>
