from functools import partial
from os.path import join
from pathlib import Path

from echo import CallbackProperty, add_callback, remove_callback
from glue_jupyter.link import dlink, link
from traitlets import Bool, default

from cosmicds.components.generic_state_component import GenericStateComponent
from ..components import ProData
from cosmicds.phases import CDSState
from cosmicds.registries import register_stage
from cosmicds.utils import (RepeatedTimer, extend_tool, load_template,
                            update_figure_css)
from hubbleds.utils import IMAGE_BASE_URL

from ..components import AgeCalc, HubbleExp, ProData, TrendsData
from ..data.styles import load_style
from ..data_management import (ALL_CLASS_SUMMARIES_LABEL, ALL_DATA_LABEL,
                               ALL_STUDENT_SUMMARIES_LABEL,
                               BEST_FIT_GALAXY_NAME, BEST_FIT_SUBSET_LABEL,
                               CLASS_DATA_LABEL, CLASS_SUMMARY_LABEL,
                               HUBBLE_1929_DATA_LABEL, HUBBLE_KEY_DATA_LABEL,
                               STUDENT_DATA_LABEL)
from ..stage import HubbleStage

from ..viewers.viewers import HubbleScatterView

class StageState(CDSState):
    
    marker = CallbackProperty("")
    indices = CallbackProperty({})
    
    markers = [
        'pro_dat0',
        'pro_dat1',
        'pro_dat2',
        'pro_dat3',
        'pro_dat4',
        'pro_dat5',
        'pro_dat6',
        'pro_dat7',
        'pro_dat8',
        'pro_dat9',
        'sto_fin1',
        ]
        
    step_markers = CallbackProperty([
        'pro_dat0',
        'pro_dat6',
    ])
    
    _NONSERIALIZED_PROPERTIES = [
        'markers', 'indices', 'step_markers', 'image_location',
    ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.marker_index = 0
        self.marker = self.markers[0]
        self.indices = {marker: idx for idx, marker in enumerate(self.markers)}

    def marker_before(self, marker):
        return self.indices[self.marker] < self.indices[marker]

    def marker_after(self, marker):
        return self.indices[self.marker] > self.indices[marker]
    
    def marker_reached(self, marker):
        return self.indices[self.marker] >= self.indices[marker]

    def move_marker_forward(self, marker_text, _value=None):
        index = min(self.markers.index(marker_text) + 1, len(self.markers) - 1)
        self.marker = self.markers[index]


@register_stage(story="hubbles_law", index=6, steps=["Edwin Hubble", "Hubble Telescope"])
class StageTest(HubbleStage):
    show_team_interface = Bool(False).tag(sync=True)
    _state_cls = StageState

        
    @default('template')
    def _default_template(self):
        return load_template("stage_five.vue", __file__)

    @default('stage_icon')
    def _default_stage_icon(self):
        return "5"

    @default('title')
    def _default_title(self):
        return "Professional Data"

    @default('subtitle')
    def _default_subtitle(self):
        return "Comparing your data with professional data"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_team_interface = self.app_state.show_team_interface

        self.stage_state.marker = self.stage_state.markers[0]
        
        # Set up prodata components
        prodata_components_dir = str(Path(
            __file__).parent.parent / "components" / "prodata_components")
        path = join(prodata_components_dir, "")
        prodata_components = [
            "guideline_professional_data0",
            "guideline_professional_data1",
            "guideline_professional_data2",
            "guideline_professional_data3",
            "guideline_professional_data4",
            "guideline_professional_data5",
            "guideline_professional_data6",
            "guideline_professional_data7",
            "guideline_professional_data8",
            "guideline_professional_data9",
            ]
            
        self.add_components_from_path(prodata_components, path, ProData)
        
        
        prodata_viewer = self.add_viewer(HubbleScatterView, "prodata_viewer",
                                         "Professional Data")
        prodata_viewer.figure.axes[1].label_offset = "5em"
        
        self.setup_prodata_viewer()

    
    def add_components_from_path(self, state_components, path, component_class = None):
        if component_class is None:
            component_class = GenericStateComponent
        ext = ".vue"
        for comp in state_components:
            label = f"c-{comp}".replace("_", "-")

            component = component_class(comp + ext, path,
                                              self.stage_state)
            self.add_component(component, label=label)


    def setup_prodata_viewer(self):
        # load the prodata_viewer
        prodata_viewer = self.get_viewer("prodata_viewer")
        
        # load the student, class, hubble, and hst data
        student_data = self.get_data(STUDENT_DATA_LABEL)
        class_data = self.get_data(CLASS_DATA_LABEL)
        hubble_data = self.get_data(HUBBLE_1929_DATA_LABEL)
        hst_data = self.get_data(HUBBLE_KEY_DATA_LABEL)
        
        
        # load data into the viewer and style
        prodata_viewer.add_data(student_data)
        student_layer = prodata_viewer.layer_artist_for_data(student_data)
        student_layer.state.color = '#FF7043'
        student_layer.state.zorder = 5
        student_layer.state.size = 8                    
        student_layer.state.alpha = 1
        student_layer.state.visible = False
        
        prodata_viewer.state.x_att = student_data.id['distance']
        prodata_viewer.state.y_att = student_data.id['velocity']
        
        
        
        # load hubble 1929 data
        prodata_viewer.add_data(hubble_data)
        hubble_layer = prodata_viewer.layer_artist_for_data(hubble_data)
        hubble_layer.state.color = '#D500F9'
        hubble_layer.state.visible = False
        
        
        # load hubble key data
        prodata_viewer.add_data(hst_data)
        hst_layer = prodata_viewer.layer_artist_for_data(hst_data)
        hst_layer.state.color = '#AEEA00'
        hst_layer.state.visible = False
        
        prodata_viewer.state.reset_limits()
        
    def _on_marker_update(self, old, new):
        if not self.trigger_marker_update_cb:
            return
        
        markers = self.stage_stage.makers
        advancing = markers.index(new) > markers.index(old)
        
        if advancing:
            prodata_viewer = self.get_viewer("prodata_viewer")
        
    
            if  new == "pro_dat1": # show hubble 1929 data. enable line fit tool
                hubble_layer = prodata_viewer.layer_artist_for_data(self.get_data(HUBBLE_1929_DATA_LABEL))
                hubble_layer.state.visible = True
                prodata_viewer.toolbar.set_tool_enabled("hubble:linefit", True)
                prodata_viewer.toolbar.tools["hubble:linefit"].show_labels = False
            
            elif new == 'pro_dat5':
                # deactivates the tool. activate() is a toggle
                if prodata_viewer.toolbar.tools["hubble:linefit"].active:
                    prodata_viewer.toolbar.tools["hubble:linefit"].activate()
                hst_layer = prodata_viewer.layer_artist_for_data(self.get_data(HUBBLE_KEY_DATA_LABEL))
                hst_layer.state.visible = True
            
            elif new == 'pro_dat6':
                # turn off the line fit tool
                prodata_viewer.toolbar.tools["hubble:linefit"].show_labels = False
                if not prodata_viewer.toolbar.tools["hubble:linefit"].active:
                    prodata_viewer.toolbar.tools["hubble:linefit"].activate()
            
            elif new == 'pro_dat8':
                # show all the ages
                prodata_viewer = self.get_viewer("prodata_viewer")
                prodata_viewer.toolbar.tools["hubble:linefit"].show_labels = True
            
            
     