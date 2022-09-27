from ipyvuetify import VuetifyTemplate
from echo.callback_container import CallbackContainer
from glue_jupyter.state_traitlets_helpers import GlueState
from numpy import isin
from traitlets import observe, Int

from cosmicds.utils import load_template

class IDSlider(VuetifyTemplate):
    template = load_template("id_slider.vue", __file__,
                             traitlet=True).tag(sync=True)
    selected = Int(0).tag(sync=True)
    state = GlueState().tag(sync=True)
    step = Int(1).tag(sync=True)
    vmax = Int(1).tag(sync=True)
    vmin = Int(0).tag(sync=True)
    
    def __init__(self, data, id_component, value_component, *args, **kwargs):
        self.glue_data = data
        self.id_component = id_component
        self.value_component = value_component
        self.refresh()

        self._id_change_cbs = CallbackContainer()

        if "step" in kwargs:
            self.step = int(kwargs["step"])
        super().__init__(*args, **kwargs)

    def update_data(self, data):
        self.glue_data = data
        self.refresh()

    def refresh(self):
        self.values = list(self.glue_data[self.value_component])
        self.vmax = len(self.values) - 1
        self.ids = sorted(self.glue_data[self.id_component], key=self._sort_key)

    def _sort_key(self, id):
        ids = list(self.glue_data[self.id_component])
        idx = ids.index(id)
        return self.values[idx]

    def on_id_change(self, callback):
        self._id_change_cbs.append(callback)

    def remove_on_id_change(self, callback):
        self._id_change_cbs.remove(callback)

    @observe('selected')
    def _selected_id_changed(self, change):
        index = change["new"]
        sel_id = self.ids[index]
        for cb in self._id_change_cbs:
            cb(sel_id)
    
