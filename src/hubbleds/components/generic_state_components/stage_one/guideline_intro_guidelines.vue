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
      Introducing the Guidelines
    </h3>
    <div
      class="mb-4"
    >
      <p>
        <strong>These orange boxes will GUIDE you as you move through the story.</strong>
      </p>
      <p>
        The information in the guideline boxes will suggest what you should focus on, or what you should do next.
      </p>
      <p>
        The images, tables, or graph where the guideline suggests action will also be highlighted with an <strong>orange outline</strong>.
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
      <v-col
        class="shrink"
        cols="7"
        >
        <span style="font-size: 16px;">Use left menu to return to Introduction.<br>(Press <v-icon>mdi-menu</v-icon> in upper left if menu is not open)</span>
        
      </v-col>
      <v-spacer></v-spacer>
      <v-col
        class="shrink"
      ></v-col>
      <v-spacer></v-spacer>
      <v-col
        class="shrink"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'sel_gal1'
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
