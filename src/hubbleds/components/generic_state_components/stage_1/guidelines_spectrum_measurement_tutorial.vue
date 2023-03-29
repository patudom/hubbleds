<template>
<v-card class="mx-auto">
  <v-card-text>
  <v-window 
    v-model="step"
    style="height: 70vh;"
    class="window-style"
    >
      <v-window-item :value="0" class="window-item-style">
        <p>This graph displays the range of velocity measurements that have been
          made for the example galaxy (by you, your classmates, and
          others who have completed this Data Story).
        </p>
        <p>
          Click here to learn more about how to interpret this kind of graph.
          <dot-plot-explainer-tut/> 
        </p>
      </v-window-item>
    
      <v-window-item :value="1" class="window-item-style">
        <p>
          Notice that most of the measurements are clustered around a “tower” of dots at roughly the same velocity.
        </p>
        <p>
          A few measurements have velocities that are very different from the measurements in the “tower.”
        </p>
        <p>
          Which measurements do you expect are closest to the “true” velocity of the galaxy?
        </p>
    
        <mc-radiogroup 
          :radio-options="[
            'A measurement in the tower.',
            'A measurement outside the tower'
            ]" 
          :feedbacks="[
            'Correct! Typically, the <i>wisdom of crowds</i> would tell you that the true value is in the tower.',
            'Typically, the <i>wisdom of crowds</i> would tell you that the true value is in the tower.'
            ]" 
          :correct-answers="[0]"
          :selected-callback="(opt) => { if (opt.correct) { console.log('correct'); } }"
          score-tag="spec_meas_tut1">
        </mc-radiogroup>
      </v-window-item>
    
      <v-window-item :value="2" class="window-item-style">
        <p>
          Let's explore what is happening with the points that are outside the tower.
        </p>
      </v-window-item>
    
      <v-window-item :value="3" class="window-item-style">
        <p>
          It would help to know what wavelengths on the spectrum graph these measurements correspond to.
        </p>
        <p>
          Use the <strong>selector tool</strong> to highlight one of the measurements outside the tower.
        </p>
      </v-window-item>
    
      <v-window-item :value="4" class="window-item-style">
        <p>
          The wavelength that corresponds to that velocity is displayed as a line on the spectrum graph.
        </p>
        <p>
          Notice where the line appears.
        </p>
      </v-window-item>
    
      <v-window-item :value="5" class="window-item-style">
        <p>
          Try selecting another point outside the “tower” and see where that lies on the spectrum graph.
        </p>
      </v-window-item>
    
      <v-window-item :value="6" class="window-item-style">
        <p>
          Now use the <i>selector tool</i> to highlight one of the measurements in the tower.
        </p>
      </v-window-item>
    
      <v-window-item :value="7" class="window-item-style">
        <p>
          Notice that measurements in the “tower” correspond to the red H-alpha marker.
        </p>
        <p>
          Measurements outside the tower might correspond to other lines or the edge of the spectrum, but are not near the
          red H-alpha marker.
        </p>
      </v-window-item>
    
      <v-window-item :value="8" class="window-item-style">
        <p>
          In this lab, the procedure for determining the galaxy speed is to make the wavelength measurement at the marked
          spectral line (in the case of this example galaxy, H-&alpha;).
        </p>
        <p>
          You will have a chance to redo your measurement later, so keep this in mind if your measured value was not near
          the marked line.
        </p>
      </v-window-item>
    
      <v-window-item :value="9" class="window-item-style">
        <p>
          At this point, how confident do you feel about your velocity measurement?
          <mc-radiogroup 
          :radio-options="[
            'Very confident',
            'Somewhat confident',
            'Not confident at all'
            ]"
            :feedbacks="[
            'Intersting! As we proceed through this section, we will see if this confidence is justified.',
            'Intersting! As we proceed through this section, we will see how we build confidence',
            'Intersting! Perhaps by the end of this section we will arrive at a more confident answer.'
            ]" 
          :neutral-answers="[0,1,2]"
          :selected-callback="(opt) => { if (opt.correct) { console.log('correct'); } }"
          score-tag="spec_meas_tut2">
            >
          </mc-radiogroup>
        </p>
      </v-window-item>
    
      <v-window-item :value="10" class="window-item-style">
        <p>
          Now that we know our measured value should be in the tower, we can look more closely at the values around the
          tower and exclude the outliers outside the tower.
        </p>
        <p> Use the zoom <v-icon>mdi-select-search</v-icon> tool </p>
      </v-window-item>
    
      <v-window-item :value="11" class="window-item-style">
        <p>
          Notice, we have also zoomed into the spectrum graph to show the range of wavelengths that corresponds to the range
          of velocities you selected.
        </p>
      </v-window-item>
    
      <v-window-item :value="12" class="window-item-style">
        <p>
          We can see that the single large tower splits into several smaller ones.
        </p>
        <p>
          This happens because each tower represents a <i>range of velocities</i>. 
          When you zoom in, there are now more bins, each covering a narrower velocity range.
        </p>
        <p>
          Your data point (if it is in this range) is shown in red.
        </p>
      </v-window-item>
    
      <v-window-item :value="13" class="window-item-style">
        <p>
          When we zoom in on the spectrum graph, notice that the region marked H-alpha actually shows a group of three
          spectral lines.
        </p>
        <p>
          You may have wondered which of the three lines is the one you should have measured.
        </p>
      </v-window-item>
    
      <v-window-item :value="14" class="window-item-style">
        <p>
          Many galaxies have this trio of lines. The H-alpha line is the one in the middle that corresponds to the marker.
          The emission lines to the left and right are of nitrogren in the galaxy.
        </p>
        <p>
          It may have been tempting to choose the tallest line present, but you should always choose the line that
          aligns with the marker.
        </p>
      </v-window-item>
    
      <v-window-item :value="15" class="window-item-style">
        <p>
          Try selecting points at different velocities and see where they line on the spectrum graph.
        </p>
        <p>
          Try to identify which tower of dots corresponds to the correct spectral line
        </p>
      </v-window-item>
    
      <v-window-item :value="16" class="window-item-style">
        <p>
          After exploring, you may have found that some measurements were made using the tallest line instead of middle
            H-&alpha; line.
        </p>
        <p>
          Some measurements may not have corresponded directly to any of the lines. This happens when a measurement was made
          without zooming in to see the 3 separate lines clearly.
        </p>
        <p>
          To get the most accurate measurement, you should always zoom in and use the marked line.
        </p>
      </v-window-item>
    
      <v-window-item :value="17" class="window-item-style">
        <p>
          Now that you have explored further, how confident do you feel about your velocity measurement?
          <mc-radiogroup 
          :radio-options="[
            'Very confident',
            'Somewhat confident',
            'Not confident at all'
            ]"
            :feedbacks="['Great!','Intersting!','Interesting']" 
          :neutral-answers="[0,1,2]"
          :selected-callback="(opt) => { if (opt.correct) { console.log('correct'); } }"
          score-tag="spec_meas_tut3">
            >
            >
          </mc-radiogroup>
        </p>
      </v-window-item>
      
      <v-window-item :value="18" class="window-item-style">
        <p>
          Go ahead and measure the wavelength of the H-&alpha; line again.
        </p>
        <p> 
          Select the second measurement in the table 
        </p>
        <p>
          Notice that the velocity in your table adjusts as you update your wavelength measurement.
        </p>
      </v-window-item>

      
      </v-window>
    </v-card-text>
      <v-card-actions v-if="showControls" class="justify-space-between">
        <!-- <v-btn text @click="prev">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn >
        <v-btn v-if="step < length-1" text @click="next">
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
        <v-btn
          v-if = "step == length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { $emit('close'); dialog = false; step = 0; opened = true;  reset_spectrum_viewer_limits() }"
        >
          Done
        </v-btn> -->
        <v-btn
          :disabled="step === 0"
          class="black--text"
          color="accent"
          depressed
          @click="prev"
        >
          Back
        </v-btn>
        <v-spacer></v-spacer>
          <v-btn
          v-if="step < length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { step++; }"
        >
          {{ step < length-1 ? 'next' : '' }}
        </v-btn>
        <v-btn
          v-if = "step == length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { $emit('close'); dialog = false; step = 0; opened = true;  reset_spectrum_viewer_limits() }"
        >
          Done
        </v-btn>
    </v-card-actions>
</v-card>
</template>


<style>
  .window-style, .window-item-style {
    transition: none !important;
  }
</style>


<script>
module.exports = {

  props: ['toStep', 'showControls'],

  data: () => {
    return {
      step: 0,
      length: 19,
      toStep: 0,
      showControls: false
    }
  },

  methods: {
    next () {
      this.step = this.step === this.length - 1
        ? this.length - 1
        : this.step + 1
    },
    prev () {
      this.step = this.step - 1 < 0
        ? this.length - 1
        : this.step - 1
    },
  },

  watch: {
    step(val) {
      this.$emit('step', val)
      
    },

    toStep(val) {
      this.step = val
    }
  },
}

</script>
