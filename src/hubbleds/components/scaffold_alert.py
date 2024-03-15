import solara
import reacton.ipyvuetify as rv


@solara.component
def ScaffoldAlert(
    children=[],
    title=None,
    info_text=None,
    next_callback=None,
    back_callback=None,
    show=True,
):
    if not show:
        return

    with rv.Card(outlined=True, color="deep-orange darken-2"):
        if title is not None:
            with rv.CardTitle(children=title):
                pass

        with rv.CardText():
            with solara.Row():
                with solara.Column(children=children):
                    pass

        rv.Divider()

        with rv.CardActions():
            if back_callback is not None:
                solara.Button("Back", on_click=back_callback)

            solara.IconButton(icon_name="mdi-account-voice")

            if info_text is not None:
                rv.Divider(vertical=True, style_="border-width: 2px", class_="mx-2")

                class _InternalVueWidget(vue.VueTemplate):
                    @traitlets.default("template")
                    def _template(self):
                        return f"""
                            <template>
                                <span style='font-size: 14px'>{info_text}</span>
                            </template>
                        """

                _InternalVueWidget.element()

            if next_callback is not None:
                rv.Spacer()
                solara.Button("Next", on_click=next_callback)
