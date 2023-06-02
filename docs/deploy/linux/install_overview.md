# ROCm Installation Options (Linux)

Users installing ROCm must choose between various installation options. A new
user should follow the [Quick Start guide](./quick_start).

## Distro Package Manager Commands versus AMDGPU Installer?

Users can install the same packages via two CLI interfaces as follows:

- Linux distro package manager commands.
- a proprietary installer known as the `amdgpu-install` script

There is no difference in the final installation state when choosing either CLI.

Integrating with the distribution's package manager lets the user install,
upgrade and uninstall using familiar commands and workflows. Third party
ecosystem support is the same as your OS package manager.

The `amdgpu-install` script is a wrapper around the package manager. The same
packages are installed by this script as the package manager system.

(installation-types)=

## Standard (Single Version) ROCm install versus Multi-Version

ROCm packages are versioned with both semantic versioning that is package
specific and a ROCm release version.

### Single-version Installation

The single-version ROCm installation refers to the following:

- Installation of a single instance of the ROCm release on a system
- Use of non-versioned ROCm meta-packages

### Multi-version Installation

The multi-version installation refers to the following:

- Installation of multiple instances of the ROCm stack on a system. Extending
  the package name and its dependencies with the release version adds the
  ability to support multiple versions of packages simultaneously.
- Use of versioned ROCm meta-packages.

```{note}
Multiversion install is not available for the AMDGPU stack.
```

The following image demonstrates the difference between single-version and
multi-version ROCm installation types:

```{figure-md} install-types

<img src="/data/deploy/linux/image.001.png" alt="">

ROCm Installation Types
```
