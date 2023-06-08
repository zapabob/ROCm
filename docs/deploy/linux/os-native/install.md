# Installation (Linux)

## Understanding the Release-specific AMDGPU and ROCm Repositories on Linux Distributions

The release-specific repositories consist of packages from a specific release of
versions of AMDGPU and ROCm. The repositories are not updated for the latest
packages with subsequent releases. When a new ROCm release is available, the new
repository, specific to that release, is added. You can select a specific
release to install, update the previously installed single version to the later
available release, or add the latest version of ROCm along with the currently
installed version by using the multi-version ROCm packages.

## Step by Step Instructions

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{rubric} 1. Download and convert the package signing key
::::

```shell
# Make the directory if it doesn't exist yet.
# This location is recommended by the distribution maintainers.
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
# Download the key, convert the signing-key to a full
# keyring required by apt and store in the keyring directory
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | \
    gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null
```

```{note}
The GPG key may change; ensure it is updated when installing a new release. If
the key signature verification fails while updating, re-add the key from the
ROCm to the apt repository as mentioned above. The current `rocm.gpg.key` is not
available in a standard key ring distribution but has the following SHA1 sum
hash: `73f5d8100de6048aa38a8b84cd9a87f05177d208 rocm.gpg.key`
```

::::{rubric} 2. Add the AMDGPU Repository and Install the Kernel-mode Driver
::::

```{tip}
If you have a version of the kernel-mode driver installed, you may skip this
section.
```

To add the AMDGPU repository, follow these steps:

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
# amdgpu repository for focal
echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/5.5.1/ubuntu focal main' \
    | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
# amdgpu repository for jammy
echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/5.5.1/ubuntu jammy main' \
    | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update
```

:::
::::

Install the kernel mode driver and reboot the system using the following
commands:

```shell
sudo apt install amdgpu-dkms
sudo reboot
```

::::{rubric} 3. Add the ROCm Repository
::::

To add the ROCm repository, use the following steps:

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
# ROCm repositories for focal
for ver in 5.3.3 5.4.3 5.5.1; do
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$ver focal main" \
    | sudo tee --append /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
    | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
# ROCm repositories for jammy
for ver in 5.3.3 5.4.3 5.5.1; do
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$ver jammy main" \
    | sudo tee --append /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
    | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
::::

::::{rubric} 4. Install packages
::::

Install packages of your choice in a single-version ROCm install or
in a multi-version ROCm install fashion. For more information on what
single/multi-version installations are, refer to {ref}`installation-types`.
For a comprehensive list of meta-packages, refer to
{ref}`meta-package-desc`.

- Sample Single-version installation

   ```shell
   sudo apt install rocm-hip-sdk
   ```

- Sample Multi-version installation

   ```shell
   sudo apt install rocm-hip-sdk5.5.1 rocm-hip-sdk5.3.3
   ```

:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{rubric} 1. Add the AMDGPU Stack Repository and Install the Kernel-mode Driver
::::

```{tip}
If you have a version of the kernel-mode driver installed, you may skip this
section.
```

::::{tab-set}
:::{tab-item} RHEL 8.6
:sync: RHEL-8.6
:sync: RHEL-8

```shell
sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
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
:sync: RHEL-8

