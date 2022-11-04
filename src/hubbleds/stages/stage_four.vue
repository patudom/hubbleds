<template>
  <v-container>
    <!-- add special button to put stage_state and story_state in the console -->
    <v-row v-if="show_team_interface">
      <v-col>
        <v-btn
          color="error"
          class="black--text"
          @click="() => {
            console.log('stage state:', stage_state);
            console.log('story state:', story_state);
          }"
        >
          State
        </v-btn>
        Marker: {{ stage_state.marker }}
      </v-col>
    </v-row>

    <!--------------------- TABLE ROW ----------------------->
    <v-row
      class="d-flex align-stretch"
    >
      <v-col
        cols="12"
        lg="5"
      >

      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        
          <v-lazy>
            <jupyter-widget :widget="viewers.prodata_viewer"/>
          </v-lazy>
        </v-card>
      </v-col>
    </v-row>

    
    <!--------------------- ALL DATA HISTOGRAM VIEWER ----------------------->
    <v-row
      class="d-flex align-stretch"
    >
      <v-col
        cols="12"
        lg="5"
      >
        <c-guideline-class-age-distribution-c
          v-if="stage_state.marker == 'age_dis1c'"
          v-intersect.once="scrollIntoView"/>
        <c-guideline-two-histograms1
            v-if="stage_state.marker == 'two_his1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-true-age1
            v-if="stage_state.marker == 'tru_age1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-true-age2
            v-if="stage_state.marker == 'tru_age2'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-shortcomings-est3
            v-if="stage_state.marker == 'sho_est3'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-shortcomings-est-reflect4
            v-if="stage_state.marker == 'sho_est4'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-true-age-issues1
            v-if="stage_state.marker == 'tru_iss1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-imperfect-methods1
            v-if="stage_state.marker == 'imp_met1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-imperfect-assumptions1
            v-if="stage_state.marker == 'imp_ass1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-imperfect-measurements1
            v-if="stage_state.marker == 'imp_mea1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-uncertainties-random1
            v-if="stage_state.marker == 'unc_ran1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-uncertainties-systematic1
            v-if="stage_state.marker == 'unc_sys1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-uncertainties-systematic2
            v-if="stage_state.marker == 'unc_sys2'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-two-histograms-mc2
            v-if="stage_state.marker == 'two_his2'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-lack-bias-mc1
            v-if="stage_state.marker == 'lac_bia1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-lack-bias-reflect2
            v-if="stage_state.marker == 'lac_bia2'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-lack-bias-reflect3
            v-if="stage_state.marker == 'lac_bia3'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-more-data-distribution
            v-if="stage_state.marker == 'mor_dat1'"
            v-intersect.once="scrollIntoView"/>
        <c-guideline-account-uncertainty
            v-if="stage_state.marker == 'acc_unc1'"
            v-intersect.once="scrollIntoView"/>
      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        
          <v-lazy>
            <!-- Change v-if marker to include when we want tos tart showing student value-->
            <jupyter-widget :widget="viewers.all_distr_viewer_student"
              v-if="stage_state.indices[stage_state.marker] > stage_state.indices['con_int2c']"
            />
          </v-lazy>
          <v-lazy>
            <jupyter-widget :widget="viewers.all_distr_viewer_class"/>
          </v-lazy>
        </v-card>
      </v-col>
    </v-row>
    
    
  </v-container>
</template>


<style>

.v-dialog .v-card__text {
  font-size: 18px !important;
}

.v-radio label.theme--dark{
  color: white !important;
}
.v-radio label.theme--light{
  color: black !important;
}

.v-alert .v-input--radio-group+.v-alert, .v-dialog .v-input--radio-group+.v-alert {
  background-color: #000b !important;
}

.v-slider__thumb:hover, .v-slider__thumb-label-container:hover {
  cursor: grab;
}

.v-slider__thumb:active, .v-slider__thumb-label-container:active {
  cursor: grabbing;
}

.comparison_viewer.v-card {
  border-bottom-left-radius: 0px !important;
  border-bottom-right-radius: 0px !important;
  margin-bottom: 1px !important;
}

.slider_card {
  border-top-left-radius: 0px !important;
  border-top-right-radius: 0px !important;
}

.g_legend{
  fill: #F002 !important;
}

</style>


<script>

module.exports = {
  mounted() {
    const config = { childList: true, subtree: true };
    const onMutation = (mutationList, observer) => {
      for (const mutation of mutationList) {
        if (mutation.type === 'childList') {
          const target = mutation.target;
          const viewerName = this.viewerName(target);
          if (viewerName !== null) {
            const resizeObserver = new ResizeObserver((entries) => {
              for (const entry of entries) {
                const pixelSize = entry.devicePixelContentBoxSize[0];
                const width = pixelSize.inlineSize;
                const nticks = Math.floor(width / 125);
                this.set_viewer_nticks({ nticks: nticks, axis: 'x', viewer: viewerName });
              }
            });
            resizeObserver.observe(target, { box: 'device-pixel-content-box' });
          }
        }
      }
    }
    const observer = new MutationObserver(onMutation);
    observer.observe(this.$el, config);
  },
  methods: {
    scrollIntoView: function(entries, observer, isIntersecting) {
      if (isIntersecting) {
        entries[0].target.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      }
    },
    viewerName: function(node) {
      for (const key of Object.keys(this.viewers)) {
        if (node.classList.contains(key)) {
          return key;
        }
      }
      return null;
    }
  }
}

</script>
