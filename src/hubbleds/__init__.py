import ipyvue
from pathlib import Path
from cosmicds import STORY_PATHS
from .story import *
from .stages import *
from .tools import *
from .viewers import *
from .components import *


STORY_PATHS['hubble'] = Path(__file__).parent / "HubbleDS.ipynb"

# Register any custom Vue components
comp_dir = Path(__file__).parent / "components" / "generic_state_components"

for comp_path in comp_dir.rglob("*.vue"):
    if comp_path.is_file:
        print("REGISTERING", comp_path.stem)
        ipyvue.register_component_from_string(
            name=comp_path.stem.replace('_', '-'),
            value=comp_path.read_text())
