import solara
from ..components import IntroSlideshow

from hubbleds.layout import Layout


@solara.component
def Page():
    IntroSlideshow()
