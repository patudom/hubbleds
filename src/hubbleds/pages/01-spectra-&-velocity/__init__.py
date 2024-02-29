from pathlib import Path

import ipyvuetify as v
import solara
from reacton import ipyvuetify as rv

import json
import datetime

from glue_jupyter.app import JupyterApplication
from ...widgets.exploration_tool import ExplorationTool
from cosmicds.widgets.table import Table
from ...data_management import *
from ...state import GLOBAL_STATE
import numpy as np
from enum import Enum
from ...components import ScaffoldAlert


StepMarkers = Enum(
    "StepMarkers", ["mee_gui1", "sel_gal1", "sel_gal2", "sel_gal3", "sel_gal4"]
)


@solara.component
def Page():
    gjapp = JupyterApplication(GLOBAL_STATE.data_collection, GLOBAL_STATE.session)

    stage_step, set_stage_step = solara.use_state(0)
    total_galaxies = solara.reactive(0)

    print(type(StepMarkers.mee_gui1))

    with rv.Row():
        with rv.Col(cols=4):
            if stage_step == 0:
                with ScaffoldAlert(
                    next_callback=lambda: set_stage_step(stage_step + 1)
                ):
                    solara.Text(
                        """
                        These orange boxes will guide you as you move through 
                        the story.
                        """
                    )
                    solara.Text(
                        """
                        The information in the boxes will suggest what you 
                        should focus on, or what you should do next."""
                    )
                    solara.Text(
                        """The images, tables, or graph where the guideline 
                        suggests action will also be highlighted with an 
                        orange outline."""
                    )

        with rv.Col(cols=8):
            exploration_tool = ExplorationTool.element()

    with rv.Row():
        with rv.Col(cols=4):
            if stage_step == 1:
                with ScaffoldAlert(
                    next_callback=lambda: set_stage_step(stage_step - 1)
                ):
                    solara.Text(
                        """
                        Notice that your table now has a row for your selected galaxy, 
                        and the marker on your galaxy has changed from green to yellow.
                        """
                    )

        with rv.Col(cols=8):
            galaxy_table = Table.element(
                session=gjapp.session,
                data=None,  # gjapp.data_collection[EXAMPLE_GALAXY_DATA],
                glue_components=[
                    "id",
                    "name",
                    "ra",
                    "decl",
                    # NAME_COMPONENT,
                    # ELEMENT_COMPONENT,
                    # RESTWAVE_COMPONENT,
                    # MEASWAVE_COMPONENT,
                    # VELOCITY_COMPONENT,
                ],
                key_component=NAME_COMPONENT,
                names=[
                    "Galaxy Name",
                    "Element",
                    "&lambda;<sub>rest</sub> (&Aring;)",
                    "&lambda;<sub>obs</sub> (&Aring;)",
                ],
                title="My Galaxies",
                selected_color="#ffffff",  # self.app_state.dark_mode),
                use_subset_group=False,
                single_select=True,  # True for now
                # tools=[add_velocities_tool],
            )
