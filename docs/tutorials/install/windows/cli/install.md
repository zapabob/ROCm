# Installation using the CLI

The steps to install the HIP SDK for Windows are described in this document.

## System requirements

The HIP SDK is supported on Windows 10 and 11. The HIP SDK may be installed on a
system without AMD GPUs to use the build toolchains. To run HIP applications, a
compatible GPU is required. Please see the supported GPU guide for more details.

## HIP SDK installation

The command-line installer is the same executable which is used by the graphical
front-end. Download the installer from the
[HIP-SDK download page](https://www.amd.com/en/developer/rocm-hub/hip-sdk.html).
The options supported by the command-line interface (CLI) are summarized in the following table.

```{table} HIP SDK Command Line Options
:name: hip-sdk-cli-install
| **Install Option** | **Description** |
|:------------------:|:---------------:|
| `-install` | Command used to install packages, both driver and applications. No output to the screen. |
| `-install -boot` | Silent install with auto reboot. |
| `-install -log <absolute path>` | Write install result code to the specified log file. The specified log file must be on a local machine. Double quotes are needed if there are spaces in the log file path. |
| `-uninstall` | Command to uninstall all packages installed by this installer on the system. There is no option to specify which packages to uninstall. |
| `-uninstall -boot` | Silent uninstall with auto reboot. |
| `/?` or /help | Shows a brief description of all switch commands. |
```

```{note}
Unlike the graphical installer, the CLI doesn't support
selectively installing parts of the SDK bundle. It's all or nothing.
```

### Launching the installer from the command line

The installer is still a graphical application with a `WinMain` entry point, even
when called on the command line. This means that the application lifetime is
tied to a window, even on headless systems where that window may not be visible.
To launch the installer from PowerShell that will block until the installer
exits, one may use the following pattern:

```pwsh
Start-Process $InstallerExecutable -ArgumentList $InstallerArgs -NoNewWindow -Wait
```

```{important}
Running the installer requires Administrator Privileges.
```

For example, installing all components and

```pwsh
Start-Process ~\Downloads\Setup.exe -ArgumentList '-install','-log',"${env:USERPROFILE}\installer_log.txt" -NoNewWindow -Wait
```
