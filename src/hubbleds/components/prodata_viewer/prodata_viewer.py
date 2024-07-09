from random import randint

import solara
from glue.core import Data
from reacton import ipyvuetify as rv

from hubbleds.state import (
    LOCAL_STATE, 
    GLOBAL_STATE, 
    )
from hubbleds.viewers.hubble_fit_viewer import HubbleFitView


@solara.component
def ProdataViewer(gjapp, data=None, height=400):
    with rv.Card() as main:
        with rv.Toolbar(dense=True, class_="toolbar"):
            with rv.ToolbarTitle():
                title_container = rv.Html(tag="div")

            rv.Spacer()
            toolbar_container = rv.Html(tag="div")

        viewer_container = rv.Html(tag="div", style_=f"width: 100%; height: {height}px")

        def _add_viewer():

            prodata_viewer = gjapp.new_data_viewer(
                HubbleFitView, show=False
            )

            title_widget = solara.get_widget(title_container)
            title_widget.children = (prodata_viewer.state.title or "Professional Data",)

            toolbar_widget = solara.get_widget(toolbar_container)
            toolbar_widget.children = (prodata_viewer.toolbar,)

            viewer_widget = solara.get_widget(viewer_container)
            viewer_widget.children = (prodata_viewer.figure_widget,)

            # prodata_viewer.figure_widget.update_layout(height=None, width=None)
            # prodata_viewer.figure_widget.update_layout(autosize=True, height=height)

            def cleanup():
                for cnt in (title_widget, toolbar_widget, viewer_widget):
                    cnt.children = ()

                for wgt in (prodata_viewer.toolbar, prodata_viewer.figure_widget):
                    wgt.close() 
            
            return cleanup

        solara.use_effect(_add_viewer, dependencies=[])

    return main

def add_data_layer(viewer, data_label, markersize, color, x_att, y_att):
    data = GLOBAL_STATE.value.glue_data_collection[data_label]
    if data not in viewer.state.layers_data:
        print('adding', data_label)
        data.style.markersize = markersize
        data.style.color = color
        viewer.add_data(data)
        viewer.state.x_att = data.id[x_att]
        viewer.state.y_att = data.id[y_att]
        layer = viewer.layer_artist_for_data(data)

    viewer.state.reset_limits() 


