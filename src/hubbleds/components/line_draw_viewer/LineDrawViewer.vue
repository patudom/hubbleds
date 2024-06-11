<script>
export default {
  name: "LineDrawViewer",
  props: ["chart"],
  mounted() {
    Plotly.newPlot(this.$refs[this.chart.uuid], this.chart.traces, this.chart.layout)
      .then(() => {
        this.element = document.getElementById(this.chart.uuid);
        this.setupMouseHandlers(this.active);
        this.element.on("plotly_click", this.plotlyClickHandler);
        this.element.on("plotly_hover", this.plotlyHoverHandler);
        this.element.on("plotly_unhover", this.plotlyUnhoverHandler);
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
        layout: { xaxis: { range: [0, 1], autorange: false }, yaxis: { range: [0, 1], autorange: false }, hovermode: "closest" },
      },
      active: true,
      element: null,
    };
  },
  methods: {
    screenToWorld(event) {
      const layout = this.element._fullLayout;
      const rect = this.element.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      const xWorld = layout.xaxis.p2c(x - layout.margin.l);
      const yWorld = layout.yaxis.p2c(y - layout.margin.t);
      return [xWorld, yWorld];
    },
    mouseMoveHandler(event) {
      const [xWorld, yWorld] = this.screenToWorld(event);
      const newLayout = { xaxis: { range: [0, 1], autorange: false }, yaxis: { range: [0, 1], autorange: false } };
      Plotly.update(
        this.chart.uuid,
        { 'x.1': xWorld, 'y.1': yWorld },
        {},
        [0]
      );
    },
    clickHandler(event) {
      if (this.active) {
        this.active = false;
        const [x, y] = this.screenToWorld(event);
        Plotly.addTraces(this.chart.uuid, { x: [x], y: [y], type: "scatter", mode: "markers", marker: { size: 10, color: "red" }, meta: "endcap" });
      }
    },
    plotlyClickHandler(event) {
      console.log(!this.active);
      console.log(event.points[0].curveNumber === 1);
      if (!this.active && event.points[0].curveNumber === 1) {
        console.log("HERE");
        this.active = true; 
        Plotly.update(
          this.chart.uuid,
          {},
          { hovermode: "x" }
        );
      }
    },
    plotlyHoverHandler(event) {
      console.log("hover");
      console.log(event.points[0].curveNumber);
      if (!this.active && event.points[0].curveNumber === 1) {
        this.element.style.cursor = "grab";
      }
    },
    plotlyUnhoverHandler(event) {
      console.log("unhover");
      console.log(event.points[0].curveNumber);
      if (!this.active && event.points[0].curveNumber === 1) {
        this.element.style.cursor = "crosshair";
      }
    },
    setupMouseHandlers(active) {
      if (active) {
        if (this.element.data.length > 1) {
          try {
            Plotly.deleteTraces(this.chart.uuid, 1);
          } catch (e) {
            console.log(e);
          }
        }
        this.element.addEventListener("mousemove", this.mouseMoveHandler);
        this.element.addEventListener("mousedown", this.clickHandler);
      } else if (this.element != null) {
        this.element.removeEventListener("mousemove", this.mouseMoveHandler);
        this.element.removeEventListener("mousedown", this.clickHandler);
      }
    }
  },
  watch: {
    chart() {
      Plotly.react(
        this.$refs["chart"],
        this.chart.traces,
        this.chart.layout
      );
    },
    active(value) {
      this.setupMouseHandlers(value);
    }
  }
}
</script>

<template>
<div
  :ref="chart.uuid"
  :id="chart.uuid"
  :class="active ? ['active'] : []"
></div>
</template>
