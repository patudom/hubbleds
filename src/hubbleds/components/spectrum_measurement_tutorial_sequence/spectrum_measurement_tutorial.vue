<template>
  

<v-dialog
  v-model="dialog"
  persistent
  id="spec_meas_tut"
  min-height="100rem"
  max-width="90%"
  >
  <template v-slot:activator="{ on, attrs }">
    
    <v-btn
      block
      color="primary"
      v-bind="attrs"
      v-on="on"
      @click.stop="() => { dialog = true; opened = true;}"
    >
    <v-spacer></v-spacer>
      Compare Velocities
    <v-spacer></v-spacer>
    </v-btn>
  </template>
  <p> Stubb </p>
</v-dialog>
</template>

<style>


.tutorial-frame
{
  /* margin: 10px; */
  padding: 2%;
}

.viewers-frame {
  padding: 2%;
  padding-left: 2%
}

div.viewers-frame > div.row > div.second-dotplot  > div.v-card > header {
  background-color: transparent !important;
  /* outline: 2px solid red; */
}

</style>

<script>
module.exports = {

  methods: {
    next() {
      this.step = this.step === this.length - 1
        ? pass
        : this.step + 1
    },
    prev() {
      this.step = this.step - 1 < 0
        ? this.length - 1
        : this.step - 1
    },

    log_out_state() {
      console.log(this.tutorial_state)
    },
  },

 
}
</script>

