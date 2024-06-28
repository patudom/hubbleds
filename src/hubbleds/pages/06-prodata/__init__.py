# Stage 6 (prodata)
import solara
from hubbleds.state import LOCAL_STATE, GLOBAL_STATE
from .component_state import COMPONENT_STATE, Marker
from hubbleds.remote import LOCAL_API
from glue_jupyter import JupyterApplication
import asyncio
from pathlib import Path
from cosmicds.components import (
    ScaffoldAlert,
    LayerToggle,
    StateEditor,
    ViewerLayout
)
from reacton import ipyvuetify as rv
from hubbleds.base_component_state import (
    transition_to,
    transition_previous,
    transition_next,
)
from hubbleds.components import (
    SelectionTool,
    DataTable,
    DopplerSlideshow,
    SpectrumViewer,
    SpectrumSlideshow,
    DotplotViewer,
    ReflectVelocitySlideshow,
    DotplotTutorialSlideshow,
)

from ...viewers import HubbleFitView

from solara.lab import Ref
from cosmicds.logger import setup_logger

from ...data_management import *
# from ...state import mc_callback, mc_serialize_score, get_free_response, fr_callback
# import for type definitions
from typing import cast, Tuple

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
    loaded_component_state = solara.use_reactive(False)

    async def _load_component_state():
        # Load stored component state from database, measurement data is
        #   considered higher-level and is loaded when the story starts.
        LOCAL_API.get_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)

    logger.info("Finished loading component state.")
    loaded_component_state.set(True)

    solara.lab.use_task(_load_component_state)

    def _glue_setup() -> JupyterApplication:
        # NOTE: use_memo has to be part of the main page render. Including it
        #  in a conditional will result in an error.

        # create glue app with the global data collection and session
        gjapp = JupyterApplication(
            GLOBAL_STATE.value.glue_data_collection, GLOBAL_STATE.value.glue_session
        )

        # TODO: Should viewer creation happen somewhere else?

        # viewer = gjapp.new_data_viewer(HubbleFitView, show=False)
        # viewer.state.title = "Professional Data"
        # viewer.figure.update_xaxes(showline=True, mirror=False)
        # viewer.figure.update_yaxes(showline=True, mirror=False)
        
        # return gjapp, cast(HubbleFitView, viewer)
        return gjapp
    
    gjapp = solara.use_memo(_glue_setup)


    
    
    # # viewer.toolbar.set_tool_enabled("hubble:linefit", False)
    # component_state.add_data_by_marker(viewer)
    # component_state.show_legend(viewer, show=True)
    
    # print('\n =============  setting up mc scoring ============= \n')
    # mc_scoring, set_mc_scoring  = solara.use_state(LOCAL_STATE.mc_scoring.value)
    # print('\n =============  done setting up mc scoring ============= \n')

        
    # StateEditor(Marker, component_state)
    
    # solara.Markdown(
    #     f"""

    #     mc-scoring: {mc_scoring}  

    #     free-responses: {LOCAL_STATE.free_responses}

    #     """
    # )
    
    solara.Text(f"{GLOBAL_STATE.value.dict()}")
    solara.Text(f"{LOCAL_STATE.value.dict()}")
    solara.Text(f"{COMPONENT_STATE.value.dict()}")
    
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
            #     event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, callback=set_mc_scoring),
            #     state_view={'mc_score': mc_serialize_score(mc_scoring.get('pro-dat1')), 'score_tag': 'pro-dat1'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData2.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat2),
                # event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, callback=set_mc_scoring),
                # state_view={'mc_score': mc_serialize_score(mc_scoring.get('pro-dat2')), 'score_tag': 'pro-dat2'}
                
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData3.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat3),
                # event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, callback=set_mc_scoring),
                # state_view={'mc_score': mc_serialize_score(mc_scoring.get('pro-dat3')), 'score_tag': 'pro-dat3'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData4.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat4),
                # event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, callback=set_mc_scoring),
                # event_fr_callback=lambda event: fr_callback(event=event, local_state=LOCAL_STATE),
                # state_view={'mc_score': mc_serialize_score(mc_scoring.get('pro-dat4')), 'score_tag': 'pro-dat4',
                #             'free_response': get_free_response(LOCAL_STATE.free_responses,'prodata-free-4')
                #             }
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
                # event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, callback=set_mc_scoring),
                # state_view={
                #     'hst_age': component_state.hst_age, 
                #     'class_age': component_state.class_age.value,
                #     'mc_score': mc_serialize_score(mc_scoring.get('pro-dat6')), 
                #     'score_tag': 'pro-dat6'
                #     }
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData7.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat7),
                # event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, callback=set_mc_scoring),
                # event_fr_callback=lambda event: fr_callback(event=event, local_state=LOCAL_STATE),
                # state_view={'mc_score': mc_serialize_score(mc_scoring.get('pro-dat7')), 'score_tag': 'pro-dat7', 
                #             'free_response': get_free_response(LOCAL_STATE.free_responses,'prodata-free-7')}
                
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData8.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat8),
                # event_fr_callback=lambda event: fr_callback(event=event, local_state=LOCAL_STATE),
                # state_view={
                #     'free_response_a': get_free_response(LOCAL_STATE.free_responses,'prodata-reflect-8a'),
                #     'free_response_b': get_free_response(LOCAL_STATE.free_responses,'prodata-reflect-8b'),
                #     'free_response_c': get_free_response(LOCAL_STATE.free_responses,'prodata-reflect-8c'),
                # }
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData9.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.pro_dat9),
                # event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, callback=set_mc_scoring),
                # state_view={'mc_score': mc_serialize_score(mc_scoring.get('pro-dat9')), 'score_tag': 'pro-dat9'}
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
                    # LayerToggle(viewer)
                    with solara.Card(style="background-color: var(--error);"):
                        solara.Markdown("Layer Toggle")
                with rv.Col(class_="no-padding"):
                    # ViewerLayout(viewer)
                    with solara.Card(style="background-color: var(--error);"):
                        solara.Markdown("Hubble Viewer")
    