```shell
sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
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
:sync: RHEL-9

```shell
sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/5.5.1/rhel/9.1/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo yum clean all
```

:::
::::

Install the kernel mode driver and reboot the system using the following
commands:

```shell
sudo yum install amdgpu-dkms
sudo reboot
```

::::{rubric} 2. Add the ROCm Stack Repository
::::

To add the ROCm repository, use the following steps, based on your distribution:

::::{tab-set}
:::{tab-item} RHEL 8
:sync: RHEL-8

```shell
for ver in 5.3.3 5.4.3 5.5.1; do
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[ROCm-$ver]
name=ROCm$ver
baseurl=https://repo.radeon.com/rocm/rhel8/$ver/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo yum clean all
```

:::
:::{tab-item} RHEL 9
:sync: RHEL-9

```shell
for ver in 5.3.3 5.4.3 5.5.1; do
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[ROCm-$ver]
name=ROCm$ver
baseurl=https://repo.radeon.com/rocm/rhel9/$ver/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo yum clean all
```

:::
::::

::::{rubric} 3. Install packages
::::

Install packages of your choice in a single-version ROCm install or
in a multi-version ROCm install fashion. For more information on what
single/multi-version installations are, refer to {ref}`installation-types`.
For a comprehensive list of meta-packages, refer to
{ref}`meta-package-desc`.

- Sample Single-version installation

   ```shell
   sudo yum install rocm-hip-sdk
   ```

- Sample Multi-version installation

   ```shell
   sudo yum install rocm-hip-sdk5.5.1 rocm-hip-sdk5.3.3
   ```

:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

::::{rubric} 1. Add the AMDGPU Repository and Install the Kernel-mode Driver
::::

```{tip}
If you have a version of the kernel-mode driver installed, you may skip this
section.
```

```shell
sudo tee /etc/zypp/repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/5.5.1/sle/15.4/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo zypper ref
```

Install the kernel mode driver and reboot the system using the following
commands:

```shell
sudo zypper --gpg-auto-import-keys install amdgpu-dkms
sudo reboot
```

::::{rubric} 2. Add the ROCm Stack Repository
::::

To add the ROCm repository, use the following steps:

```shell
for ver in 5.3.3 5.4.3 5.5.1; do
sudo tee --append /etc/zypp/repos.d/rocm.repo <<EOF
[ROCm-$ver]
name=ROCm$ver
name=rocm
baseurl=https://repo.radeon.com/rocm/zyp/$ver/main
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo zypper ref
```

::::{rubric} 3. Install packages
::::

Install packages of your choice in a single-version ROCm install or
in a multi-version ROCm install fashion. For more information on what
single/multi-version installations are, refer to {ref}`installation-types`.
For a comprehensive list of meta-packages, refer to
{ref}`meta-package-desc`.

- Sample Single-version installation

   ```shell
   sudo zypper --gpg-auto-import-keys install rocm-hip-sdk
   ```

- Sample Multi-version installation

   ```shell
   sudo zypper --gpg-auto-import-keys install rocm-hip-sdk5.5.1 rocm-hip-sdk5.3.3
   ```

:::::
::::::

(post-install-actions-linux)=

## Post-install Actions and Verification Process

The post-install actions listed here are optional and depend on your use case,
but are generally useful. Verification of the install is advised.

### Post-install Actions

1. Instruct the system linker where to find the shared objects (`.so` files) for
   ROCm applications.

   ```shell
   sudo tee --append /etc/ld.so.conf.d/rocm.conf <<EOF
   /opt/rocm/lib
   /opt/rocm/lib64
   EOF
   sudo ldconfig
   ```

   ```{note}
   Multi-version installations require extra care. Having multiple versions on
   the system linker library search path is unadvised. One must take care both
   at compile-time and at run-time to assure that the proper libraries are
   picked up. You can override `ld.so.conf` entries on a case-by-case basis
   using the `LD_LIBRARY_PATH` environmental variable.
   ```

2. Add binary paths to the `PATH` environment variable.

   ```shell
   export PATH=$PATH:/opt/rocm-5.5.1/bin:/opt/rocm-5.5.1/opencl/bin
   ```

   ```{attention}
   When using CMake to build applications, having the ROCm install location on
   the PATH subtly affects how ROCm libraries are searched for. See [Config Mode
   Search Procedure](https://cmake.org/cmake/help/latest/command/find_package.html#config-mode-search-procedure)
   and [CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH](https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH.html)
   for details.

   (Entries in the `PATH` minus `bin` and `sbin` are added to library search
   paths, therefore this convenience will affect builds and result in ROCm
   libraries almost always being found. This may be an issue when you're
   developing these libraries or want to use self-built versions of them.)
   ```

(verifying-kernel-mode-driver-installation)=

### Verifying Kernel-mode Driver Installation

Check the installation of the kernel-mode driver by typing the command given
below:

```shell
dkms status
```

### Verifying ROCm Installation

After completing the ROCm installation, execute the following commands on the
system to verify if the installation is successful. If you see your GPUs listed
by both commands, the installation is considered successful:

```shell
/opt/rocm/bin/rocminfo
# OR
/opt/rocm/opencl/bin/clinfo
```

### Verifying Package Installation

To ensure the packages are installed successfully, use the following commands:

::::{tab-set}
:::{tab-item} Ubuntu
:sync: ubuntu

```shell
sudo apt list --installed
```

:::

:::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

```shell
sudo yum list installed
```

:::

:::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

```shell
sudo zypper search --installed-only
```

:::
::::
