<template>
  <!-- add persistant to prevent closing by clicking out -->
  <v-dialog
      v-model="dialog"
      max-width="1000px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        class="my-2"
        block
        color="secondary"
        elevation="2"
        id="slideshow-button"
        @click.stop="() => { dialog = true; opened = true }"
      >
        Dot Plot (Histogram) Tutorial
      </v-btn>
    </template>
    <v-card
      class="mx-auto"
      ref="content"
    >
      <v-toolbar
        color="secondary"
        dense
        dark
      >
        <v-toolbar-title
          class="text-h6 text-uppercase font-weight-regular"
        >
          {{ currentTitle }}
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <speech-synthesizer
          :root="() => this.$refs.content.$el"
          :autospeak-on-change="step"
          :speak-flag="dialog"
          :selectors="['div.v-toolbar__title', 'div.v-card__text.black--text', 'h3', 'p']"
          />
        <v-btn
          icon
          @click="closeDialog()"
          :disabled="maxStepCompleted < length - 1"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>

        <v-window
          v-model="step"
          style="height: 70vh;"
          class="overflow-auto"
        >
        
        <v-btn
          class="black--text"
          color="accent"
          depressed
          @click="activate_zoom_tool"
        >
          activate zoom tool
        </v-btn>
        
        <v-btn
          class="black--text"
          color="accent"
          depressed
          @click="activate_selector"
        >
          activate tower selection
        </v-btn>

        <v-window-item :value="0" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    Slide 0
                  </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="1" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols = "12"
                  lg = "5"
                >
                   <p>
                    Slide 1
                   </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>
        
        <v-window-item :value="2" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols = "12"
                  lg = "5"
                >
                   <p>
                    Slide 1
                   </p>
                </v-col>
                <v-col
                  cols="12"
                  lg="7">
                  <jupyter-widget :widget="dotplot_viewer"/>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

       

      </v-window>
      
      <v-divider></v-divider>

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
              :disabled="n > maxStepCompleted + 2"
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
          :disabled="step > maxStepCompleted"
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
          @click="() => { $emit('close'); dialog = false; step = 0; opened = true }"
        >
          Done
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  
  watch: {
    step(newStep) {
      const isInteractStep = this.interactSteps.includes(newStep);
      const newCompleted = isInteractStep ? newStep - 1 : newStep;
      this.maxStepCompleted = Math.max(this.maxStepCompleted, newCompleted);
    },
  },

  methods: {
    closeDialog() {
      if (this.maxStepCompleted == this.length - 1) {
        this.$emit('close');
        this.dialog = false;
        if (this.step == this.length - 1) {
          this.step = 0;
        }
      }
    }
  }

  
};

</script>

<style>
.no-transition {
  transition: none;
}
</style>
