iframe-size
===========

.. plotly::
   :iframe-width: 500px
   :iframe-height: 300px

   import plotly.express as px

   px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])


You can set the default ``iframe-width`` and ``iframe-height`` by specifying ``plotly_iframe_width`` (default: ``"100%"``) and ``plotly_iframe_height`` (default: ``"500px"``) in ``conf.py``.

.. code-block:: python

   # conf.py

   plotly_iframe_width = "500px"
   plotly_iframe_height = "300px"
