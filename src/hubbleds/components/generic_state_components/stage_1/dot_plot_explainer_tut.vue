<template>
  <v-row>
  <v-btn
    block
    color="deep-orange darken-2"
    @click="show = !show"

  >
    What is a Histogram? {{ show }}
  </v-btn>

  <v-card v-show="show">
    <v-card-text>
      <v-window v-model="step">
        <v-window-item class="window-item-style">
          <p> Each dot represents a sinlge velocity measurement </p>
        </v-window-item>

        <v-window-item class="window-item-style">
          <p> The larger <span style="color:red">RED</span> dot shows YOUR measurments </p>
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
      <p> {{step + 1}} / {{length}} </p>
      <v-btn text @click="next">
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
  </v-row>
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
      show: false,
    }
  },

  // props: ["state"],

  methods: {
    next() {
      this.step = this.step === this.length - 1
        ? this.step + 0
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
    show(val) {
      console.log('show', val)
    },
  },
}

</script>
