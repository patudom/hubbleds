<!-- this state.marker = 'lac_bia3' -->
<template>
  <scaffold-alert
    header-text="Which Might Produce a Closer Result?"
    @back="
      state.marker = 'lac_bia2';
    "
    @next="
      state.marker = 'mor_dat1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Why do you think the class (with 50-100 galaxies) is likely to produce a result closer to the true value than a student (with 5 galaxies)?
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Reason"
        tag="reason-class-closer"
      ></free-response>
    </div>
  </scaffold-alert>
</template>
