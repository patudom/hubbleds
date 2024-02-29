from dataclasses import dataclass
from cosmicds.state import GlobalState


@dataclass
class LocalState:
    pass


GLOBAL_STATE = GlobalState()
LOCAL_STATE = LocalState()
