<template>
  <scaffold-alert
    title-text="Trends in the Data"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Click Class Data box
    </template>

    <div
      class="mb-4"
    >
      <p>
        It can be difficult to notice a trend with so few data points.
      </p>
      <p>
        Since everyone in your class also measured 5 galaxies, let's look at a dataset that combines everyone's measurements.
      </p>
      <p>
        Click the box next to  <span class="inline-guideline-button" style="background-color: white; color:black!important; font-size: 80%"><b>Class Data</b></span>  in the legend panel to display measurements from your entire class.
      </p>
    </div>
  </scaffold-alert>
</template>