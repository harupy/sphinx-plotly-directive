import os

import plotly.express as px
import pytest

from sphinx_plotly_directive.utils import (
    assign_last_line_into_variable,
    create_code_block,
    create_directive_block,
    ends_with_show,
    save_plotly_figure,
    strip_last_line,
)


def tset_save_plotly_figure(tmpdir):
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    out_path = os.path.join(tmpdir.strpath, "fig.html")
    save_plotly_figure(fig, out_path)
    assert os.path.exists(out_path)


def test_assign_last_line_into_variable():
    code = """
a = 1
a
"""
    expected = """
a = 1
b = a
"""

    assert assign_last_line_into_variable(code, "b") == expected


def test_create_directive_block():
    name = "plotly"
    arguments = ["foo", "bar"]
    options = {"a": 0, "b": 1}
    content = ["print(0)", "print(1)"]

    actual = create_directive_block(name, arguments, options, content)
    expected = """
.. plotly:: foo bar
   :a: 0
   :b: 1

   print(0)
   print(1)
""".strip()

    assert actual == expected


def test_create_code_block():
    code = """
print(0)
print(1)
""".strip()

    expected = """
.. code-block:: python

   print(0)
   print(1)
""".lstrip()

    assert create_code_block(code, "python") == expected


@pytest.mark.parametrize(
    "code, expected_result",
    [
        ("a", ""),
        ("a\nb", "a"),
        ("a\nb\nc", "a\nb"),
    ],
)
def test_strip_last_line(code, expected_result):
    assert strip_last_line(code) == expected_result


@pytest.mark.parametrize(
    "code, expected_result",
    [
        ("fig.show()", True),  # simple
        ("fig.show(1, a=2)", True),  # contains arguments
        ("fig = dummy\nfig.show()\n", True),  # multiline
        ("fig", False),  # no show
    ],
)
def test_ends_with_show(code, expected_result):
    assert ends_with_show(code) == expected_result
