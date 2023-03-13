<!-- this state.marker = 'sho_est4' -->
<template>
  <scaffold-alert
    title-text="Shortcomings in Your Estimate"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        Is there anything more you would like to add now that you’ve seen more data? (It’s OK if not.)
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Shortcoming #4"
        hint="(if you can think of any more)"
        tag="shortcoming-4"
      ></free-response>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
