# Installation Overview (Linux)

This chapter provides an overview of ROCm™ installation.

## About This Document

This document is intended for users familiar with Linux® and discusses the
installation/uninstallation of ROCm on the various Linux distributions.

```{note}
The rest of this document refers to _Radeon™ Software for Linux_ as the AMDGPU
stack and `amdgpu-dkms` driver as the kernel-mode driver.
```

The guide provides instructions for the following:

- Kernel-mode driver installation
- ROCm single-version and multi-version installation
- ROCm and kernel-mode driver version upgrade
- ROCm single-version and multi-version uninstallation
- Kernel-mode driver uninstallation

## Installation Methods

It is customary for Linux installers to integrate into the system's package
manager. There are two notable groups of package sources:

- AMD-hosted repositories maintained by AMD available to register on supported
  Linux distribution versions. For a complete list of AMD-supported platforms,
  refer to the article: [GPU and OS Support](../release/gpu_os_support).
- Distribution-hosted repositories maintained by the developer of said Linux
  distribution. These require little to no setup from the user, but aren't tested
  by AMD. For support on these installations, contact the relevant maintainers.

AMD also provides installer scripts for those that wish to drive installations
in a more manual fashion.

## Package Licensing

```{attention}
AQL Profiler and AOCC CPU optimization are both provided in binary form, each
subject to the license agreement enclosed in the directory for the binary and is
available here: `/opt/rocm/share/doc/rocm-llvm-alt/EULA`. By using, installing,
copying or distributing AQL Profiler and/or AOCC CPU Optimizations, you agree to
the terms and conditions of this license agreement. If you do not agree to the
terms of this agreement, do not install, copy or use the AQL Profiler and/or the
AOCC CPU Optimizations.
```

Access the EULA agreement at: <https://www.amd.com/en/support/gpu-pro-eula>

For the rest of the ROCm packages, you can find the licensing information at the
following location: `/opt/rocm/share/doc/<component-name>/`

For example, you can fetch the licensing information of the `_amd_comgr_`
component (Code Object Manager) from the `amd_comgr` folder. A file named
`LICENSE.txt` contains the license details at:
`/opt/rocm-5.4.3/share/doc/amd_comgr/LICENSE.txt`

### Package Manager Integration

Integrating with the distribution's package manager let's the user install,
upgrade and uninstall using familiar commands and workflows. The actual commands
vary from distribution to distribution. For more information, refer to
[Package Manager Integration](installing_linux/package_manager_integration).

### Installer Script

The `amdgpu-install` script streamlines the installation process by:

- Abstracting the distribution-specific package installation logic
- Performing the repository setup
- Allowing you to specify the use case and automating the installation of all
  the required packages
- Installing multiple ROCm releases simultaneously on a system
- Automating updating local repository information through enhanced
  functionality of the `amdgpu-install` script
- Performing post-install checks to verify whether the installation was
  completed successfully
- Upgrading the installed ROCm release
- Uninstalling the installed single-version or multi-version ROCm releases

```{tip}
The installer script is provided for convenience. It doesn't do anything the
user otherwise couldn't. It automates some tasks surrounding installation, such
as registering/unregistering and driving the system's package manager, but the
bulk of the work will still be done by the system's package manager. As is the
case with most convenience wrappers, some degree of customization is lost for
the sake of simplicity.
```

#### Use cases

The installer script introduces the notion of "use cases", which denote usage
patterns or reasons why someone installs ROCm. This is to allow users to install
only a subset of the ROCm ecosystem, parts concerning them, resulting in
smaller installation footprint and faster installs/upgrades.

Some of the ROCm-specific use cases the installer supports are:

- OpenCL (ROCr/KFD based) runtime
- HIP runtimes
- ROCm libraries and applications
- ROCm Compiler and device libraries
- Kernel-mode driver

For more information, refer to the How to Install ROCm section in this guide.

(installation-types)=

## Installation types

This section discusses the single-version and multi-version installation of the
ROCm software stack.

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

<img src="../data/understand/installing_linux/image.001.png" alt="">

ROCm Installation Types
```
