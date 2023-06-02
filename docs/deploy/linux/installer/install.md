# Installation (Scripted)

(install-script-method)=

The installer script method automates the installation process for the AMDGPU
and ROCm stack. The installer script handles the complete installation process
for ROCm, including setting up the repository, cleaning the system, updating,
and installing the desired drivers and meta-packages. Users who are
less familiar with the Linux standard commands can choose this method for ROCm
installation.

Prior to beginning, please ensure you have the [prerequisites](../prerequisites)
installed.

## Download and Install the Installer Script

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

<!-- markdownlint-disable-next-line MD013 -->
::::{rubric} To download the amdgpu-install script on the system, use the following commands.
::::

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.4.3/ubuntu/focal/amdgpu-install_5.4.50403-1_all.deb
sudo apt install ./amdgpu-install_5.4.50403-1_all.deb
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.4.3/ubuntu/jammy/amdgpu-install_5.4.50403-1_all.deb
sudo apt install ./amdgpu-install_5.4.50403-1_all.deb
```

:::
::::
:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

<!-- markdownlint-disable-next-line MD013 -->
::::{rubric} To download the amdgpu-install script on the system, use the following commands.
::::

::::{tab-set}
:::{tab-item} RHEL 8.6
:sync: RHEL-8.6

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.4.3/rhel/8.6/amdgpu-install-5.4.50403-1.el8.noarch.rpm
```

:::
:::{tab-item} RHEL 8.7
:sync: RHEL-8.7

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.4.3/rhel/8.7/amdgpu-install-5.4.50403-1.el8.noarch.rpm
```

:::
:::{tab-item} RHEL 9.1
:sync: RHEL-9.1

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.4.3/rhel/9.1/amdgpu-install-5.4.50403-1.el9.noarch.rpm
```

:::
::::
:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

<!-- markdownlint-disable-next-line MD013 -->
::::{rubric} To download the amdgpu-install script on the system, use the following commands.
::::

::::{tab-set}
:::{tab-item} Service Pack 4
:sync: SLES15-SP4

```shell
sudo zypper --no-gpg-checks install https://repo.radeon.com/amdgpu-install/5.4.3/sle/15.4/amdgpu-install-5.4.50403-1.noarch.rpm
```

:::
::::
:::::
::::::

## Using the Installer Script for Single-version ROCm Installation

To install use cases specific to your requirements, use the installer
`amdgpu-install` as follows:

- To install a single use case:

  ```shell
  sudo amdgpu-install --usecase=rocm
  ```

- To install kernel-mode driver:

  ```shell
  sudo amdgpu-install --usecase=dkms
  ```

- To install multiple use cases:

  ```shell
  sudo amdgpu-install --usecase=hiplibsdk,rocm
  ```

- To display a list of available use cases:

  ```shell
  sudo amdgpu-install --list-usecase
  ```

  Following is a sample of output listed by the command above:

  ```{note}
  The list in this section represents only a sample of available use cases for ROCm:
  ```

  ```none
  If --usecase option is not present, the default selection is "graphics,opencl,hip"

  Available use cases:
  rocm(for users and developers requiring full ROCm stack)
  - OpenCL (ROCr/KFD based) runtime
  - HIP runtimes
  - Machine learning framework
  - All ROCm libraries and applications
  - ROCm Compiler and device libraries
  - ROCr runtime and thunk
  lrt(for users of applications requiring ROCm runtime)
  - ROCm Compiler and device libraries
  - ROCr runtime and thunk
  opencl(for users of applications requiring OpenCL on Vega or
  later products)
  - ROCr based OpenCL
  - ROCm Language runtime

  openclsdk (for application developers requiring ROCr based OpenCL)
  - ROCr based OpenCL
  - ROCm Language runtime
  - development and SDK files for ROCr based OpenCL

  hip(for users of HIP runtime on AMD products)
  - HIP runtimes
  hiplibsdk (for application developers requiring HIP on AMD products)
  - HIP runtimes
  - ROCm math libraries
  - HIP development libraries
  ```

```{tip}
Adding `-y` as a parameter to `amdgpu-install` skips user prompts (for
automation). Example: `amdgpu-install -y --usecase=rocm`
```

## Using Installer Script in Docker

When the installation is initiated in Docker, the installer tries to install the
use case along with the kernel-mode driver. However, you cannot install the
kernel-mode driver in a Docker container. To skip the installation of the
kernel-mode driver, proceed with the `--no-dkms` option, as shown below:

```shell
sudo amdgpu-install --usecase=rocm --no-dkms
```

## Using the Installer Script for Multi-version ROCm Installation

The multi-version ROCm installation requires you to download and install the
latest ROCm release installer from the list of ROCm releases you want to install
simultaneously on your system.

**Example:** If you want to install ROCm releases 4.5.0, 4.5.1, and 5.4.3
simultaneously, you are required to download the installer from the latest ROCm
release v5.4.3.

To download and install the installer, refer to the [Download and Install the
Installer Script](#download-and-install-the-installer-script) section.

```{attention}
If the existing ROCm release contains non-versioned ROCm packages, uninstall
those packages before proceeding with the multi-version installation to avoid
conflicts.
```

### Add Required ROCm Repositories

Add the required repositories using the following steps:

```{important}
Add the AMDGPU and ROCm repositories manually for all ROCm releases you want to
install except the latest one. The amdgpu-install script automatically adds the
required repositories for the latest release.
```

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
for ver in 5.0.2 5.1.4 5.2.5 5.3.3; do
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver focal main" | sudo tee /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
for ver in 5.0.2 5.1.4 5.2.5 5.3.3; do
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver jammy main" | sudo tee /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
::::
:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

```shell
for ver in 5.0.2 5.1.4 5.2.5 5.3.3; do
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[ROCm-$ver]
Name=ROCm$ver
baseurl=https://repo.radeon.com/rocm/$ver/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo yum clean all
```

:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

```shell
for ver in 5.0.2 5.1.4 5.2.5 5.3.3; do
sudo tee --append /etc/zypp/repos.d/rocm.repo <<EOF
name=rocm
baseurl=https://repo.radeon.com/amdgpu/$ver/sle/15.4/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo zypper ref
```

:::::
::::::

## Use the Installer to Install Multi-version ROCm Meta-packages

Use the installer script as given below:

```none
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-1>
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-2>
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-3>
```

```{tip}
If the kernel-mode driver is already present on the system and you do not want
to upgrade it, use the `--no-dkms` option to skip the installation of the
kernel-mode driver, as shown in the following samples:
```

```none
sudo amdgpu-install --usecase=rocm --rocmrelease=4.5.0 --no-dkms
sudo amdgpu-install --usecase=rocm --rocmrelease=5.4.3 --no-dkms
```

Following are examples of ROCm multi-version installation. The kernel-mode
driver, associated with the ROCm release v5.4.3, will be installed as its latest
release in the list.

```none
sudo amdgpu-install --usecase=rocm --rocmrelease=4.5.0
sudo amdgpu-install --usecase=rocm --rocmrelease=4.5.2
sudo amdgpu-install --usecase=rocm --rocmrelease=5.4.3
```
