<template>
  <scaffold-alert
    title-text="Most Likely Values"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        When scientists measure an unknown quantity, they use the available data to determine: 
        <ol>
          <li>the measured value they think is <b>most likely</b>, and </li>
          <li>the most plausible range of measured values (called the <b>confidence interval</b>). </li> 
        </ol>
      </p>
      <p>
        Let's explore how to do this for your class's measurements.
      </p>
    </div>
  </scaffold-alert>
</template>


