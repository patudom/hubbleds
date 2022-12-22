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
    :allow-back="allowBack"
    :can-advance="(_state) => { canAdvance(); }"
    :state="state"
  >
    <template #before-next>
      Choose a response.
    </template>
    <slot :allow-advance="allowAdvance" :can-advance="canAdvance"></slot>
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
      default: '',
    },
    nextMarker: {
      type: String,
      default: ''
    },
    allowBack: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    canAdvance() {
      console.log(this.index);
      console.log(this.state.max_prodata_index);
      return this.state.max_prodata_index > this.index;
    }
  },
  methods: {
    retreat() {
      this.state.marker = this.prevMarker;
    },
    allowAdvance() {
      console.log("In allowAdvance");
      console.log(this.state.max_prodata_index, this.index);
      console.log(Math.max(this.state.max_prodata_index, this.index));
      console.log("======");
      this.state.max_prodata_index = Math.max(this.state.max_prodata_index, this.index + 1);
    },
    advance() {
      this.allowAdvance();
      this.state.marker = this.nextMarker;
    }
  }
}
</script>
