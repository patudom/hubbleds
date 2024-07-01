<template>
  <scaffold-alert
    title-text="Shortcomings in Your Estimate"
    @back="back_callback()"
  >
  <!-- state.marker = 'ran_var1'; -->
    <div
      class="mb-4"
    >
      <p>
        Here are some shortcomings you might have identified. If you have a neighbor at the same point in the Data Story as you, you can discuss some of these issues with them:
      </p>
      <ul>
        <li>Do you think 5 galaxies is a large enough sample size for making a scientific measurement?</li>
        <li>Your distance measurement makes an important assumption that all galaxies are the same size as the Milky Way. Do you think this is a good assumption?</li>
        <li>Did you have difficulty identifying the “edge” of the galaxies when measuring angular size?</li>
        <li>Did you zoom in to an appropriate wavelength range when measuring the observed spectral lines for your galaxies?</li> 
      </ul>
      <p class="mt-3">
        Note: These kinds of measurements are not straightforward. If you had any difficulties, that is inherent to the process and it does NOT mean you are "bad" at this.
      </p>
    </div>
  </scaffold-alert>
</template>
