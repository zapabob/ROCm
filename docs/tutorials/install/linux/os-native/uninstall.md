# Uninstallation with package manager (Linux)

This section describes how to uninstall ROCm with the Linux distribution's
package manager. This method should be used if ROCm was installed via the package
manager. If the installer script was used for installation, then it should be
used for uninstallation too, refer to {doc}`../installer/uninstall`.

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{rubric} Uninstalling specific meta-packages
::::

```shell
# Uninstall single-version ROCm packages
sudo apt autoremove <package-name>
# Uninstall multi-version ROCm packages
sudo apt autoremove <package-name with release version>
```

::::{rubric} Complete uninstallation of ROCm packages
::::

```shell
# Uninstall single-version ROCm packages
sudo apt autoremove rocm-core
# Uninstall multi-version ROCm packages
sudo apt autoremove rocm-core<release version>
```

::::{rubric} Uninstall kernel-mode driver
::::

```shell
sudo apt autoremove amdgpu-dkms
```

::::{rubric} Remove ROCm and AMDGPU repositories
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

::::{rubric} Uninstalling specific meta-packages
::::

```shell
# Uninstall single-version ROCm packages
sudo yum remove <package-name>
# Uninstall multi-version ROCm packages
sudo yum remove <package-name with release version>
```

::::{rubric} Complete uninstallation of ROCm packages
::::

```shell
# Uninstall single-version ROCm packages
sudo yum remove rocm-core
# Uninstall multi-version ROCm packages
sudo yum remove rocm-core<release version>
```

::::{rubric} Uninstall kernel-mode driver
::::

```shell
sudo yum autoremove amdgpu-dkms
```

::::{rubric} Remove ROCm and AMDGPU repositories
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
:::::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

::::{rubric} Uninstalling specific meta-packages
::::

```shell
# Uninstall all single-version ROCm packages
sudo zypper remove <package-name>
# Uninstall all multi-version ROCm packages
sudo zypper remove <package-name with release version>
```

::::{rubric} Complete uninstallation of ROCm packages
::::

```shell
# Uninstall all single-version ROCm packages
sudo zypper remove rocm-core
# Uninstall all multi-version ROCm packages
sudo zypper remove rocm-core<release version>
```

::::{rubric} Uninstall kernel-mode driver
::::

```shell
sudo zypper remove --clean-deps amdgpu-dkms
```

::::{rubric} Remove ROCm and AMDGPU repositories
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
