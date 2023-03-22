import ipyvuetify as v
from pathlib import Path
from traitlets import Int, Bool, Unicode, List
from cosmicds.utils import load_template
from glue_jupyter.state_traitlets_helpers import GlueState


# theme_colors()

class DotPlotExplainer(v.VuetifyTemplate):
    template = load_template("dot_plot_explainer_tut.vue", __file__, traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(5).tag(sync=True)
    dialog = Bool(True).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    interactSteps = List([1]).tag(sync=True)
    maxStepCompleted = Int(0).tag(sync=True)

    _titles = [ "Dot Plot"
    ]
    _default_title = "Histograms"

    def __init__(self, length, *args, **kwargs):
        self.currentTitle = self._default_title
        self.length = length
        print('DotPlotExplainer init')
        
        super().__init__(*args, **kwargs)
        
        