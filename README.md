# sphinx-plotly-directive

![CI](https://github.com/harupy/sphinx-plotly-directive/workflows/CI/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/sphinx-plotly-directive/badge/?version=latest)](https://sphinx-plotly-directive.readthedocs.io/en/latest/?badge=latest)

A directive for including a Plotly figure in a Sphinx document.

## Install

```bash
# pypi
pip install sphinx-plotly-directive

# dev version
pip install git+https://github.com/harupy/sphinx-plotly-directive.git
```

## How to use

#### Source:

```
.. plotly::

   import plotly.express as px
   px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
```

The last line of a code block must end with an expression that evaluates to a plotly figure.

#### Output:

<img src="https://user-images.githubusercontent.com/17039389/96469067-c3275b80-1267-11eb-89b5-4370e945ac2c.png" width="80%" />

See [documentation](https://sphinx-plotly-directive.readthedocs.io/en/latest/index.html) for details

## Development

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
