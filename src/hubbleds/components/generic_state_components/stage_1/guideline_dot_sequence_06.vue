<template>
  <scaffold-alert
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Let's focus on the part of the dot plot that includes most of the data and ignore outliers.
      </p>
      <p>
        As you did in the tutorial, use <v-icon>mdi-select-search</v-icon> to zoom in around the main tower of data.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
