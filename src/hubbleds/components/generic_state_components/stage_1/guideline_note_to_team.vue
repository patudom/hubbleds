<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div style="color:#1DE9B6!important">
      <p>
        Implement same slideshow functionality as the Hubble runners slideshow. (text on left, dot plot viewer on right)
      </p>
      <ul>
        <li> Explain how each dot represents a measurement. You can see how many measured values are in a bin
        <li> Zooming in breaks up measurements into smaller bins, to tall dot towers split into smaller towers.
      </ul>
      <p>
        Check what else is in existing tutorial that we should keep
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
