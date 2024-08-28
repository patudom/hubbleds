<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div>
      <p>
       This bottom dot plot shows second measurements. Zoom in to see if there is more consensus in the second measurements than for the first measurements above.
      </p>
    </div>
  </scaffold-alert>
</template>
