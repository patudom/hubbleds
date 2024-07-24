import solara
from solara.toestand import Ref
import reacton.ipyvuetify as rv

# cosmicds
from cosmicds.components import (
    ScaffoldAlert,
    LayerToggle,
    StateEditor,
    ViewerLayout
)
from cosmicds.logger import setup_logger

# hubbleds
from hubbleds.remote import LOCAL_API
from hubbleds.base_component_state import (
    transition_previous,
    transition_next,
)
from hubbleds.state import (
    LOCAL_STATE, 
    GLOBAL_STATE, 
    mc_callback, 
    fr_callback, 
    get_free_response, 
    get_multiple_choice
    )

from ...utils import HST_KEY_AGE

from .component_state import COMPONENT_STATE, Marker

# glue-jupyter
from glue_jupyter import JupyterApplication
from glue.core.data_factories import load_data

# misc.
from pathlib import Path

from glue_plotly.viewers import PlotlyBaseView
from ...viewers import HubbleFitView

from typing import Tuple, cast
from ...data_management import HUBBLE_1929_DATA_LABEL, HUBBLE_KEY_DATA_LABEL

# from ...data_management import *

logger = setup_logger("STAGE")

# the guidelines in the current files parent directory
GUIDELINE_ROOT = Path(__file__).parent / "guidelines"


def basic_viewer_setup(viewer_class, glue_session, data_collection, name, x_att, y_att):
    viewer = viewer_class(glue_session)
    viewer.add_data(data_collection[name])
    viewer.state.x_att = x_att
    viewer.state.y_att = y_att
    return viewer

    
