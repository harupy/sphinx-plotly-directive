import re
import textwrap

import plotly


INDENT_SPACES = " " * 3


def save_plotly_figure(fig, path):
    r"""
    Save a Plotly figure.

    Parameters
    ----------
    fig : plotly figure
        A plotly figure to save.
    path : str
        A file path.

    Returns
    -------
    None

    Examples
    --------
    >>> import plotly.express as px
    >>> import tempfile
    >>> fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    >>> path = tempfile.NamedTemporaryFile(suffix=".html").name
    >>> save_plotly_figure(fig, path)
    """
    fig_html = plotly.offline.plot(fig, output_type="div", include_plotlyjs="cdn", auto_open=False)
    with open(path, "w") as f:
        f.write(fig_html)


def assign_last_line_into_variable(code, variable_name):
    r"""
    Save a Plotly figure.

    Parameters
    ----------
    code : str
        A string representing code.
    name : str
        A variable name.

    Returns
    -------
    str
        Mew code.

    Examples
    --------
    >>> code = "a = 1\nfunc(a)"
    >>> new_code = assign_last_line_into_variable(code, "b")
    >>> print(new_code)
    a = 1
    b = func(a)
    """
    lines = code.split("\n")
    for idx in range(len(lines) - 1, -1, -1):
        if lines[idx].strip() != "":
            lines[idx] = "{} = ".format(variable_name) + lines[idx]
            break
    return "\n".join(lines)


def create_directive_block(name, arguments, options, content):
    r"""
    Create a directive block.

    Parameters
    ----------
    name : str
        A directive name.
    arguments : list of str
        Arguments of the directive.
    option : dict
        Option of the directive.
    content : list of str
        Content of the directive.

    Returns
    -------
    str
        A directive block.

    Examples
    --------
    >>> block = create_directive_block(
    ...     "plotly",
    ...     ["f1", "f2"],
    ...     {"a": 0, "b": 1},
    ...     ["l1", "l2"],
    ... )
    >>> print(block)
    .. plotly:: f1 f2
       :a: 0
       :b: 1
    <BLANKLINE>
       l1
       l2
    """
    header = ".. {}:: ".format(name) + " ".join(arguments)
    code = "\n".join(map(str, content))

    lines = [header]

    if len(options.items()) > 0:

        def process_value(v):
            if isinstance(v, list):
                return ", ".join(v)
            return v

        options_block = "\n".join(":{}: {}".format(k, process_value(v)) for k, v in options.items())
        lines.append(textwrap.indent(options_block, INDENT_SPACES))

    lines.append("")
    lines.append(textwrap.indent(code, INDENT_SPACES))

    return "\n".join(lines)


def create_code_block(code, language=None):
    return "\n".join(
        [
            ".. code-block::{}".format(" " + language if language else ""),
            "",
            textwrap.indent(code.strip(), INDENT_SPACES),
            "",
        ]
    )


def strip_last_line(code):
    r"""
    Strips the last line of the give code block

    Parameters
    ----------
    code : str
        Code to strip

    Returns
    -------
    str:
        Stripped code

    Examples
    --------
    >>> strip_last_line("a")
    ''
    >>> strip_last_line("a\nb")
    'a'
    >>> strip_last_line("a\nb\nc")
    'a\nb'
    """
    return "\n".join(code.strip().split("\n")[:-1])


def ends_with_show(code):
    r"""
    Returns True if the last line of the given code block ends with `show()`

    Parameters
    ----------
    code : str
        Code that may contain a line that looks like `fig.show()`

    Returns
    -------
    str:
        Variable name of the object that calls `show()`

    Examples
    --------
    >>> ends_with_show("fig.show()")  # simple
    True
    >>> ends_with_show("fig.show(1, a=2)")  # show with arguments
    True
    >>> ends_with_show("fig = dummy\nfig.show()\n")  # multiline
    True
    >>> ends_with_show("foo")  # doesn't contains `show`
    False
    """
    # TODO: Use a more strict regular expression
    pattern = r"^(.+)\.show\(.*\)$"
    match = re.search(pattern, code.strip().split("\n")[-1], flags=re.DOTALL)
    return bool(match)
