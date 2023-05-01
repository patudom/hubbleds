from cosmicds.viewers.cds_viewer import cds_viewer
from cosmicds.viewers.dotplot.viewer import BqplotDotPlotView
from cosmicds.viewers.dotplot.state import DotPlotViewerState

from cosmicds.mixins import LineHoverStateMixin, LineHoverViewerMixin

__all__ = [ 'HubbleDotPlotView', 'HubbleDotPlotViewer', 'HubbleDotPlotViewerState']


class HubbleDotPlotViewerState(LineHoverStateMixin,DotPlotViewerState):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def reset_limits(self):
        DotPlotViewerState.reset_limits(self)
        # LineHoverStateMixin.reset_limits(self)
        
    def reset_y_limits_for_view(self):
        # needed if you use hubble:wavezoom tool 
        pass
    
        

class HubbleDotPlotViewer(LineHoverViewerMixin,BqplotDotPlotView):
    
    _state_cls = HubbleDotPlotViewerState
    
    def __init__(self, *args, **kwargs):
        super(HubbleDotPlotViewer, self).__init__(*args, **kwargs)
        
    @staticmethod
    def _label_text(value):
        return f"{value:.0f} km/s"
    
    def add_marks(self, new_marks):
        marks = []
        for new_mark in new_marks:
            if new_mark not in self.figure.marks:
                marks += [new_mark]
        
        if len(marks) > 0:
            self.figure.marks = self.figure.marks + marks
        
    def show_line(self, show = True, show_label = False):
        self.line.visible = show
        self.line_label.visible = show_label
        lines = [self.line, self.line_label]
        self.add_marks(lines)
        
    def show_previous_line(self, show = True, show_label = True):
        self.previous_line.visible = False
        self.previous_line_label.visible = False
        lines = [self.previous_line, self.previous_line_label]
        self.add_marks(lines)
    
    def add_lines_to_figure(self, add_line = True, add_previous_line = True):
        if add_line:
            self.show_line(show = self.line.visible, show_label = self.line_label.visible)
        if add_previous_line:
            self.show_previous_line(show = self.previous_line.visible, show_label = self.previous_line_label.visible)
    
    def remove_marks(self, marks):
        # make sure marks is a list
        if not isinstance(marks, list):
            marks = [marks]

        keep_marks = [m for m in self.figure.marks if m not in marks]
        self.figure.marks = keep_marks
        
    def remove_lines_from_figure(self, line = True, previous_line = True):
        if line:
            self.remove_marks([self.line, self.line_label])
        if previous_line:
            self.remove_marks([self.previous_line, self.previous_line_label])
    
    def redraw(self):
        super().redraw()
        self.add_lines_to_figure()
        
        


HubbleDotPlotView = cds_viewer(
    HubbleDotPlotViewer,
    name="HubbleDotPlotView",
    viewer_tools=[
        "bqplot:home",
        "hubble:wavezoom",
        #'hubble:towerselect'
    ],
    label="Dot Plot",
    state_cls=HubbleDotPlotViewerState
)
