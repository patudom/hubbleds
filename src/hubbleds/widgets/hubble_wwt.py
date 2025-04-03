from traitlets import Unicode

from ipywwt import WWTWidget


class HubbleWWTWidget(WWTWidget):

    background = Unicode(
        "Black Sky Background",
        help="The layer to show in the background (`str`)",
    ).tag(wwt=None, wwt_reset=True)

    foreground = Unicode(
        "SDSS9 color",
        help="The layer to show in the foreground (`str`)",
    ).tag(wwt=None, wwt_reset=True)