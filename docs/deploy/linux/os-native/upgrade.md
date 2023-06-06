# Upgrade ROCm with the package manager

This section explains how to upgrade the existing AMDGPU driver and ROCm
packages to the latest version using your OS's distributed package manager.

```{note}
Package upgrade is applicable to single-version packages only. If the preference
is to install an updated version of the ROCm along with the currently
installed version, refer to the [](install) page.
```

## Upgrade Steps

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{rubric} Update the AMDGPU Repository
::::

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
echo 'deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/amdgpu/5.5.1/ubuntu focal main' | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
echo 'deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/amdgpu/5.5.1/ubuntu jammy main' | sudo tee /etc/apt/sources.list.d/amdgpu.list
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

::::{rubric} Update the ROCm Repository
::::

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/5.5.1 focal main" | sudo tee /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/5.5.1 jammy main" | sudo tee /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
::::

::::{rubric} Upgrade the ROCm meta-packages
::::

Your packages can be upgraded now through their meta-packages, for example:

```shell
sudo apt install --only-upgrade rocm-hip-sdk
```

:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{rubric} Update the AMDGPU repository
::::

::::{tab-set}
:::{tab-item} RHEL 8.6
:sync: RHEL-8.6

```shell
sudo tee --append /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
Name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/5.5.1/rhel/8.6/main/x86_64/
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
baseurl=https://repo.radeon.com/amdgpu/5.5.1/rhel/8.7/main/x86_64/
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
baseurl=https://repo.radeon.com/amdgpu/5.5.1/rhel/9.2/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo yum clean all
```

:::
::::

::::{rubric} Upgrade the Kernel-mode driver and reboot the System
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
baseurl=https://repo.radeon.com/rocm/5.5.1/main
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
sudo apt install --only-upgrade rocm-hip-sdk
```

:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

::::{rubric} Update the AMDGPU repository
::::

```shell
sudo tee --append /etc/zypp/repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/5.5.1/sle/15.4/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo zypper ref
```

::::{rubric} Upgrade the Kernel-mode driver and reboot the System
::::

Upgrade the kernel mode driver and reboot the system using the following
commands:

```shell
sudo zypper --gpg-auto-import-keys install amdgpu-dkms
sudo reboot
```

::::{rubric} Update the ROCm repository
::::

```shell
sudo tee --append /etc/zypp/repos.d/rocm.repo <<EOF
name=rocm
baseurl=https://repo.radeon.com/amdgpu/5.5.1/sle/15.4/main/x86_64
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

## Verification Process

To verify if the upgrade is successful, refer to the
{ref}`post-install-actions-linux` given in the
[Installation](install) section.
