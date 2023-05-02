<template>
  <guideline-professional-data
    prev-marker="pro_dat4"
    next-marker="pro_dat6"
    :auto-advance="true"
    :state="state"
    :index="5"
  >
    <div
      class="mb-4"
    >
      <p>
        Now let's consider more modern data from 2001, shown in lime green. 
        This data is from the HST Key Project, led by astronomer Wendy Freedman, who used data from the Hubble Space Telescope to measure a quantity known as the <strong>Hubble constant</strong>
        (which is the inverse of the age value you calculated).
      </p>
    </div>
  </guideline-professional-data>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
