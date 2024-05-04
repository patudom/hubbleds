import solara
from ..components import IntroSlideshow
import dataclasses
import astropy.units as u
from astropy.coordinates import SkyCoord
from solara import Reactive

from cosmicds.layout import Layout


@dataclasses.dataclass
class ComponentState:
    coordinates: Reactive[SkyCoord] = dataclasses.field(
        default=Reactive(SkyCoord(0 * u.deg, 0 * u.deg, frame="icrs"))
    )


component_state = ComponentState()


@solara.component
def Page():
    IntroSlideshow(component_state.coordinates)
