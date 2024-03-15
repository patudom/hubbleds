import dataclasses

import numpy as np
import pandas as pd
import solara
from cosmicds.widgets.table import Table
from cosmicds.components import ScaffoldAlert
from cosmicds import load_custom_vue_components
from glue_jupyter.app import JupyterApplication
from reacton import ipyvuetify as rv
from solara import Reactive
from pathlib import Path

from ...components import DataTable, SpectrumViewer
from ...data_management import *
from ...state import GLOBAL_STATE
from ...widgets.selection_tool import SelectionTool
from ...data_models.student import student_data, StudentMeasurement, example_data
from .component_state import ComponentState, Marker


GUIDELINE_ROOT = Path(__file__).parent / "guidelines"

gjapp = JupyterApplication(GLOBAL_STATE.data_collection, GLOBAL_STATE.session)

component_state = ComponentState()


def _on_galaxy_selected(state, galaxy):
    is_in = np.isin(
        [x.name for x in student_data.measurements], galaxy["name"]
    )  # Avoid duplicates
    already_present = is_in.size > 0 and is_in[0]

    if not already_present:
        filename = galaxy["name"]
        gal_type = galaxy["type"]

        print(galaxy)

        # if not self._filling_data:
        #     galaxy.pop("element")
        #
        # self.story_state.load_spectrum_data(filename, gal_type)
        # self.add_data_values(STUDENT_MEASUREMENTS_LABEL, galaxy)
        # self.stage_state.galaxy = galaxy
        student_data.measurements.append(StudentMeasurement(**galaxy))
        state.total_galaxies.value += 1


def _on_example_galaxy_table_row_selected(row):
    galaxy = row["item"]
    component_state.selected_example_galaxy.value = galaxy


@solara.component
def Page():
    # Custom vue-only components have to be registered in the Page element
    #  currently, otherwise they will not be available in the front-end
    load_custom_vue_components()

    # Solara's reactivity is often tied to the _context_ of the Page it's
    #  being rendered in. Currently, in order to trigger subscribed callbacks,
    #  state connections need to be initialized _inside_ a Page.
    component_state.setup()

    solara.Text(
        f"Current step: {component_state.current_step.value}, "
        f"Can advance: {component_state.can_transition(next=True)}"
        f"{component_state.selected_example_galaxy}"
    )

    with rv.Row():
        with rv.Col(cols=4):
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineIntro.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.mee_gui1),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineSelectGalaxies1.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.sel_gal1),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineSelectGalaxies2.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.sel_gal2),
                state_view={
                    "total_galaxies": component_state.total_galaxies.value,
                    "selected_galaxy": bool(component_state.selected_galaxy.value),
                },
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineSelectGalaxies3.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.sel_gal3),
                state_view={
                    "total_galaxies": component_state.total_galaxies.value,
                    "selected_galaxy": bool(component_state.selected_galaxy.value),
                },
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineSelectGalaxies4.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.sel_gal4),
            )

        with rv.Col(cols=8):
            # TODO: for some reason, if a component using `element` takes too
            #  long to load, it'll be inserted at the end of the page render.
            #  Wrapping in a card seems to alleviate this.
            with rv.Card(class_="pa-0 ma-0", elevation=0):
                selection_tool = SelectionTool.element(
                    table_layer_data=component_state.galaxy_data
                )

            def _define_selection_tool_callbacks():
                """Store a galaxy that has been clicked in the selection tool"""
                selection_tool_widget = solara.get_widget(selection_tool)
                selection_tool_widget.on_galaxy_selected = (
                    lambda gal: _on_galaxy_selected(component_state, gal)
                )
                selection_tool_widget.observe(
                    lambda gal: component_state.selected_galaxy.set(gal["new"]),
                    ["current_galaxy"],
                )

            solara.use_effect(_define_selection_tool_callbacks)

            def _update_selection_tool():
                """Whenever the step changes, check to see if we need to update
                the highlighting or show/hide the green dots."""
                selection_tool_widget = solara.get_widget(selection_tool)
                selection_tool_widget.show_galaxies(
                    component_state.is_current_step(Marker.sel_gal2)
                    or component_state.is_current_step(Marker.sel_gal3)
                )
                if component_state.is_current_step(
                    Marker.sel_gal2
                ) or component_state.is_current_step(Marker.sel_gal3):
                    selection_tool_widget.center_on_start_coordinates()
                selection_tool_widget.highlighted = component_state.is_current_step(
                    Marker.sel_gal2
                ) or component_state.is_current_step(Marker.sel_gal3)

            solara.use_effect(
                _update_selection_tool, [component_state.current_step.value]
            )

    with rv.Row():
        with rv.Col(cols=4):
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineNoticeGalaxyTable.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.not_gal_tab),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineChooseRow.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.cho_row1),
            )

        with rv.Col(cols=8):
            if component_state.is_current_step(
                Marker.cho_row1
            ) or component_state.is_current_step(Marker.mee_spe1):
                example_data_table = DataTable(
                    title="Example Galaxy",
                    headers=[
                        {
                            "text": "Galaxy Name",
                            "align": "start",
                            "sortable": False,
                            "value": "name",
                        },
                        {"text": "Element", "value": "element"},
                        {
                            "text": "&lambda;<sub>rest</sub> (&Aring;)",
                            "value": "rest_wave",
                        },
                        {
                            "text": "&lambda;<sub>obs</sub> (&Aring;)",
                            "value": "measured_wave",
                        },
                        {"text": "Velocity (km/s)", "value": "velocity"},
                    ],
                    items=example_data.model_dump()["measurements"],
                    highlighted=component_state.is_current_step(Marker.cho_row1),
                    event_on_row_selected=_on_example_galaxy_table_row_selected,
                )
            else:
                data_table = DataTable(
                    title="My Galaxies",
                    headers=[
                        {
                            "text": "Galaxy Name",
                            "align": "start",
                            "sortable": False,
                            "value": "name",
                        },
                        {"text": "Element", "value": "element"},
                        {
                            "text": "&lambda;<sub>rest</sub> (&Aring;)",
                            "value": "rest_wave",
                        },
                        {
                            "text": "&lambda;<sub>obs</sub> (&Aring;)",
                            "value": "measured_wave",
                        },
                        {"text": "Velocity (km/s)", "value": "velocity"},
                    ],
                    items=student_data.model_dump()["measurements"],
                    highlighted=component_state.is_current_step(Marker.not_gal_tab),
                )

    with rv.Row():
        with rv.Col(cols=4):
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineSpectrum.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.mee_spe1),
                state_view={
                    "spectrum_tutorial_opened": bool(
                        component_state.spectrum_tutorial_opened.value
                    )
                },
            )

        with rv.Col(cols=8):
            if component_state.is_current_step(Marker.mee_spe1):
                from astropy.table import Table

                df = Table(
                    {
                        "wave": np.linspace(3000, 8000, 1000),
                        "flux": np.random.sample(1000),
                    }
                ).to_pandas()
                spectrum_viewer = SpectrumViewer(df)
