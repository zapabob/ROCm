# Upgrading with the Installer Script (Linux)

This section explains how to upgrade the existing kernel-mode driver and ROCm
packages to the latest version. The assumption is that you already have a
version of the kernel-mode driver and the ROCm software stack is installed on
the system.

```{note}
Package upgrade is applicable to single-version packages only. If the preference
is to install an updated version of the ROCm stack along with the currently
installed version, refer to the [](install) page.
```

## Installer Script Method

The installer script method automates the upgrade process for the AMDGPU and
ROCm stack. The `amdgpu-install` script handles the complete upgrade process for
ROCm, including updating the required repositories and upgrading the desired
meta-packages.

The upgrade procedure is exactly the same as installing for 1st time use. Refer
to the {ref}`install-script-method` section on the exact procedure to follow.

## Verification Process

To verify if the upgrade is successful, refer to the
{ref}`post-install-actions-linux` given in the
[Installation](install) section.
