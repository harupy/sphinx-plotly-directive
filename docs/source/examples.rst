.. _examples:

Examples
========

script
~~~~~~

.. plotly::

   import plotly.express as px

   px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

doctest
~~~~~~~

.. plotly::

   >>> import plotly.express as px
   >>> px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])


function
~~~~~~~~

.. plotly:: test_func.py func


fig-vars (single)
~~~~~~~~~~~~~~~~~

.. plotly::
   :fig-vars: fig1

   import plotly.express as px

   fig1 = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])


fig-vars (multiple)
~~~~~~~~~~~~~~~~~~~

.. plotly::
   :fig-vars: fig1, fig2

   import plotly.express as px

   fig1 = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
   fig2 = px.scatter(x=[4, 3, 2, 1, 0], y=[0, 1, 4, 9, 16])


Using pre-imported modules
~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the following code will be executed before running each code block. This allows to use
``np``, ``plotly``, ``go``, and `px` without importing them.

.. code-block:: python

   import numpy as np
   import plotly
   import plotly.graph_objects as go
   import plotly.express as px

.. plotly::
   :fig-vars: fig1, fig2

   x = np.arange(5)
   y = x ** 2

   title = "plotly version: {}".format(plotly.__version__)
   fig1 = go.Figure(go.Scatter(x=x, y=y), layout=dict(title=title))
   fig2 = px.scatter(x=x, y=y, title=title)
