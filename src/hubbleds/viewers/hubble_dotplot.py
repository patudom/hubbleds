from cosmicds.viewers.cds_viewer import cds_viewer
from cosmicds.viewers.dotplot.viewer import BqplotDotPlotView
from cosmicds.viewers.dotplot.state import DotPlotViewerState

from cosmicds.mixins import LineHoverStateMixin, LineHoverViewerMixin

__all__ = [ 'HubbleDotPlotView', 'HubbleDotPlotViewer', 'HubbleDotPlotViewerState']


class HubbleDotPlotViewerState(LineHoverStateMixin,DotPlotViewerState):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class HubbleDotPlotViewer(LineHoverViewerMixin,BqplotDotPlotView):
    
    _state_cls = HubbleDotPlotViewerState
    
    def __init__(self, *args, **kwargs):
        super(HubbleDotPlotViewer, self).__init__(*args, **kwargs)
        
    @staticmethod
    def _label_text(value):
        return f"{value:.0f} km/s"
    
    def show_line(self, show = True, show_label = False):
        self.line.visible = show
        self.line_label.visible = show_label
        lines = [self.line, self.line_label]
        marks = [m for m in self.figure.marks if m not in lines]
        marks = [self.line] + marks
        marks = [self.line_label] + marks
        self.figure.marks = marks
        
    def show_previous_line(self, show = True, show_label = True):
        self.previous_line.visible = False
        self.previous_line_label.visible = False
        lines = [self.previous_line, self.previous_line_label]
        marks = [m for m in self.figure.marks if m not in lines]
        marks = [self.previous_line] + marks
        marks = [self.previous_line_label] + marks
        self.figure.marks = marks
    
    def add_lines_to_figure(self):
        self.show_line(show = self.line.visible, show_label = self.line_label.visible)
        self.show_previous_line(show = self.previous_line.visible, show_label = self.previous_line_label.visible)
    
    def redraw(self):
        super().redraw()
        self.add_lines_to_figure()
        
        


HubbleDotPlotView = cds_viewer(
    HubbleDotPlotViewer,
    name="HubbleDotPlotView",
    viewer_tools=[
        "bqplot:home",
        "bqplot:xzoom",
        'hubble:towerselect'
    ],
    label="Dot Plot",
    state_cls=HubbleDotPlotViewerState
)