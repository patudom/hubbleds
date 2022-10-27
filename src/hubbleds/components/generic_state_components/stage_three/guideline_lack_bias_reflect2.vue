<!-- this state.marker = 'lac_bia2' -->
<template>
  <scaffold-alert
    header-text="Which Might Produce a Closer Result?"
    @back="
      state.marker = 'lac_bia1';
    "
    @next="
      state.marker = 'lac_bia3';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Again, assuming no systematic bias, let’s consider two scenarios:
      </p>
      <p>
        If a <strong>student</strong> could only make one measurement, how far away from the true value would you expect their measurement to be?
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="How far away"
        tag="student-distance-from-true"
      ></free-response>
    </div>
    <div
      class="mb-4"
    >
      <p>
        If a <strong>class</strong> could only make one measurement, how far away from the true value would you expect their measurement to be?
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="How far away"
        tag="class-distance-from-true"
      ></free-response>
    </div>
  </scaffold-alert>
</template>
