import dataclasses
from cosmicds.state import GlobalState
from solara import Reactive


@dataclasses.dataclass
class LocalState:
    debug_mode: Reactive[bool] = dataclasses.field(default=Reactive(False))


GLOBAL_STATE = GlobalState()
LOCAL_STATE = LocalState()
