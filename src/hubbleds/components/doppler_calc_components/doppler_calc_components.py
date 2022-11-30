import ipyvuetify as v
from cosmicds.utils import load_template
from echo import delay_callback
from glue_jupyter.state_traitlets_helpers import GlueState
from traitlets import Float, Bool, Int, Unicode, List


class DopplerCalc(v.VuetifyTemplate):
    template = Unicode().tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(6).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    failedValidation4 = Bool(False).tag(sync=True)
    failedValidation5 = Bool(False).tag(sync=True)
    interactSteps5 = List([3, 4]).tag(sync=True)
    maxStepCompleted5 = Int(0).tag(sync=True)
    studentc = Float(0).tag(sync=True)
    student_vel_calc = Bool(False).tag(
        sync=True)  # stage_one.py listens for whether this value changes
    complete = Bool(False).tag(sync=True)
    lambda_obs = Float(0, allow_none=True).tag(sync=True)
    lambda_rest = Float(0, allow_none=True).tag(sync=True)
    show_doppler_calc_dialog = Bool(False).tag(sync=True)

    _titles = [
        "Doppler Calculation",
        "Doppler Calculation",
        "Doppler Calculation",
        "Reflect on Your Result",
        "Enter Speed of Light",
        "Your Galaxy's Velocity",
    ]
    _default_title = "Doppler Calculation"

    def __init__(self, filename, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = load_template(filename, path)
        self.currentTitle = self._default_title

        def update_title(change):
            index = change["new"]
            if index in range(len(self._titles)):
                self.currentTitle = self._titles[index]
            else:
                self.currentTitle = self._default_title

        self.observe(update_title, names=["step"])

    def lambda_obs_changed(self, value):
        self.lambda_obs = value

    def lambda_rest_changed(self, value):
        self.lambda_rest = value
