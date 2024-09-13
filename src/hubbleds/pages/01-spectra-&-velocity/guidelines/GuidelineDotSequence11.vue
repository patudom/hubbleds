<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div>
      <p>
        It may have been tempting to choose the tallest line present, but you should always choose the line that aligns with the marker.
      </p>
    </div>
  </scaffold-alert>
</template>
