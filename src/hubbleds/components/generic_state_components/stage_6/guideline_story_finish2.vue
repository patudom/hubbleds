<template>
  <scaffold-alert
    @back="state.marker = 'sto_fin1'"
    :can-advance="(_state) => false"
  >
    <div
      class="mb-4"
    >
    <p>
      <strong>There is no right answer</strong>, but we hope this story has given you a better understanding of how scientists use data to determine how much confidence you can have in a new result.
    </p>
    <p>
      Science is always moving forward and there is always more humans can learn about our universe. Follow NASA to learn what new discoveries are being made by HST's successor, the James Webb Space Telescope!
    </p>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
