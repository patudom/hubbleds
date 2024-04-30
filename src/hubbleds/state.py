import dataclasses
from cosmicds.state import GlobalState
from solara import Reactive


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


GLOBAL_STATE = GlobalState()
LOCAL_STATE = LocalState()
