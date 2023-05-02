<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :can-advance="(state) => state.meas_two_row_selected"
    :state="state"
  >
      <!-- :can-advance="(state) => state.meas_two_row_selected" -->
    <template #before-next>
      Click second row
    </template>
    <div>
      <p>
        Click the second row of the example galaxy table. 
        <!-- {{ state.meas_two_row_selected ? 'You have selected the second row.' : '' }} -->
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
