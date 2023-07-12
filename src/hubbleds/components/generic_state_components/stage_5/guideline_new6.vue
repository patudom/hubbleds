<template>
  <scaffold-alert
    title-text="Select Best Value"
    @back="state.marker_backward = 1"
    @next="state.marker_forward = 1"
  >
    <div
      class="mb-4"
    >
    <p>
      The range you pick will have a tradeoff between how likely it is that the “true” value actually lies within the range you choose vs. having a narrow enough range that your measurement is actually useful.
    </p>

    <ul>
      <li>
        A very large range is more likely to include the "true" value, but may be so nonspecific that it is not useful.
      </li>
      <li>
        A narrow range has more specificity but may not include the "true" value.
      </li>
    </ul>

    <p>
      Different people will feel more or less comfortable with the
    different sides of this tradeoff, and there isn’t really a 
    right or wrong answer as long as you justify why you
    chose what you did.
  </p>

    <p>
      We have provided 3 options that respectively encompass the inner 50%, 68%, and 95% of all measurements.
    </p>

    <p>
      Try clicking them all to compare what ranges of ages
    </p>


    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  props: ['state']
}
</script>
