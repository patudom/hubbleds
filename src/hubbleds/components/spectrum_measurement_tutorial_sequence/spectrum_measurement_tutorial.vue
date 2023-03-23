<template>
  

<v-dialog
  v-model="dialog"
  id="spec_meas_tut"
  min-height="100rem"
  max-width="90%"
  >
  <template v-slot:activator="{ on, attrs }">
    
    <v-btn
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
        />
      </v-col>
      <!-- Put the viewers in here -->
      <v-col  class="viewers-frame" cols="8">
        <v-row>
          <dot-plot-explainer-tut/>
        </v-row>
        <v-row>
          <v-card v-if="this.show_dotplot" width="90%">
          <jupyter-widget :widget="dotplot_viewer_widget"/>
          </v-card>
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
      <v-btn text @click="() =>  { $emit('close'); dialog = false; step = 0; opened = true;  reset_spectrum_viewer_limits() }">
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
          @click="step--"
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


</style>

<script>
module.exports = {

  props: ['state'],
  
  methods: {
    next () {
      this.step = this.step === this.length - 1
        ? pass
        : this.step + 1
    },
    prev () {
      this.step = this.step - 1 < 0
        ? this.length - 1
        : this.step - 1
    },
  },

  watch: {
    step (val) {
      this.$emit('step', val)
      console.log('spectrum measurement tutorial step: ' + val)

      if (val > 0) {
        this.show_dotplot = true;
        this.show_specviewer = true;
        this.show_table = true;
      }
      
      if (val === 1) {
        console.log("Adding first measurement")
        this.add_first_measurement()
        
      }

      if (val == 2) {
        console.log("Adding second measurement")
        this.add_second_measurement()
        this.toggle_second_measurement()
      }
    },
  },
}
</script>

