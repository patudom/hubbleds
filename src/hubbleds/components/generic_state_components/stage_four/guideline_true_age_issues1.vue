<!-- this state.marker = 'tru_iss1' -->
<template>
  <scaffold-alert
    title-text="Issues with Our Estimates"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        There are a few things that could prevent us from finding the true age of the universe:
      </p>
      <ul>
        <li>Our <strong>methods</strong> are imperfect</li>
        <li>Our <strong>assumptions</strong> about the universe are imperfect</li>
        <li>Our <strong>measurements</strong> are imperfect</li>
      </ul>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
