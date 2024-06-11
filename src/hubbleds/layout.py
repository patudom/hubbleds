from cosmicds.layout import BaseLayout
import solara
from cosmicds.components import MathJaxSupport


@solara.component
def Layout(children=[]):

    # Mount external javascript libraries
    def _load_math_jax():
        MathJaxSupport()

    solara.use_memo(_load_math_jax, dependencies=[])

    BaseLayout(children=children, story_name="hubbles_law", story_title="Hubble's Law")