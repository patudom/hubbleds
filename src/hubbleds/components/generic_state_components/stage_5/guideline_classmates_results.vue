<template>
  <scaffold-alert
    title-text="Classmates' Data"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
      <p>
        Let’s look at your classmates' data, student by student. Someone in your class measured the lowest age value for the universe. Someone measured the highest age.
      </p>
      <p>
        Use the slider to scan through the age estimates that each person in your class measured. 
      </p>
      <p>
        Your value appears as a different color than your classmates'.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
