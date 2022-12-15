<!-- this state.marker = 'tru_age2' -->
<template>
  <scaffold-alert
    header-text="Which Value Is the True Age?"
    @back="
      state.marker = 'tru_age1';
    "
    @next="
      state.marker = 'sho_est3';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        First, let’s think about <strong>why</strong> we found a range of values in the first place (rather than all getting the same value).
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
