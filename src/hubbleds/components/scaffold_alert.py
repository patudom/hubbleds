import solara
import reacton.ipyvuetify as rv


@solara.component
def ScaffoldAlert(children=[], title=None, next_callback=lambda: None):
    with rv.Card(outlined=True, color="deep-orange darken-2"):
        if title is not None:
            with rv.CardTitle(children=title):
                pass

        with rv.CardText():
            with solara.Column(children=children):
                pass

        rv.Divider()

        with rv.CardActions():
            rv.Btn(icon_name="mdi-account-voice", icon=True)
            rv.Spacer()
            solara.Button("Next", on_click=next_callback)
