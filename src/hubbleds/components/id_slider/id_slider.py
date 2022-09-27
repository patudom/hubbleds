from ipyvuetify import VuetifyTemplate
from echo.callback_container import CallbackContainer
from glue_jupyter.state_traitlets_helpers import GlueState
from numpy import where
from traitlets import observe, Float, Int

from cosmicds.utils import load_template

class IDSlider(VuetifyTemplate):
    template = load_template("id_slider.vue", __file__,
                             traitlet=True).tag(sync=True)
    selected = Int(0).tag(sync=True)
    state = GlueState().tag(sync=True)
    step = Int(1).tag(sync=True)
    thumb_value = Float().tag(sync=True)
    vmax = Int(1).tag(sync=True)
    vmin = Int(0).tag(sync=True)
    
    def __init__(self, data, id_component, value_component, *args, **kwargs):
        # NB: We can't call this member value data
        # since VuetifyTemplate already has a data member
        # (that represents the typical Vue data)
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
        self.values = sorted(self.glue_data[self.value_component])
        self.ids = sorted(self.glue_data[self.id_component], key=self._sort_key)
        self.vmax = len(self.values) - 1
        self.selected_id = int(self.ids[self.selected])
        self.thumb_value = self.values[self.selected]

    def _sort_key(self, id):
        idx = where(self.glue_data[self.id_component] == id)[0][0]
        return self.values[idx]

    def on_id_change(self, callback):
        self._id_change_cbs.append(callback)

    def remove_on_id_change(self, callback):
        self._id_change_cbs.remove(callback)

    @observe('selected')
    def _selected_id_changed(self, change):
        index = change["new"]
        self.selected_id = int(self.ids[index])
        self.thumb_value = self.values[self.selected]
        for cb in self._id_change_cbs:
            cb(self.selected_id)
    
