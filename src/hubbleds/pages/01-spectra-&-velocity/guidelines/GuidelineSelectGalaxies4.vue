<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Example Galaxy"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="!can_advance"
  >


    <div>
      <p>
        We'll start with an example galaxy so that we can learn how to make good measurements. 
      </p>
      <p>
        Everyone will measure a velocity for the same galaxy.
      </p>
    </div>
  

  </scaffold-alert>
</template>
