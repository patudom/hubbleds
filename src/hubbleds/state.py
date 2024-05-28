import dataclasses
from cosmicds.state import GlobalState
from solara import Reactive
from glue.core.data_factories import load_data
from pathlib import Path

# from glue.config import settings as glue_settings
# glue_settings.BACKGROUND_COLOR = 'white'
# glue_settings.FOREGROUND_COLOR= 'black'

from typing import Optional, Callable, Any

from .data_management import HUBBLE_1929_DATA_LABEL, HUBBLE_KEY_DATA_LABEL
from .tools import *

@dataclasses.dataclass
class MCScore:
    tag: str = dataclasses.field(init=True)
    # Why are we using default_factory instead of default? 
    # Because each instance of MCScore should have its own Reactive object.
    score: Reactive[float] = dataclasses.field(default_factory = lambda: Reactive(None))
    choice: Reactive[int] = dataclasses.field(default_factory = lambda: Reactive(None))
    tries: Reactive[int] = dataclasses.field(default_factory = lambda: Reactive(0))
    wrong_attempts: Reactive[int] = dataclasses.field(default_factory = lambda: Reactive(0))
    
    @classmethod
    def update_score(self, score = None, choice = None, tries = None, wrong_attempts = None, **kwargs):
        if score is not None:
            self.score.set(score)
        if choice is not None:
            self.choice.set(choice)
        if tries is not None:
            self.tries.set(tries)
        if wrong_attempts is not None:
            self.wrong_attempts.set(wrong_attempts)
    
    def toJSON(self):
        return {
            'tag': self.tag,
            'score': self.score.value,
            'choice': self.choice.value,
            'tries': self.tries.value,
            'wrong_attempts': self.wrong_attempts.value
        }
    
    def __repr__(self):
        return f"MCScore({self.toJSON()})"
@dataclasses.dataclass
class LocalState:
    debug_mode: Reactive[bool] = dataclasses.field(default=Reactive(False))
    title: Reactive[str] = dataclasses.field(default=Reactive("Hubble's Law"))
    measurements: Reactive[dict] = dataclasses.field(default=Reactive({}))
    calculations: Reactive[dict] = dataclasses.field(default=Reactive({}))
    validation_failure_counts: Reactive[dict] = dataclasses.field(default=Reactive({}))
    has_best_fit_galaxy: Reactive[bool] = dataclasses.field(default=Reactive(False))
    enough_students_ready: Reactive[bool] = dataclasses.field(default=Reactive(False))
    started: Reactive[bool] = dataclasses.field(default=Reactive(False))
    class_data_students: Reactive[list] = dataclasses.field(default=Reactive([]))
    class_data_info: Reactive[dict] = dataclasses.field(default=Reactive({}))
    mc_scoring : Reactive[dict[str, MCScore]]  = dataclasses.field(default=Reactive({
        # 'pro-dat1': {'tag': 'pro-dat1', 'score': 0.0, 'choice': 1, 'tries': 1, 'wrong_attempts': 0},
    }))


GLOBAL_STATE = GlobalState()
LOCAL_STATE = LocalState()

# add a csv file to the data collection

def add_link(from_dc_name, from_att, to_dc_name, to_att):
        from_dc = GLOBAL_STATE.data_collection[from_dc_name]
        to_dc = GLOBAL_STATE.data_collection[to_dc_name]
        GLOBAL_STATE._glue_app.add_link(from_dc, from_att, to_dc, to_att)


data_dir = Path(__file__).parent / "data"
GLOBAL_STATE.data_collection.append(load_data(data_dir / f"{HUBBLE_KEY_DATA_LABEL}.csv"))
GLOBAL_STATE.data_collection.append(load_data(data_dir / f"{HUBBLE_1929_DATA_LABEL}.csv"))

add_link(HUBBLE_1929_DATA_LABEL, 'Distance (Mpc)', HUBBLE_KEY_DATA_LABEL, 'Distance (Mpc)')
add_link(HUBBLE_1929_DATA_LABEL, 'Tweaked Velocity (km/s)', HUBBLE_KEY_DATA_LABEL, 'Velocity (km/s)')


       
# create handlers for mc_radiogroup
def on_init_response(local_state: LocalState, tag: str, callback: Optional[Callable]= None):
    print("onInitResponse")
    # print(tag not in component_state.mc_scoring.value.keys())
    if tag not in local_state.mc_scoring.value.keys():
        print("adding tag", tag)
        mc_scoring = local_state.mc_scoring.value
        print(MCScore(tag=tag))
        mc_scoring[tag] =  MCScore(tag=tag)
        print(mc_scoring)
        local_state.mc_scoring.set(mc_scoring)
        if callback is not None:
            callback(mc_scoring)
    else:
        print("tag already exists")

def on_mc_score(local_state, data, callback: Optional[Callable] = None):
    print("on_mc_score")
    mc_scoring = local_state.mc_scoring.value
    mc_scoring[data['tag']].update_score(**data)
    # mc_scoring[data['tag']].score.set(data['score'])
    # mc_scoring[data['tag']].choice.set(data['choice'])
    # mc_scoring[data['tag']].tries.set(data['tries'])
    # mc_scoring[data['tag']].wrong_attempts.set(data['wrong_attempts'])
    local_state.mc_scoring.set(mc_scoring)
    if callback is not None:
        callback(mc_scoring)


def mc_callback(event, local_state, callback: Optional[Callable] = None):
    # mc-initialize-callback returns data which is a string
    if event[0] == 'mc-initialize-response':
        return on_init_response(local_state = local_state, tag=event[1], callback=callback)
    # mc-score event returns a data which is an mc-score dictionary
    elif event[0] == 'mc-score':
        return on_mc_score(local_state=local_state, data=event[1], callback=callback)
    else:
        print(f"Unknown event in mc_callback: <<{event}>> ")

def mc_serialize_score(mc_score = None):
        if mc_score is None:
            return None
        return mc_score.toJSON()