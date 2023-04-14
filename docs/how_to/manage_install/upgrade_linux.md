# Upgrade

This section explains how to upgrade the existing kernel-mode driver and ROCm
packages to the latest version. The assumption is that you already have a
version of the kernel-mode driver and the ROCm software stack is installed on
the system.

```{note}
Package upgrade is applicable to single-version packages only. If the preference
is to install an updated version of the ROCm stack along with the currently
installed version, refer to the How to [Install ROCm](./install_linux.md)
section.
```

You may use the following upgrade methods to upgrade ROCm:

- Package manager method
- Installer script method

## Package Manager Method

To upgrade the system with the desired ROCm release using the package manager
method, follow the steps below:

1. **Update the AMDGPU stack repository** – Ensure you have updated the AMDGPU
   repository.

2. **Upgrade the kernel-mode driver and reboot the system** – Ensure you have
   upgraded the kernel-mode driver and rebooted the system.

3. **Update the ROCm repository** – Ensure you have updated the ROCm repository
   with the desired ROCm release.

4. **Upgrade the ROCm meta-packages** – Upgrade the ROCm meta-packages.

5. **Verify the upgrade for the applicable distributions** – Verify if the
   upgrade is successful.

To upgrade ROCm on different Linux distributions, refer to the sections below
for specific commands.

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{rubric} Update the AMDGPU Stack Repository
::::

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
echo 'deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/amdgpu/5.4.3/ubuntu focal main' | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
echo 'deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/amdgpu/5.4.3/ubuntu jammy main' | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update
```

:::
::::

Upgrade the kernel mode driver and reboot the system using the following
commands:

```shell
sudo apt install amdgpu-dkms
sudo reboot
```

::::{rubric} Update the ROCm Stack Repository
::::

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/5.4.3 focal main" | sudo tee /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/5.4.3 jammy main" | sudo tee /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
::::

::::{rubric} Upgrade the ROCm Meta-packages
::::

Your packages can be upgraded now through their meta-packages, for example:

```shell
sudo apt install –-only-upgrade rocm-hip-sdk
```

:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{rubric} Update the AMDGPU Stack Repository
::::

::::{tab-set}
:::{tab-item} RHEL 8.6
:sync: RHEL-8.6

```shell
sudo tee --append /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
Name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/5.4.3/rhel/8.6/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo yum clean all
```

:::

:::{tab-item} RHEL 8.7
:sync: RHEL-8.7

```shell
sudo tee --append /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
Name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/5.4.3/rhel/8.7/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo yum clean all
```

:::

:::{tab-item} RHEL 9.1
:sync: RHEL-9.1

```shell
sudo tee --append /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
Name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/5.4.3/rhel/9.2/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo yum clean all
```

:::
::::

::::{rubric} Upgrade the Kernel-mode Driver and Reboot the System
::::

Upgrade the kernel mode driver and reboot the system using the following
commands:

```shell
sudo yum install amdgpu-dkms
sudo reboot
```

::::{rubric} Update the ROCm Repository
::::

```shell
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[ROCm-5.4.3]
Name=ROCm5.4.3
baseurl=https://repo.radeon.com/rocm/5.4.3/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo yum clean all
```

::::{rubric} Upgrade the ROCm Meta-packages
::::

Your packages can be upgraded now through their meta-packages, for example:

```shell
sudo apt install –-only-upgrade rocm-hip-sdk
```

:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

::::{rubric} Update the AMDGPU Stack Repository
::::

```shell
sudo tee --append /etc/zypp/repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/5.4.3/sle/15.4/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo zypper ref
```

::::{rubric} Upgrade the Kernel-mode Driver and Reboot the System
::::

Upgrade the kernel mode driver and reboot the system using the following
commands:

```shell
sudo zypper --gpg-auto-import-keys install amdgpu-dkms
sudo reboot
```

::::{rubric} Update the ROCm Stack Repository
::::

```shell
sudo tee --append /etc/zypp/repos.d/rocm.repo <<EOF
name=rocm
baseurl=https://repo.radeon.com/amdgpu/5.4.3/sle/15.4/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo zypper ref
```

::::{rubric} Upgrade the ROCm Meta-packages
::::

Your packages can be upgraded now through their meta-packages, for example:

```shell
sudo zypper --gpg-auto-import-keys update -y rocm-hip-sdk
```

:::::
::::::

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
[Installation](./install_linux.md) section.
