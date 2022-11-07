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
      Professional Data
    </h3>
    <div
      class="mb-4"
    >
      Reflect a bit on what this tells you.
      <v-container
        class="px-0"
        fluid
      >
      
      <p> What did astronomers in the early 1920's believe about the universe before Edwin Hubble's discovery?</p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Reflection #1"
        tag="prodata-reflect-8a"
      ></free-response>
      
      <p>What age of the universe can be obtained from Edwin Hubble's data?</p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Age from Edwin Hubble"
        tag="prodata-reflect-8b"
      ></free-response>
      
    <p>What age of the universe can be obtained from the HST Key project's data?</p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Age from HST Key Project"
        hint="(if you can think of any more)"
        tag="prodata-reflect-8c"
      ></free-response>
      </v-container>
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
              () => {
                state.marker = 'pro_dat7';
              }
            "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!true"
      >
        <div
          style="font-size: 16px;"
        >
          Choose a response.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="true"
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
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
