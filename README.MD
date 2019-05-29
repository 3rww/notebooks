# 3RWW Notebooks

*Documentation for the use of 3RWW's geo/data API services for stormwater modeling and other applications.*

## Usage

There are several ways to consume the documentation provided in this repository.

### Here on GitHub

Documentation for various 3RWW data resources is provided in subfolders. You can view those notebooks directly on GitHub.

### On `mybinder.org`

This repository has also been setup so that the notebooks can be interactively used on `mybinder.org`

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/3rww/notebooks/master). 

When you view the notebooks on `mybinder.org`, then know that is is an ephemeral, private, individual-to-you instance of the Notebook. Any edits you make or new cells you create will vanish when you close your browser. Use that space to explore a Jupyter Notebook environment with demo data & pre-loaded libraries ready for you to play with.

### On your computer

If you want to use these notebooks locally, follow the **Installation** and **Running Locally** instructions below.

## Installation

Clone this repository locally with `git`:

`git clone https://github.com/3rww/notebooks.git`

Then install dependencies using either Conda or Pip, described below.

### With Conda (recommended)

`conda create --name rainways-nbs --file requirements.txt`

This will create a new conda environment called `rainways-nbs` and install pacakges spec'd in `requirements.txt`

Alternatively, if on Windows, you can attempt to create the exact build using the conda environment file:

`conda env create -f windows.environment.yml`

...however that's probably not necessary; using `requirements.txt` is just fine.

### With Pip

`pip install -r requirements.txt`

When using Pip for local development, a `virtualenv` (e.g., via `pipenv`) is *strongly* recommended.

## Running Locally

For local development, run Jupyter from within a project virtualenv. To set up the correct Python kernel (Python 3.6+ required) with `virtualenv` packages, run the following within the `virtualenv`:

`python -m ipykernel install --user --name rainways-nbs`

After that, start Jupyter:

`python -m jupyter notebook`

From within the Notebook interface, change the kernel (`Kernel --> Change Kernel --> <name of venv>`) to use the newly created project kernel.