<template>
  <scaffold-alert
    @back="state.marker = 'pro_dat9'"
    @next="state.marker = 'sto_fin2'"
  >
    <div
      class="mb-4"
    >
    <p>
      Nice work! You have completed the Hubble Data Story and determined an age for our universe. Check out your total <v-icon>mdi-piggy-bank</v-icon> points in the upper right of the screen.
    </p>
    <p>
      Now you may be wondering "So what's the <strong>right</strong> answer?"
    </p>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
