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
def SpectrumViewer(data=pd.DataFrame(), on_click=None):
    with rv.Card():
        with rv.Toolbar(color="primary", dense=True):
            with rv.ToolbarTitle():
                solara.Text("MY GALAXIES")

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

        fig.update_layout(
            xaxis_zeroline=False,
            yaxis_zeroline=False,
            xaxis=dict(
                spikecolor="white",
                spikethickness=1,
                spikedash="solid",
                spikemode="across",
                spikesnap="cursor",
            ),
            spikedistance=-1,
            #     hoverdistance=0,
            hovermode="x",
        )

        solara.FigurePlotly(
            fig,
        )
