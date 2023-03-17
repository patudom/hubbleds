<!-- this state.marker = 'sho_est3' -->
<template>
  <scaffold-alert
    header-text="Shortcomings in Your Estimate"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        Recall your thoughts about shortcomings in your estimate:
      </p>
      <p>
        Shortcoming #1:
      </p>
      <p>
        {{ state.age_calc_state.short_one }}
      </p>
      <p>
        Shortcoming #2:
      </p>
      <p>
        {{ state.age_calc_state.short_two }}
      </p>
      <p>
        Other shortcomings:
      </p>
      <p>
        {{ state.age_calc_state.short_other }}
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
