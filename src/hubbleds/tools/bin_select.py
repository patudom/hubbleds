from glue_jupyter.bqplot.common.tools import BqplotSelectionTool
from glue.config import viewer_tool
from echo import CallbackProperty
from bqplot_image_gl.interacts import MouseInteraction, mouse_events
from glue_jupyter.bqplot.common.tools import InteractCheckableTool, CheckableTool


from glue.config import viewer_tool
from glue_jupyter.bqplot.common.tools import INTERACT_COLOR

from contextlib import nullcontext


from bqplot.interacts import BrushIntervalSelector, IndexSelector

from glue.core.roi import RangeROI
from glue.core.subset import RangeSubsetState
from glue.config import viewer_tool
import numpy as np


# this decorator tells glue this is a viewer tool, so it knows what to do with
# all this info
@viewer_tool
class BinSelect(BqplotSelectionTool):
    icon = 'glue_xrange_select'
    mdi_icon = "mdi-select-compare"
    tool_id = 'hubble:binselect'
    action_text = 'Select fully enclosed bins'
    tool_tip = 'Select fully enclosed bins'
    tool_activated = CallbackProperty(False)
    x_min = CallbackProperty(0)
    x_max = CallbackProperty(0)
    

    def __init__(self, viewer, **kwargs):

        super().__init__(viewer, **kwargs)

        self.interact = BrushIntervalSelector(scale=self.viewer.scale_x,
                                              color=INTERACT_COLOR)

        self.interact.observe(self.update_selection, "brushing")

    def update_selection(self, *args):
        with self.viewer._output_widget or nullcontext():
            bins = self.viewer.state.bins
            bin_centers = (bins[:-1] + bins[1:]) / 2
            if self.interact.selected is not None:
                x = self.interact.selected
                if x is not None and len(x):
                    print(x)
                    if min(x) != max(x):
                        left = np.searchsorted(bin_centers, min(x), side='left')
                        right = np.searchsorted(bin_centers, max(x), side='right')
                        x = bins[left], bins[right]
                    self.x_min = min(x)
                    self.x_max = max(x)
                    roi = RangeROI(min=min(x), max=max(x), orientation='x')
                    self.viewer.apply_roi(roi)
            self.interact.selected = None
        

    def activate(self):
        with self.viewer._output_widget or nullcontext():
            self.interact.selected = None
        super().activate()
        self.tool_activated = True
    




# this decorator tells glue this is a viewer tool, so it knows what to do with
# all this info
@viewer_tool
class SingleBinSelect(InteractCheckableTool):
    icon = 'glue_crosshair'
    mdi_icon = "mdi-cursor-default-click"
    tool_id = 'hubble:onebinselect'
    action_text = 'Select a bins'
    tool_tip = 'Select a bins'
    tool_activated = CallbackProperty(False)
    x = CallbackProperty(0)
    msg = CallbackProperty({'x':None,'viewer':None})
    
    
    

    def __init__(self, viewer, **kwargs):

        super().__init__(viewer, **kwargs)
        
        self.interact = MouseInteraction(
            x_scale=self.viewer.scale_x,
            y_scale=self.viewer.scale_y,
            move_throttle=70,
            next=None,
            events=['click']
        )
        self.x =  [0,0]
        self.interact.on_msg(self._message_handler)
    
    def _message_handler(self, interaction, content, buffers):
        if content['event'] == 'click':
            x = content['domain']['x']
            self.tower_select(x)
            
    def tower_select(self, x):
        # select the histogram bin corresponding to the x-position of the selector line
        if x is None:
            return
        viewer = self.viewer
        layer = viewer.layers[0]
        bins, hist = layer.bins, layer.hist
        dx = bins[1] - bins[0]
        index = np.searchsorted(bins, x, side='right')
        # only update the subset if the bin is not empty
        if hist[max(index-1,0)] > 0:
            right_edge = bins[index]
            left_edge = right_edge - dx
            self.x = left_edge, right_edge
        else:
            self.x = None
        
        self.msg = {'x': self.x, 'viewer': viewer}
        print(self.msg)
        # self.viewer.toolbar.active_tool = None
        

    def activate(self):
        return super().activate()
    
    def deactivate(self):
        print('deactivating')
        self.x = None
        self.msg = {'x': None, 'viewer': None}
        return super().deactivate()
   
