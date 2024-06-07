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
    data,
    lambda_obs=None,
    spectrum_click_enabled=False,
    on_wavelength_measured=None,
    on_lambda_clicked=None,
    on_zoom_clicked=None,
    on_spectrum_clicked=None,
):
    vertical_line_visible = solara.use_reactive(False)

    with rv.Card():
        with rv.Toolbar(color="primary", dense=True):
            with rv.ToolbarTitle():
                solara.Text("SPECTRUM VIEWER")

            rv.Spacer()

            solara.IconButton(icon_name="mdi-select-search", on_click=on_zoom_clicked)
            solara.IconButton(icon_name="mdi-lambda", on_click=on_lambda_clicked)

        fig = px.line(data.value, x="wave", y="flux")

        fig.add_vline(
            x=lambda_obs.value,
            line_width=1,
            line_color="red",
            # annotation_text="1BASE",
            # annotation_font_size=12,
            # annotation_position="top right",
            visible=vertical_line_visible.value and lambda_obs.value > 0.0,
        )

        fig.add_shape(
            editable=False,
            x0=6790,
            x1=6830,
            y0=85,
            y1=100,
            xref="x",
            yref="y",
            line_color="red",
            fillcolor="red",
            # visible=
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
            hovermode="x",
        )

        def _clicked(**kwargs):
            if spectrum_click_enabled:
                vertical_line_visible.set(True)
                # lambda_obs.set(round(kwargs['points']['xs'][0]))
                on_wavelength_measured(round(kwargs['points']['xs'][0]))
                on_spectrum_clicked()

        solara.FigurePlotly(
            fig,
            on_click=lambda kwargs: _clicked(**kwargs),
            dependencies=[lambda_obs.value, vertical_line_visible.value, data.value]
        )
