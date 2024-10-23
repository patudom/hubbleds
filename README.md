[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org)

# Hubble's Law
  A Cosmic Data Story about Hubble's Law


### Requirements
- Python-based Cosmic Data Stories now run on [solara](https://solara.dev).
- `hubbleds` requires the base [`cosmicds`](https://github.com/cosmicds/cosmicds/) to be installed.
- Developers need an API key to access the CosmicDS database. Contact the team for more information.

### Installation
- Optional but recommended, set up a new python environment.
- Install `pip` if you don't already have it.
- If you haven't already installed these packages,
```
    $ pip install solara
    $ pip install python-dotenv
```
- Pull down both the cosmicds & hubbleds repos.
- Inside the cosmicds folder in your terminal,
    `$ pip install -e .`
- Inside the hubbleds folder in your terminal,
    `$ pip install -e .`

### Running HubbleDS
Inside the hubbleds folder in your terminal,
```
    $ CDS_API_KEY="<your api key>" solara run hubbleds.pages --theme-variant dark
```

### Development Tip

If you update .css, you have to force refresh your browser (`shift-command-r` on a mac) for the changes to register.

# Legacy Code
As of 4/30/2024, the voila-based code has been moved to the [legacy](https://github.com/cosmicds/hubbleds/tree/legacy) branch.

To run the legacy code, you also need the [legacy](https://github.com/cosmicds/cosmicds/tree/legacy) branch of the cosmicds repo.

- Pull down both those branches and set up a new python environment.
- In the cosmicds directory:
    `$ pip install -e .`
- In the hubbleds directory:
    `$ pip install -e .`
- You may need to pip install any missing dependencies.
- If you have trouble installing voila, you may need to downgrade your version of `node.js` to a Long Term Support (LTS) version (14.x or 16.x).
- Open jupyter notebook and run `src/hubbleds/HubbleDS.ipynb`

or

- From the command line:
   `$ cosmicds hubble`

# Development environment

In order to keep consistency with development, this repository contains an environment file that specifies dependency versions.
You can create a conda environment using this file via

```bash
conda env create --name <env-name> --file environment.yml
```

To re-create the environment file using the packages in your current environment, you can run the `make_environment.py` script. Note that this file
will make sure that we install the `ipywwt` package from its git repository. It also removes any references to `cosmicds` and `hubbleds`, as this is supposed
to generate a development environment for the `hubbleds` package. This script only retains information about Python packages installed via pip; other conda
dependencies may differ between machines and aren't important for our purposes.


## Note
This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
