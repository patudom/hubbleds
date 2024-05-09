from echo import delay_callback, add_callback
from glue_plotly.viewers.scatter import PlotlyScatterView
from cosmicds.viewers import CDSScatterViewerState
from cosmicds.viewers import cds_viewer

__all__ = [
    "HubbleScatterViewerState", "HubbleFitViewerState",
    "HubbleFitView", "HubbleScatterView",
]


class HubbleScatterViewerState(CDSScatterViewerState):

    def reset_limits(self, visible_only=True):
        with delay_callback(self, 'x_min', 'x_max', 'y_min', 'y_max'):
            super().reset_limits(visible_only=visible_only)
            self.x_min = min(self.x_min, 0) if self.x_min is not None else 0
            self.y_min = min(self.y_min, 0) if self.y_min is not None else 0


class HubbleFitViewerState(HubbleScatterViewerState):
    
    def reset_limits(self, visible_only=True):
        with delay_callback(self, 'x_min', 'x_max', 'y_min', 'y_max'):
            super().reset_limits(visible_only=visible_only)
            if self.x_max is not None:
                self.x_max = 1.1 * self.x_max
            if self.y_max is not None:
                self.y_max = 1.1 * self.y_max


HubbleFitView = cds_viewer(
    PlotlyScatterView,
    name="HubbleFitView",
    viewer_tools=[
        'plotly:home',
        'plotly:zoom',
        'plotly:rectangle',
        "hubble:linefit"
    ],
    label='Fit View',
    state_cls=HubbleFitViewerState
)

HubbleFitLayerView = cds_viewer(
    PlotlyScatterView,
    name="HubbleFitLayerView",
    viewer_tools=[
        "hubble:linefit",
    ],
    label='Layer View',
    state_cls=HubbleFitViewerState
)

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
