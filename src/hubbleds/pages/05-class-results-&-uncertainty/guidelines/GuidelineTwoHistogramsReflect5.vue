<template>
  <scaffold-alert
    title-text="Select Best Value"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Enter a response.
    </template>
    <div
      class="mb-4"
    >
      <p>
        The smoother, less clustered distribution for the All Students data tells us that an age value measured by one student has more uncertainty than an age value measured by a single class.
      </p>
      <p>
        Explain why you think this might be true.
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="My Reasoning"
        :tag="state_view.free_response.tag"
        :initial-response="state_view.free_response.response"
        :initialized="state_view.free_response.initialized"
        @fr-emit="fr_callback($event)"
      ></free-response>
    </div>
    <v-btn
      color="secondary lighten-1"
      @click="uncertainty_hint_dialog = true"
    >
      hint
      <v-dialog
        v-model="uncertainty_hint_dialog"
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
              style="color: white;"
            >
              Hint
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <span
              @click="
                () => {
                  $emit('close');
                  uncertainty_hint_dialog = false;
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
              Recall that each student used 5 galaxies to measure the age of the universe, while each class used ~100-150 galaxies. Why might this lead to a smaller uncertainty for a single class compared with a single student?
            </p>
          </div>
        </v-card>
      </v-dialog>
    </v-btn>
  </scaffold-alert>
</template>


<script>
export default {
  data() {
    return {
      uncertainty_hint_dialog: false
    }
  },
}
</script>
