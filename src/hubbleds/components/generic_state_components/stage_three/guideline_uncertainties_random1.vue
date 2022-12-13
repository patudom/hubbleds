<!-- this state.marker = 'unc_ran1' -->
<template>
  <scaffold-alert
    header-text="Random Uncertainties"
    @back="
      state.marker = 'imp_mea1';
    "
    @next="
      state.marker = 'unc_sys1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Given the imperfect nature of our measurements and assumptions, there is a chance that our results are different than the true age of the universe. We refer to these differences as <strong>uncertainties</strong> in our result.
      </p>
      <p>
        Some uncertainties are <strong>random</strong>. For example, if some galaxies in your sample are larger or smaller than the Milky Way, your resulting distances may be too close or too far, and then your resulting age may be too young or too old.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
