import ipyvuetify as v
from pathlib import Path
from sympy import preview
from traitlets import Int, Bool, Unicode, List, Instance
from cosmicds.utils import load_template, extend_tool
from glue_jupyter.state_traitlets_helpers import GlueState
from ipywidgets import widget_serialization, DOMWidget
from functools import partial


# theme_colors()

class DotplotTutorialSlideshow(v.VuetifyTemplate):
    template = load_template("dotplot_tutorial_slideshow.vue", __file__, traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(4).tag(sync=True)
    dialog = Bool(False).tag(sync=True)
    finished = Bool(False).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    maxStepCompleted = Int(0).tag(sync=True)
    dotplot_viewer = Instance(DOMWidget).tag(sync=True, **widget_serialization)

    _default_title = "Dot Plot Tutorial"

    def __init__(self, viewers, *args, **kwargs):
        self.currentTitle = self._default_title
        self.dotplot_viewer = viewers[0]
        self.dotplot_viewer_viewer = viewers[0].viewer
        self.dotplot_viewer_viewer.add_lines_to_figure()
        
        extend_tool(self.dotplot_viewer_viewer, "bqplot:xzoom", activate_cb=self.on_zoom_active, deactivate_cb=self.on_zoom_deactive)        

        super().__init__(*args, **kwargs)
        
    def vue_home_add_line(self, _data = None):
        f = partial(self.dotplot_viewer_viewer.add_lines_to_figure, add_line = True, add_previous_line = False)
        extend_tool(self.dotplot_viewer_viewer, "bqplot:home", activate_cb=f, activate_before_tool=False)
    def vue_home_add_previous_line(self, _data = None):
        f = partial(self.dotplot_viewer_viewer.add_lines_to_figure, add_line = False, add_previous_line = True)
        extend_tool(self.dotplot_viewer_viewer, "bqplot:home", activate_cb=f, activate_before_tool=False)
    
    def vue_activate_zoom_tool(self, _data = None):
        self.dotplot_viewer_viewer.toolbar.set_tool_enabled("bqplot:xzoom", True)
    
    def vue_activate_selector(self, _data = None):
        self.dotplot_viewer_viewer.show_previous_line(False, False)
        self.dotplot_viewer_viewer.add_event_callback(self.dotplot_viewer_viewer._on_click, events = ['click'])
        
    def vue_activateMeasuringTool(self, _data = None):
        self.dotplot_viewer_viewer.show_line(True, True)
    
    def vue_removeMeasuringTool(self, _data = None):
        try:
            # try to remove callback if it exists
            self.dotplot_viewer_viewer.remove_event_callback( self.dotplot_viewer_viewer._on_click)
        except KeyError:
            pass
        self.dotplot_viewer_viewer.show_previous_line(False, False)
        self.dotplot_viewer_viewer.show_line(False, False)
    
    def on_zoom_active(self, *args, **kwargs):
        self.vue_removeMeasuringTool()
            
    def on_zoom_deactive(self, *args, **kwargs):
        self.vue_activateMeasuringTool()
        if self.step >=3:
            self.vue_activate_selector()

