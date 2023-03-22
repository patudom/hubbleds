<template>
  <v-card class="mx-auto">
    <v-card-text>
      <v-window v-model="step" style="height: 70vh;">
        <v-window-item class="window-item-style">
          <p> Each bar tells us the number of measurements made at a particular velocity </p>
        </v-window-item>

        <v-window-item class="window-item-style">
          <p> The <span style="color:red">RED</span> line shows the value of YOUR measurment </p>
        </v-window-item>

        <v-window-item class="window-item-style">
          <p> The horizontal axis shows the measure velocity values </p>
        </v-window-item>

        <v-window-item class="window-item-style">
          <p> The vertical axis shows how many measurments were made at or near a particular velocity value </p>
        </v-window-item>

        <v-window-item class="window-item-style">
          <p> Each "tower" of dots represents measurements withing a certain velocity range (called a velocity "bin") </p>
        </v-window-item>

        <v-window-item class="window-item-style">
        <p></p>
        </v-window-item>
      </v-window>
    </v-card-text>

    <v-card-actions class="justify-space-between">
      <v-btn text @click="prev">
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
      <v-btn text @click="next">
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<style>
.window-item-style
{
  transition: none;
}
</style>

<script>
module.exports = {

  data: () => {
    return {
      step: 0,
      length: 5,
    }
  },

  // props: ["state"],

  methods: {
    next() {
      this.step = this.step === this.length - 1
        ? pass
        : this.step + 1
    },
    prev() {
      this.step = this.step - 1 < 0
        ? this.length - 1
        : this.step - 1
    },
  },

  watch: {
    step(val) {
      this.$emit('step', val)
    },
  },
}

</script>