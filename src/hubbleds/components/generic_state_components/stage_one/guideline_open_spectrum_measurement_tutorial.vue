<template>
  <scaffold-alert
    title-text="Choose a Row"
    @back="() => { state.marker = 'dop_cal5'; }"
    @next="() => { state.marker = 'smt_tut'; }"
  >

  <div class="mb-4">
    Now that you have measured the velocity of the example galaxy, 
    let's compare it with existing measurements in our database!
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
