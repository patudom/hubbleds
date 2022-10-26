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
        PROFESSIONAL DATA VIEWER
      </h3>
      <div
        class="mb-4"
      >
        <p>
          This viewers shows you data from professional astronomers. You can see Hubble's data.
        </p>
        <p>
         Maybe you do something before you click next.
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
              // state.marker = 'pro_view'
            "
          >
            back
          </v-btn>
        <v-spacer></v-spacer>
        <v-col
          cols="6"
          class="shrink"
          v-if="!state.prodata_action"
        >
          <div
            style="font-size: 16px;"
          >
            Do the thing we ask you
          </div>
        </v-col>
        <v-col
          class="shrink"
          v-if="state.prodata_action"
        >
          <v-btn
            class="black--text"
            color="accent"
            elevation="2"
            @click="
              // state.marker = 'pro_view'
            "
          >
            next
          </v-btn>
        </v-col>
      </v-row>
    </v-alert>
  </template>
  