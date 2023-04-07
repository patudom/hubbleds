import ipyvuetify as v
from pathlib import Path
from traitlets import Int, Bool, Unicode, List, Instance
from cosmicds.utils import load_template
from ipywidgets import widget_serialization, DOMWidget

from glue_jupyter.link import link, dlink
from echo import add_callback, delay_callback, CallbackProperty
from bqplot import Label
from bqplot.marks import Lines, Scatter
from cosmicds.utils import vertical_line_mark


from cosmicds.viewers.dotplot.state import DotPlotViewerState
from hubbleds.data_management import VELOCITY_COMPONENT
from glue.core.message import NumericalDataChangedMessage
from glue.core import HubListener

# theme_colors()

class SpectrumMeasurementTutorialSequence(v.VuetifyTemplate,HubListener):
    template = load_template("./spectrum_measurement_tutorial.vue", __file__, traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(19).tag(sync=True)
    dialog = Bool(False).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    maxStepCompleted = Int(0).tag(sync=True)
    spectrum_viewer_widget = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    dotplot_viewer_widget = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    dotplot_viewer_2_widget = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    example_galaxy_table = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    show_specviewer = Bool(False).tag(sync=True)
    show_dotplot = Bool(True).tag(sync=True)
    show_table = Bool(False).tag(sync=True)
    allow_specview_mouse_interaction = Bool(False).tag(sync=True)
    show_first_measurment = Bool(False).tag(sync=True)
    show_second_measurment = Bool(False).tag(sync=True)
    zoom_tool_enabled = Bool(False).tag(sync=True)

    _titles = [
        "Measurement Tutorial",
    ]
    _default_title = "Specrum Measurement Tutorial"

    def __init__(self, viewer_layouts, *args, **kwargs):
        # self.state = stage_state
        self.currentTitle = self._default_title
        
        self.dotplot_viewer_widget = viewer_layouts[0]
        self.dotplot_viewer_2_widget = viewer_layouts[1]
        self.spectrum_viewer_widget = viewer_layouts[2]
        self.example_galaxy_table = viewer_layouts[3]
        
        self.dotplot_viewer = self.dotplot_viewer_widget.viewer
        self.dotplot_viewer_2 = self.dotplot_viewer_2_widget.viewer
        self.spectrum_viewer = self.spectrum_viewer_widget.viewer
        
        self.first_meas_plotted = False
        self.second_meas_plotted = False
        self.first_meas_line = None
        self.second_meas_line = None
        
        self.selector_line_dp1 = Lines( x = [0,0], y = [0,0], scales=self.dotplot_viewer.scales, colors=['red'], opacities=[1], visible=False, label='selector_line_dp1')
        self.selector_line_dp2 = Lines( x = [0,0], y = [0,0], scales=self.dotplot_viewer_2.scales, colors=['red'], opacities=[1], visible=False, label='selector_line_dp2')
        self.selector_line_spec = Lines( x = [0,0], y = [0,0], scales=self.spectrum_viewer.scales, colors=['red'], opacities=[1], visible=False, label='selector_line_spec')
        
        self.x_lim = self.dotplot_viewer.state.x_min, self.dotplot_viewer.state.x_max
        self.y_lim = self.dotplot_viewer.state.y_min, self.dotplot_viewer.state.y_max
        
        self.element = self.spectrum_viewer.element 
        # Both in angstroms
        H_ALPHA_REST_LAMBDA = 6565 
        MG_REST_LAMBDA = 5172 

        self.rest = MG_REST_LAMBDA if self.element == 'Mg-I' else H_ALPHA_REST_LAMBDA
        
        super().__init__(*args, **kwargs)
        
        
        # link wavelength and velocity limits of viewers
        link((self.dotplot_viewer.state, 'x_min'), (self.spectrum_viewer.state, 'x_min'), self.v2w,  self.w2v)
        link((self.dotplot_viewer.state, 'x_max'), (self.spectrum_viewer.state, 'x_max'), self.v2w,  self.w2v)
        link((self.dotplot_viewer.state, 'x_min'), (self.dotplot_viewer_2.state, 'x_min'))
        link((self.dotplot_viewer.state, 'x_max'), (self.dotplot_viewer_2.state, 'x_max'))
        

        # link(((self.selector_line_spec,'x'), self.selector_line_dp1,'x'), self.w2v, self.w2v)
        # link(((self.selector_line_spec,'x'), self.selector_line_dp2,'x'), self.w2v, self.w2v)
        
        # do something whenever the axis limits change
        for val in ['x_min','x_max']:
            add_callback(self.dotplot_viewer.state, val ,self.on_x_axis_limits_changed)
            add_callback(self.dotplot_viewer_2.state, val ,self.on_x_axis_limits_changed)
            # add_callback(self.spectrum_viewer.state, val ,self.on_x_axis_limits_changed)
        
        data = self.example_galaxy_table._glue_data
        data.hub.subscribe(
            self, NumericalDataChangedMessage,
            filter = lambda msg: msg.data.label == data.label ,
            handler=self._on_data_change)
        
        self.observe(self._on_dialog_open, 'dialog')
        self.observe(self._on_data_change, ['show_first_measurment', 'show_second_measurment'])
        self.observe(self.toggle_specview_mouse_interaction, 'allow_specview_mouse_interaction')
        self.observe(self.zoom_tool_enabled, 'on_zoom_tool_enabled')
        
        # add_callback(self.dotplot_viewer.toolbar, 'active_tool', self._on_tool_change)
        # self.dotplot_viewer.toolbar.observe(self._on_tool_change, 'active_tool')
        self.spectrum_viewer.add_event_callback(self._update_selector_tool_sv, events=['click'])
        self.dotplot_viewer.add_event_callback(self._update_selector_tool_dp, events=['click'])
        self.dotplot_viewer_2.add_event_callback(self._update_selector_tool_dp, events=['click'])
        
    
    
    def _on_dialog_open(self, change):
        if change['new']:
            self.spectrum_viewer.toolbar.set_tool_enabled("bqplot:home",True)
            self.on_x_axis_limits_changed()
        else:
            self.vue_on_close()
    
    def _on_tool_change(self, change):
        print('on tool chang')
        active_tool = change['new']
        if active_tool is not None:
            tool_id = active_tool.tool_id
            self.dotplot_viewer_2.toolbar.active_tool = self.dotplot_viewer_2.toolbar.tools[tool_id]
        
    def on_zoom_tool_enabled(self):
        self.dotplot_viewer.toolbar.set_tool_enabled("bqplot:xzoom", self.zoom_tool_enabled)
        self.dotplot_viewer_2.toolbar.set_tool_enabled("bqplot:xzoom", self.zoom_tool_enabled)

        
    def on_x_axis_limits_changed(self, change = None): 
        # # when the x-axis limits are changed, we need to update the histogram limits
        # if not isinstance(self.dotplot_viewer.state, DotPlotViewerState):
        #     # this functionality is automatically included inthe DotPlotViewerState
        #     with delay_callback(self.dotplot_viewer.state, 'hist_x_min', 'hist_x_max'):
        #         self.dotplot_viewer.state.hist_x_min = self.dotplot_viewer.state.x_min
        #         self.dotplot_viewer.state.hist_x_max = self.dotplot_viewer.state.x_max
            
        self.plot_measurements(self.example_galaxy_table._glue_data)
        self._update_selector_tool_dp()
        # self._update_selector_tool_sv() 
        self.add_selector_lines()
    
    def add_selector_lines(self):
        self.dotplot_viewer.figure.marks = [m for m in self.dotplot_viewer.figure.marks if 'selector_line_dp1' not in m.labels] + [self.selector_line_dp1]
        self.dotplot_viewer_2.figure.marks = [m for m in self.dotplot_viewer_2.figure.marks if 'selector_line_dp2' not in m.labels] + [self.selector_line_dp2]
        # self.spectrum_viewer.figure.marks = self.spectrum_viewer.figure.marks + [self.spectrum_viewer.line]
    
    def vue_selector_lines_on(self, _data = None):
        self.selector_line_dp1.visible = True
        self.selector_line_dp2.visible = True
    
    def vue_selector_lines_off(self, _data = None):
        self.selector_line_dp1.visible = False
        self.selector_line_dp2.visible = False
        
    def get_y_bounds(self, viewer, frac = 0.8):
        """ frac must be (0,1]"""
        y_min, y_max = viewer.state.y_min, viewer.state.y_max
        frac = (1 - frac) / 2 if frac > 0 else 0
        return y_min + frac * (y_max - y_min), y_max - frac * (y_max - y_min)
    
    def _update_selector_tool_dp(self, event = None):
        if event is not None:
            new_x = [event['domain']['x'], event['domain']['x']]
            self.selector_line_dp1.x = new_x
            self.selector_line_dp2.x = new_x
            self.spectrum_viewer.line.x = self.v2w(new_x)
            self.spectrum_viewer.line_label.x = self.spectrum_viewer.line.x
            
        self.selector_line_dp1.y = self.get_y_bounds(self.dotplot_viewer)
        self.selector_line_dp2.y = self.get_y_bounds(self.dotplot_viewer_2)


    def _update_selector_tool_sv(self, event = None):
        self.selector_line_dp1.x = self.w2v(self.spectrum_viewer.line.x)
        self.selector_line_dp1.y = self.get_y_bounds(self.dotplot_viewer)
        
        self.selector_line_dp2.x = self.selector_line_dp1.x
        self.selector_line_dp2.y = self.get_y_bounds(self.dotplot_viewer_2)
        
    def vue_on_close(self, data = None):
        self.spectrum_viewer.state.reset_limits()
        marks = self.spectrum_viewer.figure.marks
        marks = [m for m in marks if ('first measurment' not in m.labels)]
        marks = [m for m in marks if ('second measurment' not in m.labels)]
        self.spectrum_viewer.figure.marks = marks
        
    def _on_data_change(self, message):
        if self.dialog:
            self.plot_measurements(self.example_galaxy_table._glue_data)
            self.show_on_specviewer()

    def plot_measurements(self, data):
        """ data should be a glue data"""
        data = data.to_dataframe()
        # data = self.example_galaxy_table._glue_data.to_dataframe()
        vel = data[VELOCITY_COMPONENT]
        
        if self.show_first_measurment:
            viewer = self.dotplot_viewer
            self.first_meas_line = self.add_point(viewer, vel[0], '#00ff00','first measurment')
            marks = [m for m in viewer.figure.marks if ('first measurment' not in m.labels)]
            viewer.figure.marks = marks + [self.first_meas_line]
            self.first_meas_plotted = True
        else:
            self.first_meas_plotted = False
        
        if self.show_second_measurment:
            viewer = self.dotplot_viewer_2
            self.second_meas_line = self.add_point(viewer, vel[1], '#0000ff','second measurment')
            marks = [m for m in viewer.figure.marks if ('second measurment' not in m.labels)]
            viewer.figure.marks = marks+ [self.second_meas_line]
            self.second_meas_plotted = True
        else:
            self.second_meas_plotted = False
    
    def show_on_specviewer(self):
        label1 = 'first measurment'
        label2 = 'second measurment'
        viewer = self.spectrum_viewer
        marks = [m for m in viewer.figure.marks if (label1 not in m.labels) and (label2 not in m.labels)]
        if self.first_meas_plotted:
            x0 = self.v2w(self.first_meas_line.x[0])
            color = self.first_meas_line.colors[0]
            label = self.first_meas_line.labels[0]
            marks = [m for m in viewer.figure.marks if (label not in m.labels)]
            marks = marks + [self.vertical_line_mark(self.spectrum_viewer, x0, color, label)]
        if self.second_meas_plotted:
            x0 = self.v2w(self.second_meas_line.x[0])
            color = self.second_meas_line.colors[0]
            label = self.second_meas_line.labels[0]
            marks = [m for m in viewer.figure.marks if (label not in m.labels)]
            marks = marks + [self.vertical_line_mark(self.spectrum_viewer, x0, color, label)]
        
        self.spectrum_viewer.figure.marks = marks
        
    def frange(start, stop, step):
        i = start
        while i < stop:
            yield i
            i += step 
        
    def v2w(self, v):
        # convert v from velocity (km/s) to wavelength (Angstroms)
        if hasattr(v, '__iter__'):
            return [self.v2w(x) for x in v]
        return self.rest * (1 + v / (3 * (10 ** 5)))
    
    def w2v(self, l):
        # convert x from wavelength (Angstroms) to velocity (km/s)
        if hasattr(l, '__iter__'):
            return [self.w2v(x) for x in l]
        return (3 * (10 ** 5) * (l / self.rest - 1))
    
    def vertical_line_mark(self,viewer, x, color, label=None):
        scales = {'x': viewer.figure.scale_x, 'y': viewer.figure.scale_y}
        ymin, ymax = scales['y'].min, scales['y'].max
        return Lines(x=[x,x], y=[ymin, ymax], scales=scales, colors=[color], labels=[label])
    
    def add_point(self, viewer, x, color, label = None): 
        scales = {'x': viewer.figure.scale_x, 'y': viewer.figure.scale_y}
        size = viewer.layers[0].bars.default_size * 5
        return  Scatter(x=[x], y=[1], 
                         scales=scales, colors=[color], 
                         labels=[label], opacities = [1],
                         default_size = size,marker='circle',)
        
    
    def vue_show_all_layers(self, data = None):
        for layer in self.dotplot_viewer.layers:
            layer.visible = True
        for layer in self.dotplot_viewer_2.layers:
            layer.visible = True
        
    
    def vue_toggle_first_measurement(self, data = None):
        self.dotplot_viewer.layers[1].visible = True
        # self.on_x_axis_limits_changed()
    
    def vue_toggle_second_measurement(self, data = None):
        self.dotplot_viewer_2.layers[2].visible = True 
        # self.on_x_axis_limits_changed()

    def vue_set_x_axis_limits(self, data = None):
        self.dotplot_viewer.state.x_min = data['xmin']
        self.dotplot_viewer.state.x_max = data['xmax']
        self.on_x_axis_limits_changed()
    
    def toggle_specview_mouse_interaction(self, change):
        if change['new']:
            self.spectrum_viewer.add_event_callback(self.spectrum_viewer._on_mouse_moved,
                                               events=['mousemove'])
            self.spectrum_viewer.add_event_callback(self.spectrum_viewer._on_click,
                                               events=['click'])
            
        else:
            self.spectrum_viewer.remove_event_callback(self.spectrum_viewer._on_mouse_moved)
            self.spectrum_viewer.remove_event_callback(self.spectrum_viewer._on_click)
            
    def vue_prep_second_measurement(self, data = None):
        
        self.example_galaxy_table.filter_by(lambda item: item['measurement_number'] == 'second')

