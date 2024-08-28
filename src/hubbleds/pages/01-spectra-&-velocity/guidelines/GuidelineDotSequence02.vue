<template>
  <scaffold-alert
    title-text="Your measurement vs Others'"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div>
      <p>
        One thing to check is whether your measurement is close or far away from other values.
      </p>
      <p>
        A far away measurement is called an <strong>outlier</strong> and may indicate that the value was measured incorrectly.
      </p>
      <p>
        Don't worry if your value is an outlier. You will have a chance to remeasure it.
      </p>
    </div>
  </scaffold-alert>
</template>
