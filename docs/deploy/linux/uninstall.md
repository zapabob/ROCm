# Uninstallation (Linux)

Uninstallation of ROCm entails removing ROCm packages, tools, and libraries from
the system.

You can uninstall using the following methods:

- Package manager uninstallation
- Uninstallation using the uninstall script

```{attention}
Use the same uninstall method that you used to install ROCm. Mixing procedures
is untested and may result in inconsistent system state.
```

## Package Manager Method

The package manager uninstallation offers a method for a clean uninstallation
process for ROCm. This section describes how to uninstall the ROCm instance from
various Linux distributions.

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{rubric} Uninstalling Specific Meta-packages
::::

```shell
# Uninstall single-version ROCm packages
sudo apt autoremove <package-name>
# Uninstall multiversion ROCm packages
sudo apt autoremove <package-name with release version>
```

::::{rubric} Complete Uninstallation of ROCm Packages
::::

```shell
# Uninstall single-version ROCm packages
sudo apt autoremove rocm-core
# Uninstall multiversion ROCm packages
sudo apt autoremove rocm-core<release version>
```

::::{rubric} Uninstall Kernel-mode Driver
::::

```shell
sudo apt autoremove amdgpu-dkms
```

::::{rubric} Remove ROCm and AMDGPU Repositories
::::

1. Execute these commands:

   ```shell
   sudo rm /etc/apt/sources.list.d/<rocm_repository-name>.list
   sudo rm /etc/apt/sources.list.d/<amdgpu_repository-name>.list
   ```

2. Clear the cache and clean the system.

   ```shell
   sudo rm -rf /var/cache/apt/*
   sudo apt-get clean all
   ```

3. Restart the system.

   ```shell
   sudo reboot
   ```

:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{rubric} Uninstalling Specific Meta-packages
::::

```shell
# Uninstall single-version ROCm packages
sudo yum remove <package-name>
# Uninstall multiversion ROCm packages
sudo yum remove <package-name with release version>
```

::::{rubric} Complete Uninstallation of ROCm Packages
::::

```shell
# Uninstall single-version ROCm packages
sudo yum remove rocm-core
# Uninstall multiversion ROCm packages
sudo yum remove rocm-core<release version>
```

::::{rubric} Uninstall Kernel-mode Driver
::::

```shell
sudo yum autoremove amdgpu-dkms
```

::::{rubric} Remove ROCm and AMDGPU Repositories
::::

1. Execute these commands:

   ```shell
   sudo rm -rf /etc/yum.repos.d/<rocm_repository-name> # Remove only rocm repo
   sudo rm -rf /etc/yum.repos.d/<amdgpu_repository-name> # Remove only amdgpu repo
   ```

2. Clear the cache and clean the system.

   ```shell
   sudo rm -rf /var/cache/yum #Remove the cache
   sudo yum clean all
   ```

3. Restart the system.

   ```shell
   sudo reboot
   ```

:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

::::{rubric} Uninstalling Specific Meta-packages
::::

```shell
# Uninstall all single-version ROCm packages
sudo zypper remove <package-name>
# Uninstall all multiversion ROCm packages
sudo zypper remove <package-name with release version>
```

::::{rubric} Complete Uninstallation of ROCm Packages
::::

```shell
# Uninstall all single-version ROCm packages
sudo zypper remove rocm-core
# Uninstall all multiversion ROCm packages
sudo zypper remove rocm-core<release version>
```

::::{rubric} Uninstall Kernel-mode Driver
::::

```shell
sudo zypper remove --clean-deps amdgpu-dkms
```

::::{rubric} Remove ROCm and AMDGPU Repositories
::::

1. Execute these commands:

   ```shell
   sudo zypper removerepo <rocm_repository-name>
   sudo zypper removerepo <amdgpu_repository-name>
   ```

2. Clear the cache and clean the system.

   ```shell
   sudo zypper clean --all
   ```

3. Restart the system.

   ```shell
   sudo reboot
   ```

:::::
::::::

## Installer Script Method

::::{rubric} Uninstalling Single-Version Install
::::

```console shell
sudo amdgpu-install --uninstall
```

```{note}
This command uninstalls all ROCm packages associated with the installed ROCm
release along with the kernel-mode driver.
```

::::{rubric} Uninstalling a Specific ROCm Release
::::

```console shell
sudo amdgpu-install --uninstall --rocmrelease=<release-number>
```

::::{rubric} Uninstalling all ROCm Releases
::::

```console shell
sudo amdgpu-install --uninstall --rocmrelease=all
```
