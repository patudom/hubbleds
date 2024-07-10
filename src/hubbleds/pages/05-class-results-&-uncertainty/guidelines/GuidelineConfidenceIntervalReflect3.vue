<template>
  <scaffold-alert
    title-text="Identify Your Confidence Interval"
    ref="scaffold"
    @back="back_callback()"
    @next="() => {
      if (revealIter < 1) {
        revealIter = revealIter + 1;
      }
      else {
        next_callback();
        // state_view.trend_line_drawn = false;
        // state_view.best_fit_clicked = false;
      }
    }"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        After comparing different percentage ranges for your class's age measurements in the histogram, enter your responses below.
      </p>
      <v-row
      >
        <v-col
          cols="12"
          lg="9"
        >
          3. The range of age values for the universe that I am most confident in based on my class’s data set: 
        </v-col>
        <v-col>
          <v-btn
            color="secondary lighten-1"
            @click="dialog = true"
          >
            hint
            <v-dialog
              v-model="dialog"
              persistent
              max-width="600px">
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
                    Hint #2
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <span
                    @click="
                      () => {
                        $emit('close');
                        dialog = false;
                      }
                    "
                  >
                    <v-btn icon>
                      <v-icon> mdi-close </v-icon>
                    </v-btn>
                  </span>
                </v-toolbar>
                <div class="pa-6">
                  <p>
                    The range you pick will have a tradeoff between how likely it is that the “true” value actually lies within the range you choose vs. having a narrow enough range that your measurement is actually useful. A very large range is more likely to include the "true" value, but may be so nonspecific that it is not useful. A narrow range has more specificity but may not include the "true" value.
                  </p>
                  <p>
                    Different people will feel more or less comfortable with the different sides of this tradeoff, and there isn’t really a right or wrong answer as long as you justify why you chose what you did.
                  </p>
                  <p>
                    If you are feeling really stuck, feel free to discuss this with a classmate or your instructor.
                  </p>
                </div>
              </v-card>
            </v-dialog>
          </v-btn>
        </v-col>
      </v-row>
      <v-row
        v-if="revealIter >= 0"
      >
        <v-col
          cols="12"
          lg="3">
          <free-response
            outlined
            rows="1"
            label="Likely Low Age"
            tag="likely-low-age"
            type="float"
            :initial-response="state_view.free_response_a.response"
            :initialized="state_view.free_response_a.initialized"
            @fr-emit="fr_callback($event)"
          ></free-response>
        </v-col>
        <v-col
          lg="2">
          Gyr
        </v-col>
              <v-col
          cols="12"
          lg="3">
          <free-response
            outlined
            rows="1"
            label="Likely High Age"
            tag="likely-high-age"
            type="float"
            :initial-response="state_view.free_response_b.response"
            :initialized="state_view.free_response_b.initialized"
            @fr-emit="fr_callback($event)"
          ></free-response>
        </v-col>
        <v-col
          lg="2">
          Gyr
        </v-col>
      </v-row>

      <v-row
        v-if="revealIter >= 1"
      >
        <v-col>
          4. Explain why you chose your values using information from the histogram or other viewers:
        </v-col>
      </v-row>
      <v-row
        v-if="revealIter >= 1"
      >
        <v-col>
          <free-response
            outlined
            auto-grow
            rows="2"
            label="My Reasoning"
            tag="my-reasoning-2"
            :initial-response="state_view.free_response_c.response"
            :initialized="state_view.free_response_c.initialized"
            @fr-emit="fr_callback($event)"
          ></free-response>
        </v-col>
      </v-row>


    </div>
  </scaffold-alert>
</template>

<script>
export default {
  data() {
    return {
      revealIter: 0,
      dialog: false,
    }
  },
  watch: {
    revealIter(_value) {
      const scaffold = this.$refs.scaffold;
      this.$nextTick(() => {
        scaffold.$refs.next.$el.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      });
    }
  }
}
</script>

