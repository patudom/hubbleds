<template>
  <scaffold-alert
    title-text="Age of the Universe"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
      v-intersect="typesetMathJax"
    >
      <p>
        In the units astronomers use, we can write this as:
      </p>
      <v-card
        outlined
        class="legend mt-8"
        color="info"
      >
        <v-container>
          <v-row
            no-gutters
          >
            <v-col>
              <div
                class="JaxEquation"
              >
                $$ t \text{ (in Gyr)}= {{ Math.round(state_view.age_const) }}  \times \frac{d \text{ (in Mpc)}}{v \text{ (in km/s)}} $$

              </div>
            </v-col>
          </v-row>
          <v-divider></v-divider>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              
            >
              \(t\)
            </v-col>
            <v-col
              cols="10"
            >
              age of the universe, in Gyr. (1 Gyr = 1 billion years)
            </v-col>
          </v-row>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              cols="2"
            >
              \(d\)
            </v-col>
            <v-col
              cols="10"
            >
              distance the galaxy has traveled (distance to the galaxy, in Mpc)
            </v-col>
          </v-row>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              cols="2"
            >
              \(v\)
            </v-col>
            <v-col
              cols="10"
            >
              velocity of the galaxy (in km/s)
            </v-col>
          </v-row>
        </v-container>
      </v-card>
      <p>

      </p>
      <!--

      <p>
        To simplify the units astronomers use, we can write this as:
      </p>
      <p>
        Time (age of universe Gyr) = Distance in Mpc / velocity in km/s * :conversion factor to give time in Gyr:
      </p>
      <p>
        (A Gyr = 1 billion years).
      </p>
      <p>
        Use the distance and velocity of your “best fit galaxy” to calculate the age of the universe.
      </p>
      <p>
        Age measured with my dataset = _________ Gyr.
      </p>
      -->
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  methods: {
    typesetMathJax(entries, _observer, intersecting) {
      if (intersecting) {
        MathJax.typesetPromise(entries.map(entry => entry.target));
      }
    },
  },
}
</script>

<style>

.JaxEquation {
  margin: 0;
}

.JaxEquation .MathJax {
  margin: 20px auto !important;
}

.v-application .legend {
  border: 1px solid white !important;
  max-width: 300px;
  margin: 0 auto 0;
  font-size: 15px !important;
}

</style>
