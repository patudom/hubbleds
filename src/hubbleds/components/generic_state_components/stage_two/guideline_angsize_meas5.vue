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
      Angular Size Measurement
    </h3>
    <div
      class="mb-4"
    >
      <p>
        Notice your galaxy’s angular size is now displayed in the table.
      </p>
    </div>

    <v-divider
      class="my-4"
    >
    </v-divider>

    <v-row
      align="center"
      no-gutters
    >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'ang_siz4'
          "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        class="shrink"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'ang_siz5a'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>