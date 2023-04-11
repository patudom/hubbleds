from asyncio import create_subprocess_exec
import ipyvuetify as v
from pathlib import Path
from traitlets import Int, Bool, Unicode, List, Instance
from cosmicds.utils import load_template
from ipywidgets import widget_serialization, DOMWidget

from cosmicds.utils import extend_tool

from bqplot import Label

from glue_jupyter.link import link, dlink
from echo import add_callback, delay_callback, CallbackProperty
from bqplot import Label
from bqplot.marks import Lines, Scatter
from cosmicds.utils import vertical_line_mark


from cosmicds.viewers.dotplot.state import DotPlotViewerState
from glue.core.message import NumericalDataChangedMessage, SubsetMessage
from glue.core import HubListener
from glue.core.subset import RangeSubsetState

from itertools import cycle
from functools import partial
# theme_colors()

class SpectrumMeasurementTutorialSequence(v.VuetifyTemplate,HubListener):
    template = load_template("./spectrum_measurement_tutorial.vue", __file__, traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(19).tag(sync=True)
    dialog = Bool(False).tag(sync=True)
    opened = Bool(False).tag(sync=True)
    been_opened = Bool(False).tag(sync=True)
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
    zoom_tool_enabled = Bool(True).tag(sync=True)
    show_selector_lines = Bool(True).tag(sync=True)
    allow_tower_select = Bool(True).tag(sync=True)

    _titles = [
        "Measurement Tutorial",
    ]
    _default_title = "Specrum Measurement Tutorial"

    def __init__(self, viewer_layouts, *args, **kwargs):
        
        self.currentTitle = self._default_title
        
        
        self.dotplot_viewer_widget = viewer_layouts[0]
        self.dotplot_viewer_2_widget = viewer_layouts[1]
        self.spectrum_viewer_widget = viewer_layouts[2]
        self.example_galaxy_table = viewer_layouts[3]
        
        super().__init__(*args, **kwargs)
        
        self.observe(self._on_dialog_open, 'dialog')
        
        self.dotplot_viewer = self.dotplot_viewer_widget.viewer
        self.dotplot_viewer_2 = self.dotplot_viewer_2_widget.viewer
        self.spectrum_viewer = self.spectrum_viewer_widget.viewer

        
        galaxy_table_data = self.example_galaxy_table._glue_data
        self.glue_data = self.dotplot_viewer.state.layers[0].layer

        # cycle will cycle infitely through the list of colors
        self.color_cycle = cycle(['#9e17bf','#d98d0b','#07e856','#e80707','#e807e8','#07e8e8'])
        
        
        
        self.element = self.spectrum_viewer.element 
        H_ALPHA_REST_LAMBDA = 6565 
        MG_REST_LAMBDA = 5172
        self.rest = MG_REST_LAMBDA if self.element == 'Mg-I' else H_ALPHA_REST_LAMBDA
        
        self.which_measurement = {
            'first': {
            'label': 'first measurement',
            'viewer': self.dotplot_viewer
            },
            'second': {
            'label': 'second measurement',
            'viewer': self.dotplot_viewer_2
            }
        }
        
        
        self.first_meas_plotted = False
        self.second_meas_plotted = False
        
        self.first_meas_line = self.add_point(self.dotplot_viewer, x = 0, color = '#FB5607', label = 'first_meas_line')
        self.second_meas_line = self.add_point(self.dotplot_viewer_2, x = 0, color = '#0000ff', label = 'second_meas_line')
        self.first_meas_line.visible = True
        self.second_meas_line.visible = True
        
        self.spec_view_first = self.vertical_line_mark(self.spectrum_viewer, x = 0, color = self.first_meas_line.colors[0], label = 'spec_view_first')
        self.spec_view_second = self.vertical_line_mark(self.spectrum_viewer, x = 0, color = self.second_meas_line.colors[0] , label = 'spec_view_second')
        self.spec_view_first_label = Label(
                        text=["my vel"],
                        x=[self.spec_view_first.x[0]],
                        y=[self.spec_view_first.y[1]],
                        x_offset=10,
                        y_offset=10,
                        scales=self.spec_view_first.scales,
                        colors=self.spec_view_first.colors,
                        visible=True
                    )
        
        self.spec_view_second_label = Label(
                        text=["my vel"],
                        x=[self.spec_view_second.x[0]],
                        y=[self.spec_view_second.y[1]],
                        x_offset=10,
                        y_offset=10,
                        scales=self.spec_view_second.scales,
                        colors=self.spec_view_second.colors,
                        visible=True
                    )
        
        # link x-axes
        link((self.dotplot_viewer.state, 'x_min'), (self.spectrum_viewer.state, 'x_min'), self.v2w,  self.w2v)
        link((self.dotplot_viewer.state, 'x_max'), (self.spectrum_viewer.state, 'x_max'), self.v2w,  self.w2v)
        link((self.dotplot_viewer.state, 'x_min'), (self.dotplot_viewer_2.state, 'x_min'))
        link((self.dotplot_viewer.state, 'x_max'), (self.dotplot_viewer_2.state, 'x_max'))
            

        # do something whenever the axis limits change
        for val in ['x_min','x_max', 'layers']:
            add_callback(self.dotplot_viewer.state, val ,self._on_dotplot_change)
            add_callback(self.dotplot_viewer_2.state, val ,self._on_dotplot_change)
        
        
        galaxy_table_data.hub.subscribe(
            self, NumericalDataChangedMessage,
            filter = lambda msg: msg.data.label == galaxy_table_data.label ,
            handler=self._on_data_change)
        
        # create initial tower selection subsets
        self.component = self.glue_data.id[self.dotplot_viewer.state.x_att]
        self.comp_data = self.glue_data[self.component]
        self.range_subset = None
        
        # create the ignorer before creating the subset
        self.dotplot_viewer.ignore(lambda layer: layer.label == 'selected_tower_2')
        self.dotplot_viewer_2.ignore(lambda layer: layer.label == 'selected_tower')
        self.selected_tower = self.create_range_subsets(self.dotplot_viewer, self.glue_data, 'selected_tower')
        self.selected_tower_2 = self.create_range_subsets(self.dotplot_viewer_2, self.glue_data, 'selected_tower_2')
        
        # clear_subsets currently does nothing
        extend_tool(self.dotplot_viewer, 'bqplot:home', partial(self.clear_subsets,self.dotplot_viewer))
        extend_tool(self.dotplot_viewer_2, 'bqplot:home', partial(self.clear_subsets,self.dotplot_viewer_2))
        
        extend_tool(self.dotplot_viewer,'hubble:onebinselect', 
                    deactivate_cb = partial(self.toggle_tower_select, self.dotplot_viewer), 
                    deactivate_before_tool=True)
        extend_tool(self.dotplot_viewer_2,'hubble:onebinselect', 
                    deactivate_cb = partial(self.toggle_tower_select,self.dotplot_viewer_2), 
                    deactivate_before_tool=True)
        
    
    @staticmethod    
    def link_variables(var1, var2, forward = lambda x: x, backward = lambda x: x):
        """
        "fake" the glue linking framework using callbacks
        """
        def update(var, value, new_value, func):
            if getattr(var,value, None) != new_value:
                setattr(var, value, func(new_value))
            
        add_callback(var1[0], var1[1], lambda change: update(var2[0], var2[1], change['new'], forward))
        add_callback(var2[0], var2[1], lambda change: update(var1[0], var1[1], change['new'], backward))
        
    
    def _on_dialog_open(self, change):
        if change['new'] & (not self.been_opened):
            self.been_opened = True
            self.spectrum_viewer.toolbar.set_tool_enabled("bqplot:home",True)
            
            self.add_selector_lines()
            self.dotplot_viewer.line.visible = False
            self.dotplot_viewer_2.line.visible = False
            self.dotplot_viewer.toolbar.set_tool_enabled("bqplot:xzoom",self.zoom_tool_enabled)
            
            self.spectrum_viewer.add_event_callback(self._update_selector_tool_sv, events=['mousemove'])
            self.dotplot_viewer.add_event_callback(self._update_selector_tool_dp, events=['mousemove'])
            self.dotplot_viewer_2.add_event_callback(self._update_selector_tool_dp2, events=['mousemove'])
            
            self.observe(lambda msg: self.plot_measurements(self.example_galaxy_table._glue_data), ['show_first_measurment', 'show_second_measurment'])
            self.observe(self.toggle_specview_mouse_interaction, 'allow_specview_mouse_interaction')
            self.observe(self.on_zoom_tool_enabled, 'zoom_tool_enabled')
            
            self.spectrum_viewer.add_event_callback(
                callback = lambda event: self._on_viewer_focus(self.spectrum_viewer, event), 
                events=['moustenter', 'mouseleave'])
            self.dotplot_viewer.add_event_callback(
                callback = lambda event: self._on_viewer_focus(self.dotplot_viewer, event),
                events=['moustenter', 'mouseleave'])
            self.dotplot_viewer_2.add_event_callback(
                callback = lambda event: self._on_viewer_focus(self.dotplot_viewer_2, event),
                events=['moustenter', 'mouseleave'])

        else:
            pass
    
    def _on_viewer_focus(self, viewer, event = {'event': None}):
        if event['event'] == 'mouseenter':
            # viewer.line.visible = True
            viewer.previous_line.visible = True
            viewer.previous_line_label.visible = True
        elif event['event'] == 'mouseleave':
            # viewer.line.visible = False
            viewer.previous_line.visible = False
            viewer.previous_line_label.visible = False

    
    def _on_data_change(self, message):
        # things that need to be redrawn when dotplots are changed
        self.plot_measurements(self.example_galaxy_table._glue_data, update_only = True)
    
    def _on_tool_change(self, change):
        active_tool = change['new']
        if active_tool is not None:
            tool_id = active_tool.tool_id
            self.dotplot_viewer_2.toolbar.active_tool = self.dotplot_viewer_2.toolbar.tools[tool_id]
    
    def create_range_subsets(self, viewer, data, label = None):
        subset_init = {
            'lo': viewer.state.x_min,
            'hi': viewer.state.x_max,
            'att': viewer.state.x_att
        }
        self.range_subset = RangeSubsetState(**subset_init)
        
        new_subset_init = {
            'label': label,
            'subset_state': self.range_subset,
            'color': next(self.color_cycle,'#000000')
        }
        return data.new_subset(**new_subset_init)
    
    def _on_dotplot_change(self, change = None):
        if change is not None:
            self.add_selector_lines()
        
        y_max = max(self.dotplot_viewer.state.y_max, self.dotplot_viewer_2.state.y_max)
        self.dotplot_viewer.state.y_max = y_max
        self.dotplot_viewer_2.state.y_max = y_max
        
        self.plot_measurements(self.example_galaxy_table._glue_data) # plots the measurements again
        # set the y-axis to be the same on dotplots
        
    
    def update_line_y_bounds(self, change = None):
        self.dotplot_viewer.line.y = self.get_y_bounds(self.dotplot_viewer)
        self.dotplot_viewer_2.line.y = self.get_y_bounds(self.dotplot_viewer_2)
    
        
    def on_zoom_tool_enabled(self, data=None):
        self.dotplot_viewer.toolbar.set_tool_enabled("bqplot:xzoom", self.zoom_tool_enabled)
        self.dotplot_viewer_2.toolbar.set_tool_enabled("bqplot:xzoom", self.zoom_tool_enabled)
  
    
    def clear_subsets(self,viewer):
        pass

    def add_selector_lines(self):
        self.dotplot_viewer.show_line(show = True, show_label = True)
        self.dotplot_viewer_2.show_line(show = True, show_label = True)
        self.dotplot_viewer.show_previous_line(show = True, show_label = True)
        self.dotplot_viewer_2.show_previous_line(show = True, show_label = True)
        
    def get_y_bounds(self, viewer, frac = 0.8):
        """ frac must be (0,1]"""
        y_min, y_max = viewer.state.y_min, viewer.state.y_max
        frac = (1 - frac) / 2 if frac > 0 else 0
        return y_min + frac * (y_max - y_min), y_max - frac * (y_max - y_min)
    
    
    
    def toggle_tower_select(self,viewer):
        # self.allow_tower_select = not self.allow_tower_select
        x = viewer.toolbar.tools['hubble:towerselect'].x
        if x is None:
            return
        
        which = 'second' if viewer == self.dotplot_viewer_2 else 'first'
        
        # get label of measurement layer (works before other layer is already filtered out by ignore)
        layer = next((l for l in viewer.state.layers if 'measurement' in l.layer.label),None)
        layer_label = layer.layer.label if layer is not None else None  
        
        tower_subset = self.selected_tower if which == 'first' else self.selected_tower_2

        tool_subset = viewer.toolbar.tools['hubble:towerselect'].subset_state
        meas_subset = self.get_data_subset_by_name(self.glue_data, layer_label)
        
        tower_subset.subset_state = tool_subset & meas_subset.subset_state
    
    
    @staticmethod
    def get_layer_by_name(viewer, name):
        return next((layer for layer in viewer.layers if name in layer.layer.label), None)
    
    @staticmethod
    def get_data_subset_by_name(data,  name):
        for subset in data.subsets:
            if subset.label == name:
                return subset
        return None
    
    @staticmethod    
    def search_sorted(arr, x):
        """ 
        returns the right most index of the array that is less than x
        """
        if len(arr) == 0:
            return 0
        if arr[-1] < x:
            return len(arr)
        if arr[0] > x:
            return 0
        for i in range(len(arr)):
            if arr[i] > x:
                return i
        return len(arr)
        
        
    
    def _update_selector_tool_dp(self, event = None):
        if event is not None:
            new_x = [event['domain']['x'], event['domain']['x']]
            self.dotplot_viewer_2.line.x = new_x
            self.spectrum_viewer.line.x = self.v2w(new_x)
            self.spectrum_viewer.line_label.x = self.spectrum_viewer.line.x
    
    def _update_selector_tool_dp2(self, event = None):
        if event is not None:
            new_x = [event['domain']['x'], event['domain']['x']]
            self.dotplot_viewer.line.x = new_x
            self.spectrum_viewer.line.x = self.v2w(new_x)
            self.spectrum_viewer.line_label.x = self.spectrum_viewer.line.x

    def _update_selector_tool_sv(self, event = None):
        self.dotplot_viewer.line.x = self.w2v(self.spectrum_viewer.line.x)
        self.dotplot_viewer_2.line.x = self.dotplot_viewer.line.x



    def plot_measurements(self, data, update_only = False):
        """ data should be a glue data"""
        data = data.to_dataframe()
        vel = data['velocity']
        
        if self.show_first_measurment:
            viewer = self.dotplot_viewer
            bins = viewer.state.bins
            index = self.search_sorted(bins, vel[0])
            x = (bins[index] + bins[index-1]) / 2
            self.first_meas_line.x = [x,x]
            self.first_meas_plotted = True
        else:
            self.first_meas_plotted = False
        
        if self.show_second_measurment:
            viewer = self.dotplot_viewer_2
            bins = viewer.state.bins
            index = self.search_sorted(bins, vel[1])
            x = (bins[index] + bins[index-1]) / 2
            self.second_meas_line.x = [x,x]
            self.second_meas_plotted = True
        else:
            self.second_meas_plotted = False
        
        if self.first_meas_plotted and self.first_meas_line not in self.dotplot_viewer.figure.marks:

            self.dotplot_viewer.figure.marks = self.dotplot_viewer.figure.marks + [self.first_meas_line]
        if self.second_meas_plotted and self.second_meas_line not in self.dotplot_viewer_2.figure.marks:
            self.dotplot_viewer_2.figure.marks = self.dotplot_viewer_2.figure.marks + [self.second_meas_line]
        

        self.show_measurements_on_specviewer()
    
    def show_measurements_on_specviewer(self):
        
        things_to_remove = [self.spec_view_first, 
               self.spec_view_second, 
               self.spec_view_first_label, 
               self.spec_view_second_label
               ]
        
        viewer = self.spectrum_viewer
        
        marks = [m for m in viewer.figure.marks if [m not in things_to_remove]]
        
        d = 0.2 # fraction of the y range to use for the line
        ymin = viewer.state.y_min
        ymax = viewer.state.y_max
        
        if self.first_meas_plotted:
            x0 = self.v2w(self.first_meas_line.x[0])
            mark = next((m for m in viewer.figure.marks if m == self.spec_view_first), None)
            if mark is not None:
                mark.x = x0
            else:
                self.spec_view_first.x = [x0, x0]
                self.spec_view_first.y = [ymin, ymin + d * (ymax-ymin)]
                self.spec_view_first_label.x = [x0]
                self.spec_view_first_label.y = [self.spec_view_first.y[1]]
                marks = marks + [self.spec_view_first] + [self.spec_view_first_label]
                
        if self.second_meas_plotted:
            x0 = self.v2w(self.second_meas_line.x[0])
            mark = next((m for m in viewer.figure.marks if m == self.spec_view_second), None)
            if mark is not None:
                mark.x = x0
            else:
                self.spec_view_second.x = [x0, x0]
                self.spec_view_second.y = [ymin, ymin + d * (ymax-ymin)]
                self.spec_view_second_label.x = [x0]
                self.spec_view_second_label.y = [self.spec_view_second.y[1]]
                marks = marks + [self.spec_view_second] + [self.spec_view_second_label]
        
        self.spectrum_viewer.figure.marks = marks
    
    @staticmethod
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
    
    def toggle_specview_mouse_interaction(self, change):
        """ callback function for self.allow_specview_mouse_interaction """
        if change['new']:
            self.spectrum_viewer.add_event_callback(self.spectrum_viewer._on_mouse_moved,
                                               events=['mousemove'])
            self.spectrum_viewer.add_event_callback(self.spectrum_viewer._on_click,
                                               events=['click'])
            
        else:
            self.spectrum_viewer.remove_event_callback(self.spectrum_viewer._on_mouse_moved)
            self.spectrum_viewer.remove_event_callback(self.spectrum_viewer._on_click) # turns on measuring interaction
    
    def vue_set_x_axis_limits(self, data = None):
        self.dotplot_viewer.state.x_min = data['xmin']
        self.dotplot_viewer.state.x_max = data['xmax']
        self._on_dotplot_change()
     
    def vue_prep_second_measurement(self, data = None):
        self.example_galaxy_table.filter_by(lambda item: item['measurement_number'] == 'second')
        
    def vue_selector_lines_on(self, _data = None):
        self.show_selector_lines = True       
        self.dotplot_viewer.line.visible = True
        self.dotplot_viewer_2.line.visible = True
    
    def vue_selector_lines_off(self, _data = None):
        self.show_selector_lines = False
        self.dotplot_viewer.line.visible = False
        self.dotplot_viewer_2.line.visible = False

    
    def vue_on_close(self, data = None):
        self.spectrum_viewer.state.reset_limits()
        marks = self.spectrum_viewer.figure.marks
        marks = [m for m in marks if ('first measurment' not in m.labels)]
        marks = [m for m in marks if ('second measurment' not in m.labels)]
        self.spectrum_viewer.figure.marks = marks
        self.unobserve(self._on_data_change, ['show_first_measurment', 'show_second_measurment'])
        self.unobserve(self.toggle_specview_mouse_interaction, 'allow_specview_mouse_interaction')
        self.unobserve(self.on_zoom_tool_enabled, 'zoom_tool_enabled')
        # self.spectrum_viewer.remove_event_callback(self._update_selector_tool_sv)
    
