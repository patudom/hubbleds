import ipyvuetify as v
import solara
from reacton import ipyvuetify as rv

from ..widgets.exploration_tool import ExplorationTool

from cosmicds.layout import Layout
from cosmicds.utils import API_URL

from glue_jupyter.app import JupyterApplication

from ..state import GLOBAL_STATE


@solara.component
def Page():
    step, on_step = solara.use_state(0)

    @solara.lab.computed
    def index():
        return step + 1

    with rv.Carousel(
        v_model=step,
        on_v_model=on_step,
        value=step + 1,
        hide_delimiters=True,
        hide_delimiter_background=True,
        show_arrows=False,
        height="100%",
    ) as carousel:
        with rv.CarouselItem():
            solara.HTML(
                tag="h2",
                unsafe_innerHTML="Our Place in the Universe",
                classes=["display-1", "mb-4"],
            )

            with solara.Row():
                with solara.Column():
                    solara.Text(
                        """
                        Humans have always looked to the sky and wondered how we 
                        and our universe came to be.
                        """
                    )
                    solara.Text(
                        """
                        In this Cosmic Data Story, you will use authentic 
                        astronomical data to investigate the mysteries of our 
                        Universe. In particular, you will be answering these 
                        questions:
                        """
                    )

                    with rv.Alert(
                        text=True,
                        color="info",
                        outlined=True,
                        icon="mdi-help-circle",
                        class_="mt-4",
                    ):
                        solara.Text("Has the universe always existed?")

                    with rv.Alert(
                        text=True,
                        color="info",
                        outlined=True,
                        icon="mdi-help-circle",
                    ):
                        solara.Text("If not, how long ago did it form?")
                with solara.Column():
                    solara.Image(
                        image="/static/public/MilkyWayOverMountainsNASASTScILevay.jpg",
                    )
                    solara.Text(
                        "Our Milky Way galaxy over a mountain range. (Credit: NASA and STScI)",
                        classes=["caption"],
                        style="text-align: center",
                    )
        with rv.CarouselItem():
            solara.HTML(
                tag="h2",
                unsafe_innerHTML="Answering Questions with Data",
                classes=["display-1", "mb-4"],
            )
        with rv.CarouselItem():
            solara.HTML(
                tag="h2",
                unsafe_innerHTML="Astronomy in the Early 1900's",
                classes=["display-1", "mb-4"],
            )
        with rv.CarouselItem():
            solara.HTML(
                tag="h2",
                unsafe_innerHTML="Explore the Cosmic Sky",
                classes=["display-1", "mb-4"],
            )

            with solara.Column():
                solara.Text(
                    """
                    The frame below provides an interactive view of the night sky, 
                    using images from real observations.
                    """
                )
                solara.Text(
                    """
                    The brighter band you see going diagonally across the frame 
                    (before you try the controls) is caused by stars and dust in 
                    our home galaxy, called the Milky Way.
                    """
                )
                solara.Text(
                    """
                    You can explore this view and see what is in the night sky, as 
                    astronomers have been doing for centuries. Pan 
                    (click and drag) and zoom (scroll in and out) to see parts of 
                    the sky beyond this view."""
                )

                with solara.Columns([2, 1]):
                    with solara.Column():
                        ExplorationTool.element()
                    with solara.Column():
                        with solara.Row():
                            rv.Chip(label=True, outlined=True, children=["Pan"])
                            solara.Text("click + drag (or use I-J-K-L keys)")
                        with solara.Row():
                            rv.Chip(label=True, outlined=True, children=["Zoom"])
                            solara.Text("scroll in and out (or use Z-X keys)")

    rv.Divider(class_="mt-4")

    rv.Pagination(
        v_model=index.value,
        on_v_model=lambda i: on_step(i - 1),
        length=len(carousel.kwargs.get("children", [])),
        circle=True,
        class_="elevation-0",
        navigation_color="red",
    )
