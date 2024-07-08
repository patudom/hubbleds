from random import randint

import solara
from glue.core import Data
from reacton import ipyvuetify as rv

from hubbleds.viewers.hubble_dotplot import HubbleDotPlotView, HubbleDotPlotViewer
from glue.viewers.common.viewer import Viewer
from glue_plotly.viewers.common import PlotlyBaseView
from cosmicds.utils import vertical_line_mark
from itertools import chain
from uuid import uuid4
from plotly.graph_objects import Scatter
from numbers import Number
from typing import Callable, Iterable, List, cast
from solara.toestand import Reactive


@solara.component
def DotplotViewer(gjapp, data=None, component_id=None, title = None, height=400, on_click_callback = None, line_marker_at = None, line_marker_color = 'red', vertical_line_visible = True):
    
    
    with rv.Card() as main:
        with rv.Toolbar(dense=True, class_="toolbar"):
            with rv.ToolbarTitle():
                title_container = rv.Html(tag="div")

            rv.Spacer()
            toolbar_container = rv.Html(tag="div")

        viewer_container = rv.Html(tag="div", style_=f"width: 100%; height: {height}px")
        
        def _line_ids_for_viewer(viewer: PlotlyBaseView):
            line_ids = []
            traces = list(chain(l.traces() for l in viewer.layers))
            for trace in viewer.figure.data:
                if trace not in traces and isinstance(trace, Scatter) and getattr(trace, "meta", None):
                    line_ids.append(trace.meta)

            return line_ids
        
        def _remove_lines(viewers: List[PlotlyBaseView], line_ids: List[List[str]]):
            for (viewer, viewer_line_ids) in zip(viewers, line_ids):
                lines = list(viewer.figure.select_traces(lambda t: t.meta in viewer_line_ids))
                viewer.figure.data = list(reversed([t for t in viewer.figure.data if t not in lines]))
        
        
        def _add_vertical_line(viewer: PlotlyBaseView, value: Number, color: str, label: str = None, line_ids: list[str] = []):
            print("adding line")
            line = vertical_line_mark(viewer.layers[0], value, color, label = label)
            line_id = str(uuid4())
            line["meta"] = line_id
            line_ids.append(line_id)
            
            viewer.figure.add_trace(line)
            
        
            

        def _add_viewer():
            if data is None:
                viewer_data = Data(label = "Test Data", x=[randint(1, 10) for _ in range(30)])
                gjapp.data_collection.append(viewer_data)
            else: 
                if isinstance(data, Data):
                    viewer_data = data
            
                    dotplot_view: HubbleDotPlotViewer = gjapp.new_data_viewer(
                        HubbleDotPlotView, data=viewer_data, show=False
                    )
                elif isinstance(data, list):
                    dotplot_view: HubbleDotPlotViewer = gjapp.new_data_viewer(
                        HubbleDotPlotView, data = data[0], show=False)
                    print("component_id", component_id)
                    if component_id is not None:
                        dotplot_view.state.x_att = data[0].id[component_id]
                    for viewer_data in data[1:]:
                        dotplot_view.add_data(viewer_data)
            
            
                        

            
            line_ids = [] #[_line_ids_for_viewer(dotplot_view)]
            
            def _update_lines(value = None):
                # remove any pre existing lines

                _remove_lines([dotplot_view], line_ids)
                
                line_ids.clear()
                
                if vertical_line_visible and value is not None:
                    _add_vertical_line(dotplot_view, value, line_marker_color, label = "Line Marker", line_ids = line_ids)
                
                # line_ids.append(_line_ids_for_viewer(dotplot_view))
            
            
            
            if title is not None:
                dotplot_view.state.title = title
    
            title_widget = solara.get_widget(title_container)
            title_widget.children = (dotplot_view.state.title or "DOTPLOT VIEWER",)

            toolbar_widget = solara.get_widget(toolbar_container)
            toolbar_widget.children = (dotplot_view.toolbar,)

            viewer_widget = solara.get_widget(viewer_container)
            viewer_widget.children = (dotplot_view.figure_widget,)

            # The auto sizing in the plotly widget only works if the height
            #  and width are undefined. First, unset the height and width,
            #  then enable auto sizing.
            dotplot_view.figure_widget.update_layout(height=None, width=None)
            dotplot_view.figure_widget.update_layout(autosize=True, height=height)
            dotplot_view.figure_widget.update_layout(
                hovermode="x",
                spikedistance=-1,
                xaxis=dict(
                    spikecolor="black",
                    spikethickness=1,
                    spikedash="solid",
                    spikemode="across",
                    spikesnap="cursor",
                    showspikes=True
                ),
            )
            
            def on_click(trace, points, selector):
                _update_lines(value = randint(36, 44))
                if on_click_callback is not None:
                    on_click_callback(trace, points, selector)
                
            dotplot_view.figure.update_layout(clickmode="event", hovermode="closest")
            dotplot_view.selection_layer.on_click(on_click)
            dotplot_view.set_selection_active(True)
            dotplot_view.selection_layer.update(visible=True, z=[[1]], opacity=0)
            
            
            if line_marker_at is not None:
                _update_lines(value = line_marker_at)

            def cleanup():
                for cnt in (title_widget, toolbar_widget, viewer_widget):
                    cnt.children = ()

                for wgt in (dotplot_view.toolbar, dotplot_view.figure_widget):
                    # wgt.layout.close()
                    wgt.close()

            return cleanup

        solara.use_effect(_add_viewer, dependencies=[])

    return main
