<template>
  <scaffold-alert
    header-text="Confidence Interval"
    @back="
      state.marker = 'cla_age4';
    "
    @next="
      state.marker = 'age_dis1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        When scientists make a measurement of an unknown quantity, they report the value that they think is most likely based on their measurements, and they report something called a confidence interval which gives lower and upper bounds on the most plausible <strong>range</strong> of measurement values.
      </p>
      <p>
        We'll guide you through how to do this for your class's measurements.
      </p>
    </div>
  </scaffold-alert>
</template>

<style>
  .JaxEquation .MathJax {
    margin: 3px auto !important;
  }
</style>