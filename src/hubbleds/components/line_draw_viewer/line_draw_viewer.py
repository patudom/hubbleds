import reacton.ipyvuetify as rv
import solara


@solara.component_vue("LineDrawPlot.vue")
def LineDrawPlot(active,
                 fit_active=False,
                 event_line_drawn=None,
                 plot_data=None,
                 x_axis_label=None,
                 y_axis_label=None
):
    pass


@solara.component
def LineDrawViewer(plot_data=None, x_axis_label=None, y_axis_label=None):

    draw_active = solara.use_reactive(False)
    fit_active = solara.use_reactive(False)

    def on_draw_clicked():
        fit_active.set(False)
        draw_active.set(not draw_active.value)

    def on_fit_clicked():
        draw_active.set(False)
        fit_active.set(not fit_active.value) 

    # If we want to disable the tool after finishing a line draw
    # pass this function to `LineDrawPlot` as `event_line_drawn`
    # def disable(*args):
    #     active.set(False)

    with rv.Card():
        with rv.Toolbar(class_="toolbar", dense=True):
            with rv.ToolbarTitle(class_="toolbar"):
                solara.Text("LINE DRAW VIEWER")

            rv.Spacer()

            fit_button = solara.IconButton(classes=["toolbar"], icon_name="mdi-chart-timeline-variant", on_click=on_fit_clicked)
            draw_button = solara.IconButton(classes=["toolbar"], icon_name="mdi-message-draw", on_click=on_draw_clicked)
            rv.BtnToggle(v_model="selected", children=[fit_button, draw_button], background_color="primary", borderless=True)

        LineDrawPlot(active=draw_active.value,
                     fit_active=fit_active.value,
                     event_line_drawn=None,
                     plot_data=plot_data,
                     x_axis_label=x_axis_label,
                     y_axis_label=y_axis_label
        )
