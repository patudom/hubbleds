<script>
export default {
  name: "LineDrawViewer",
  props: ["chart"],
  mounted() {
    Plotly.newPlot(this.$refs[this.chart.uuid], this.chart.traces, this.chart.layout)
      .then(() => {
        const div = document.getElementById(this.chart.uuid);
        const chart = this.$refs[this.chart.uuid];
        div.addEventListener("mousemove", (event) => {
          const layout = chart._fullLayout;
          const rect = div.getBoundingClientRect();
          const x = event.clientX - rect.left;
          const y = event.clientY - rect.top;
          const xWorld = layout.xaxis.p2c(x - layout.margin.l);
          const yWorld = layout.yaxis.p2c(y - layout.margin.t);
          const line = { x: [0, xWorld], y: [0, yWorld], line: { color: "red" } };
          const newLayout = { xaxis: { range: [0, 1], autorange: false }, yaxis: { range: [0, 1], autorange: false } };
          Plotly.react(
            this.chart.uuid,
            [line],
            newLayout,
          );
        });
      });
  },
  data() {
    return {
      chart: {
        uuid: "abcde",
        traces: [
          {
            x: [0, 1],
            y: [0, 1],
            line: {
              color: "#5e9e7e",
              width: 4,
              shape: "line"
            }
          }
        ],
        layout: { xaxis: { range: [0, 1], autorange: false }, yaxis: { range: [0, 1], autorange: false } },
      }
    };
  },
  watch: {
    chart: {
      handler: function() {
        Plotly.react(
          this.$refs["chart"],
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
<div :ref="chart.uuid" :id="chart.uuid"></div>
</template>
