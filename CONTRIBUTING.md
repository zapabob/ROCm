# Contributing to ROCm Docs

AMD values and encourages the ROCm community to contribute to our code and
documentation. This repository is focused on ROCm documentation and this
contribution guide describes the recommend method for creating and modifying our
documentation.

While interacting with ROCm Documentation, we encourage you to be polite and
respectful in your contributions, content or otherwise. Authors, maintainers of
these docs act on good intentions and to the best of their knowledge.
Keep that in mind while you engage. Should you have issues with contributing
itself, refer to
[discussions](https://github.com/RadeonOpenCompute/ROCm/discussions) on the
GitHub repository.

## Supported Formats

Our documentation includes both markdown and rst files. Markdown is encouraged
over rst due to the lower barrier to participation. GitHub flavored markdown is preferred
for all submissions as it will render accurately on our GitHub repositories. For existing documentation,
[MyST](https://myst-parser.readthedocs.io/en/latest/intro.html) markdown
is used to implement certain features unsupported in GitHub markdown. This is
not encouraged for new documentation. AMD will transition
to stricter use of GitHub flavored markdown with a few caveats. ROCm documentation
also uses [sphinx-design](https://sphinx-design.readthedocs.io/en/latest/index.html)
in our markdown and rst files. We also will use breathe syntax for doxygen documentation
in our markdown files. Other design elements for effective HTML rendering of the documents
may be added to our markdown files. Please see
[GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github)'s
guide on writing and formatting on GitHub as a starting point.

ROCm documentation adds additional requirements to markdown and rst based files
as follows:

- Level one headers are only used for page titles. There must be only one level
  1 header per file for both Markdown and Restructured Text.
- Pass [markdownlint](https://github.com/markdownlint/markdownlint) check via
  our automated github action on a Pull Request (PR).

## Filenames and folder structure

Please use snake case for file names. Our documentation follows pitchfork for
folder structure. All documentation is in /docs except for special files like
the contributing guide in the / folder. All images used in the documentation are
place in the /docs/data folder.

## How to provide feedback for for ROCm documentation

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

Adopting Microsoft CPP-Docs guidelines for [Voice and Tone
](https://github.com/MicrosoftDocs/cpp-docs/blob/main/styleguide/voice-tone.md).

ROCm documentation templates to be made public shortly. ROCm templates dictate
the recommended structure and flow of the documentation. Guidelines on how to
integrate figures, equations, and tables are all based off
[MyST](https://myst-parser.readthedocs.io/en/latest/intro.html).

Font size and selection, page layout, white space control, and other formatting
details are controlled via rocm-docs-core, sphinx extention. Please raise issues
in rocm-docs-core for any formatting concerns and changes requested.

## Building Documentation

While contributing, one may build the documentation locally on the command-line
or rely on Continuous Integration for previewing the resulting HTML pages in a
browser.

### Command line documentation builds

Python versions known to build documentation:

- 3.8

To build the docs locally using Python Virtual Environment (`venv`), execute the
following commands from the project root:

```sh
python3 -mvenv .venv
# Windows
.venv/Scripts/python -m pip install -r docs/sphinx/requirements.txt
.venv/Scripts/python -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html
# Linux
.venv/bin/python     -m pip install -r docs/sphinx/requirements.txt
.venv/bin/python     -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html
```

Then open up `_build/html/index.html` in your favorite browser.

### Pull Requests documentation builds

When opening a PR to the `develop` branch on GitHub, the page corresponding to
the PR (`https://github.com/RadeonOpenCompute/ROCm/pull/<pr_number>`) will have
a summary at the bottom. This requires the user be logged in to GitHub.

- There, click `Show all checks` and `Details` of the Read the Docs pipeline. It
  will take you to `https://readthedocs.com/projects/advanced-micro-devices-rocm/
  builds/<some_build_num>/`
  - The list of commands shown are the exact ones used by CI to produce a render
    of the documentation.
- There, click on the small blue link `View docs` (which is not the same as the
  bigger button with the same text). It will take you to the built HTML site with
  a URL of the form `https://
  advanced-micro-devices-demo--<pr_number>.com.readthedocs.build/projects/alpha/en
  /<pr_number>/`.

### Build the docs using VS Code

One can put together a productive environment to author documentation and also
test it locally using VS Code with only a handful of extensions. Even though the
extension landscape of VS Code is ever changing, here is one example setup that
proved useful at the time of writing. In it, one can change/add content, build a
new version of the docs using a single VS Code Task (or hotkey), see all errors/
warnings emitted by Sphinx in the Problems pane and immediately see the
resulting website show up on a locally serving web server.

#### Configuring VS Code

1. Install the following extensions:

    - Python (ms-python.python)
    - Live Server (ritwickdey.LiveServer)

2. Add the following entries in `.vscode/settings.json`

    ```json
    {
      "liveServer.settings.root": "/.vscode/build/html",
      "liveServer.settings.wait": 1000,
      "python.terminal.activateEnvInCurrentTerminal": true
    }
    ```

    The settings in order are set for the following reasons:
    - Sets the root of the output website for live previews. Must be changed
      alongside the `tasks.json` command.
    - Tells live server to wait with the update to give time for Sphinx to
      regenerate site contents and not refresh before all is don. (Empirical value)
    - Automatic virtual env activation is a nice touch, should you want to build
      the site from the integrated terminal.

3. Add the following tasks in `.vscode/tasks.json`

    ```json
    {
      "version": "2.0.0",
      "tasks": [
        {
          "label": "Build Docs",
          "type": "process",
          "windows": {
            "command": "${workspaceFolder}/.venv/Scripts/python.exe"
          },
          "command": "${workspaceFolder}/.venv/bin/python3",
          "args": [
            "-m",
            "sphinx",
            "-j",
            "auto",
            "-T",
            "-b",
            "html",
            "-d",
            "${workspaceFolder}/.vscode/build/doctrees",
            "-D",
            "language=en",
            "${workspaceFolder}/docs",
            "${workspaceFolder}/.vscode/build/html"
          ],
          "problemMatcher": [
            {
              "owner": "sphinx",
              "fileLocation": "absolute",
              "pattern": {
                "regexp": "^(?:.*\\.{3}\\s+)?(\\/[^:]*|[a-zA-Z]:\\\\[^:]*):(\\d+):\\s+(WARNING|ERROR):\\s+(.*)$",
                "file": 1,
                "line": 2,
                "severity": 3,
                "message": 4
              },
            },
            {
              "owner": "sphinx",
              "fileLocation": "absolute",
              "pattern": {
                "regexp": "^(?:.*\\.{3}\\s+)?(\\/[^:]*|[a-zA-Z]:\\\\[^:]*):{1,2}\\s+(WARNING|ERROR):\\s+(.*)$",
                "file": 1,
                "severity": 2,
                "message": 3
              }
            }
          ],
          "group": {
            "kind": "build",
            "isDefault": true
          }
        },
      ],
    }
    ```

    > (Implementation detail: two problem matchers were needed to be defined,
    > because VS Code doesn't tolerate some problem information being potentially
    > absent. While a single regex could match all types of errors, if a capture
    > group remains empty (the line number doesn't show up in all warning/error
    > messages) but the `pattern` references said empty capture group, VS Code
    > discards the message completely.)

4. Configure Python virtual environment (venv)

    - From the Command Palette, run `Python: Create Environment`
      - Select `venv` environment and the `docs/sphinx/requirements.txt` file.
      _(Simply pressing enter while hovering over the file from the dropdown is
      insufficient, one has to select the radio button with the 'Space' key if
      using the keyboard.)_

5. Build the docs

    - Launch the default build Task using either:
      - a hotkey _(default is 'Ctrl+Shift+B')_ or
      - by issuing the `Tasks: Run Build Task` from the Command Palette.

6. Open the live preview

    - Navigate to the output of the site within VS Code, right-click on
    `.vscode/build/html/index.html` and select `Open with Live Server`. The
    contents should update on every rebuild without having to refresh the
    browser.

<!-- markdownlint-restore -->
