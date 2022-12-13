<!-- this state.marker = 'unc_sys1' -->
<template>
  <scaffold-alert
    header-text="Systematic Uncertainties"
    @back="
      state.marker = 'unc_sys1';
    "
    @next="
      state.marker = 'two_his2';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Here are possible sources of systematic uncertainty:
      </p>
      <p>
If we all miss measuring the faint outer edges of all our galaxies, our angular size measurements will all be a little bit too small, and everyone’s distance measurements will be a little bit too far, leading to ages that are a little bit too old.
      </p>
      <p>
We know that there is natural variation in the sizes of galaxies. If our Milky Way happens to be an “average” galaxy (somewhere in the middle of the actual distribution of galaxy sizes), our result would not have a bias. If the “average” size of a galaxy is different than the size of the Milky Way, that could lead to a bias in our age measurements.
      </p>
      <p>
        Sometimes sources of systematic uncertainty bias our results in different directions, effectively cancelling each other out.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
