<template>
  <scaffold-alert
    header-text="Trend Lines"
    @back="
      state.marker = 'hub_exp1';
    "
    @next="
      state.marker = 'tre_lin2';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Let's return to your own 5 data points and see what we can learn from them now that we are aware of a trend in the larger data set.
      </p>
    </div>
  </scaffold-alert>
</template>
