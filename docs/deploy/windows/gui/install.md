# Installation Using the Graphical Interface

The steps to install the HIP SDK for Windows are described in this document.

## System Requirements

The HIP SDK is supported on Windows 10 and 11. The HIP SDK may be installed on a
system without AMD GPUs to use the build toolchains. To run HIP applications, a
compatible GPU is required. Please see the supported GPU guide for more details.

## HIP SDK Installation

### Launching the installer

To launch the AMD HIP SDK Installer, click the **Setup** icon shown in
{numref}`setup-icon`.

```{figure} /data/deploy/windows/000-setup-icon.png
:name: setup-icon
:alt: Icon with AMD arrow logo and User Access Control Shield overlayed.
Setup Icon
```

The installer requires Administrator Privileges, so you may be greeted with a
User Access Control (UAC) pop-up. Click Yes.

```{figure} /data/deploy/windows/001-uac-dark.png
:name: uac-dark
:class: only-dark
:alt: User Access Control pop-up
User Access Control pop-up
```

```{figure} /data/deploy/windows/001-uac-light.png
:name: uac-light
:class: only-light
:alt: User Access Control pop-up
User Access Control pop-up
```

The installer executable will temporarily extract installer packages to `C:\AMD`
which it will remove after installation completes. This extraction is signified
by the "Initializing install" window in {numref}`init-install`.

```{figure} /data/deploy/windows/002-initializing.png
:name: init-install
:alt: Window with AMD arrow logo, futuristic background and progress counter.
Installer initialization window
```

The installer will then detect your system configuration as per
{numref}`detecting-system-components` to decide, which installable components
are applicable to your system.

```{figure} /data/deploy/windows/003-detecting-system-config.png
:name: detecting-system-components
:alt: Window with AMD arrow logo, futuristic background and activity indicator.
Installer initialization window.
```

### Customizing the install

When the installer launches, it displays a window that lets the user customize
the installation. By default, all components are selected for installation.
Refer to {numref}`installer-window` for an instance when the Select All option
is turned on.

```{figure} /data/deploy/windows/004-installer-window.png
:name: installer-window
:alt: Window with AMD arrow logo, futuristic background and activity indicator.
Installer initialization window.
```

#### HIP SDK Installer

The HIP SDK installation options are listed in {numref}`hip-sdk-options`.

```{table} HIP SDK Components for Installation
:name: hip-sdk-options
| **HIP Components** | **Install Type** | **Additional Options** |
|:------------------:|:----------------:|:----------------------:|
| HIP SDK Core         | 5.5.0               | Install location                        |
| HIP Libraries        | Full, Partial, None | Runtime, Development (Libs and headers) |
| HIP Runtime Compiler | Full, Partial, None | Runtime, Development (Headers)          |
| HIP Ray Tracing      | Full, Partial, None | Runtime, Development (Headers)          |
| Visual Studio Plugin | Full, Partial, None | Visual Studio 2017, 2019, 2022 Plugin   |
```

```{note}
The Select/DeSelect All option only applies to the installation of HIP SDK
components. To install the bundled AMD Display Driver, manually select the
install type.
```

```{tip}
Should you only wish to install a few select components,
DeSelecting All and then picking the individual components may be more
convenient.
```

#### AMD Display Driver

The HIP SDK installer bundles an AMD Radeon Software PRO 23.10 installer. The
supported install options are summarized by
{numref}`display-driver-install-options`:

```{table} AMD Display Driver Install Options
:name: display-driver-install-options
| **Install Option** | **Description** |
|:------------------:|:---------------:|
| Install Location         | Location on disk to store driver files. |
| Install Type             | The breadth of components to be installed. Refer to {numref}`display-driver-install-types` for details. |
| Factory Reset (Optional) | A Factory Reset will remove all prior versions of AMD HIP SDK and drivers. You will not be able to roll back to previously installed drivers. |
```

```{table} AMD Display Driver Install Types
:name: display-driver-install-types
| **Install Type** | **Description** |
|:----------------:|:---------------:|
| Full Install     | Provides all AMD Software features and controls for gaming, recording, streaming, and tweaking the performance on your graphics hardware. |
| Minimal Install  | Provides only the basic controls for AMD Software features and does not include advanced features such as performance tweaking or recording and capturing content. |
| Driver Only      | Provides no user interface for AMD Software features. |
```

```{note}
You must perform a system restart for a complete installation of the
Display Driver.
```

### Installing Components

Please wait for the installation to complete during as shown in
{numref}`install-progress`.

```{figure} /data/deploy/windows/012-install-progress.png
:name: install-progress
:alt: Window with AMD arrow logo, futuristic background and progress meter.
Installation Progress
```

### Installation Complete

Once the installation is complete, the installer window may prompt you for a
system restart. Click **Restart** at the lower right corner, shown in
{numref}`install-complete`

```{figure} /data/deploy/windows/013-install-complete.png
:name: install-complete
:alt: Window with AMD arrow logo, futuristic background and completion notice.
Installation Complete
```

```{error}
Should the installer terminate due to unexpcted circumstances, or the user
forcibly terminates the installer, the temporary directory created under
`C:\AMD` may be safely removed. Installed components will not depend on this
folder (unless the user specifies `C:\AMD` as an install folder explicitly).
```
