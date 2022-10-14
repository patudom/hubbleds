from bqplot.marks import Label, Lines
from echo import CallbackProperty
from glue_jupyter.state_traitlets_helpers import GlueState
from glue.config import viewer_tool
from glue.viewers.common.tool import CheckableTool, Tool

from ..utils import H_ALPHA_REST_LAMBDA, MG_REST_LAMBDA


@viewer_tool
class LayerToggleTool(Tool):
    class_layer_toggled = CallbackProperty(0)

    tool_id = "hubble:togglelayer"
    action_text = "Toggle display of the classes data"
    tool_tip = "Toggle display of the classes data"
    mdi_icon = "mdi-google-classroom"

    base_layer = 'mine'
    class_layer = 'class'

    def __init__(self, viewer, **kwargs):
        super().__init__(viewer, **kwargs)
        self.layer_index = 0
    

    def activate(self):
        # if we have no layers, don't do anything
        if len(self.viewer.layers) > 0:
            self.layer_to_toggle.visible = not self.layer_to_toggle.visible
        self.class_layer_toggled += 1
        
        if self.layer_to_toggle.visible:
            self.viewer.state.reset_limits()
    
    def set_layer_to_toggle(self, layer = None):
        if layer is not None:
            self.layer_to_toggle = layer
        else:
            self.layer_to_toggle = self.viewer.layers[self.layer_index]
        
    def _on_view_change(self, event=None):
        pass