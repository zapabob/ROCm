<head>
  <meta charset="UTF-8">
  <meta name="description" content="ROCm documentation toolchain">
  <meta name="keywords" content="documentation, toolchain, Sphinx, Doxygen, MyST">
</head>

# ROCm documentation toolchain

Our documentation relies on several open source toolchains and sites.

## `rocm-docs-core`

[rocm-docs-core](https://github.com/RadeonOpenCompute/rocm-docs-core) is an AMD-maintained
project that applies customization for our documentation. This
project is the tool most ROCm repositories use as part of the documentation
build. It is also available as a [pip package on PyPI](https://pypi.org/project/rocm-docs-core/).

See the user and developer guides for rocm-docs-core at {doc}`rocm-docs-core documentation<rocm-docs-core:index>`.

## Sphinx

[Sphinx](https://www.sphinx-doc.org/en/master/) is a documentation generator
originally used for Python. It is now widely used in the open source community.
Originally, Sphinx supported reStructuredText (RST) based documentation, but
Markdown support is now available.
ROCm documentation plans to default to Markdown for new projects.
Existing projects using RST are under no obligation to convert to Markdown. New
projects that believe Markdown is not suitable should contact the documentation
team prior to selecting RST.

## Read the Docs

[Read the Docs](https://docs.readthedocs.io/en/stable/) is the service that builds
and hosts the HTML documentation generated using Sphinx to our end users.

## Doxygen

[Doxygen](https://www.doxygen.nl/) is a documentation generator that extracts
information from inline code.
ROCm projects typically use Doxygen for public API documentation unless the
upstream project uses a different tool.

### Breathe

[Breathe](https://www.breathe-doc.org/) is a Sphinx plugin to integrate Doxygen
content.

### MyST

[Markedly Structured Text (MyST)](https://myst-tools.org/docs/spec) is an extended
flavor of Markdown ([CommonMark](https://commonmark.org/)) influenced by reStructuredText (RST) and Sphinx.
It is integrated into ROCm documentation by the Sphinx extension [`myst-parser`](https://myst-parser.readthedocs.io/en/latest/).
A cheat sheet that showcases how to use the MyST syntax is available over at
the [Jupyter reference](https://jupyterbook.org/en/stable/reference/cheatsheet.html).

### Sphinx External ToC

[Sphinx External ToC](https://sphinx-external-toc.readthedocs.io/en/latest/intro.html)
is a Sphinx extension used for ROCm documentation navigation. This tool generates a navigation menu on the left
based on a YAML file that specifies the table of contents.
It was selected due to its flexibility that allows scripts to operate on the
YAML file. Please transition to this file for the project's navigation. You can
see the `_toc.yml.in` file in this repository in the `docs/sphinx` folder for an
example.

### Sphinx-book-theme

[Sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/en/latest/) is a Sphinx theme
that defines the base appearance for ROCm documentation.
ROCm documentation applies some customization,
such as a custom header and footer on top of the Sphinx Book Theme.

### Sphinx design

[Sphinx design](https://sphinx-design.readthedocs.io/en/latest/index.html) is a Sphinx extension that adds design
functionality.
ROCm documentation uses Sphinx Design for grids, cards, and synchronized tabs.
