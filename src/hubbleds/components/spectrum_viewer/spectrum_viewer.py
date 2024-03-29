import pandas as pd
import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from astropy.table import Table


df = Table(
    {"wave": np.linspace(3000, 8000, 1000), "flux": np.random.sample(1000)}
).to_pandas()


@solara.component
def SpectrumViewer(
    data=pd.DataFrame(),
    on_lambda_clicked=None,
    on_zoom_clicked=None,
    on_spectrum_clicked=None,
):
    with rv.Card():
        with rv.Toolbar(color="primary", dense=True):
            with rv.ToolbarTitle():
                solara.Text("SPECTRUM VIEWER")

            rv.Spacer()

            solara.IconButton(icon_name="mdi-select-search", on_click=on_zoom_clicked)
            solara.IconButton(icon_name="mdi-lambda", on_click=on_lambda_clicked)
            solara.IconButton(icon_name="mdi-lambda", on_click=on_spectrum_clicked)

        fig = px.line(data, x="wave", y="flux")

        fig.add_hline(
            y=1,
            line_width=0.5,
            line_dash="dot",
            line_color="cyan",
            annotation_text="1BASE",
            annotation_font_size=12,
            annotation_position="bottom right",
        )

        fig.add_shape(
            editable=True,
            x0=6790,
            x1=6830,
            y0=85,
            y1=100,
            xref="x",
            yref="y",
            line_color="red",
            fillcolor="red",
        )

        fig.update_layout(
            xaxis_zeroline=False,
            yaxis_zeroline=False,
            xaxis=dict(
                spikecolor="black",
                spikethickness=1,
                spikedash="solid",
                spikemode="across",
                spikesnap="cursor",
            ),
            spikedistance=-1,
            #     hoverdistance=0,
            hovermode="x",
        )

        line = fig.data[0]

        line.on_click(lambda: print("CLICKED POLOT"))

        solara.FigurePlotly(
            fig,
        )