# create the Page for the current stage
@solara.component
def Page():
    # === Setup State Loading and Writing ===
    loaded_component_state = solara.use_reactive(False)
    
    async def _load_component_state():
        LOCAL_API.get_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)
        logger.info("Finished loading component state")
        loaded_component_state.set(True)
    
    solara.lab.use_task(_load_component_state)
    
    async def _write_component_state():
        if not loaded_component_state.value:
            return

        # Listen for changes in the states and write them to the database
        LOCAL_API.put_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)

        logger.info("Wrote component state to database.")

    solara.lab.use_task(_write_component_state, dependencies=[COMPONENT_STATE.value])
    
    # === Setup Glue ===
    
    def _glue_setup() -> Tuple[JupyterApplication, PlotlyBaseView]:
        # NOTE: use_memo has to be part of the main page render. Including it
        #  in a conditional will result in an error.
        gjapp = JupyterApplication(
            GLOBAL_STATE.value.glue_data_collection, GLOBAL_STATE.value.glue_session
        )
        
        
        def add_link(from_dc_name, from_att, to_dc_name, to_att):
                from_dc = gjapp.data_collection[from_dc_name]
                to_dc = gjapp.data_collection[to_dc_name]
                gjapp.add_link(from_dc, from_att, to_dc, to_att)


        data_dir = Path(__file__).parent.parent.parent / "data"
        if HUBBLE_KEY_DATA_LABEL not in gjapp.data_collection:
            gjapp.data_collection.append(load_data(data_dir / f"{HUBBLE_KEY_DATA_LABEL}.csv"))
        if HUBBLE_1929_DATA_LABEL not in gjapp.data_collection:
            gjapp.data_collection.append(load_data(data_dir / f"{HUBBLE_1929_DATA_LABEL}.csv"))

        add_link(HUBBLE_1929_DATA_LABEL, 'Distance (Mpc)', HUBBLE_KEY_DATA_LABEL, 'Distance (Mpc)')
        add_link(HUBBLE_1929_DATA_LABEL, 'Tweaked Velocity (km/s)', HUBBLE_KEY_DATA_LABEL, 'Velocity (km/s)')

        viewer = cast(PlotlyBaseView, gjapp.new_data_viewer(HubbleFitView, show=False))
        viewer.state.title = "Professional Data"
        viewer.figure.update_xaxes(showline=True, mirror=False)
        viewer.figure.update_yaxes(showline=True, mirror=False)
        
        return gjapp, viewer
    
    

    gjapp, viewer = solara.use_memo(_glue_setup)

    def _state_callback_setup():
        # We want to minimize duplicate state handling, but also keep the states
        #  independent. We'll set up observers for changes here so that they
        #  automatically keep the states in sync.
        # See Stage 1 for an example of how to do this manually.
        pass

    solara.use_memo(_state_callback_setup)    
    
    
    def add_data_by_marker(viewer):
        
        if COMPONENT_STATE.value.current_step.value == Marker.pro_dat1.value:
            data = gjapp.data_collection[HUBBLE_1929_DATA_LABEL]
            if data not in viewer.state.layers_data:
                print('adding Hubble 1929')
                data.style.markersize = 10
                data.style.color = '#D500F9'
                viewer.add_data(data)
                viewer.state.x_att = data.id['Distance (Mpc)']
                viewer.state.y_att = data.id['Tweaked Velocity (km/s)']
                
        if COMPONENT_STATE.value.current_step.value == Marker.pro_dat5.value:
            data = gjapp.data_collection[HUBBLE_KEY_DATA_LABEL]
            if data not in viewer.state.layers_data:
                print('adding HST key')
                data.style.markersize = 10
                data.style.color = '#AEEA00'
                viewer.add_data(data)
                viewer.state.x_att = data.id['Distance (Mpc)']
                viewer.state.y_att = data.id['Velocity (km/s)']
        
        viewer.state.reset_limits()
    
    def show_legend(viewer, show=True):
        layout_update = {"showlegend": show}
        if show:
            layout_update["legend"] = {
                'yanchor': 'top',
                'xanchor': 'left',
                "y": 0.99,
                "x": 0.01
            }
        viewer.figure.update_layout(**layout_update)
        return

    def legend_hide_layer_traces(viewer):
        for layer in viewer.layers:
            for trace in layer.traces():
                trace.update(showlegend=False)

    # viewer.toolbar.set_tool_enabled("hubble:linefit", False)
    add_data_by_marker(viewer)
    legend_hide_layer_traces(viewer)
    show_legend(viewer, show=True)
    
    # print('\n =============  setting up mc scoring ============= \n')
    # mc_scoring, set_mc_scoring  = solara.use_state(LOCAL_STATE.mc_scoring.value)
    # print('\n =============  done setting up mc scoring ============= \n')

    StateEditor(Marker, COMPONENT_STATE, LOCAL_STATE, LOCAL_API)

    # with solara.Card():
    #     with solara.Div():
    #         solara.Text(f"mc_scoring: {LOCAL_STATE.value.mc_scoring}")
    #     with solara.Div():
    #         solara.Text(f"free_responses: {LOCAL_STATE.value.free_responses}")
    

    with solara.ColumnsResponsive(12, large=[4,8]):
        with rv.Col():
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData0.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat0),
            )
            s = ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData1.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat1),
                event_mc_callback = lambda event: mc_callback(event, LOCAL_STATE),
                state_view={'mc_score': get_multiple_choice(LOCAL_STATE, 'pro-dat1'), 'score_tag': 'pro-dat1'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData2.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat2),
                event_mc_callback = lambda event: mc_callback(event, LOCAL_STATE),
                state_view={'mc_score': get_multiple_choice(LOCAL_STATE, 'pro-dat2'), 'score_tag': 'pro-dat2'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData3.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat3),
                event_mc_callback = lambda event: mc_callback(event, LOCAL_STATE),
                state_view={'mc_score': get_multiple_choice(LOCAL_STATE, 'pro-dat3'), 'score_tag': 'pro-dat3'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData4.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat4),
                event_mc_callback = lambda event: mc_callback(event, LOCAL_STATE),
                event_fr_callback = lambda event: fr_callback(event, LOCAL_STATE, lambda: LOCAL_API.put_story_state(GLOBAL_STATE, LOCAL_STATE)),
                state_view={
                    'mc_score': get_multiple_choice(LOCAL_STATE, 'pro-dat4'), 
                    'score_tag': 'pro-dat4',
                    'free_response': get_free_response(LOCAL_STATE, 'prodata-free-4'),
                    'mc_completed': LOCAL_STATE.value.question_completed("pro-dat4"),
                }
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData5.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat5),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData6.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat6),
                event_mc_callback = lambda event: mc_callback(event, LOCAL_STATE),
                state_view={
                    'hst_age': HST_KEY_AGE, 
                    'class_age': COMPONENT_STATE.value.class_age,
                    'mc_score': get_multiple_choice(LOCAL_STATE, 'pro-dat6'), 
                    'score_tag': 'pro-dat6'
                }
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData7.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat7),
                event_mc_callback = lambda event: mc_callback(event, LOCAL_STATE),
                event_fr_callback = lambda event: fr_callback(event, LOCAL_STATE, lambda: LOCAL_API.put_story_state(GLOBAL_STATE, LOCAL_STATE)),
                state_view={
                    'mc_score': get_multiple_choice(LOCAL_STATE, 'pro-dat7'), 
                    'score_tag': 'pro-dat7',
                    'free_response': get_free_response(LOCAL_STATE, 'prodata-free-7'),
                    'mc_completed': LOCAL_STATE.value.question_completed("pro-dat7"),
                }                
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData8.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat8),
                event_fr_callback = lambda event: fr_callback(event, LOCAL_STATE, lambda: LOCAL_API.put_story_state(GLOBAL_STATE, LOCAL_STATE)),
                state_view={
                    'free_response_a': get_free_response(LOCAL_STATE,'prodata-reflect-8a'),
                    'free_response_b': get_free_response(LOCAL_STATE,'prodata-reflect-8b'),
                    'free_response_c': get_free_response(LOCAL_STATE,'prodata-reflect-8c'),
                }
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData9.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat9),
                event_mc_callback = lambda event: mc_callback(event, LOCAL_STATE),
                state_view={'mc_score': get_multiple_choice(LOCAL_STATE, 'pro-dat9'), 'score_tag': 'pro-dat9'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineStoryFinish.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.sto_fin1),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineStoryFinish2.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.sto_fin2),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineStoryFinish3.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.sto_fin3),
            )
        
        with rv.Col(class_="no-padding"):
            with solara.Columns([3,9], classes=["no-padding"]):
                with rv.Col(class_="no-padding"):
                    # TODO: LayerToggle should refresh when the data changes
                    LayerToggle(viewer)
                    with solara.Card(style="background-color: var(--error);"):
                        solara.Markdown("Layer Toggle")
                with rv.Col(class_="no-padding"):
                    ViewerLayout(viewer)
                    with solara.Card(style="background-color: var(--error);"):
                        solara.Markdown("Hubble Viewer")
