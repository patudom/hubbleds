<template>
  

<v-dialog
  v-model="dialog"
  id="spec_meas_tut"
  min-height="100rem"
  max-width="90%"
  >
  <template v-slot:activator="{ on, attrs }">
    
    <v-btn
      block
      color="primary"
      v-bind="attrs"
      v-on="on"
      @click.stop="() => { dialog = true; opened = true;}"
    >
    <v-spacer></v-spacer>
      Compare Velocities
    <v-spacer></v-spacer>
    </v-btn>
  </template>
  <v-card>
    
    <v-toolbar
        color="info"
        dense
        dark
      >
        <v-toolbar-title
        >
        Velocity Measurement Tutorial (Step #{{ step  }})
        </v-toolbar-title>
      </v-toolbar>

      
    <v-row>
      <v-col class="tutorial-frame" cols="4">
        <guidelines-spectrum-measurement-tutorial
        @step="(val) => {this.step = val; this.maxStepCompleted = Math.max(this.maxStepCompleted, val)}"
        :toStep="this.step"
        :showControls="true"
        :nextDisabled="this.next_disabled"
        @close="() => { $emit('close'); dialog = false; opened = true;  on_close() }"
        @turnOnSpecViewer="() => { this.show_specviewer = true; this.next_disabled = false; }"
        />
      </v-col>
      <!-- Put the viewers in here -->
      <v-col  class="viewers-frame" cols="8">
        <v-row>
          <!-- <v-col> -->
          <v-card v-if="this.show_dotplot" width="90%">
          <jupyter-widget :widget="dotplot_viewer_widget"/>
          </v-card>
        </v-row>
        <v-row>
          <!-- </v-col> -->
          <!-- <v-col> -->
          <v-card class='second-dotplot' v-if="this.show_dotplot & this.show_second_measurment" width="90%">
          <jupyter-widget :widget="dotplot_viewer_2_widget"/>
          </v-card>
          <!-- </v-col> -->
        </v-row>
        <v-row>
          <v-card v-if="this.show_specviewer" width="90%">
            <jupyter-widget :widget="spectrum_viewer_widget"/>
          </v-card>
        </v-row>
        <v-row>
          <v-card v-if="this.show_table" width="90%">
          <jupyter-widget :widget="example_galaxy_table"/>
          </v-card>
        </v-row>
      </v-col>
    </v-row>
    <v-card-actions>
      <v-btn style="background-color: purple;" text @click="() =>  { $emit('close'); dialog = false; step = 0; opened = true;  on_close() }">
          <span> Finish tutorial </span>
        </v-btn>

    </v-card-actions>
    <v-card-actions
        class="justify-space-between"
      >
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
        <v-item-group
          v-model="step"
          class="text-center"
          mandatory
        >
          <v-item
            v-for="n in length"
            :key="`btn-${n}`"
            v-slot="{ active, toggle }"
          >
            <v-btn
              :disabled="n > step"
              :input-value="active"
              icon
              @click="toggle"
            >
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </v-item>
        </v-item-group>
        <v-spacer></v-spacer>
          <v-btn
          v-if="step < length-1"
          color="accent"
          class="black--text"
          depressed
          @click="next"
        >
          {{ step < length-1 ? 'next' : '' }}
        </v-btn>
        <v-btn
          v-if = "step == length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { $emit('close'); dialog = false; opened = true;  on_close() }"
        >
          Done
        </v-btn>
      </v-card-actions>
  </v-card>
</v-dialog>
</template>

<style>


.tutorial-frame
{
  /* margin: 10px; */
  padding: 2%;
}

.viewers-frame {
  padding: 2%;
  padding-left: 2%
}

div.viewers-frame > div.row > div.second-dotplot  > div.v-card > header {
  background-color: transparent !important;
  /* outline: 2px solid red; */
}

</style>

<script>
module.exports = {

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
      console.log('0-indexed spectrum measurement tutorial step: ' + val)

      // val == 0 never gets run
      if (val == 0) {
        // this never get's called. anything you want done here 
        // should be done when in the python __init__ function
        // this.tracking_lines_off() // turn off the tracking lines
      }

      if (val === 1) {
        console.log("step 1: showing 1st measurment")
        
        this.allow_specview_mouse_interaction = false; // disable mouse interaction on spectrum-viewer
        this.show_first_measurment = true // shows the first measurement on dotplot 1
        this.show_table = true // shows the example galaxy table
        // Ex: setting x-axis limits manually
        // this.set_x_axis_limits({ xmin: 0, xmax: 30000 }) // in velocity (km/s)
        // SEQUENCING::: no zoom tool yet
        
      }
      if (val == 2) {
        // this.show_specviewer = true; // done by clicking button in step 2
       }
      if (val == 3) {// turn on the tower selector
        this.tracking_lines_on()
        this.allow_specview_mouse_interaction = true
      }
      if (val == 4) {
        this.turn_on_tower_selector() 
      }
      if (val == 5) {  }
      if (val == 6) { 
      }
      if (val == 7) { 
        this.enable_zoom_tool(); // this is a toggle. here were toggle it on, call again to toggle off
      }
      if (val == 8) { }
      if (val == 9) { }
      if (val == 10) { }
      if (val == 11) { }
      if (val == 12) { }
      if (val == 13) { }
      if (val == 14) { }
      if (val == 15) { }
      if (val == 16) { }
      if (val == 17) { }
      if (val == 18) {   
        console.log("Adding second measurement")
        // this.tracking_lines_off()
        this.show_second_measurement_table() // filter table to only show second measurement
        this.show_second_measurment = true // show dotplot 2

         }
      if (val == 19) { }

    },
  }
}
</script>

