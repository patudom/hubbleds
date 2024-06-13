from hubbleds.utils import GALAXY_FOV
import solara
from ..components import IntroSlideshow
import dataclasses
import astropy.units as u
from astropy.coordinates import SkyCoord
from solara import Reactive

from ..layout import Layout


@solara.component
def Page():
    IntroSlideshow()
