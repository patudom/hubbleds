from echo import delay_callback
from glue_plotly.viewers.scatter import PlotlyScatterView
from cosmicds.viewers import CDSHistogramViewerState, CDSScatterViewerState, PlotlyHistogramView
from cosmicds.viewers import cds_viewer

__all__ = [
    "HubbleScatterView",
]

class HubbleScatterViewerState(CDSScatterViewerState):

    def reset_limits(self, visible_only=True):
        with delay_callback(self, 'x_min', 'x_max', 'y_min', 'y_max'):
            super().reset_limits(visible_only=visible_only)
            self.x_min = min(self.x_min, 0) if self.x_min is not None else 0
            self.y_min = min(self.y_min, 0) if self.y_min is not None else 0


class HubbleHistogramViewerState(CDSHistogramViewerState):

    def reset_limits(self, visible_only=True):
        with delay_callback(self, 'x_min', 'x_max'):
            super().reset_limits(visible_only=visible_only)
            self.x_min = round(self.x_min, 0) - 2.5 if self.x_min is not None else 0
            self.x_max = round(self.x_max, 0) + 2.5 if self.x_max is not None else 0


HubbleScatterView = cds_viewer(
    PlotlyScatterView,
    name="HubbleScatterView",
    viewer_tools=[
        'plotly:home',
        'plotly:zoom',
        'hubble:linefit'
    ],
    label='Scatter View',
    state_cls=HubbleScatterViewerState
)


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
