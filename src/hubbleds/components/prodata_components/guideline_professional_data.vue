<!-- # multiple choice -->
<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    header-text="Professional Data"
    @back="retreat()"
    @next="advance()"
    :can-advance="(state) => state.max_prodata_index > index"
    :state="state"
  >
    <template #before-next>
      Choose a response.
    </template>
    <slot></slot>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: {
    state: {
      type: Object,
      required: true
    },
    index: {
      type: Number,
      required: true
    },
    prevMarker: {
      type: String,
      required: true
    },
    nextMarker: {
      type: String,
      required: true
    }
  },
  methods: {
    retreat() {
      this.state.marker = this.prevMarker;
    },
    advance() {
      this.state.marker = this.nextMarker;
      this.state.max_prodata_index = Math.max(state.max_prodata_index, this.index);
    }
  }
}
</script>
