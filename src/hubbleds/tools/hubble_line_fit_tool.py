from glue.config import viewer_tool
from numpy import isnan

from ..utils import age_in_gyr_simple
from cosmicds.tools import LineFitTool

@viewer_tool
class HubbleLineFitTool(LineFitTool):

    tool_id = 'hubble:linefit'

    def label(self, layer, line):
        slope = line.slope.value
        age = age_in_gyr_simple(slope)
        return 'H0=%.0f km/s/Mpc;  %.0f Gyr' % (slope, age) if not isnan(slope) else None

    