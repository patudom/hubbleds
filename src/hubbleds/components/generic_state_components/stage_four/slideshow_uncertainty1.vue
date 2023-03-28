<template>
  <v-dialog
      v-model="state.uncertainty_dialog"
      persistent
      max-width="1000px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        class="my-2"
        block
        color="secondary"
        elevation="2"
        id="hubble-exp-button"
        @click.stop="() => { state.uncertainty_dialog = true; state.uncertainty_dialog_opened = true }"
      >
        Uncertainty Tutorial
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
          {{ state.uncertainty_state.titles[state.uncertainty_state.step] }}
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <speech-synthesizer
          :root="() => this.$refs.content.$el"
          :selectors="['div.v-toolbar__title', 'div.v-card__text.black--text', 'h3', 'p']"
          />
        <v-btn
          icon
          @click="state.uncertainty_dialog = false"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>

        <v-window
          v-model="state.uncertainty_state.step"
          style="height: 70vh;"
          class="overflow-auto"
        >

        <v-window-item :value="0" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    There is only one universe that we live in, so our universe only has one age. Our job as scientists is to figure out if the <strong>true age</strong> of the universe is included within the ranges shown within these histograms, and if so, which value within the range is the true age.
                  </p>
                  <p>
                    First, let’s think about <strong>why</strong> we found a range of values in the first place (rather than all getting the same value).
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
                    Recall your thoughts about shortcomings in your measurements and your estimate of the universe's age.
                  </p>
                  <p
                    class="mb-3 mt-10"
                  >
                    Shortcoming #1:
                  </p>
                  <p 
                    class = "pa-2 StudentResponses">

                    {{ state.age_calc_state.short_one }}
                  </p>
                  <p
                    class="mb-3 mt-10"
                  >
                    Shortcoming #2:
                  </p>
                  <p
                    class = "pa-2 StudentResponses">

                    {{ state.age_calc_state.short_two }}
                  </p>
                  <p
                    class="mb-3 mt-10"
                  >
                    Other shortcomings:
                  </p>
                  <p
                    class = "pa-2 StudentResponses">

                    {{ state.age_calc_state.short_other }}
                  </p>
                  <p class="mt-10">
                    Is there anything more you would like to add now that you’ve seen more data? (It’s OK if not.)
                  </p>
                  <free-response
                    outlined
                    auto-grow
                    rows="2"
                    label="Shortcoming #4"
                    hint="(if you can think of any more)"
                    tag="shortcoming-4"
                  ></free-response>
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
                    There are a few things that could prevent us from finding the true age of the universe:
                  </p>
                  <ul>
                    <li>Our <strong>methods</strong> are imperfect</li>
                    <li>Our <strong>assumptions</strong> about the universe are imperfect</li>
                    <li>Our <strong>measurements</strong> are imperfect</li>
                  </ul>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="3" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols = "12"
                  lg = "5"
                >
                  <p>
                    Given the messiness of our velocity vs. distance graphs, it is clear that we did not use an optimal method for making these measurements.
                  </p>
                  <p>
                    In particular, professional astronomers have more sophisticated ways to measure <strong>distances</strong> to galaxies (but those are outside of the scope of this data story).
                  </p>
                  <p>
                    To make our measurements, we assumed that all galaxies are the same size as our own galaxy, the Milky Way. This is not a correct assumption, as galaxies have a large amount of natural variability in their sizes. This is likely the biggest source of “messiness” in our results.
                  </p>
                </v-col>
                <v-col
                  cols="12"
                  lg="7"
                >
                  This is a placeholder to remind ourselves that we need real images for this slideshow dialog.
                  <v-img
                    id="runners"
                    class="mb-4 mx-a mt-n3"
                    contain
                    :src="`${state.image_location}/runners_km.png`"
                  ></v-img>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="4" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  lg="5"
                  >
                  <p>
                    Human error contributes to imperfect measurements too. Some people are more meticulous than others.
                  </p>
                  <p>
                    Sometimes our tools limit our measurements. For example, did you feel confident that you were able to measure the edges of your galaxies correctly?
                  </p>
                </v-col>
                <v-col
                  cols="12"
                  lg="7">
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="5" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  lg="5"
                  >
                  <p>
                    Given the imperfect nature of our measurements and assumptions, there is a chance that our results are different than the true age of the universe. We refer to these differences as <strong>uncertainties</strong> in our result.
                  </p>
                </v-col>
                <v-col
                  cols="12"
                  lg="7">
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="6" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  lg="5"
                  >
                  <p>
                    Some uncertainties are <strong>random</strong>. For example, if some galaxies in your sample are larger or smaller than the Milky Way, your resulting distances may be too close or too far, and then your resulting age may be too young or too old.
                  </p>
                </v-col>
                <v-col
                  cols="12"
                  lg="7">
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="7" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  lg="5"
                  >
                  <p>
                    Some uncertainties are <strong>systematic</strong>. These are problems with our methods or assumptions that lead to all measurements, on average, being <strong>incorrect in the same direction</strong>, which biases our final result.
                  </p>
                  <p>
                    Can you think of any problems in our methods that could bias everyone’s results in the same direction?
                  </p>
                  <free-response
                    outlined
                    auto-grow
                    rows="2"
                    label="Problems in Our Methods"
                    hint="(problems that might lead to systematic uncertainty)"
                    tag="systematic-uncertainty"
                  ></free-response>
                </v-col>
                <v-col
                  cols="12"
                  lg="7">
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="8" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  >
                  <p>
                    Here are possible sources of systematic uncertainty:
                  </p>
                  <p>
                    If we all miss measuring the faint outer edges of all our galaxies, our angular size measurements will all be a little bit too small, and everyone’s distance measurements will be a little bit too far, leading to ages that are a little bit too old.
                  </p>
                  <p>
                    We know that there is natural variation in the sizes of galaxies. If our Milky Way happens to be an “average” galaxy (somewhere in the middle of the actual distribution of galaxy sizes), our result would not have a bias. If the “average” size of a galaxy is different than the size of the Milky Way, that could lead to a bias in our age measurements.
                  </p>
                  <p>
                    Sometimes sources of systematic uncertainty bias our results in different directions, effectively cancelling each other out.
                  </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>
      </v-window>

        <v-window-item :value="9" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  >
                  <p>
                    <v-img
                      class="mb-4"
                      contain
                      height="128"
                      src="https://www.pngrepo.com/png/211744/512/rocket-ship-launch-missile.png"
                    ></v-img>
                    <h3 class="text-h6 font-weight-light mb-2">
                      You're ready to continue exploring everyone's data now.
                    </h3>
                    <span class="text-caption grey--text">Click the <strong>UNCERTAINTY TUTORIAL</strong> button again if you'd like to come back for a refresher.</span>
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
          :disabled="state.uncertainty_state.step === 0"
          class="black--text"
          color="accent"
          depressed
          @click="state.uncertainty_state.step--"
        >
          Back
        </v-btn>
        <v-spacer></v-spacer>
        <v-item-group
          v-model="state.uncertainty_state.step"
          class="text-center"
          mandatory
        >
          <v-item
            v-for="n in state.uncertainty_state.length"
            :key="`btn-${n}`"
            v-slot="{ active, toggle }"
          >
            <v-btn
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
          v-if="state.uncertainty_state.step < state.uncertainty_state.length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { state.uncertainty_state.step++; console.log(state.uncertainty_state.step) }"
        >
          {{ state.uncertainty_state.step < state.uncertainty_state.length-1 ? 'next' : '' }}
        </v-btn>
        <v-btn
          v-if = "state.uncertainty_state.step == state.uncertainty_state.length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { $emit('close'); state.uncertainty_dialog = false; state.uncertainty_state.step = 0; state.uncertainty_dialog_opened = true }"
        >
          Done
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style>
  .StudentResponses {
    color: black !important;
    background-color: #FFAB91;
    width: 80%;
  }
</style>


<script>
module.exports = {
  props: ['state'],
};
</script>