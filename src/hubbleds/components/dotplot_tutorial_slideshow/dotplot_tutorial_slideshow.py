import ipyvuetify as v
from pathlib import Path
from traitlets import Int, Bool, Unicode, List, Instance
from cosmicds.utils import load_template, extend_tool
from glue_jupyter.state_traitlets_helpers import GlueState
from ipywidgets import widget_serialization, DOMWidget


# theme_colors()

class DotplotTutorialSlideshow(v.VuetifyTemplate):
    template = load_template("dotplot_tutorial_slideshow.vue", __file__, traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(5).tag(sync=True)
    dialog = Bool(False).tag(sync=True)
    opened = Bool(False).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    maxStepCompleted = Int(0).tag(sync=True)
    interactSteps = List([]).tag(sync=True)
    image_location = Unicode().tag(sync=True)
    # layer_viewer = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    dotplot_viewer = Instance(DOMWidget).tag(sync=True, **widget_serialization)

    _titles = [
        "Title 1",
        "Title 2",
        "Title 3",
        "Title 4",
        "Title 5",

    ]
    _default_title = "Dot Plot Tutorial"

    def __init__(self, viewers, *args, **kwargs):
        self.currentTitle = self._default_title
        self.dotplot_viewer = viewers[0]
        self.dotplot_viewer_viewer = viewers[0].viewer
        # self.layer_viewer = viewers[1]
        
        extend_tool(self.dotplot_viewer_viewer, "bqplot:xzoom", activate_cb=self.on_zoom_active, deactivate_cb=self.on_zoom_deactive)
        

        def update_title(change):
            index = change["new"]
            print("step:", index)
            if index in range(len(self._titles)):
                self.currentTitle = self._titles[index]
            else:
                self.currentTitle = self._default_title

        self.observe(update_title, names=["step"])

        super().__init__(*args, **kwargs)
    
    def vue_activate_zoom_tool(self, _data = None):
        self.dotplot_viewer_viewer.toolbar.set_tool_enabled("bqplot:xzoom", True)
    
    def vue_activate_selector(self, _data = None):
        # self.dotplot_viewer_viewer.toolbar.set_tool_enabled("hubble:towerselect", True)
        self.dotplot_viewer_viewer.show_previous_line(True, True)
    
    def on_zoom_active(self, *args, **kwargs):
        self.vue_removeMeasuringTool()
        
    def on_zoom_deactive(self, *args, **kwargs):
        self.vue_activateMeasuringTool()
    
    def vue_activateMeasuringTool(self, _data = None):
        self.dotplot_viewer_viewer.show_line(True, True)
    
    def vue_removeMeasuringTool(self, _data = None):
        self.dotplot_viewer_viewer.remove_lines_from_figure(line=True, previous_line=True)
