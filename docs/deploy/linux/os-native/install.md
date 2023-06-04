# Installation (Linux)

## Understanding the Release-specific AMDGPU and ROCm Stack Repositories on Linux Distributions

The release-specific repositories consist of packages from a specific release of
the AMDGPU stack and ROCm stack. The repositories are not updated for the latest
packages with subsequent releases. When a new ROCm release is available, the new
repository, specific to that release, is added. You can select a specific
release to install, update the previously installed single version to the later
available release, or add the latest version of ROCm along with the currently
installed version by using the multi-version ROCm packages.

## Step by Step Instructions

```{note}
Users installing multiple versions of the ROCm stack must use the
release-specific repository URL.
```

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
   for ver in 5.3.3 5.5.1; do
   echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver focal main" | sudo tee /etc/apt/sources.list.d/rocm.list
   done
   echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
   sudo apt update
   ```

   :::
   :::{tab-item} Ubuntu 22.04
   :sync: ubuntu-22.04

   ```shell
   for ver in 5.3.3 5.5.1; do
   echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver jammy main" | sudo tee --append /etc/apt/sources.list.d/rocm.list
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
   sudo apt install rocm-hip-sdk5.5.1 rocm-hip-sdk5.3.3
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

2. Add the ROCm Stack Repository and Install Meta-packages

   To add the ROCm repository, use the following steps:

   ```shell
   for ver in 5.3.3 5.5.1; do
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
   sudo yum install rocm-hip-sdk5.5.1 rocm-hip-sdk5.3.3
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

2. Add the ROCm Stack Repository and Install Meta-packages

   To add the ROCm repository, use the following steps:

   ```shell
   for ver in 5.3.3 5.5.1; do
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

:::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

```shell
sudo zypper search --installed-only
```

:::
::::
