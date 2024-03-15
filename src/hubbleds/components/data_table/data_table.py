import solara
import reacton.ipyvuetify as rv
from ipyvuetify import VuetifyTemplate


@solara.component_vue("DataTable.vue")
def DataTable(title, headers, items, highlighted, event_on_row_selected):
    pass
