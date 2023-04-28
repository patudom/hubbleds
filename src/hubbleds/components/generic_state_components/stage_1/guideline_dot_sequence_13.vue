<template>
  <scaffold-alert
    @back="() => { state.marker = 'dot_seq12'; }"
    @next="() => { state.marker = 'rem_gal1'; }"
    :state="state"
  >
    <div>
      <p>
       Click the second row of the example galaxy table and take your second measurement keeping in mind what you learned from the dot plots. 
      </p>
    </div>
  </scaffold-alert>
</template>




<script>
module.exports = {
 props: ['state']
}
</script>
