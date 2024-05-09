<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
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
        Click the box next to  <span style="background-color: white; border-radius : 5px; padding: 3px; color:black!important; font-size: 80%"><strong>Class Data</strong></span>  in the legend panel to display measurements from your entire class.
      </p>
    </div>
  </scaffold-alert>
</template>