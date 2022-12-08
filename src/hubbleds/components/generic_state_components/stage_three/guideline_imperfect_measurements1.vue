<!-- this state.marker = 'imp_mea1' -->
<template>
  <scaffold-alert
    header-text="Our Measurements are Imperfect"
    @back="
      state.marker = 'imp_ass1';
    "
    @next="
      state.marker = 'unc_ran1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Human error contributes to imperfect measurements. Some people are more meticulous than others.
      </p>
      <p>
        Sometimes our tools limit our measurements. For example, did you feel confident that you were able to measure the edges of your galaxies correctly?
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
