# sphinx-plotly-directive

[![pypi badge](https://img.shields.io/pypi/v/sphinx-plotly-directive?color=blue)](https://pypi.org/project/sphinx-plotly-directive/)
![CI](https://github.com/harupy/sphinx-plotly-directive/workflows/CI/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/sphinx-plotly-directive/badge/?version=latest)](https://sphinx-plotly-directive.readthedocs.io/en/latest/?badge=latest)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A directive for including a Plotly figure in a Sphinx document.

_**This package is based on [matplotlib's plot directive](https://matplotlib.org/3.1.1/devel/plot_directive.html).**_

## Install

```bash
# pypi
pip install sphinx-plotly-directive

# dev version
pip install git+https://github.com/harupy/sphinx-plotly-directive.git
```

## Usage

#### Source:

```
.. plotly::

   import plotly.express as px
   px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
```

#### Output:

<img src="https://user-images.githubusercontent.com/17039389/97077273-4278ae80-161d-11eb-89d7-9963776b7ed3.gif" width="80%" />

See [documentation](https://sphinx-plotly-directive.readthedocs.io/en/latest/index.html) for details.

## Development

### Install dependencies

```
pip install -e ".[dev]"
```

### Format code

```
flake8 .
isort .
black .
```

### Run tests

```
pytest tests
```

### Build document

```
cd docs
make html
```
