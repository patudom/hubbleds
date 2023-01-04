<!-- this state.marker = 'imp_met1' -->
<template>
  <scaffold-alert
    title-text="Our Methods are Imperfect"
    @back="
      state.marker = 'tru_iss1';
    "
    @next="
      state.marker = 'imp_ass1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Given the messiness of our velocity vs. distance measurements, it is clear that we did not use an optimal method for making these measurements.
      </p>
      <p>
        In particular, professional astronomers have more sophisticated ways to measure <strong>distances</strong> to things that are outside of the scope of this data story.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
