# Quick Start (Linux)

## Install Prerequisites

The driver package uses
[`DKMS`](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support) to build
the amdgpu module (driver) for the installed kernels. This requires the linux
kernel headers and modules to be installed for each.

To install these for the currently active kernel run the command corresponding
to your distribution.
::::{tab-set}
:::{tab-item} Ubuntu
:sync: ubuntu

```shell  
sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
```
:::

:::{tab-item} Red Hat Enterprise Linux
:sync: RHEL
```shell
# TODO
```
:::

:::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15
```shell
# TODO
```
:::
::::

## Add Repositories

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{rubric} 1. Download and convert the package signing key
::::

```shell
# Download the key
wget https://repo.radeon.com/rocm/rocm.gpg.key
# Make the directory if it doesn't exist yet.
# This location is recommended by the distribution maintainers.
mkdir --parents --mode=0755 /etc/apt/keyrings
# Convert the signing-key to a full keyring required
# by apt and store in the keyring directory
TMPRING="$(mktemp --suffix=.gpg --quiet)"
gpg --keyring="$TMPRING" --no-default-keyring --import rocm.gpg.key
gpg --keyring="$TMPRING" --no-default-keyring --export --output /etc/apt/keyrings/rocm.gpg
# Remove the key and the temporary keyring used for the conversion
rm -f "$TMPRING" rocm.gpg.key
```

::::{rubric} 2. Add the repositories
::::

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04
```shell
# Kernel driver repository for focal
sudo tee /etc/apt/sources.list.d/amdgpu.list <<'EOF'
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/latest/ubuntu focal main
EOF
# ROCm repository for focal
sudo tee /etc/apt/sources.list.d/rocm.list <<'EOF'
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/debian focal main
EOF
```
:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04
```shell
# Kernel driver repository for jammy
sudo tee /etc/apt/sources.list.d/amdgpu.list <<'EOF'
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/latest/ubuntu jammy main
EOF
# ROCm repository for jammy
sudo tee /etc/apt/sources.list.d/rocm.list <<'EOF'
echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/debian jammy main
EOF
```
:::
::::

::::{rubric} 3. Update the list of packages
::::
```shell
sudo apt update
```

:::::

:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

TODO

::::{tab-set}
:::{tab-item} RHEL8
:sync: RHEL8
```shell
# TODO
```
:::

:::{tab-item} RHEL9
:sync: RHEL9
```shell
# TODO
```
:::
::::
:::::

:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

TODO

::::{tab-set}
:::{tab-item} SLES15 SP3
:sync: SLES15-SP3
```shell
# TODO
```
:::

:::{tab-item} SLES15 SP4
:sync: SLES15-SP4
```shell
# TODO
```
:::

::::
:::::
::::::

## Install Drivers

Install the amdgpu kernel module, aka driver, on your system.

::::{tab-set}

:::{tab-item} Ubuntu
:sync: ubuntu
```shell
sudo apt install amdgpu-dkms
```
:::

:::{tab-item} Red Hat Enterprise Linux
:sync: RHEL
```shell
sudo yum install amdgpu-dkms
```
:::

:::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15
```shell
sudo zypper --gpg-auto-import-keys install amdgpu-dkms
```
:::

::::

## Install ROCm Runtimes

Install the `rocm-hip-runtime` metapackage. This contains depedencies for most
common ROCm applications.

::::{tab-set}
:::{tab-item} Ubuntu
:sync: ubuntu
```console shell
sudo apt install rocm-hip-libraries
```
:::

:::{tab-item} Red Hat Enterprise Linux
:sync: RHEL
```console shell
sudo yum install rocm-hip-libraries
```
:::

:::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15
```console shell
sudo zypper --gpg-auto-import-keys install rocm-hip-libraries
```
:::
::::

## Reboot the system

Loading the new driver requires a reboot of the system.

```shell
sudo reboot
```
