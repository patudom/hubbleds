from functools import partial
from os.path import join
from pathlib import Path

from echo import CallbackProperty, add_callback, remove_callback
from glue_jupyter.link import dlink, link
from traitlets import Bool, default

from cosmicds.components.generic_state_component import GenericStateComponent
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


class StageState(CDSState):
    
    marker = CallbackProperty("")
    indices = CallbackProperty({})
    
    markers = [
        "mar_ker1",
        "mar_ker2",
        "mar_ker3",
        "mar_ker4",
        "mar_ker5",
        ]
        
    step_markers = CallbackProperty([
        'mar_ker1',
        'mar_ker3',
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


@register_stage(story="hubbles_law", index=5, steps=["TEST STEP1", "TEST STEP2"])
class StageTest(HubbleStage):
    show_team_interface = Bool(False).tag(sync=True)
    _state_cls = StageState
    
    @default('stage_state')
    def _default_state(self):
        return StageState()
    
    @default('template')
    def _default_template(self):
        return load_template("stage_test.vue", __file__)

    @default('stage_icon')
    def _default_stage_icon(self):
        return "4"

    @default('title')
    def _default_title(self):
        return "Test"

    @default('subtitle')
    def _default_subtitle(self):
        return "Testing"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.show_team_interface = self.app_state.show_team_interface

        self.add_viewer(label="layer_viewer")
    
    def add_components_from_path(self, state_components, path):
        
        ext = ".vue"
        for comp in state_components:
            label = f"c-{comp}".replace("_", "-")

            component = GenericStateComponent(comp + ext, path,
                                              self.stage_state)
            self.add_component(component, label=label)


    def _on_marker_update(self, old, new):
        if not self.trigger_marker_update_cb:
            return
        
        markers = self.stage_stage.makers
        advancing = markers.index(new) > markers.index(old)
        
        if advancing:
            pass