<script>
export default {
  name: "LineDrawPlot",
  props: ["active", "line_drawn", "plot_data"],
  async mounted() {
    await window.plotlyPromise;
    Plotly.newPlot(this.$refs[this.chart.uuid], this.chart.traces, this.chart.layout, this.chart.config)
      .then(() => {
        this.element = document.getElementById(this.chart.uuid);
        this.dragLayer = this.element.querySelector(".nsewdrag");
        if (this.plot_data) {
          this.plotDataCount = this.plot_data.length;
          Plotly.addTraces(this.chart.uuid, this.plot_data);
        }
        this.setupMouseHandlers(this.active);
        this.setupPlotlyHandlers(this.active);
      });
  },
  data() {
    const baseAxis = {
      showspikes: false,
      zeroline: false,
      mirror: true,
      ticks: "outside",
      showline: true,
      showgrid: false,
      showticklabels: true,
      autorange: false,
    };
    const xaxis = { ...baseAxis, range: [0, 1] };
    const yaxis = { ...baseAxis, range: [0, 1] };
    return {
      chart: {
        uuid: "abcde",
        traces: [
          {
            x: [0, 0],
            y: [0, 0],
            line: {
              color: "#000000",
              width: 4,
              shape: "line"
            },
            hoverinfo: "skip"
          }
        ],
        layout: { xaxis, yaxis, hovermode: "none", dragmode: false, showlegend: false },
        config: { displayModeBar: false },
      },
      element: null,
      lineDrawn: false,
      mouseDown: false,
      movingLine: true,
      lastEndpoint: null,
      plotDataCount: 0,
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
    updateLine(event) {
      const [xWorld, yWorld] = this.screenToWorld(event);
      Plotly.update(
        this.chart.uuid,
        { 'x.1': xWorld, 'y.1': yWorld },
        {},
        [this.lineTraceIndex]
      );
    },
    mouseMoveHandler(event) {
      if (this.movingLine) {
        this.updateLine(event);
      }
    },
    mouseDownHandler(event) {
      this.mouseDown = true;
      if (this.movingLine) {
        this.movingLine = false;
        this.drawEndpoint(event);
        this.lineDrawn = true;
        if (this.line_drawn) {
          this.line_drawn();
        }
      }
    },
    mouseUpHandler(_event) {
      this.mouseDown = false;
    },
    plotlyClickHandler(event) {
      if (event.points[0].curveNumber === this.endpointTraceIndex) {
        if (this.hoveringEndpoint) {
          this.hoveringEndpoint = false;
          this.movingLine = true;
          this.clearEndpoint();
        }
      }
    },
    plotlyHoverHandler(event) {
      if (event.points[0].curveNumber === this.endpointTraceIndex) {
        this.hoveringEndpoint = true;
        this.element.style.cursor = "move";
        this.dragLayer.style.cursor = "move";
        this.dragLayer.classList.remove("cursor-crosshair");
      }
    },
    plotlyUnhoverHandler(event) {
      if (event.points[0].curveNumber === this.endpointTraceIndex) {
        this.hoveringEndpoint = false;
        this.element.style.cursor = "crosshair";
        this.dragLayer.style.cursor = "crosshair";
        this.dragLayer.classList.add("cursor-crosshair");
      }
    },
    clearEndpoint() {
      const dataTracesCount = this.plot_data?.length ?? 0;
      if (this.element.data.length > dataTracesCount + 1) {
        try {
          Plotly.deleteTraces(this.chart.uuid, this.endpointTraceIndex);
        } catch (e) {
          console.warn(e);
        }
      }
    },
    drawEndpoint(event) {
      const [x, y] = this.screenToWorld(event);
      Plotly.addTraces(this.chart.uuid, { x: [x], y: [y], type: "scatter", mode: "markers", marker: { size: 10, color: "#000000" }, hoverinfo: "none" });
      this.lastEndpoint = [x, y];
    },
    setupMouseHandlers(active) {
      // Using document as the event listener for mouseup is intentional
      // See this thread here: https://community.plotly.com/t/plotly-onmousedown-and-onmouseup/4812
      // For some reason, mousedown works fine on the Plotly graph, but not mouseup
      // Any ideas on how to not need to do this would be great!
      if (active) {
        this.clearEndpoint();
        this.element.addEventListener("mousemove", this.mouseMoveHandler);
        this.element.addEventListener("mousedown", this.mouseDownHandler);
        document.addEventListener("mouseup", this.mouseUpHandler);
      } else if (this.element != null) {
        this.element.removeEventListener("mousemove", this.mouseMoveHandler);
        this.element.removeEventListener("mousedown", this.mouseDownHandler);
        document.removeEventListener("mouseup", this.mouseUpHandler);
      }
    },
    setupPlotlyHandlers(active) {
      if (active) {
        this.element.on("plotly_click", this.plotlyClickHandler);
        this.element.on("plotly_hover", this.plotlyHoverHandler);
        this.element.on("plotly_unhover", this.plotlyUnhoverHandler);
      } else {
        this.element.removeListener("plotly_click", this.plotlyClickHandler);
        this.element.removeListener("plotly_hover", this.plotlyHoverHandler);
        this.element.removeListener("plotly_unhover", this.plotlyUnhoverHandler);
      }
    }
  },
  computed: {
    lineTraceIndex() {
      return 0;
    },
    endpointTraceIndex() {
      return (this.plot_data?.length ?? 0) + 1;
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
      this.setupPlotlyHandlers(value);
    }
  }
}
</script>

<template>
<div
  :ref="chart.uuid"
  :id="chart.uuid"
></div>
</template>

<style>
div.js-plotly-plot {
  width: 100%;
}
</style>
