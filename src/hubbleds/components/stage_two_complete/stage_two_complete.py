import ipyvuetify as v
from cosmicds.utils import load_template
from glue_jupyter.state_traitlets_helpers import GlueState
from traitlets import Bool

# theme_colors()

class StageTwoComplete(v.VuetifyTemplate):
    template = load_template(
        "guideline_stage_two_complete.vue", __file__, traitlet=True).tag(sync=True)
    stage_two_complete = Bool(False).tag(sync=True)
    state = GlueState().tag(sync=True)

    def __init__(self, stage_state, *args, **kwargs):
        self.state = stage_state
        super().__init__(*args, **kwargs)