from asyncio import events
from echo import add_callback
from glue.config import viewer_tool


from cosmicds.tools import LineDrawTool

@viewer_tool
class HubbleLineDrawTool(LineDrawTool):

    tool_id = 'hubble:linedraw'
    
    def __init__(self, viewer, **kwargs):
        super().__init__(viewer, **kwargs)
        self.viewer.add_event_callback(self._handle_dblclick, events=['dblclick'])
        
    def _handle_dblclick(self, data):
        """
        If the user double clicks on the plot we want
        to clear the line, but only when the tool is
        inactive so that behavior is consistent
        """
        endpoint = getattr(self, 'endpoint', None)
        if endpoint is not None and self.viewer.toolbar.active_tool is None:
            self.clear()
            self.tool_tip = self.draw_tool_tip
    
    def deactivate(self):
        super().deactivate()
        if self.line is not None:
            self.tool_tip = "Update trend line. Double click graph to clear"
        
    def erase_line(self):
        super().clear()

    