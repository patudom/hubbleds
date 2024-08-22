
import solara
from solara.toestand import Ref

from hubbleds.components import IntroSlideshowVue
from hubbleds.state import LOCAL_STATE, GLOBAL_STATE

from hubbleds.remote import LOCAL_API
from ..utils import IMAGE_BASE_URL

from hubbleds.layout import Layout
from cosmicds.logger import setup_logger

logger = setup_logger("STAGE INTRO")

@solara.component
def Page():
    router = solara.use_router()

    IntroSlideshowVue(
        step = 0,
        length = 5,
        titles = [
        "Our Place in the Universe",
        "Answering Questions with Data",
        "Astronomy in the early 1900s",
        "Henrietta Leavitt's Discovery",
        "Vesto Slipher and Spectral Data"
        ],
        image_location=f"{IMAGE_BASE_URL}/stage_intro",
        event_slideshow_finished=lambda _: router.push("01-spectra-&-velocity"),
        debug = LOCAL_STATE.value.debug_mode,
    )
