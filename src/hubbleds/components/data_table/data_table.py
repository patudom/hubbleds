import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate


DEFAULT_HEADERS = [
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
            "value": "obs_wave",
        },
        {"text": "Velocity (km/s)", "value": "velocity"},
    ]

@solara.component_vue("DataTable.vue")
def DataTable(
    title="",
    headers=DEFAULT_HEADERS,
    items=[],
    highlighted=None,
    selected=[],
    event_on_row_selected=lambda: None,
    show_velocity_button=False,
    event_calculate_velocity=lambda: None,
):
    pass
