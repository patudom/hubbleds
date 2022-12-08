<!-- this state.marker = 'unc_sys1' -->
<template>
  <scaffold-alert
    header-text="Systematic Uncertainties"
    @back="
      state.marker = 'unc_ran1';
    "
    @next="
      state.marker = 'unc_sys2';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Some uncertainties are <strong>systematic</strong>. These are problems with our methods or assumptions that lead to all measurements, on average, being <strong>incorrect in the same direction</strong>, which biases our final result.
      </p>
      <p>
        Can you think of any problems in our methods that could bias everyone’s results in the same direction?
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Problems in Our Methods"
        hint="(problems that might lead to systematic uncertainty)"
        tag="systematic-uncertainty"
      ></free-response>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
