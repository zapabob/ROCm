# Installation (Linux)

Installing can be done in one of two ways, depending on your preference:

- Using an installer script
- Through your system's package manager

```{attention}
For information on installing ROCm on devices with NVIDIA GPUs, refer to the HIP
Installation Guide.
```

(install-script-method)=

## Installer Script Method

The installer script method automates the installation process for the AMDGPU
and ROCm stack. The installer script handles the complete installation process
for ROCm, including setting up the repository, cleaning the system, updating,
and installing the desired drivers and meta-packages. With this approach, the
system has more control over the ROCm installation process. Thus, those who are
less familiar with the Linux standard commands can choose this method for ROCm
installation.

For AMDGPU and ROCm installation using the installer script method on Linux
distribution, follow these steps:

1. **Meet prerequisites** – Ensure the Prerequisites are met before downloading
   and installing the installer using the installer script method.

2. **Download and install the installer script** – Ensure you download and
   install the installer script from the recommended URL.

   ```{tip}
   The installer package is updated periodically to resolve known issues and add
   new features. The links for each Linux distribution always point to the latest
   available build.
   ```

3. **Use the installer script on Linux distributions** – Ensure you execute the
   script for installing use cases.

### Download and Install the Installer Script

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

### Using the Installer Script for Single-version ROCm Installation

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

### Using Installer Script in Docker

When the installation is initiated in Docker, the installer tries to install the
use case along with the kernel-mode driver. However, you cannot install the
kernel-mode driver in a Docker container. To skip the installation of the
kernel-mode driver, proceed with the `--no-dkms` option, as shown below:

```shell
sudo amdgpu-install --usecase=rocm --no-dkms
```

### Using the Installer Script for Multi-version ROCm Installation

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

#### Add Required ROCm Repositories

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

#### Use the Installer to Install Multi-version ROCm Meta-packages

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

## Package Manager Method

The package manager method involves a manual setup of the repository, which
includes setting up the repository, updating, and installing/uninstalling
meta-packages. This involves using standard commands such as yum, apt, and
others respective to the Linux distribution.

The functions of a package manager installation system are:

- Grouping packages based on function
- Extracting package archives
- Ensuring a package is installed with all necessary packages and dependencies
  are managed
- From a remote repository, looking up, downloading, installing, or updating
  existing packages
- Ensuring the authenticity and integrity of the package

### Installing ROCm on Linux Distributions

For a fresh ROCm installation using the package manager method on a Linux
distribution, follow the steps below:

1. **Meet prerequisites** – Ensure the Prerequisites are met before the ROCm
   installation.

2. **Install kernel headers and development packages** – Ensure kernel headers
   and development packages are installed on the system.

3. **Select the base URLs for AMDGPU and ROCm stack repository** – Ensure the
   base URLs for AMDGPU and ROCm stack repositories are selected.

4. **Add the AMDGPU stack repository** – Ensure the AMDGPU stack repository is
   added.

5. **Install the kernel-mode driver and reboot the system** – Ensure the
   kernel-mode driver is installed and the system is rebooted.

6. **Add ROCm stack repository** – Ensure the ROCm stack repository is added.

7. **Install single-version or multi-version ROCm meta-packages** – Install the
   desired meta-packages.

8. **Verify installation for the applicable distributions** – Verify if the
   installation is successful.

```{important}
You cannot install a kernel-mode driver in a Docker container. Refer to the
sections below for specific commands to install the AMDGPU and ROCm stack on
various Linux distributions.
```

#### Understanding the Release-specific AMDGPU and ROCm Stack Repositories on Linux Distributions

The release-specific repositories consist of packages from a specific release of
the AMDGPU stack and ROCm stack. The repositories are not updated for the latest
packages with subsequent releases. When a new ROCm release is available, the new
repository, specific to that release, is added. You can select a specific
release to install, update the previously installed single version to the later
available release, or add the latest version of ROCm along with the currently
installed version by using the multi-version ROCm packages.

```{note}
Users installing multiple versions of the ROCm stack must use the
release-specific base URL.
```

#### Using the Package Manager

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{rubric} Installation of Kernel Headers and Development Packages
::::

