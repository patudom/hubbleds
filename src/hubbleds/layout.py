from cosmicds.layout import Layout as BaseLayout
import solara
from .state import GLOBAL_STATE
from cosmicds.components import MathJaxSupport


@solara.component
def Layout(children=[]):

    # Mount external javascript libraries
    def _load_math_jax():
        MathJaxSupport()

    solara.use_memo(_load_math_jax, dependencies=[])

    with BaseLayout(children=children, story_name="hubbles_law", story_title="Hubble's Law"):
        pass