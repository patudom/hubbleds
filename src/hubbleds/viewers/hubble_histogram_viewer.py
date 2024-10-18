from echo import delay_callback
from cosmicds.viewers import CDSHistogramViewerState, PlotlyHistogramView
from cosmicds.viewers import cds_viewer


__all__ = [
    "HubbleHistogramView",
]


class HubbleHistogramViewerState(CDSHistogramViewerState):

    def reset_limits(self, visible_only=True):
        with delay_callback(self, 'x_min', 'x_max'):
            super().reset_limits(visible_only=visible_only)
            self.x_min = round(self.x_min, 0) - 2.5 if self.x_min is not None else 0
            self.x_max = round(self.x_max, 0) + 2.5 if self.x_max is not None else 0


HubbleHistogramView = cds_viewer(
    PlotlyHistogramView,
    name="HubbleHistogramView",
    viewer_tools=[
        'plotly:home',
        'plotly:hzoom',
    ],
    label="Histogram",
    state_cls=HubbleHistogramViewerState
)
