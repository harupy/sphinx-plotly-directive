import os
import re

from setuptools import find_packages, setup


PACKAGE_NAME = "sphinx-plotly-directive"
GITHUB_REPO_URL = "https://github.com/harupy/{}".format(PACKAGE_NAME)
ROOT = os.path.abspath(os.path.dirname(__file__))


def extract_version(line):
    return re.search(r'__version__ = "(.+)"', line).group(1)


def get_version():
    version_filepath = os.path.join(ROOT, PACKAGE_NAME.replace("-", "_"), "version.py")
    with open(version_filepath) as f:
        for line in f:
            if line.startswith("__version__"):
                return extract_version(line)

    # should not reach this line
    assert False


def get_readme():
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_install_requires():

    return [
        "plotly",
        "pandas",  # required for plotly express
    ]


def get_extras_require():
    return {
        "dev": [
            # code formatting
            "flake8",
            "isort",
            "black",
            # test
            "pytest",
            # document
            "sphinx==3.0.4",
            "sphinx-rtd-theme",
        ]
    }


setup(
    name=PACKAGE_NAME,
    version=get_version(),
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=get_install_requires(),
    extras_require=get_extras_require(),
    maintainer="harupy",
    maintainer_email="hkawamura0130@gmail.com",
    url=GITHUB_REPO_URL,
    description="A directive for including a plotly figure in a Sphinx document",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
)
