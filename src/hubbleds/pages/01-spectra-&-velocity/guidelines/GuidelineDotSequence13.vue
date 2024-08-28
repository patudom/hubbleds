<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
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
