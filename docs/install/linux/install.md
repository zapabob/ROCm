# Install ROCm on Linux

To install ROCm on Linux, you can use our [quick-start guide](./install-quick.md) or you can
follow the instructions listed below.

**Topics:**

* [Installation options](#installation-options)
* [Prerequisites](#prerequisites)
* [Install ROCm](#install-rocm)
* [Post-install actions and verification](#post-install-actions-and-verification)
* [Upgrade ROCm](#upgrade-rocm)
* [Uninstall ROCm](#uninstall-rocm)

## Installation options

ROCm supports two methods for installation:

* Directly using the Linux distribution's package manager
* The `amdgpu-install` script

There is no difference in the final installation state when choosing either option.

Using the distribution's package manager lets the user install, upgrade and uninstall using familiar
commands and workflows. Third party ecosystem support is the same as your OS package manager.

The `amdgpu-install` script is a wrapper around the package manager. The same packages are installed
by this script as the package manager system.

The installer automates the installation process for the AMDGPU and ROCm stack. It handles the
complete installation process for ROCm, including setting up the repository, cleaning the system,
updating, and installing the desired drivers and meta-packages. Users who are less familiar with the
package manager can choose this method for ROCm installation.

(linux-install-methods)=

### Single-version versus multi-version ROCm install

ROCm packages are versioned with both semantic versioning that is package
specific and a ROCm release version.

* Single-version installation:
  * Installation of a single instance of the ROCm release on a system
  * Use of non-versioned ROCm meta-packages

* Multi-version installation:
  * Installation of multiple instances of the ROCm stack on a system. Extending
    the package name and its dependencies with the release version adds the
    ability to support multiple versions of packages simultaneously.
  * Use of versioned ROCm meta-packages.

```{attention}
ROCm packages that were previously installed from a single-version installation
must be removed before proceeding with the multi-version installation to avoid
conflicts.
```

```{note}
Multi-version install is not available for the kernel driver module (AMDGPU).
```

The following image shows the difference between single-version and
multi-version ROCm installations:

![ROCm installation types](../../data/install/linux/linux001.png "ROCm installation types")

## Prerequisites

Verify that your system meets all the installation requirements. The ROCm installation is supported only
on specific Linux distributions and kernel versions.

1. Verify the Linux distribution and confirm that it matches those listed in {ref}`linux-support`.

      ```shell
      uname -m && cat /etc/*release
      ```

   Running this command on an Ubuntu system results in the following output:

      ```shell
      x86_64
      DISTRIB_ID=Ubuntu
      DISTRIB_RELEASE=20.04
      DISTRIB_CODENAME=focal
      DISTRIB_DESCRIPTION="Ubuntu 20.04.5 LTS"
      ```

2. Verify the kernel version and confirm that it matches with system requirements listed in
   {ref}`linux-support`.

      ```shell
      uname -srmv
      ```

   Note that the output of the command above lists the kernel version in the
   following format:

      ```output
      Linux 5.15.0-46-generic #44~20.04.5-Ubuntu SMP Fri Jun 24 13:27:29 UTC 2022 x86_64
      ```

3. Enable additional package repositories. On some distributions the ROCm packages depend on packages
   outside the default package repositories. These extra repositories need to be enabled before
   installation. Follow the instructions below based on your distributions.

   ::::::{tab-set}

   :::::{tab-item} Ubuntu
   :sync: ubuntu

   All packages are available in the default Ubuntu repositories, therefore no additional repositories
   need to be added.

   :::::
   :::::{tab-item} Red Hat Enterprise Linux
   :sync: RHEL

   ::::{rubric} a. Add the EPEL repository.
   ::::

   ::::{tab-set}
   :::{tab-item} RHEL 8
   :sync: RHEL-8

   ```shell
   wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
   sudo rpm -ivh epel-release-latest-8.noarch.rpm
   ```

   :::
   :::{tab-item} RHEL 9
   :sync: RHEL-9

   ```shell
   wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
   sudo rpm -ivh epel-release-latest-9.noarch.rpm
   ```

   :::
   ::::

   ::::{rubric} b. Enable the CodeReady Linux Builder repository.
   ::::

   Run the following command and follow the instructions.

   ```shell
   sudo crb enable
   ```

   :::::
   :::::{tab-item} SUSE Linux Enterprise Server
   :sync: SLES

   Add the perl languages repository.

   ::::{tab-set}
   :::{tab-item} SLES 15.4
   :sync: SLES-15.4

   ```shell
   zypper addrepo https://download.opensuse.org/repositories/devel:languages:perl/SLE_15_SP4/devel:languages:perl.repo
   ```

   :::
   :::{tab-item} SLES 15.5
   :sync: SLES-15.5

   ```shell
   zypper addrepo https://download.opensuse.org/repositories/devel:/languages:/perl/15.5/devel:languages:perl.repo
   ```

   :::
   ::::
   :::::
   ::::::

4. Install kernel headers and development packages. The driver package uses
   [{abbr}`DKMS (Dynamic Kernel Module Support)`][DKMS-wiki] to build the `amdgpu-dkms` module
   (driver) for the installed kernels. This requires the Linux kernel headers and modules to be installed for
   each. Usually these are automatically installed with the kernel, but if you have multiple kernel versions
   or you have downloaded the kernel images and not the kernel meta-packages then they must be
   manually installed.

   [DKMS-wiki]: https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support

   To install for the currently active kernel run the command corresponding
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
   sudo yum install kernel-headers kernel-devel
   ```

   :::

   :::{tab-item} SUSE Linux Enterprise Server
   :sync: SLES

   ```shell
   sudo zypper install kernel-default-devel
   ```

   :::
   ::::

5. Set group permissions. If you want to add any current user to a video group to access GPU
   resources, follow these steps:

   ```{note}
      Use of the video group is recommended for all ROCm-supported operating
      systems.
   ```

   To check the groups in your system, issue the following command:

   ```shell
      groups
   ```

   Add yourself to the `render` and `video` group using the command:

   ```shell
      sudo usermod -a -G render,video $LOGNAME
   ```

   To add all future users to the `video` and `render` groups by default, run
   the following commands:

   ```shell
      echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
      echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
      echo 'EXTRA_GROUPS=render' | sudo tee -a /etc/adduser.conf
   ```

## Install ROCm

Note that the release-specific repositories consist of packages from a specific release of versions of
AMDGPU and ROCm. The repositories are not updated for the latest packages with subsequent
releases. When a new ROCm release is available, the new repository, specific to that release, is added.

You can select a specific release to install, update the previously installed single version to the later
available release, or add the latest version of ROCm along with the currently installed version by using
the multi-version ROCm packages.

::::::::{tab-set}
:::::::{tab-item} Linux package manager
:sync: package

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

::::{rubric} 2. Add the AMDGPU repository and install the kernel-mode driver
::::

```{tip}
If you have a version of the kernel-mode driver installed, you may skip this
section.
```

To add the AMDGPU repository, follow these steps:

::::{tab-set}
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
# version
ver=5.7

# amdgpu repository for jammy
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/$ver/ubuntu jammy main" \
    | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update
# Prefer packages from the rocm repository over system packages
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
```

:::
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
# version
ver=5.7

# amdgpu repository for focal
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/$ver/ubuntu focal main" \
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

::::{rubric} 3. Add the ROCm repository
::::

To add the ROCm repository, use the following steps:

::::{tab-set}
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
# ROCm repositories for jammy
for ver in 5.3.3 5.4.6 5.5.3 5.6.1 5.7; do
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$ver jammy main" \
    | sudo tee --append /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
    | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
# ROCm repositories for focal
for ver in 5.3.3 5.4.6 5.5.3 5.6.1 5.7; do
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$ver focal main" \
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

* Sample Single-version installation

   ```shell
   sudo apt install rocm-hip-sdk
   ```

* Sample Multi-version installation

   ```shell
   sudo apt install rocm-hip-sdk5.7 rocm-hip-sdk5.6.1 rocm-hip-sdk5.5.3
   ```

:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{rubric} 1. Add the AMDGPU stack repository and install the kernel-mode driver
::::

```{tip}
If you have a version of the kernel-mode driver installed, you may skip this
section.
```

::::{tab-set}
:::{tab-item} RHEL 9.2
:sync: RHEL-9.2
:sync: RHEL-9

```shell
# version
ver=5.7

sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/$ver/rhel/9.2/main/x86_64/
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
# version
ver=5.7

sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/$ver/rhel/9.1/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo yum clean all
```

:::

:::{tab-item} RHEL 8.8
:sync: RHEL-8.8
:sync: RHEL-8

```shell
# version
ver=5.7

sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/$ver/rhel/8.8/main/x86_64/
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
# version
ver=5.7

sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/$ver/rhel/8.7/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo yum clean all
```

:::

:::{tab-item} RHEL 8.6
:sync: RHEL-8.6
:sync: RHEL-8

```shell
# version
ver=5.7


sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/$ver/rhel/8.6/main/x86_64/
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

::::{rubric} 2. Add the ROCm stack repository
::::

To add the ROCm repository, use the following steps, based on your distribution:

::::{tab-set}
:::{tab-item} RHEL 9
:sync: RHEL-9

```shell
for ver in 5.3.3 5.4.6 5.5.3 5.6.1 5.7; do
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
:::{tab-item} RHEL 8
:sync: RHEL-8

```shell
for ver in 5.3.3 5.4.6 5.5.3 5.6.1 5.7; do
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
::::

::::{rubric} 3. Install packages
::::

Install packages of your choice in a single-version ROCm install or
in a multi-version ROCm install fashion. For more information on what
single/multi-version installations are, refer to {ref}`installation-types`.
For a comprehensive list of meta-packages, refer to
{ref}`meta-package-desc`.

* Sample Single-version installation

   ```shell
   sudo yum install rocm-hip-sdk
   ```

* Sample Multi-version installation

   ```shell
   sudo yum install rocm-hip-sdk5.7 rocm-hip-sdk5.6.1
   ```

:::::
:::::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

::::{rubric} 1. Add the AMDGPU repository and install the kernel-mode driver
::::

```{tip}
If you have a version of the kernel-mode driver installed, you may skip this
section.
```

::::{tab-set}
:::{tab-item} SLES 15.5
:sync: SLES-15.5

```shell
# version
ver=5.7

sudo tee /etc/zypp/repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/$ver/sle/15.5/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo zypper ref
```

:::
:::{tab-item} SLES 15.4
:sync: SLES-15.4

```shell
# version
ver=5.7


sudo tee /etc/zypp/repos.d/amdgpu.repo <<EOF
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/$ver/sle/15.4/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo zypper ref
```

:::
::::

Install the kernel mode driver and reboot the system using the following
commands:

```shell
sudo zypper --gpg-auto-import-keys install amdgpu-dkms
sudo reboot
```

::::{rubric} 2. Add the ROCm stack repository
::::

To add the ROCm repository, use the following steps:

```shell
for ver in 5.3.3 5.4.6 5.5.3 5.6.1 5.7; do
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

* Sample Single-version installation

   ```shell
   sudo zypper --gpg-auto-import-keys install rocm-hip-sdk
   ```

* Sample Multi-version installation

   ```shell
   sudo zypper --gpg-auto-import-keys install rocm-hip-sdk5.7 rocm-hip-sdk5.6.1
   ```

:::::
::::::

(post-install-actions-linux)=

## Post-install actions and verification

The post-install actions listed here are optional and depend on your use case,
but are generally useful. Verification of the install is advised.

### Post-install actions

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
   export PATH=$PATH:/opt/rocm-5.7.0/bin:/opt/rocm-5.7.0/opencl/bin

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

### Verifying kernel-mode driver installation

Check the installation of the kernel-mode driver by typing the command given
below:

```shell
dkms status
```

**Verifying ROCm installation.**

After completing the ROCm installation, execute the following commands on the system to verify if the
installation is successful. If you see your GPUs listed by both commands, the installation is considered
successful.

```shell
/opt/rocm/bin/rocminfo
```

**Verifying package installation.**

To ensure the packages are installed successfully, use the following commands.

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

```shell
sudo apt list --installed
```

:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

```shell
sudo yum list installed
```

:::::
:::::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

```shell
sudo zypper search --installed-only
```

:::::
:::::::
:::::::{tab-item} AMDGPU install script
:sync: amdgpu

To download and install the `amdgpu-install` script on the system, use the
following commands based on your distribution.

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{tab-set}
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.7/ubuntu/jammy/amdgpu-install_5.7.50700-1_all.deb
sudo apt install ./amdgpu-install_5.7.50700-1_all.deb
```

:::
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.7/ubuntu/focal/amdgpu-install_5.7.50700-1_all.deb
sudo apt install ./amdgpu-install_5.7.50700-1_all.deb
```

:::
::::
:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{tab-set}
:::{tab-item} RHEL 9.2
:sync: RHEL-9.2
:sync: RHEL-9

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.7/rhel/9.2/amdgpu-install-5.7.50700-1.el9.noarch.rpm
```

:::
:::{tab-item} RHEL 9.1
:sync: RHEL-9.1
:sync: RHEL-9

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.7/rhel/9.1/amdgpu-install-5.7.50700-1.el9.noarch.rpm
```

:::
:::{tab-item} RHEL 8.8
:sync: RHEL-8.8
:sync: RHEL-8

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.7/rhel/8.8/amdgpu-install-5.7.50700-1.el8.noarch.rpm
```

:::
:::{tab-item} RHEL 8.7
:sync: RHEL-8.7
:sync: RHEL-8

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.7/rhel/8.7/amdgpu-install-5.7.50700-1.el8.noarch.rpm
```

:::
:::{tab-item} RHEL 8.6
:sync: RHEL-8.6
:sync: RHEL-8

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.7/rhel/8.6/amdgpu-install-5.7.50700-1.el8.noarch.rpm
```

:::
::::
:::::
:::::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

::::{tab-set}
:::{tab-item} SLES 15.5
:sync: SLES-15.5

```shell
sudo zypper --no-gpg-checks install https://repo.radeon.com/amdgpu-install/5.7/sle/15.5/amdgpu-install-5.7.50700-1.noarch.rpm
```

:::
:::{tab-item} SLES 15.4
:sync: SLES-15.4

```shell
sudo zypper --no-gpg-checks install https://repo.radeon.com/amdgpu-install/5.7/sle/15.4/amdgpu-install-5.7.50700-1.noarch.rpm
```

:::
::::
:::::
::::::

### Use cases

Instead of installing individual applications or libraries the installer script
groups packages into specific use cases, matching typical workflows and runtimes.

To display a list of available use cases execute the command:

```shell
sudo amdgpu-install --list-usecase
```

The available use-cases will be printed in a format similar to the example
output below.

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

hip (for users of HIP runtime on AMD products)
- HIP runtimes
hiplibsdk (for application developers requiring HIP on AMD products)
- HIP runtimes
- ROCm math libraries
- HIP development libraries
```

To install use cases specific to your requirements, use the installer
`amdgpu-install` as follows:

* To install a single use case add it with the `--usecase` option:

  ```shell
  sudo amdgpu-install --usecase=rocm
  ```

* For multiple use cases separate them with commas:

  ```shell
  sudo amdgpu-install --usecase=hiplibsdk,rocm
  ```

### Single-version and multi-version ROCm installation

By default (without the `--rocmrelease` option)
the installer script will install packages in the single-version layout.

For the multi-version ROCm installation you must use the installer script from
the latest release of ROCm that you wish to install.

**Example:** If you want to install ROCm releases 5.5.3, 5.6.1 and 5.7
simultaneously, you are required to download the installer from the latest ROCm
release 5.7.

### Add required repositories

You must add the ROCm repositories manually for all ROCm releases
you want to install except the latest one. The `amdgpu-install` script
automatically adds the required repositories for the latest release.

Run the following commands based on your distribution to add the repositories:

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{tab-set}
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
for ver in 5.5.3 5.6.1 5.7; do
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver jammy main" | sudo tee /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
for ver in 5.5.3 5.6.1 5.7; do
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver focal main" | sudo tee /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
::::
:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{tab-set}
:::{tab-item} RHEL 9
:sync: RHEL-9

```shell
for ver in 5.5.3 5.6.1 5.7; do
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
:::{tab-item} RHEL 8
:sync: RHEL-8

```shell
for ver in 5.5.3 5.6.1 5.7; do
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
::::
:::::
:::::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

```shell
for ver in 5.5.3 5.6.1 5.7; do
sudo tee --append /etc/zypp/repos.d/rocm.repo <<EOF
name=rocm
baseurl=https://repo.radeon.com/rocm/zyp/$ver/main
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo zypper ref
```

:::::
::::::

### Install packages

Use the installer script as given below:

```none
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-1>
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-2>
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-3>
```

Following are examples of ROCm multi-version installation. The kernel-mode
driver, associated with the ROCm release 5.7, will be installed as its latest
release in the list.

```none
sudo amdgpu-install --usecase=rocm --rocmrelease=5.7
sudo amdgpu-install --usecase=rocm --rocmrelease=5.6.1
sudo amdgpu-install --usecase=rocm --rocmrelease=5.5.3
```

### Additional options

1. Unattended installation.
      Adding `-y` as a parameter to `amdgpu-install` skips user prompts (for
      automation). Example: `amdgpu-install -y --usecase=rocm`

2. Skipping kernel mode driver installation.
      The installer script tries to install the kernel mode driver
      along with the requested use cases. This might be unnecessary as in the case of docker containers or
      you may wish to keep a specific version when using multi-version installation, and not have the last
      installed version overwrite the kernel mode driver.

      To skip the installation of the kernel-mode driver add the `--no-dkms` option
      when calling the installer script.

:::::::
::::::::

## Upgrade ROCm

::::::::{tab-set}

:::::::{tab-item} Linux package manager
:sync: package

The upgrade procedure with the installer script is exactly the same as installing for first-time use.

:::::::

:::::::{tab-item} AMDGPU
:sync: amdgpu

Note that package upgrade is applicable to single-version packages only. If the preference is to install
an updated version of the ROCm along with the currently installed version, refer to the [](install) page.

1. Update the AMDGPU repository.

      ::::::{tab-set}
      :::::{tab-item} Ubuntu
      :sync: ubuntu

      ::::{tab-set}
      :::{tab-item} Ubuntu 22.04
      :sync: ubuntu-22.04

      ```shell
         # version
         version=5.7

         # amdgpu repository for jammy
         echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/$version/ubuntu jammy main" \
            | sudo tee /etc/apt/sources.list.d/amdgpu.list
         sudo apt update
      ```

      :::
      :::{tab-item} Ubuntu 20.04
      :sync: ubuntu-20.04

      ```shell
         # version
         version=5.7

         # amdgpu repository for focal
         echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/$version/ubuntu focal main" \
            | sudo tee /etc/apt/sources.list.d/amdgpu.list
         sudo apt update
      ```

      :::
      ::::
      :::::
      :::::{tab-item} Red Hat Enterprise Linux
      :sync: RHEL
      ::::{tab-set}
      :::{tab-item} RHEL 9.2
      :sync: RHEL-9.2
      :sync: RHEL-9

      ```shell
         # version
         version=5.7

         sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
         [amdgpu]
         name=amdgpu
         baseurl=https://repo.radeon.com/amdgpu/$version/rhel/9.2/main/x86_64/
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
         # version
         version=5.7

         sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
         [amdgpu]
         name=amdgpu
         baseurl=https://repo.radeon.com/amdgpu/$version/rhel/9.1/main/x86_64/
         enabled=1
         priority=50
         gpgcheck=1
         gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
         EOF
         sudo yum clean all
      ```

      :::
      :::{tab-item} RHEL 8.8
      :sync: RHEL-8.8
      :sync: RHEL-8

      ```shell
         # version
         version=5.7

         sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
         [amdgpu]
         name=amdgpu
         baseurl=https://repo.radeon.com/amdgpu/$version/rhel/8.8/main/x86_64/
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
         # version
         version=5.7

         sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
         [amdgpu]
         name=amdgpu
         baseurl=https://repo.radeon.com/amdgpu/$version/rhel/8.7/main/x86_64/
         enabled=1
         priority=50
         gpgcheck=1
         gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
         EOF
         sudo yum clean all
      ```

      :::
      :::{tab-item} RHEL 8.6
      :sync: RHEL-8.6
      :sync: RHEL-8

      ```shell
         # version
         version=5.7

         sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
         [amdgpu]
         name=amdgpu
         baseurl=https://repo.radeon.com/amdgpu/$version/rhel/8.6/main/x86_64/
         enabled=1
         priority=50
         gpgcheck=1
         gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
         EOF
         sudo yum clean all
      ```

      :::
      ::::
      :::::

      :::::{tab-item} SUSE Linux Enterprise Server
      :sync: SLES

      ::::{tab-set}
      :::{tab-item} SLES 15.5
      :sync: SLES-15.5

      ```shell
         # version
         version=5.7

         sudo tee /etc/zypp/repos.d/amdgpu.repo <<EOF
         [amdgpu]
         name=amdgpu
         baseurl=https://repo.radeon.com/amdgpu/$version/sle/15.5/main/x86_64
         enabled=1
         gpgcheck=1
         gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
         EOF
         sudo zypper ref
      ```

      :::
      :::{tab-item} SLES 15.4
      :sync: SLES-15.4

      ```shell
         # version
         version=5.7

         sudo tee /etc/zypp/repos.d/amdgpu.repo <<EOF
         [amdgpu]
         name=amdgpu
         baseurl=https://repo.radeon.com/amdgpu/$version/sle/15.4/main/x86_64
         enabled=1
         gpgcheck=1
         gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
         EOF
         sudo zypper ref
      ```

      :::
      ::::
      :::::
      ::::::

2. Upgrade the kernel-mode driver and reboot the system.

    ::::{tab-set}
    :::{tab-item} Ubuntu
    :sync: ubuntu

    ```shell
        sudo apt install amdgpu-dkms
        sudo reboot
    ```

    :::
    :::{tab-item} Red Hat Enterprise Linux
    :sync: RHEL

    ```shell
        sudo yum install amdgpu-dkms
        sudo reboot
    ```

    :::
    :::{tab-item} SUSE Linux Enterprise Server
    :sync: SLES

    ```shell
        sudo zypper --gpg-auto-import-keys install amdgpu-dkms
        sudo reboot
    ```

    :::
    ::::

3. Update the ROCm repository.

    ::::::{tab-set}
    :::::{tab-item} Ubuntu
    :sync: ubuntu

    ::::{tab-set}
    :::{tab-item} Ubuntu 22.04
    :sync: ubuntu-22.04

    ```shell
        # version
        version=5.7


        echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$version jammy main" \
            | sudo tee /etc/apt/sources.list.d/rocm.list
        echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
            | sudo tee /etc/apt/preferences.d/rocm-pin-600
        sudo apt update
    ```

    :::
    :::{tab-item} Ubuntu 20.04
    :sync: ubuntu-20.04

    ```shell
        # version
        version=5.7


        echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$version focal main" \
            | sudo tee /etc/apt/sources.list.d/rocm.list
        echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
            | sudo tee /etc/apt/preferences.d/rocm-pin-600
        sudo apt update
    ```

    :::
    ::::
    :::::
    :::::{tab-item} Red Hat Enterprise Linux
    :sync: RHEL

    ::::{tab-set}
    :::{tab-item} RHEL 9
    :sync: RHEL-9

    ```shell
        # version
        version=5.7


        sudo tee /etc/yum.repos.d/rocm.repo <<EOF
        [ROCm-$ver]
        name=ROCm$ver
        baseurl=https://repo.radeon.com/rocm/rhel9/$version/main
        enabled=1
        priority=50
        gpgcheck=1
        gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
        EOF
        sudo yum clean all
    ```

    :::
    :::{tab-item} RHEL 8
    :sync: RHEL-8

    ```shell
        # version
        version=5.7


        sudo tee /etc/yum.repos.d/rocm.repo <<EOF
        [ROCm-$ver]
        name=ROCm$ver
        baseurl=https://repo.radeon.com/rocm/rhel8/$version/main
        enabled=1
        priority=50
        gpgcheck=1
        gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
        EOF
        sudo yum clean all
    ```

    :::
    ::::
    :::::
    :::::{tab-item} SUSE Linux Enterprise Server
    :sync: SLES

    ```shell
        # version
        version=5.7

        sudo tee /etc/zypp/repos.d/rocm.repo <<EOF
        [ROCm-$ver]
        name=ROCm$ver
        name=rocm
        baseurl=https://repo.radeon.com/rocm/zyp/$version/main
        enabled=1
        gpgcheck=1
        gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
        EOF
        sudo zypper ref
    ```

    :::::
    ::::::

4. Upgrade the ROCm packages.

    ::::{tab-set}
    :::{tab-item} Ubuntu
    :sync: ubuntu

    ```shell
        sudo apt install --only-upgrade rocm-hip-sdk
    ```

    :::
    :::{tab-item} Red Hat Enterprise Linux
    :sync: RHEL

    ```shell
        sudo yum update rocm-hip-sdk
    ```

    :::
    :::{tab-item} Suse Linux Enterprise Server
    :sync: SLES

    ```shell
        sudo zypper --gpg-auto-import-keys update rocm-hip-sdk
    ```

    :::
    ::::

:::::::
::::::::

## Uninstall ROCm

To uninstall all ROCm packages and the kernel-mode driver the following commands
can be used.

::::{rubric} Uninstalling Single-Version Install
::::

```console shell
sudo amdgpu-install --uninstall
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
