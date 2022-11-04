from cosmicds.phases import CDSState
from cosmicds.registries import register_stage
from cosmicds.utils import load_template
from ..stage import HubbleStage

from traitlets import default

class StageState(CDSState):
    pass

@register_stage(story="hubbles_law", index=6, steps=["STEP 5.1", "STEP 5.2"])
class StageTest(HubbleStage):

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
        return "Comparing with Edwin Hubble and HST data"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_viewer(label="layer_viewer")
