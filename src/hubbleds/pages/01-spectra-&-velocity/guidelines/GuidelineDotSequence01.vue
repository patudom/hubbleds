<template>
  <scaffold-alert
    title-text="Consensus"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div>
      <p>
        Recall that this dot plot provides one way to check our own velocity measurement using the <strong>wisdom of crowds</strong>. 
      </p>
    </div>
  </scaffold-alert>
</template>
