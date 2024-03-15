<script>
import Plotly from 'plotly.dist';

export default {
  name: "SpectrumViewer",
  props: ["chart"],
  mounted() {
    Plotly.plot(this.$refs[this.chart.uuid], this.chart.traces, this.chart.layout);
  },
  data: () => ({
    chart: {
      uuid: "123",
      traces: [
        {
          y: [],
          line: {
            color: "#5e9e7e",
            width: 4,
            shape: "line"
          }
        }
      ],
      layout: {}
    }
  }),
  watch: {
    chart: {
      handler: function() {
        Plotly.react(
          this.$refs[this.chart.uuid],
          this.chart.traces,
          this.chart.layout
        );
      },
      deep: true
    }
  }
}
</script>

<template>
<div :ref="chart.uuid"></div>
</template>

<style scoped>

</style>