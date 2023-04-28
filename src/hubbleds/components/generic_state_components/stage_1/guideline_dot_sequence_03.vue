<template>
  <scaffold-alert
    title-text="Your measurement vs Others'"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Another thing to check is whether your measurement is close or far away from other values.
      </p>
      <p>
        If your measurement is very far from others, that makes it an <strong>outlier</strong> and you may need to adjust how you made your measurement.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
