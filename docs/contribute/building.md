# Building documentation

While contributing, one may build the documentation locally on the command line
or rely on Continuous Integration for previewing the resulting HTML pages in a
browser.

## Pull request documentation builds

When opening a PR to the `develop` branch on GitHub, the page corresponding to
the PR (`https://github.com/RadeonOpenCompute/ROCm/pull/<pr_number>`) will have
a summary at the bottom. This requires the user be logged in to GitHub.

* There, click `Show all checks` and `Details` of the Read the Docs pipeline. It
  will take you to a URL of the form
  `https://readthedocs.com/projects/advanced-micro-devices-rocm/builds/<some_build_num>/`
  * The list of commands shown are the exact ones used by CI to produce a render
    of the documentation.
* There, click on the small blue link `View docs` (which is not the same as the
  bigger button with the same text). It will take you to the built HTML site with
  a URL of the form
  `https://advanced-micro-devices-demo--<pr_number>.com.readthedocs.build/projects/alpha/en/<pr_number>/`.

## Build documentation from the command line

Python versions known to build documentation:

* 3.8

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

## Build documentation using Visual Studio Code

One can put together a productive environment to author documentation and also
test it locally using Visual Studio (VS) Code with only a handful of extensions. Even though the
extension landscape of VS Code is ever changing, here is one example setup that
proved useful at the time of writing. In it, one can change/add content, build a
new version of the docs using a single VS Code Task (or hotkey), see all errors/
warnings emitted by Sphinx in the Problems pane and immediately see the
resulting website show up on a locally-served web server.

### Configuring VS Code

1. Install the following extensions:
   * Python `(ms-python.python)`
   * Live Server `(ritwickdey.LiveServer)`

2. Add the following entries in `.vscode/settings.json`

    ```json
    {
      "liveServer.settings.root": "/.vscode/build/html",
      "liveServer.settings.wait": 1000,
      "python.terminal.activateEnvInCurrentTerminal": true
    }
    ```

    The settings above are used for the following reasons:
    * `liveServer.settings.root`: Sets the root of the output website for live previews. Must be changed
      alongside the `tasks.json` command.
    * `liveServer.settings.wait`: Tells live server to wait with the update to give time for Sphinx to
      regenerate site contents and not refresh before all is done. (Empirical value)
    * `python.terminal.activateEnvInCurrentTerminal`: Automatic virtual environment activation is a nice touch,
      should you want to build the site from the integrated terminal.

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

4. Configure Python virtual environment (`venv`)

    * From the Command Palette, run `Python: Create Environment`
      * Select `venv` environment and the `docs/sphinx/requirements.txt` file.
      _(Simply pressing enter while hovering over the file from the drop down is
      insufficient, one has to select the radio button with the 'Space' key if
      using the keyboard.)_

5. Build the docs

    * Launch the default build Task using either:
      * a hotkey _(default is `Ctrl+Shift+B`)_ or
      * by issuing the `Tasks: Run Build Task` from the Command Palette.

6. Open the live preview

    * Navigate to the output of the site within VS Code, right-click on
    `.vscode/build/html/index.html` and select `Open with Live Server`. The
    contents should update on every rebuild without having to refresh the
    browser.
