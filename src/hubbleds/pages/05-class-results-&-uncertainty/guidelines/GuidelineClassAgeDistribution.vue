<template>
  <scaffold-alert
    title-text="Class Age Distribution"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        First, it is helpful to visualize the data in a different way. 
      </p>
      <p>
        This is a <b>histogram</b>, which displays the distribution of your classmates' age estimates for the universe. The <b>range</b> of age values is shown on the <b>x-axis</b>, and the number <b>count</b> of students who measured that value for the age of the universe is shown on the <b>y-axis</b>.
      </p>
    </div>
  </scaffold-alert>
</template>


