<template>
  <v-btn
    class="my-2"
    block
    color="secondary"
    elevation="2"
    @click.stop="() => { dialog = true; }"
  >
    Hubble's Discovery
    <v-dialog
        v-model="dialog"
        persistent
        max-width="1000px"
    >
      <v-card
        class="mx-auto"
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
          <span
            @click="
              () => {
                $emit('close');
                dialog = false;
                if (step == length-1) {
                  step = 0;
                }
              }
            "
          >
            <v-btn icon>
              <v-icon> mdi-close </v-icon>
            </v-btn>
          </span>
        </v-toolbar>

          <v-window
            v-model="step"
            style="height: 70vh;"
            class="overflow-auto"
          >

          <v-window-item :value="0" class="no-transition">
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <p>
                      The relationship between your galaxies’ velocity and distance is the same as what Hubble found: galaxies at a greater distance away are moving away from us at a higher velocity.
                    </p>
                    <p>
                      This was a <strong>huge</strong> deal in 1929. This relationship that Hubble found serves as evidence that we live in an <strong>expanding universe</strong>. Hubble realized that an expanding universe implies that at some point all the galaxies were much closer together — "<strong>The Big Bang</strong>". The amount of time since The Big Bang tells us the <strong>age of the universe</strong>.
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
                  <v-col>
                    <p>
                      To understand Hubble’s thinking about this, let’s use the following situation as a model: Imagine runners in the middle of a race, where the runners are running at different speeds.
                    </p>
                    <p>
                      In this diagram, runner A is running with a velocity of 4 km per hour and has run a distance of 12 km, while runner C is running faster with a velocity of 10 km per hour and has gone a distance of 30 km.
                    </p>
                    <p>
                      Can you figure out how long ago the race started — the “age” of the race? (Assume each runner has maintained a consistent speed for the entire race).
                    </p>
                    <p>
                      The race began:
                    </p>
                    <mc-radiogroup
                      :radio-options="[
                        '1/3 of an hour ago',
                        '3 hours ago',
                        '12 hours ago',
                        '75 hours ago'
                      ]"
                      :feedbacks="[
                        'Try again. The equation describes a relationship between your galaxy\’s velocity and the speed of light.',
                        'Correct. The fraction is the ratio of the observed wavelength of my spectral line over the line’s rest wavelength minus 1. This will be the case for all of your galaxies.',
                        'Try again. You are multiplying the speed of light by a value that is smaller than 1.'
                      ]"
                      :correct-answers="[1]"
                      :selected-callback="(state) => { if(state.correct) { this.maxStepCompleted = Math.max(this.maxStepCompleted, 1);} }"
                      score-tag="race-age"  
                    >
                    </mc-radiogroup>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item>

          <v-window-item :value="2" class="no-transition">
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <p>
                      To return to this data story, if we graph the runners’ velocities vs. distance, the graph would look like this.
                    </p>
                    <p>
                      Doesn’t this look a lot like your graph for the galaxies?
                    </p>
                    <p>
                      As with the runners, you can use your galaxies’ velocity and distance data to calculate the time when all galaxies were in the same place — the <strong>age of the universe</strong>.
                    </p>
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
            color="accent"
            text
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
            text
            @click="() => { step++; }"
          >
            {{ step < length-1 ? 'next' : '' }}
          </v-btn>
          <v-btn
            v-if = "step == length-1"
            color="accent"
            class="black--text"
            depressed
            @click="() => { $emit('close'); dialog = false; step = 0; }"
          >
            Done
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-btn>
</template>

<script>
export default = {
  watch: {
    step(newStep) {
      const isInteractStep = this.interactSteps.includes(newStep);
      const newCompleted = isInteractStep ? newStep - 1 : newStep;
      this.maxStepCompleted = Math.max(this.maxStepCompleted, newCompleted);
    },
  }
};
</script>

<style>
.no-transition {
  transition: none;
}
</style>
