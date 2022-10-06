from bqplot.marks import Label, Lines
from echo import add_callback, CallbackProperty
from glue.config import viewer_tool
from glue.viewers.common.tool import CheckableTool

from ..utils import H_ALPHA_REST_LAMBDA, MG_REST_LAMBDA


@viewer_tool
class LayerToggleTool(CheckableTool):
    tool_id = "hubble:togglelayer"
    action_text = "Toggle 2nd data layer"
    tool_tip = "Toggle display of the rest wavelength line"
    mdi_icon = "mdigoogleclassroom"

    base_layer = 'mine'
    class_layer = 'class'

    class_layer_on = CallbackProperty(False)

    def __init__(self, viewer, **kwargs):
        super().__init__(viewer, **kwargs)
        self.active = False
        
        # by default, toggle the last layer added
        self.layer_index = -1

    def activate(self):
        self.viewer.layers[self.layer_index].visible = True
        self.class_layer_on = True

    def deactivate(self):
        self.viewer.layers[self.layer_index].visible = False
        self.class_layer_on = False

    def _on_view_change(self, event=None):
        pass