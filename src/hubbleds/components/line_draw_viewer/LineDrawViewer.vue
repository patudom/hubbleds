<script>
export default {
  name: "LineDrawViewer",
  props: ["chart"],
  mounted() {
    Plotly.newPlot(this.$refs[this.chart.uuid], this.chart.traces, this.chart.layout)
      .then(() => {
        this.element = document.getElementById(this.chart.uuid);
        this.dragLayer = this.element.querySelector(".nsewdrag");
        this.setupMouseHandlers(this.active);
        this.setupPlotlyHandlers(this.active);
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
            },
            hoverinfo: "skip"
          }
        ],
        layout: { xaxis: { range: [0, 1], autorange: false }, yaxis: { range: [0, 1], autorange: false }, hovermode: "none", dragmode: false },
      },
      active: true,
      element: null,
      lineDrawn: false,
      mouseDown: false,
      movingLine: true,
      lastEndpoint: null,
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
        [0]
      );
    },
    mouseMoveHandler(event) {
      if (this.movingLine) {
        console.log("Updating line");
        this.updateLine(event);
      }
    },
    mouseDownHandler(event) {
      console.log("mousedown");
      this.mouseDown = true;
      if (this.movingLine) {
        this.movingLine = false;
        this.drawEndpoint(event);
        this.lineDrawn = true;
      }
      if (this.hoveringEndpoint) {
        this.movingLine = true;
        this.clearEndpoint();
      }
    },
    mouseUpHandler(_event) {
      this.mouseDown = false;
    },
    plotlyHoverHandler(event) {
      console.log("hover");
      console.log(event.points[0].curveNumber);
      if (event.points[0].curveNumber === 1) {
        console.log("Hovering");
        console.log(this.dragLayer);
        this.hoveringEndpoint = true;
        this.element.style.cursor = "move";
        this.dragLayer.style.cursor = "move";
        this.dragLayer.classList.remove("cursor-crosshair");
      }
    },
    plotlyUnhoverHandler(event) {
      console.log("unhover");
      console.log(event.points[0].curveNumber);
      if (event.points[0].curveNumber === 1) {
        this.hoveringEndpoint = false;
        this.element.style.cursor = "crosshair";
        this.dragLayer.style.cursor = "crosshair";
        this.dragLayer.classList.add("cursor-crosshair");
      }
    },
    clearEndpoint() {
      if (this.element.data.length > 1) {
        try {
          Plotly.deleteTraces(this.chart.uuid, 1);
        } catch (e) {
          console.warn(e);
        }
      }
    },
    drawEndpoint(event) {
      const [x, y] = this.screenToWorld(event);
      Plotly.addTraces(this.chart.uuid, { x: [x], y: [y], type: "scatter", mode: "markers", marker: { size: 10, color: "red" }, meta: "endcap" });
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
        this.element.on("plotly_hover", this.plotlyHoverHandler);
        this.element.on("plotly_unhover", this.plotlyUnhoverHandler);
      } else {
        this.element.removeListener("plotly_hover", this.plotlyHoverHandler);
        this.element.removeListener("plotly_unhover", this.plotlyUnhoverHandler);
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
      this.setupPlotlyHandlers(value);
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
