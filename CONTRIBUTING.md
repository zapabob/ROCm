# Contributing to ROCm Docs

AMD values and encourages the ROCm community to contribute to our code and
documentation. This repository is focused on ROCm documentation and this
contribution guide describes the recommended method for creating and modifying our
documentation.

While interacting with ROCm Documentation, we encourage you to be polite and
respectful in your contributions, content or otherwise. Authors, maintainers of
these docs act on good intentions and to the best of their knowledge.
Keep that in mind while you engage. Should you have issues with contributing
itself, refer to
[discussions](https://github.com/RadeonOpenCompute/ROCm/discussions) on the
GitHub repository.

## Supported Formats

Our documentation includes both Markdown and RST files. Markdown is encouraged
over RST due to the lower barrier to participation. GitHub flavored Markdown is preferred
for all submissions as it renders accurately on our GitHub repositories. For existing documentation,
[MyST](https://myst-parser.readthedocs.io/en/latest/intro.html) Markdown
is used to implement certain features unsupported in GitHub Markdown. This is
not encouraged for new documentation. AMD will transition
to stricter use of GitHub flavored Markdown with a few caveats. ROCm documentation
also uses [Sphinx Design](https://sphinx-design.readthedocs.io/en/latest/index.html)
in our Markdown and RST files. We also use Breathe syntax for Doxygen documentation
in our Markdown files. See
[GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github)'s
guide on writing and formatting on GitHub as a starting point.

ROCm documentation adds additional requirements to Markdown and RST based files
as follows:

- Level one headers are only used for page titles. There must be only one level
  1 header per file for both Markdown and Restructured Text.
- Pass [markdownlint](https://github.com/markdownlint/markdownlint) check via
  our automated GitHub action on a Pull Request (PR).

## Filenames and folder structure

Please use snake case (all lower case letters and underscores instead of spaces)
for file names. For example, `example_file_name.md`.
Our documentation follows pitchfork for folder structure.
All documentation is in `/docs` except for special files like
the contributing guide in the `/` folder. All images used in the documentation are
place in the /docs/data folder.

## How to provide feedback for ROCm documentation

There are three standard ways to provide feedback for this repository.

### Pull Request

All contributions to ROCm documentation should arrive via the
[GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
targetting the develop branch of the repository. If you are unable to contribute
via the GitHub Flow, feel free to email us. TODO, confirm email address.

### GitHub Issue

Issues on existing or absent docs can be filed as [GitHub issues
](https://github.com/RadeonOpenCompute/ROCm/issues).

### Email Feedback

## Language and Style

Adopt Microsoft CPP-Docs guidelines for
[Voice and Tone](https://github.com/MicrosoftDocs/cpp-docs/blob/main/styleguide/voice-tone.md).

ROCm documentation templates to be made public shortly. ROCm templates dictate
the recommended structure and flow of the documentation. Guidelines on how to
integrate figures, equations, and tables are all based off
[MyST](https://myst-parser.readthedocs.io/en/latest/intro.html).

Font size and selection, page layout, white space control, and other formatting
details are controlled via [rocm-docs-core](https://github.com/RadeonOpenCompute/rocm-docs-core).
Raise issues in `rocm-docs-core` for any formatting concerns and changes requested.

## More

For more topics, such as submitting feedback and ways to build documentation,
see the [Contributing Section](https://rocm.docs.amd.com/en/latest/contributing.html)
at [rocm.docs.amd.com](https://rocm.docs.amd.com)
