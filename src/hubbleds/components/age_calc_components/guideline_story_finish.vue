<!-- # multiple choice -->
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
      Congratulations!
    </h3>
    <div
      class="mb-4"
    >
    <p>
      You have completed the Hubble Data Story with {{ story_state.total_score}} <v-icon>mdi-piggy-bank</v-icon> points. Nice work!
    </p>
    <p>
      You may be wondering "So what's the <strong>right</strong> answer?"
    </p>
    <p>
      <strong>There is no right answer.</strong> The Universe doesn’t come with an answer key. There are only results which you may have more or less confidence in.
    </p>
    <p>
      Science is always moving forward and there is always more humans can learn about our universe. Follow NASA to learn what new discoveries will be made by HST's successor, the James Webb Space Telescope!
    </p>
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
              () => {
                state.marker = 'pro_dat9';
              }
            "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
      >
        <div
          style="font-size: 16px;"
        >
        </div>
      </v-col>
    </v-row>
  </v-alert>
</template>
