from glue.config import viewer_tool

from cosmicds.tools import LayerToggleTool

@viewer_tool
class ClassLayerToggleTool(LayerToggleTool):

    tool_id = "hubble:toggleclass"
    action_text = "Toggle display of class data"
    tool_tip = "Toggle display of class data"
    mdi_icon = "mdi-google-classroom"

    def activate(self):
        super().activate()

        if self.layer_to_toggle.visible and self.toggled_count == 1:
            x_att = str(self.viewer.state.x_att)
            y_att = str(self.viewer.state.y_att)
            self.viewer.state.x_att = self.layer_to_toggle.layer.id[x_att]
            self.viewer.state.y_att = self.layer_to_toggle.layer.id[y_att]
            self.viewer.state.reset_limits()
