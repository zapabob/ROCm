## Are You Ready to ROCK!
The ROCm Platform delivers on the vision of the  Boltzmann Initiative, bringing
new opportunities in GPU Computing Research.

On November 16th, 2015, the Radeon Technology Group rolled out Boltzmann
Initiative with three core foundation elements:

* New Linux(R) Driver and Runtime Stack optimized for HPC & Ultra-scale class
  computing,
* Heterogeneous C and C++ compiler which best address the whole system not just
  a single device
* HIP acknowledging the need for platform choice when utilizing GPU computing
  API

Using our knowledge of the HSA Standards and, more importantly, the HSA 1.1
Runtime we have been able to successfully extended support to the dGPU with
critical features for NUMA class acceleration. As a result, the ROCK driver is
composed of several components based on our efforts to develop the
Heterogeneous System Architecture for APUs, including the new AMDGPU driver,
the Kernel Fusion Driver (KFD), the HSA+ Runtime and an LLVM based compilation
stack for the building of key language support. This support starts with AMD’s
FIJI Family of dGPU, but support is planned to expand to include future ASICS.

### The Latest ROCm Platform - ROCm 1.1
The latest tested version of the drivers, tools, libraries and source code for
the ROCm platform have been released and are available under the roc-1.1.0 tag
of the following GitHub repositories:

* [ROCK-Kernel-Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/roc-1.1.0)
* [ROCR-Runtime](https://github.com/RadeonOpenCompute/ROCR-Runtime/tree/roc-1.1.0)
* [ROCT-Thunk-Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/roc-1.1.0)
* [HCC compiler](https://github.com/RadeonOpenCompute/hcc/tree/roc-1.1.0)
* [LLVM-AMDGPU-Assembler-Extra](https://github.com/RadeonOpenCompute/LLVM-AMDGPU-Assembler-Extra/tree/roc-1.1.0)
* [ROC-smi](https://github.com/RadeonOpenCompute/ROC-smi/tree/roc-1.1.0)
* [ROCnRDMA](https://github.com/RadeonOpenCompute/ROCnRDMA/tree/roc-1.1.0)
* [HIP](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/tree/roc-1.1.0)
* [HIP-Examples](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP-Examples/tree/roc-1.1.0)

In addition the following mirror repositories that support the HCC compiler are
also available on GitHub, and frozen for the roc-1.1.0 release:

* [llvm](https://github.com/RadeonOpenCompute/llvm/tree/roc-1.1.0)
* [clang](https://github.com/RadeonOpenCompute/clang/tree/roc-1.1.0)

### Installing from AMD ROCm Repositories
AMD is hosting both debian and rpm repositories for the ROCm 1.1 packages. The
packages in both repositories have been signed to ensure package integrity.
Directions for each repository are given below:

#### Supported Operating Systems

The ROCm platform has been tested on the following operating systems:
 * Ubuntu 14.04.04
 * Fedora 23

There is experimental support for the following operating systems:
 * Ubuntu 16.04
 * Fedora 22

#### Debian repository - apt-get

##### Add the ROCm apt repository
For Debian based systems, like Ubuntu, configure the Debian ROCm repository as
follows:

```shell
wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/ trusty main > /etc/apt/sources.list.d/rocm.list'
```

##### Install or Update
Next, update the apt-get repository list and install/update the rocm package:

>**Warning**: Before proceeding, make sure to completely
>[uninstall any pre-release ROCm packages](https://github.com/RadeonOpenCompute/ROCm#removing-pre-release-packages):

```shell
sudo apt-get update
sudo apt-get install rocm
```
Then, make the ROCm kernel your default kernel. If using grub2 as your
bootloader, you can edit the `GRUB_DEFAULT` variable in the following file:

```shell
sudo vi /etc/default/grub
sudo update-grub
```

Once complete, reboot your system.

We recommend you [verify your installation](https://github.com/RadeonOpenCompute/ROCm#verify-installation) to make sure everything completed successfully.

##### Un-install
To un-install the entire rocm-dev development package execute:

```shell
sudo apt-get autoremove rocm
```

##### Installing development packages for cross compilation
It is often useful to develop and test on different systems. In this scenario,
you may prefer to avoid installing the ROCm Kernel to your development system.

In this case, install the development subset of packages:

```shell
sudo apt-get update
sudo apt-get install rocm-dev
```

>**Note:** To execute ROCm enabled apps you will require a system with the full
>ROCm driver stack installed

##### Removing pre-release packages
If you installed any of the ROCm pre-release packages from github, they will
need to be manually un-installed:

```shell
sudo apt-get purge libhsakmt
sudo apt-get purge radeon-firmware
sudo apt-get purge $(dpkg -l | grep 'kfd\|rocm' | grep linux | grep -v libc | awk '{print $2}')
```

If possible, we would recommend starting with a fresh OS install.

#### RPM repository - dnf (yum)

A dnf (yum) repostiory is also available for installation of rpm packages. To configure a
system to use the ROCm rpm directory create the file /etc/yum.repos.d/rocm.repo with
the following contents:

```shell
[remote]

name=ROCm Repo

baseurl=http://packages.amd.com/rocm/yum/rpm/

enabled=1

gpgcheck=0
```
Execute the following commands:

```shell
sudo dnf clean all
sudo dnf install rocm
```

As with the debian packages, it is possible to install rocm-dev or rocm-kernel individually.
To uninstall the packages execute:

```shell
sudo dnf remove rocm
```

#### Verify Installation

To verify that the ROCm stack completed successfully you can execute to HSA
vectory\_copy sample application:

```shell
cd /opt/rocm/hsa/sample
make
./vector_copy
```

#### Closed Source Components
The ROCm platform relies on a few closed source components to provide legacy
functionality like HSAIL finalization and debugging/profiling support. These
components are only available through the ROCm repositories, and will either be
deprecated or become open source components in the future. These components are
made available in the following packages:

*  hsa-ext-rocr-dev

### Getting ROCm Source Code
Modifications can be made to the ROCm 1.1 components by modifying the open
source code base and rebuilding the components. Source code can be cloned from
each of the GitHub repositories using git, or users can use the repo command
and the ROCm 1.1 manifest file to download the entire ROCm 1.1 source code.

#### Installing repo
Google's repo tool allows you to manage multiple git repositories
simultaneously. You can install it by executing the following commands:

```shell
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
```
Note: make sure ~/bin exists and it is part of your PATH

#### Cloning the code
```shell
mkdir ROCm && cd ROCm
repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-1.1.0
repo sync
```

These series of commands will pull all of the open source code associated with
the ROCm 1.1 release.
