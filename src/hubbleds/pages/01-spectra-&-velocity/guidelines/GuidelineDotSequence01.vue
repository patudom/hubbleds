<template>
  <scaffold-alert
    title-text="Consensus"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div>
      <p>
        The dot plot provides one way to check our own velocity measurement using the <b>wisdom of crowds</b>. 
      </p>
    </div>
  </scaffold-alert>
</template>
