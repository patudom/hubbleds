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
    obs_pos = solara.use_reactive(0.0)

    with rv.Card():
        with rv.Toolbar(color="primary", dense=True):
            with rv.ToolbarTitle():
                solara.Text("SPECTRUM VIEWER")

            rv.Spacer()

            solara.IconButton(icon_name="mdi-select-search", on_click=on_zoom_clicked)
            solara.IconButton(icon_name="mdi-lambda", on_click=on_lambda_clicked)
            solara.IconButton(icon_name="mdi-lambda", on_click=on_spectrum_clicked)

        solara.Text(f"{obs_pos.value}")
        solara.Button(label="Test", on_click=lambda: obs_pos.set(np.random.randint(3000, 8000)))

        fig = px.line(data, x="wave", y="flux")

        fig.add_vline(
            x=obs_pos.value,
            line_width=0.5,
            line_dash="dot",
            line_color="cyan",
            annotation_text="1BASE",
            annotation_font_size=12,
            annotation_position="bottom right",
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
            print(kwargs)
            # fig.update_traces(patch={'x0': kwargs['points']['xs'][0],
            #                          'x1': kwargs['points']['xs'][0]})
            fig.layout.shapes[0].x0 = kwargs['points']['xs'][0]
            fig.layout.shapes[0].x1 = kwargs['points']['xs'][0]

            fig.add_vline(
                x=obs_pos.value,
                line_width=1,
                line_color="cyan",
                annotation_font_size=12,
                annotation_position="bottom right",
            )
            obs_pos.set(kwargs['points']['xs'][0])

        solara.FigurePlotly(
            fig,
            on_click=lambda kwargs: _clicked(**kwargs),
            dependencies=[obs_pos]
        )
