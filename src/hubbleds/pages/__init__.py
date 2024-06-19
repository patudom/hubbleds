import solara
from ..components import IntroSlideshow

from hubbleds.pages.layout import Layout


@solara.component
def Page():
    IntroSlideshow()
