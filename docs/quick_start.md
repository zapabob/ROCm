# Quick Start (Linux)

## Install Prerequisites

::::{tab-set}

:::{tab-item} Ubuntu 20.04
:sync: key5
Install kernel headers and modules for the active kernel.

```bash
sudo apt install linux-headers-`uname -r` linux-modules-extra-`uname -r`
```

:::

:::{tab-item} Ubuntu 22.04
:sync: key6

Content 3
:::

:::{tab-item} RHEL8
:sync: key1

Content 1
:::

:::{tab-item} RHEL9
:sync: key2

Content 2
:::

:::{tab-item} SLES15 SP3
:sync: key3

Content 3
:::

:::{tab-item} SLES15 SP4
:sync: key4

Content 3
:::

::::

## Add Repositories

::::{tab-set}

:::{tab-item} Ubuntu 20.04
:sync: key5
Add the ROCm GPG key and add the repositories

```bash
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/amdgpu/latest/ubuntu focal main' | sudo tee /etc/apt/sources.list.d/amdgpu.list
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ focal main' | sudo tee /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt-get update
```

:::

:::{tab-item} Ubuntu 22.04
:sync: key6

Content 3
:::

:::{tab-item} RHEL8
:sync: key1

Content 1
:::

:::{tab-item} RHEL9
:sync: key2

Content 2
:::

:::{tab-item} SLES15 SP3
:sync: key3

Content 3
:::

:::{tab-item} SLES15 SP4
:sync: key4

Content 3
:::

::::

## Install Drivers

::::{tab-set}

:::{tab-item} Ubuntu 20.04
:sync: key5
Install the amdgpu kernel module, aka driver, on your system.

```bash
sudo apt install amdgpu-dkms
```

:::

:::{tab-item} Ubuntu 22.04
:sync: key6

Content 3
:::

:::{tab-item} RHEL8
:sync: key1

Content 1
:::

:::{tab-item} RHEL9
:sync: key2

Content 2
:::

:::{tab-item} SLES15 SP3
:sync: key3

Content 3
:::

:::{tab-item} SLES15 SP4
:sync: key4

Content 3
:::

::::

## Install ROCm Runtimes

::::{tab-set}

:::{tab-item} Ubuntu 20.04
:sync: key5
Installs the rocm-hip-runtime metapackage. This contains depedencies for most
common ROCm applications.

```bash
sudo apt install rocm-hip-libraries
```

:::

:::{tab-item} Ubuntu 22.04
:sync: key6

Content 3
:::

:::{tab-item} RHEL8
:sync: key1

Content 1
:::

:::{tab-item} RHEL9
:sync: key2

Content 2
:::

:::{tab-item} SLES15 SP3
:sync: key3

Content 3
:::

:::{tab-item} SLES15 SP4
:sync: key4

Content 3
:::

::::

## Reboot the system

::::{tab-set}

:::{tab-item} Ubuntu 20.04
:sync: key5
The driver requires a system reboot.

```bash
sudo reboot
```

:::

:::{tab-item} Ubuntu 22.04
:sync: key6

Content 3
:::

:::{tab-item} RHEL8
:sync: key1

Content 1
:::

:::{tab-item} RHEL9
:sync: key2

Content 2
:::

:::{tab-item} SLES15 SP3
:sync: key3

Content 3
:::

:::{tab-item} SLES15 SP4
:sync: key4

Content 3
:::

::::
