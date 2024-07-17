import solara
from typing import Iterable


@solara.component_vue("PlotlyLayerToggle.vue")
def PlotlyLayerToggle(chart_id: str,
                      layer_indices: Iterable[int],
                      labels: Iterable[str],
                      colors: Iterable[str],
                      initial_selected: Iterable[int] | None=None
):
    pass
