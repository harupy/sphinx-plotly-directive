show
====

.. plotly::

   import plotly.express as px

   fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
   fig.show()


.. plotly::
   :fig-vars: figure

   import plotly.express as px

   figure = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
   figure.show()
