
precode
=======

By default, the following code will be executed before running each code block. This allows to use
``np``, ``plotly``, ``go``, and ``px`` without importing them.

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