The following instructions to install kernel headers and development packages
apply to all versions and kernels of Ubuntu. The ROCm installation requires you
to install the Linux-headers and Linux-modules-extra package with the correct
version corresponding to the kernel's version.

**Example:** If the system is running the Linux kernel version
`5.15.0-41-generic`, you must install the identical versions of Linux-headers
and development packages. Refer to {ref}`check-kernel-info` on to how to check
the system's kernel version.

To check the `kernel-headers` and `linux-modules-extra` package versions,
follow these steps:

1. For the Ubuntu/Debian environment, execute the following command to verify
   the kernel headers and development packages are installed with the
   respective versions:

   ```shell
   sudo dpkg -l | grep linux-headers
   ```

   The command indicates if there are Linux headers installed as shown below:

   ```none
   ii  linux-headers-5.15.0-41-generic            5.15.0-41.44~20.04.1                    amd64        Linux kernel headers for version 5.15.0 on 64 bit x86 SMP
   ```

2. Execute the following command to check whether the development packages are
   installed:

   ```shell
   sudo dpkg -l | grep linux-modules-extra
   ```

   The command mentioned above lists the installed `linux-modules-extra`
   packages like the output below:

   ```none
   ii  linux-modules-extra-5.15.0-41-generic      5.15.0-41.44~20.04.1                    amd64        Linux kernel extra modules for version 5.15.0 on 64 bit x86 SMP
   ```

3. If the supported version installation of Linux headers and development
   packages are not installed on the system, execute the following command
   to install the packages:

   ```shell
   sudo apt install linux-headers-`uname -r` linux-modules-extra-`uname -r`
   ```

::::{rubric} Adding the AMDGPU and ROCm Stack Repositories
::::

1. Add GPG Key for AMDGPU and ROCm Stack

   Add the GPG key for AMDGPU and ROCm repositories. For Debian-based systems
   like Ubuntu, configure the Debian ROCm repository as follows:

   ```shell
   curl -fsSL https://repo.radeon.com/rocm/rocm.gpg.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/rocm-keyring.gpg
   ```

   ```{note}
   The GPG key may change; ensure it is updated when installing a new release. If
   the key signature verification fails while updating, re-add the key from the
   ROCm to the apt repository as mentioned above. The current `rocm.gpg.key` is not
   available in a standard key ring distribution but has the following SHA1 sum
   hash: `73f5d8100de6048aa38a8b84cd9a87f05177d208 rocm.gpg.key`
   ```

2. Add the AMDGPU Stack Repository and Install the Kernel-mode Driver

   ```{attention}
   If you have a version of the kernel-mode driver installed, you may skip this
   section.
   ```

   To add the AMDGPU stack repository, follow these steps:

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

   Install the kernel mode driver and reboot the system using the following
   commands:

   ```shell
   sudo apt install amdgpu-dkms
   sudo reboot
   ```

3. Add the ROCm Stack Repository and Install Meta-packages

   To add the ROCm repository, use the following steps:

   ::::{tab-set}
   :::{tab-item} Ubuntu 20.04
   :sync: ubuntu-20.04

   ```shell
   for ver in 5.0.2 5.1.4 5.2.5 5.3.3 5.4.3; do
   echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver focal main" | sudo tee /etc/apt/sources.list.d/rocm.list
   done
   echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
   sudo apt update
   ```

   :::
   :::{tab-item} Ubuntu 22.04
   :sync: ubuntu-22.04

   ```shell
   for ver in 5.0.2 5.1.4 5.2.5 5.3.3 5.4.3; do
   echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver jammy main" | sudo tee /etc/apt/sources.list.d/rocm.list
   done
   echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
   sudo apt update
   ```

   :::
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

   ```{important}
   If the existing ROCm release contains non-versioned ROCm packages, you must
   uninstall those packages before proceeding to the multi-version installation
   to avoid conflicts.
   ```

   ```shell
   sudo apt install rocm-hip-sdk5.4.3 rocm-hip-sdk5.2.5
   ```

:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{rubric} Installation of Kernel Headers and Development Packages
::::

The ROCm installation requires that you install the kernel headers and
`linux-modules-extra` package with the correct version corresponding to the
kernel's version.

