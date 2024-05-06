from hubbleds.utils import GALAXY_FOV
import solara
from ..components import IntroSlideshow
import dataclasses
import astropy.units as u
from astropy.coordinates import SkyCoord
from solara import Reactive

from cosmicds.layout import Layout


@dataclasses.dataclass
class ComponentState:
    messier_object: Reactive[str] = dataclasses.field(
        default=Reactive(None)
    )

component_state = ComponentState()

@solara.component
def Page():
    IntroSlideshow(component_state.messier_object)
