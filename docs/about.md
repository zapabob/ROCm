# About ROCm Documentation

ROCm documentation is made available under open source [licenses](licensing.md).
Documentation is built using open source toolchains. Contributions to our
documentation is encouraged and welcome. As a contributor, please familiarize
yourself with our documentation toolchain.

## ReadTheDocs

[ReadTheDocs](https://docs.readthedocs.io/en/stable/) is our frontend for the
our documentation. By frontend, this is the tool that serves our HTML based
documentation to our end users. We are using a paid ReadTheDocs plan. Many
projects were using the free readthedocs plan. All projects should transition to
the paid readthedocs site as this is add free. The paid site has additional
functionality including longer build times, better user monitoring and the
[rocmdoc.amd.com](https://rocmdoc.amd.com) URL. Please contact the documentation
team or devops for readthedocs access.

## Doxygen

[Doxygen](https://www.doxygen.nl/) is the most common inline code documentation
standard. ROCm projects are use Doxygen for public API documentation (unless the
upstream project is using a different tool).

## Sphinx

[Sphinx](https://www.sphinx-doc.org/en/master/) is a documentation generator
originally used for python. It is now widely used in the Open Source community.
Originally, sphinx supported rst based documentation. Markdown support is now
available. ROCm documentation plans to default to markdown for new projects.
Existing projects using rst are under no obligation to convert to markdown. New
projects that believe markdown is not suitable should contact the documentation
team prior to selecting rst.

### MyST
[Markedly Structured Text (MyST)](https://myst-tools.org/docs/spec) is an extended 
flavor of Markdown ([https://commonmark.org/](CommonMark)) influenced by ReStructured 
Text (RST) and Sphinx.
It is intergrated via [`myst-parser`](https://myst-parser.readthedocs.io/en/latest/).
A cheat sheet that showcases how to use the MyST syntax is available over at [the Jupyter
reference](https://jupyterbook.org/en/stable/reference/cheatsheet.html).

### Sphinx Theme

ROCm is using the
[Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/). This
theme is used by Jupyter books. ROCm documentation applies some customization
include a header and footer on top of the Sphinx Book Theme. A future custom
ROCm theme will be part of our documentation goals.

### Sphinx Design

Sphinx Design is an extension for sphinx based websites that add design
functionality. Please see the documentation
[here](https://sphinx-design.readthedocs.io/en/latest/index.html). ROCm
documentation uses sphinx design for grids, cards, and synchronized tabs.
Other features may be used in the future.

### Sphinx External TOC

ROCm uses the
[sphinx-external-toc](https://sphinx-external-toc.readthedocs.io/en/latest/intro.html)
for our navigation. This tool allows a yml file based left navigation menu. This
tool was selected due to its flexibility that allows scripts to operate on the
yml file. Please transition to this file for the project's navigation. You can
see the `_toc.yml.in` file in this repository in the docs/sphinx folder for an
example.

### Breathe

Sphinx uses [Breathe](https://www.breathe-doc.org/) to integrate doxygen
content.

## rocm-docs-core pip package

[rocm-docs-core](https://github.com/RadeonOpenCompute/rocm-docs-core) is an AMD
maintained project that applies customization for our documentation. This
project is the tool most ROCm repositories will use as part of the documentation
build.
