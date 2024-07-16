<template>
  <v-card
    flat
    light
    variant="outlined"
    color="white"
    class="layer_toggle"
  >
    <v-list-item-group
      multiple
      v-model="selected"
    >
      <v-list-item
        v-for="(layer, index) in layer_indices"
        :key="index"
        :value="index"
        inactive
      >
        <template v-slot:default="{ active }">
          <v-list-item-content
            class="font-weight-bold"
          >
            {{ labels[index] }}
          </v-list-item-content>

          <v-list-item-action>
            <v-checkbox
              :input-value="index in selected"
              :color="colors[index]"
              @change="setLayerVisible(layer, active)"
            />
          </v-list-item-action>
        </template>

      </v-list-item>

    </v-list-item-group>
  </v-card>
</template>

<script>
export default {
  props: ["chart_id", "layer_indices", "labels", "colors", "initial_selected"],
  data() {
    return {
      element: null,
      selected: [],
    };
  },
  async mounted() {
    await window.plotlyPromise;
    this.getElement();
    this.selected = this.initial_selected || Array.from({length: this.layer_indices.length}, (x, i) => true);
  },
  methods: {
    getElement() {
      this.element = document.getElementById(this.chart_id);
    },
    setLayerVisible(index, visible) {
      if (!this.element) {
        this.getElement();
      }
      Plotly.restyle(this.element, { visible }, {}, index);
    }
  }
}
</script>

<style scoped>
.v-card {
  border: solid 1px black !important;
}
</style>
