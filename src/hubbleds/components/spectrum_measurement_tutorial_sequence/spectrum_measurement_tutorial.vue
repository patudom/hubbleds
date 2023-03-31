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
        Velocity Measurement Tutorial
        </v-toolbar-title>
      </v-toolbar>

      
    <v-row>
      <v-col class="tutorial-frame" cols="4">
        <guidelines-spectrum-measurement-tutorial
        @step="(val) => {this.step = val}"
        :toStep="this.step"
        :showControls="true"
        @close="() => { $emit('close'); dialog = false; opened = true;  on_close() }"
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
      <v-btn text @click="() =>  { $emit('close'); dialog = false; step = 0; opened = true;  on_close() }">
          <span> Finish tutorial </span>
        </v-btn>
        <v-chip> show_table: {{ show_table }} </v-chip>
        <v-chip> show_dotplot: {{ show_dotplot }} </v-chip>
        <v-chip> show_specviewer: {{ show_specviewer }} </v-chip>
        <v-chip> show_second_measurment: {{ show_second_measurment }} </v-chip>
        <v-chip> show_first_measurment: {{ show_first_measurment }} </v-chip>
        <v-chip> zoom_tool_enabled: {{ zoom_tool_enabled }} </v-chip>
        <v-chip> mouse interaction {{ allow_specview_mouse_interaction }} </v-chip>
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
  background-color: navy;
  /* outline: 2px solid red; */
  
}

.viewers-frame {
  background-color: rgb(174, 1, 27);
  padding: 2%
}

.second-dotplot > * header {
  /* display: none !important; */
  background-color: aliceblue !important;
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
      console.log('spectrum measurement tutorial step: ' + val)

      // val == 0 never gets run
      if (val == 0) {}

      if (val === 1) {
        console.log("step 1: showing 1st measurment")
        this.allow_specview_mouse_interaction = false; // disable mouse interaction
        this.show_first_measurment = true // shows the first measurement on dotplot 1
        this.show_table = true // shows the example galaxy table
        // Ex: setting x-axis limits manually
        // this.set_x_axis_limits({ xmin: 0, xmax: 30000 }) // in velocity (km/s)
        
      }
      if (val == 2) { }
      if (val == 3) {
        this.show_specviewer = true;
        this.allow_specview_mouse_interaction = true
        this.selector_lines_on()
      }
      if (val == 4) {
        this.zoom_tool_enabled = true;
        
      }
      if (val == 5) {  }
      if (val == 6) { }
      if (val == 7) { }
      if (val == 8) { }
      if (val == 9) { }
      if (val == 10) { }
      if (val == 11) {}
      if (val == 12) { }
      if (val == 13) { }
      if (val == 14) { }
      if (val == 15) { }
      if (val == 16) { }
      if (val == 17) { }
      if (val == 18) {   
        console.log("Adding second measurement")
        this.selector_lines_off()
        this.prep_second_measurement() // filter table to only show second measurement
        this.show_second_measurment = true // show dotplot 2

         }
      if (val == 19) { }

    },
  }
}
</script>

