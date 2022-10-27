<!-- this state.marker = 'sho_est3' -->
<template>
  <scaffold-alert
    header-text="Shortcomings in Your Estimate"
    @back="
      state.marker = 'tru_age2';
    "
    @next="
      state.marker = 'sho_est4';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Recall your thoughts about shortcomings in your estimate:
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Shortcoming #1"
        tag="shortcoming-1"
      ></free-response>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Shortcoming #2"
        tag="shortcoming-2"
      ></free-response>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Other Shortcomings"
        hint="(if you can think of any more)"
        tag="other-shortcomings"
      ></free-response>
    </div>
  </scaffold-alert>
</template>
