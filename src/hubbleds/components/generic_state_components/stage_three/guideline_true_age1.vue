<!-- this state.marker = 'tru_age1' -->
<template>
  <scaffold-alert
    header-text="Which Value Is the True Age?"
    @back="
      state.marker = 'two_his1';
    "
    @next="
      state.marker = 'tru_age2';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        There is only one universe that we live in, so our universe only has one age. Our job as scientists is to figure out if the <strong>true age</strong> of the universe is included within the ranges shown within these histograms, and if so, which value within the range is the true age.
      </p>
    </div>
  </scaffold-alert>
</template>
