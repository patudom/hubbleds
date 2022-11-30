<template>
  <v-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
  >
    <h3
      class="mb-4"
    >
    Random Variability
    </h3>
    <div
      class="mb-4"
    >
      <p>
        To make it possible to estimate the universe’s age in the short amount of time that we have, we made an assumption that has introduced a large amount of uncertainty in everyone’s measurement. That is the assumption that all galaxies are the same size as the Milky Way. Many galaxies are larger and many are smaller, so the distances you measured may be very different from their true distances.
      </p>
      <p>
        This random variability in galaxy size means that any one measurement that uses only 5 galaxies may be very different from another measurement that uses a different group of 5 galaxies.
      </p>
      <p>
        Let’s look at the results from each student in your class to see what we mean by this.
      </p>    </div>
    <v-divider
      class="my-4"
    >
    </v-divider>

    <v-row
      align="center"
      no-gutters
    >
      
      <v-spacer></v-spacer>
      
      <v-col
        class="shrink"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
              () => {
                state.marker = 'cla_res1';
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>


