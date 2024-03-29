<template>
  <scaffold-alert
    class="mb-4 mx-auto doppler_alert"
    color="info"
    elevation="6"
    max-width="800"
    title-text="Input Wavelengths"
    @back="back_callback()"
    :can-advance="can_advance"
    @next="() =>
      {
        const expectedAnswers = [state_view.lambda_obs, state_view.lambda_rest];
        state_view.doppler_calc_dialog = !!validateAnswersJS(['lam_obs', 'lam_rest'], expectedAnswers);
        validateAnswersJS(['lam_obs', 'lam_rest'], expectedAnswers) ? next_callback() : force_transition();
      }"
  >
    <div
        v-intersect="(entries, _observer, intersecting) => { if (intersecting) { MathJax.typesetPromise(entries.map(entry => entry.target)) }}"
        class="mb-4"
    >
      <p>
        Enter the observed wavelength and rest wavelength for the galaxy into the cells in the equation below.
      </p>
      <div
          class="JaxEquation my-8"
      >
        $$ v = c \times \left( \frac{\bbox[#FBE9E7]{\input[lam_obs][]{}} \text{ &#8491;}}{\bbox[#FBE9E7]{\input[lam_rest][]{}}\text{
        &#8491;}} - 1 \right) $$
      </div>
      <v-card
          class="legend mt-8"
          color="info"
          outlined
      >
        <v-container>
          <v-row
              no-gutters
          >
            <v-col>
              <div
                  class="JaxEquation"
              >
                $$ v = c \times \left( \frac{\lambda_{\text{obs}}}{\lambda_{\text{rest}}} - 1 \right) $$
              </div>
            </v-col>
          </v-row>
          <v-divider></v-divider>
          <v-row
              class="my-1"
              no-gutters
          >
            <v-col

            >
              \(v\)
            </v-col>
            <v-col
                cols="10"
            >
              velocity of your galaxy, in km/s
            </v-col>
          </v-row>
          <v-row
              class="my-1"
              no-gutters
          >
            <v-col
                cols="2"
            >
              \(c\)
            </v-col>
            <v-col
                cols="10"
            >
              speed of light, 300,000 km/s
            </v-col>
          </v-row>
          <v-row
              class="my-1"
              no-gutters
          >
            <v-col
                cols="2"
            >
              \(\lambda_{\text{obs}}\)
            </v-col>
            <v-col
                cols="10"
            >
              observed wavelength of spectral line in your galaxy
            </v-col>
          </v-row>
          <v-row
              class="my-1"
              no-gutters
          >
            <v-col
                cols="2"
            >
              \(\lambda_{\text{rest}}\)
            </v-col>
            <v-col
                cols="10"
            >
              rest wavelength of spectral line
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </div>
    <v-divider
        v-if="state_view.failed_validation_4"
        class="my-4"
    >
    </v-divider>
    <v-alert
        v-if="state_view.failed_validation_4"
        color="info darken-1"
        dense
    >
      Not quite. Make sure you haven't reversed the rest and observed wavelength values.
    </v-alert>
  </scaffold-alert>
</template>


<style>

.JaxEquation .MathJax {
  margin: 16px auto !important;
}

mjx-mfrac {
  margin: 0 4px !important;
}

mjx-mstyle {
  border-radius: 5px;
}

.doppler_alert .v-alert {
  font-size: 16px !important;
}

.v-application .legend {
  border: 1px solid white !important;
  max-width: 300px;
  margin: 0 auto 0;
  font-size: 15px !important;
}

#lam_obs, #lam_rest {
  color: black;
  font-size: 18px;
  font-family: "Roboto", Arial, Helvetica, sans-serif;
  padding: 3px;
}

</style>


<script>
export default {
  // mounted: () => {
  //   console.log("MOUNTED Doppler Calc 4");
  // },
  async mounted() {
    console.log("MOUNTED Doppler Calc 4");

    // Grab MathJax itself
    // We want to wait for it to finish loading, in case there are
    // any elements that need to be typeset on the initial screen
    await new Promise((resolve, reject) => {
      const mathJaxScript = document.createElement('script');
      mathJaxScript.async = false;
      mathJaxScript.src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js";
      document.head.appendChild(mathJaxScript);
      mathJaxScript.onload = (_e) => resolve();
      mathJaxScript.onerror = (_e) => reject();
    });
    await MathJax.startup.promise;

    // Not all of our elements are initially in the DOM,
    // so we need to account for that in order to get MathJax
    // to render their formulae properly
    const mathJaxOpeningDelimiters = [ "$$", "\\(", "\\[" ];
    const containsMathJax = node => mathJaxOpeningDelimiters.some(delim => node.innerHTML.includes(delim));
    const elementToScan = node => node.nodeType === Node.ELEMENT_NODE;
    const mathJaxCallback = function(mutationList, _observer) {
      mutationList.forEach(mutation => {
        if (mutation.type === 'childList') {

          const needTypesetting = [];
          mutation.addedNodes.forEach(node => {
            if (elementToScan(node) && containsMathJax(node)) {
              needTypesetting.push(node);
            }
          });
          if (needTypesetting.length > 0) {
            MathJax.typesetPromise(needTypesetting);
          }

          const toClear = [];
          mutation.removedNodes.forEach(node => {
            if (elementToScan(node) && containsMathJax(node)) {
              toClear.push(node);
            }
          })
          if (toClear.length > 0) {
            MathJax.typesetClear(toClear);
          }
        }
      });
    }
    const observer = new MutationObserver(mathJaxCallback);
    const options = { childList: true, subtree: true };
    observer.observe(this.$el, options);
  },
  methods: {
    getValue(inputID) {
      const input = document.getElementById(inputID);
      if (!input) {
        return null;
      }
      return input.value;
    },

    parseAnswer(inputID) {
      return parseFloat(this.getValue(inputID).replace(/,/g, ''));
    },

    validateAnswersJS(inputIDs, expectedAnswers) {
      return inputIDs.every((id, index) => {
        const value = this.parseAnswer(id);
        this.state_view.failed_validation_4 = (value && value === expectedAnswers[index]) ? false : true;
        return value && value === expectedAnswers[index];
      });
    }
  },
};
</script>