**Example:** If the system is running Linux kernel version
`3.10.0-1160.el7.x86_64`, you must install the identical versions of kernel
headers and development packages. Refer to {ref}`check-kernel-info` on to how to
check the system's kernel version.

To check the kernel headers and `linux-modules-extra` package versions,
follow these steps:

1. To verify you have the supported version of the installed kernel headers,
   type the following on the command line:

   ```shell
   sudo yum list installed kernel-headers
   ```

   The command mentioned above displays the list of kernel headers versions
   currently present on your system. Verify if the listed kernel headers have
   the same versions as the kernel.

2. The following command lists the development packages on your system. Verify
   if the listed development package's version number matches the kernel
   version number:

   ```shell
   sudo yum list installed kernel-devel
   ```

3. If the supported version installation of kernel headers and development
   packages does not exist on the system, execute the command below to install:

   ```shell
   sudo yum install kernel-headers-`uname -r` kernel-devel-`uname -r`
   ```

::::{rubric} Adding the AMDGPU and ROCm Stack Repositories
::::

1. Add the AMDGPU Stack Repository and Install the Kernel-mode Driver

   ```{attention}
   If you have a version of the kernel-mode driver installed, you may skip this
   section.
   ```

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

   Install the kernel mode driver and reboot the system using the following
   commands:

   ```shell
   sudo yum install amdgpu-dkms
   sudo reboot
   ```

2. Add the ROCm Stack Repository and Install Meta-packages

   To add the ROCm repository, use the following steps:

   ```shell
   for ver in 5.0.2 5.1.4 5.2.5 5.3.3 5.4.3; do
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

   ```{important}
   If the existing ROCm release contains non-versioned ROCm packages, you must
   uninstall those packages before proceeding to the multi-version installation
   to avoid conflicts.
   ```

   ```shell
   sudo yum install rocm-hip-sdk5.4.3 rocm-hip-sdk5.2.5
   ```

:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

::::{rubric} Installation of Kernel Headers and Development Packages
::::

ROCm installation requires you to install `linux-headers` and
`linux-modules-extra` package with the correct version corresponding to the
kernel's version.

**Example:** If the system is running the Linux kernel version
`5.3.18-57_11.0.18`, you must install the same versions of Linux headers and
development packages. Refer to {ref}`check-kernel-info` on to how to check
the system's kernel version.

To check the `kernel-headers` and `linux-modules-extra` package versions, follow
these steps:

1. Ensure that the correct version of the latest `kernel-default-devel` and
   `kernel-default` packages are installed. The following command lists the
   installed `kernel-default-devel` and `kernel-default` package:

   ```shell
   sudo zypper info kernel-default-devel or kernel-default
   ```

   ```{note}
   This next step is only required if you find from the above command that the
   `kernel-default-devel` and `kernel-default` versions of the package,
   corresponding to the kernel release version, do not exist on your system.
   ```

2. If the required version of packages does not exist on the system, install
   with the command below:

   ```shell
   sudo zypper install kernel-default-devel or kernel-default
   ```

::::{rubric} Adding the AMDGPU and ROCm Stack Repositories
::::

1. Add the AMDGPU Stack Repository and Install the Kernel-mode Driver

   ```{attention}
   If you have a version of the kernel-mode driver installed, you may skip this
   section.
   ```

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

   Install the kernel mode driver and reboot the system using the following
   commands:

   ```shell
   sudo zypper --gpg-auto-import-keys install amdgpu-dkms
   sudo reboot
   ```

2. Add the ROCm Stack Repository and Install Meta-packages

   To add the ROCm repository, use the following steps:

   ```shell
   for ver in 5.0.2 5.1.4 5.2.5 5.3.3 5.4.3; do
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

   ```{important}
   If the existing ROCm release contains non-versioned ROCm packages, you must
   uninstall those packages before proceeding to the multi-version installation
   to avoid conflicts.
   ```

   ```shell
   sudo zypper --gpg-auto-import-keys install rocm-hip-sdk5.4.3 rocm-hip-sdk5.2.5
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
   export PATH=$PATH:/opt/rocm-5.4.3/bin:/opt/rocm-5.4.3/opencl/bin
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

:::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

```shell
sudo zypper search --installed-only
```

:::
::::
