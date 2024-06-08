<script>
export default {
  name: "LineDrawViewer",
  props: ["chart"],
  mounted() {
    Plotly.plot(this.$refs[this.chart.uuid], this.chart.traces, this.chart.layout)
      .then(function() {
        const div = document.getElementById(this.chart.uuid);
        const chart = this.$refs[this.chart.uuid];
        const layout = chart._fullLayout;
        div.addEventListener("mousemove", function (event) {
          const xWorld = layout.xaxis.p2c(event.x - layout.margin.l);
          const yWorld = layout.yaxis.p2c(event.y - layout.margin.t);
          const line = chart.data[0];
          line.x[1] = xWorld;
          line.y[1] = yWorld;
          Plotly.react(
            chart,
            [line],
            chart.layout
          );
        });
      });
  },
  data: () => ({
    chart: {
      uuid: "abcde",
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
<div :ref="chart.uuid" :id="chart.uuid"></div>
</template>
