import ipyvue
from pathlib import Path
from cosmicds import STORY_PATHS
from .story import *
from .stages import *
from .tools import *
from .viewers import *
from .components import *


STORY_PATHS['hubble'] = Path(__file__).parent / "Notebook.ipynb"

# Register any custom Vue components
comp_dir = Path(__file__).parent / "components"

for comp_path in comp_dir.iterdir():
    if comp_path.is_file and comp_path.suffix == ".vue":
        ipyvue.register_component_from_string(
            name=comp_path.stem.replace('_', '-'),
            value=comp_path.read_text())
