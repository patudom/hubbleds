from cosmicds.viewers import PlotlyDotPlotView, cds_viewer
from .tools import WavelengthZoom  # noqa

__all__ = ["HubbleDotPlotView"]


class HubbleDotPlotViewer(PlotlyDotPlotView):

    @staticmethod
    def _label_text(value):
        return f"{value:0.f} km/s"

    
HubbleDotPlotView = cds_viewer(
    HubbleDotPlotViewer,
    name="HubbleDotPlotView",
    viewer_tools=[
        "plotly:home",
        "hubble:wavezoom",
    ],
    label="Dot Plot",
)
