<template>
  <scaffold-alert
    title-text="Consensus"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Recall that this dot plot provides one way to check our own velocity measurement using the <strong>wisdom of crowds</strong>. 
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
