"""
TODO: This needs to be removed. We only keep this here because plotly keeps
  the configuration setting hidden in the `FigureWidget` instance, and we
  don't have access to it from Solara natively.
"""

import solara
from typing import Callable, Any


@solara.component
def FigurePlotly(
    fig,
    on_selection: Callable[[Any], None] = None,
    on_deselect: Callable[[Any], None] = None,
    on_click: Callable[[Any], None] = None,
    on_hover: Callable[[Any], None] = None,
    on_unhover: Callable[[Any], None] = None,
    on_relayout: Callable[[Any], None] = None,
    dependencies=None,
    config=None,
):
    from plotly.graph_objs._figurewidget import FigureWidget

    def on_points_callback(data):
        if not data:
            return

        event_type = data["event_type"]
        event_mapping = {
            "plotly_click": on_click,
            "plotly_hover": on_hover,
            "plotly_unhover": on_unhover,
            "plotly_selected": on_selection,
            "plotly_deselect": on_deselect,
        }

        callback = event_mapping.get(event_type)
        if callback:
            callback(data)

    fig_element = FigureWidget.element(
        on__js2py_pointsCallback=on_points_callback, on__js2py_relayout=on_relayout
    )

    def update_data():
        fig_widget: FigureWidget = solara.get_widget(fig_element)
        fig_widget.layout = fig.layout

        fig_widget._config = fig._config | (config or {})

        length = len(fig_widget.data)
        fig_widget.add_traces(fig.data)
        data = list(fig_widget.data)
        fig_widget.data = data[length:]

    solara.use_effect(update_data, dependencies or fig)
    return fig_element
