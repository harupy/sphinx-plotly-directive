fig-vars
========

Single
~~~~~~

With `fig-vars` option, you can render a plotly figure assigned in a variable.

.. plotly::
   :fig-vars: fig1

   import plotly.express as px

   fig1 = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])


Multiple
~~~~~~~~

You can specify multiple variables.

.. plotly::
   :fig-vars: fig1, fig2

   import plotly.express as px

   fig1 = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
   fig2 = px.scatter(x=[4, 3, 2, 1, 0], y=[0, 1, 4, 9, 16])
