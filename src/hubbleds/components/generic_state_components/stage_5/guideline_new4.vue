<template>
  <scaffold-alert
    title-text="Identify Your Confidence Interval"
    ref="scaffold"
    @back="state.marker_backward = 1"
    @next="() => {
      if (revealIter < 1) {
        revealIter = revealIter + 1;
      }
      else {
        state.marker_forward = 1;
        state.trend_line_drawn = false;
        state.best_fit_clicked = false;
      }
    }"
  >
    <div
      class="mb-4"
    >
      <p>
        Based on these results from your class, 
        what do you think is the most likely value of the age of the 
        universe and what is a likely range of possible values?
      </p>
      <v-row>
        <v-col
          cols="12"
          lg="9">      
          1. My best guess for the age of the universe based on my entire class’s data set: 
        </v-col>
        <v-col>
          <v-btn
            color="secondary lighten-1"
            @click="state.age_calc_state.hint1_dialog = true"
          >
            hint
            <v-dialog
              v-model="state.age_calc_state.hint1_dialog"
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
                    Hint #1
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <span
                    @click="
                      () => {
                        $emit('close');
                        state.age_calc_state.hint1_dialog = false;
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
                    The mean, median, and mode may be different values. 
                    Which one do you think is the best value to use for the age of the universe?
                  </p>
                </div>
              </v-card>
            </v-dialog>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          cols="12"
          lg="3"
        >
          <free-response
            outlined
            rows="1"
            label="Best Guess Age"
            tag="best-guess-age"
          ></free-response>
        </v-col>
        <v-col>
          Gyr
        </v-col>
      </v-row>


      <v-row
        v-if="revealIter >= 1"
      >
        <v-col>
          2. Explain why you picked that value and whether whether you based it on your understanding of the mean, median, or mode

        </v-col>
      </v-row>
      <v-row
        v-if="revealIter >= 2"
      >
        <v-col>
          <free-response
            outlined
            auto-grow
            rows="2"
            label="My Reasoning"
            tag="my-reasoning"
          ></free-response>
        </v-col>
      </v-row>

    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state'],
  data() {
    return {
      revealIter: 0
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

