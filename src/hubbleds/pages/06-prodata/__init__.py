# Stage 6 (prodata)
import solara

from cosmicds.components import ScaffoldAlert
from cosmicds import load_custom_vue_components

from cosmicds.components import LayerToggle
# from cosmicds.components import ViewerLayout
from ...components import GridViewer
from ...viewers import HubbleFitView

from glue_jupyter.app import JupyterApplication


from reacton import ipyvuetify as rv
from solara import Reactive

from pathlib import Path

from ...data_management import *
from ...state import GLOBAL_STATE, LOCAL_STATE, mc_callback
# import for type definitions
from typing import cast

from .component_state import ComponentState, Marker

# the guidelines in the current files parent directory
GUIDELINE_ROOT = Path(__file__).parent / "guidelines"

# intitialize the component state
component_state = ComponentState()



def basic_viewer_setup(viewer_class, glue_session, data_collection, name, x_att, y_att):
    viewer = viewer_class(glue_session)
    viewer.add_data(data_collection[name])
    viewer.state.x_att = x_att
    viewer.state.y_att = y_att
    return viewer

    
# create the Page for the current stage
@solara.component
def Page():
    
    # NM: Custom vue-only components have to be registered in the Page element
    #  currently, otherwise they will not be available in the front-end 
    load_custom_vue_components() # currently this just loads the ScaffoldAlert component
    
    # NM: Solara's reactivity is often tied to the _context_ of the Page it's
    #  being rendered in. Currently, in order to trigger subscribed callbacks,
    #  state connections need to be initialized _inside_ a Page.
    component_state.setup()
    
    # create glue app with the global data collection and session
    def glue_setup() -> JupyterApplication:
        gjapp = JupyterApplication(GLOBAL_STATE.data_collection, GLOBAL_STATE.session)
        return gjapp
    gjapp = cast(JupyterApplication, solara.use_memo(glue_setup,[]))
    
    #TODO: Should viewer creation happen somewhere else?
    viewer = gjapp.new_data_viewer(HubbleFitView, show=False)
    viewer.state.title = "Professional Data"
    viewer.figure.update_xaxes(showline=True, mirror=False)
    viewer.figure.update_yaxes(showline=True, mirror=False)
    # viewer.toolbar.set_tool_enabled("hubble:linefit", False)
    component_state.add_data_by_marker(viewer)
    
    mc_scoring, set_mc_scoring  = solara.use_state(LOCAL_STATE.mc_scoring.value)
        

    
    solara.Markdown(
        f"""
        Current Step: {component_state.current_step.value}

        Next step: {Marker.next(component_state.current_step.value)}

        Can advance: {component_state.can_transition(next=True)}

        mc-scoring: {mc_scoring}

        """
    )
    
    
    with solara.Row():
        with solara.Column():
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData0.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat0),
            )
            s = ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData1.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat1),
                event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, set_score=set_mc_scoring),
                state_view={'mc_score': mc_scoring.get('pro-dat1'), 'score_tag': 'pro-dat1'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData2.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat2),
                event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, set_score=set_mc_scoring),
                state_view={'mc_score': mc_scoring.get('pro-dat2'), 'score_tag': 'pro-dat2'}
                
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData3.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat3),
                event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, set_score=set_mc_scoring),
                state_view={'mc_score': mc_scoring.get('pro-dat3'), 'score_tag': 'pro-dat3'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData4.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat4),
                event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, set_score=set_mc_scoring),
                state_view={'mc_score': mc_scoring.get('pro-dat4'), 'score_tag': 'pro-dat4'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData5.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat5),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData6.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat6),
                event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, set_score=set_mc_scoring),
                state_view={
                    'hst_age': component_state.hst_age, 
                    'class_age': component_state.class_age,
                    'mc_score': mc_scoring.get('pro-dat6'), 
                    'score_tag': 'pro-dat4'
                    }
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData7.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat7),
                event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, set_score=set_mc_scoring),
                state_view={'mc_score': mc_scoring.get('pro-dat7'), 'score_tag': 'pro-dat7'}
                
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData8.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat8),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineProfessionalData9.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.pro_dat9),
                event_mc_callback=lambda event: mc_callback(event=event, local_state=LOCAL_STATE, set_score=set_mc_scoring),
                state_view={'mc_score': mc_scoring.get('pro-dat9'), 'score_tag': 'pro-dat'}
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineStoryFinish.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.sto_fin1),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineStoryFinish2.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.sto_fin2),
            )
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineStoryFinish3.vue",
                event_next_callback=lambda *args: component_state.transition_next(),
                event_back_callback=lambda *args: component_state.transition_previous(),
                can_advance=component_state.can_transition(next=True),
                show=component_state.is_current_step(Marker.sto_fin3),
            )
        
        with solara.Column():
            # TODO: LayerToggle should refresh when the data changes
            LayerToggle(viewer)
            GridViewer(viewer)
        