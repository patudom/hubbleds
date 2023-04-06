from asyncio import create_subprocess_exec
import ipyvuetify as v
from pathlib import Path
from traitlets import Int, Bool, Unicode, List, Instance
from cosmicds.utils import load_template
from ipywidgets import widget_serialization, DOMWidget

from cosmicds.utils import extend_tool


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
    zoom_tool_enabled = Bool(False).tag(sync=True)
    show_selector_lines = Bool(True).tag(sync=True)
    allow_tower_select = Bool(False).tag(sync=True)

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
        
        # cycle will cycle infitely through the list of colors
        self.color_cycle = cycle(['#9e17bf','#d98d0b','#07e856','#e80707','#e807e8','#07e8e8'])
        
        # Get the data collection
        self.dc = self.dotplot_viewer._data
        self.example_seed_data = self.dotplot_viewer.state.layers[0].layer
        
        extend_tool(self.dotplot_viewer, 'bqplot:home', self.clear_subsets)
        extend_tool(self.dotplot_viewer_2, 'bqplot:home', self.clear_subsets)
        
        self.first_meas_plotted = False
        self.second_meas_plotted = False
        self.first_meas_line = None
        self.second_meas_line = None
        
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
        
        line_props = {
            'colors': ['gray'],
            'opacities': [.5],
            'line_style': 'dashed',
            'stroke_width': 1,
            'visible': False,
            'zorder': 0,
        }
        # self.dotplot_viewer.line  = Lines( x = [0,0], y = [0,0], scales=self.dotplot_viewer.scales,  **line_props, label='selector_line_dp1')
        # self.dotplot_viewer_2.line  = Lines( x = [0,0], y = [0,0], scales=self.dotplot_viewer_2.scales,**line_props, label='selector_line_dp2')
        # self.selector_line_spec = Lines( x = [0,0], y = [0,0], scales=self.spectrum_viewer.scales, **line_props, label='selector_line_spec')
        self.vue_selector_lines_on()
        
        
        self.selected_tower = self.create_range_subsets(self.dotplot_viewer, self.example_seed_data, 'selected_tower')
        self.selected_tower_2 = self.create_range_subsets(self.dotplot_viewer_2, self.example_seed_data, 'selected_tower_2')
        
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
        

        # do something whenever the axis limits change
        for val in ['x_min','x_max']:
            add_callback(self.dotplot_viewer.state, val ,self._on_dotplot_change)
            add_callback(self.dotplot_viewer_2.state, val ,self._on_dotplot_change)
        
        add_callback(self.dotplot_viewer.state, 'layers' ,self._on_dotplot_change)
        add_callback(self.dotplot_viewer_2.state, 'layers' ,self._on_dotplot_change)
        
        galaxy_table_data = self.example_galaxy_table._glue_data
        galaxy_table_data.hub.subscribe(
            self, NumericalDataChangedMessage,
            filter = lambda msg: msg.data.label == galaxy_table_data.label ,
            handler=self._on_data_change)
        
        self.observe(self._on_dialog_open, 'dialog')
        

        extend_tool(self.dotplot_viewer,'hubble:onebinselect', self.toggle_tower_select, self.toggle_tower_select)
    
    
    def toggle_tower_select(self, *args, **kwargs):
        self.allow_tower_select = not self.allow_tower_select
        if self.allow_tower_select:
            print('can now select towers')
        else:
            print('cannot select towers')
        
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
            print(change['new'], self.opened, self.dialog)
            self.spectrum_viewer.toolbar.set_tool_enabled("bqplot:home",True)
            
            self.add_selector_lines()
            
            self.spectrum_viewer.add_event_callback(self._update_selector_tool_sv, events=['mousemove'])
            self.dotplot_viewer.add_event_callback(self._update_selector_tool_dp, events=['mousemove'])
            self.dotplot_viewer_2.add_event_callback(self._update_selector_tool_dp2, events=['mousemove'])
            
            self.dotplot_viewer.add_event_callback(
                callback = lambda event: self.tower_select('first',event), 
                events=['click'])
            self.dotplot_viewer_2.add_event_callback(
                callback = lambda event: self.tower_select('second', event), 
                events=['click'])
            
            # self._on_dotplot_change()
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
            
        elif not change['new']:
            pass
            #self.vue_on_close()
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
        pass

    
    def _on_data_change(self, message):
        self.plot_measurements(self.example_galaxy_table._glue_data, update_only = True)
    
    def _on_tool_change(self, change):
        print('on tool chang')
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
        # self._update_selector_tool_dp() # updates the x-position of the selector lines
        if change is not None:
            # when it is not, then the function
            # is being called by a layer change
            # which automatically redraws the selector lines
            self.add_selector_lines()
        self.plot_measurements(self.example_galaxy_table._glue_data) # plots the measurements again
    
    def update_line_y_bounds(self, change = None):
        self.dotplot_viewer.line.y = self.get_y_bounds(self.dotplot_viewer)
        self.dotplot_viewer_2.line.y = self.get_y_bounds(self.dotplot_viewer_2)
    
        
    def on_zoom_tool_enabled(self, data=None):
        self.dotplot_viewer.toolbar.set_tool_enabled("bqplot:xzoom", self.zoom_tool_enabled)
        self.dotplot_viewer_2.toolbar.set_tool_enabled("bqplot:xzoom", self.zoom_tool_enabled)
  
    
    def clear_subsets(self,*args, **kwargs):
        pass
        # for subset in self.example_seed_data.subsets:
        #     if subset.label.split()[-1] != 'measurement':
        #         subset.delete()
        # self.create_subsets()

    def add_selector_lines(self):
        self.dotplot_viewer.show_line(show = True, show_label = False)
        self.dotplot_viewer_2.show_line(show = True, show_label = False)
        self.dotplot_viewer.show_previous_line(show = True, show_label = True)
        self.dotplot_viewer_2.show_previous_line(show = True, show_label = True)
        
        # self.dotplot_viewer.figure.marks = [m for m in self.dotplot_viewer.figure.marks if 'selector_line_dp1' not in m.labels] + [self.dotplot_viewer.line]
        # self.dotplot_viewer_2.figure.marks = [m for m in self.dotplot_viewer_2.figure.marks if 'selector_line_dp2' not in m.labels] + [self.dotplot_viewer_2.line]
    
    def get_y_bounds(self, viewer, frac = 0.8):
        """ frac must be (0,1]"""
        y_min, y_max = viewer.state.y_min, viewer.state.y_max
        frac = (1 - frac) / 2 if frac > 0 else 0
        return y_min + frac * (y_max - y_min), y_max - frac * (y_max - y_min)
    
    def tower_select(self, which = 'first',  event = None):
        # select the histogram bin corresponding to the x-position of the selector line
        if (not self.allow_tower_select) or (event is None):
            return
        
        # are we on the first or second measurement
        # get the approriate pieces
        x = event['domain']['x']
        if x is None:
            return
        print('tower select', x, which)
        layer_label = self.which_measurement[which]['label']
        subset_label = layer_label
        viewer = self.which_measurement[which]['viewer']
        
        tower_subset = self.selected_tower if which == 'first' else self.selected_tower_2
        
        layer = self.get_layer_by_name(viewer, layer_label)
        
        bins, hist = layer.bins, layer.hist
        dx = bins[1] - bins[0]
        index = self.search_sorted(bins, x) 
        # only update the subset if the bin is not empty
        if hist[max(index-1,0)] > 0:
            right_edge = bins[index]
            left_edge = right_edge - dx
            self.range_subset.lo = left_edge
            self.range_subset.hi = right_edge
            meas_subset = self.get_data_subset_by_name(self.example_seed_data, subset_label)
            tower_subset.subset_state = self.range_subset & meas_subset.subset_state
            tower_subset.color = next(self.color_cycle)
        
            other = 'second' if which == 'first' else 'first'
            layer = self.get_layer_by_name(self.which_measurement[other]['viewer'], tower_subset.label)
            layer.visible = False
        
            # self._on_dotplot_change()
        self.dotplot_viewer.toolbar.active_tool = None
    
    
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
        
        # self.dotplot_viewer.line.visible = True
        # self.dotplot_viewer_2.line.visible = True
    
    def _update_selector_tool_dp2(self, event = None):
        if event is not None:
            new_x = [event['domain']['x'], event['domain']['x']]
            self.dotplot_viewer.line.x = new_x
            self.spectrum_viewer.line.x = self.v2w(new_x)
            self.spectrum_viewer.line_label.x = self.spectrum_viewer.line.x
        
        # self.dotplot_viewer.line.visible = True
        # self.dotplot_viewer_2.line.visible = True


    def _update_selector_tool_sv(self, event = None):
        self.dotplot_viewer.line.x = self.w2v(self.spectrum_viewer.line.x)
        self.dotplot_viewer_2.line.x = self.dotplot_viewer.line.x
        
        # self.dotplot_viewer.line.visible = True
        # self.dotplot_viewer_2.line.visible = True


    def plot_measurements(self, data, update_only = False):
        """ data should be a glue data"""
        data = data.to_dataframe()
        vel = data['velocity']

        
        if self.show_first_measurment:
            viewer = self.dotplot_viewer
            bins = viewer.state.bins
            index = self.search_sorted(bins, vel[0])
            x = (bins[index] + bins[index-1]) / 2
            if not update_only:
                self.first_meas_line = self.add_point(viewer, x, '#FB5607','first measurment')
                marks = [m for m in viewer.figure.marks if ('first measurment' not in m.labels)]
                viewer.figure.marks = marks + [self.first_meas_line]
                self.first_meas_plotted = True
            else:
                mark = [m for m in viewer.figure.marks if ('first measurment' in m.labels)][0]
                mark.x = [x,x]
        else:
            self.first_meas_plotted = False
        
        if self.show_second_measurment:
            viewer = self.dotplot_viewer_2
            bins = viewer.state.bins
            index = self.search_sorted(bins, vel[1])
            x = (bins[index] + bins[index-1]) / 2
            if not update_only:
                self.second_meas_line = self.add_point(viewer, x, '#0000ff','second measurment')
                marks = [m for m in viewer.figure.marks if ('second measurment' not in m.labels)]
                viewer.figure.marks = marks+ [self.second_meas_line]
                self.second_meas_plotted = True
            else:
                mark = [m for m in viewer.figure.marks if ('second measurment' in m.labels)][0]
                mark.x = [x,x]
        else:
            self.second_meas_plotted = False
        
        self.show_measurements_on_specviewer()
    
    def show_measurements_on_specviewer(self):
        label1 = 'first measurment'
        label2 = 'second measurment'
        viewer = self.spectrum_viewer
        # get list of marks without measurement lines
        marks = [m for m in viewer.figure.marks if (label1 not in m.labels) and (label2 not in m.labels)]
        if self.first_meas_plotted:
            x0 = self.v2w(self.first_meas_line.x[0])
            if label1 in [m.labels for m in viewer.figure.marks]:
                mark = [m for m in viewer.figure.marks if (label1 in m.labels)][0]
                mark.x = x0
            else:
                color = self.first_meas_line.colors[0]
                label = self.first_meas_line.labels[0]
                # marks = [m for m in viewer.figure.marks if (label not in m.labels)]
                marks = marks + [self.vertical_line_mark(self.spectrum_viewer, x0, color, label)]
        if self.second_meas_plotted:
            x0 = self.v2w(self.second_meas_line.x[0])
            if label2 in [m.labels for m in viewer.figure.marks]:
                mark = [m for m in viewer.figure.marks if (label2 in m.labels)][0]
                mark.x = x0
            else:
                color = self.second_meas_line.colors[0]
                label = self.second_meas_line.labels[0]
                # marks = [m for m in viewer.figure.marks if (label not in m.labels)]
                marks = marks + [self.vertical_line_mark(self.spectrum_viewer, x0, color, label)]
        
        # assign new marks to figure (makes sure figure is redrawn)
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
            self.spectrum_viewer.remove_event_callback(self.spectrum_viewer._on_click)
    
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
