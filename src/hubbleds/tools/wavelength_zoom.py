from cosmicds.tools import BqplotXZoom
from glue.config import viewer_tool
from echo import CallbackProperty

# this decorator tells glue this is a viewer tool, so it knows what to do with
# all this info
@viewer_tool
class WavelengthZoom(BqplotXZoom):
    icon = 'glue_zoom_to_rect'
    mdi_icon = "mdi-select-search"
    tool_id = 'hubble:wavezoom'
    action_text = 'x axis zoom'
    tool_tip = 'Zoom in on a region of the x-axis'
    zoom_tool_activated = CallbackProperty(False)

    on_zoom = None

    def update_selection(self, *args):
        state = self.viewer.state
        xbounds_old = [state.x_min, state.x_max]
        if self.interact.brushing:
            return
        super().update_selection(*args)

        state.reset_y_limits_for_view()

        if self.on_zoom is not None:
            xbounds_new = [state.x_min, state.x_max]
            self.on_zoom(xbounds_old, xbounds_new)

        self.deactivate()
    
    def activate(self):
        super().activate()
        self.zoom_tool_activated = True
