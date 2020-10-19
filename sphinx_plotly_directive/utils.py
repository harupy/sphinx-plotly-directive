import textwrap

import plotly


INDENT_SPACES = " " * 3


def save_plotly_figure(fig, path):
    fig_html = plotly.offline.plot(fig, output_type="div", include_plotlyjs="cdn", auto_open=False)
    with open(path, "w") as f:
        f.write(fig_html)


def assign_last_line_into_variable(code, variable_name):
    *rest, last = code.strip().split("\n")
    last = "{} = ".format(variable_name) + last
    return "\n".join([*rest, last])


def create_directive_block(name, arguments, options, content):
    header = ".. {}:: ".format(name) + " ".join(arguments)
    code = "\n".join(map(str, content))

    lines = [header]

    if len(options.items()) > 0:
        options_block = "\n".join(":{}: {}".format(k, v) for k, v in options.items())
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
