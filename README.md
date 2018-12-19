## Are You Ready to ROCK?
The ROCm Platform brings a rich foundation to advanced computing by seamlessly
integrating the CPU and GPU with the goal of solving real-world problems.
This software enables the high-performance operation of AMD GPUs for computationally-oriented tasks in the Linux operating system.

### Current ROCm Version: 2.0

- [Hardware Support](#hardware-support)
  * [Supported GPUs](#supported-gpus)
  * [Supported CPUs](#supported-cpus)
  * [Not supported or very limited support under ROCm](#not-supported-or-very-limited-support-under-rocm)
- [New features and enhancements in ROCm 2.0](#new-features-and-enhancements-in-rocm-20)
- [New features and enhancements in ROCm 1.9.2](#new-features-and-enhancements-in-rocm-192)
- [New features and enhancements in ROCm 1.9.1](#new-features-and-enhancements-in-rocm-191)
- [New features and enhancements in ROCm 1.9.0](#new-features-and-enhancements-in-rocm-190)
- [The latest ROCm platform - ROCm 2.0](#the-latest-rocm-platform---rocm-20)
- [Installing from AMD ROCm repositories](#installing-from-amd-rocm-repositories)
  * [Ubuntu Support - Installing from a Debian repository](#ubuntu-support---installing-from-a-debian-repository)
  * [CentOS/RHEL 7 (7.4, 7.5 and 7.6) Support](#centosrhel-7-74-75-76-support)
- [Known Issues / Workarounds](#known-issues--workarounds)
- [Closed source components](#closed-source-components)
- [Getting ROCm source code](#getting-rocm-source-code)

### Hardware Support
ROCm is focused on using AMD GPUs to accelerate computational tasks, such as machine learning, engineering workloads, and scientific computing. In order to focus our development efforts on these domains of interest, ROCm supports a targeted set of hardware configurations which are detailed further in this section. 

#### Supported GPUs
Because the ROCm Platform has a focus on particular computational domains, we offer official support for a selection of AMD GPUs that are designed to offer good performance and price in these domains.

ROCm officially supports AMD GPUs that have use following chips:
  * GFX8 GPUs
    * "Fiji" chips, such as on the the AMD Radeon R9 Fury X and Radeon Instinct MI8
    * "Polaris 10" chips, such as on the AMD Radeon RX 580 and Radeon Instinct MI6
    * "Polaris 11" chips, such as on the AMD Radeon RX 570 and Radeon Pro WX 4100
  * GFX9 GPUs
    * "Vega 10" chips, such as on the AMD Radeon Radeon RX Vega 64 and Radeon Instinct MI25
    * Vega 7nm

ROCm is a collection of software ranging from drivers and runtimes to libraries and developer tools.
Some of this software may work with more GPUs than the "officially supported" list above, though AMD does not make any official claims of support for these devices on the ROCm software platform.
The following list of GPUs are likely to work within ROCm, though full support is not guaranteed:
  * GFX7 GPUs
    * "Hawaii" chips, such as the AMD Radeon R9 390X and FirePro W9100

As described in the next section, GFX8 GPUs require PCIe gen 3 with support for PCIe atomics. This requires both CPU and motherboard support. GFX9 GPUs, by default, also require PCIe gen 3 with support for PCIe atomics, but they can operate in most cases without this capability.

At this time, the integrated GPUs in AMD APUs are not officially supported targets for ROCm.

For a more detailed list of hardware support, please see [the following documentation](https://rocm.github.io/hardware.html).

#### Supported CPUs
As described above, GFX8 and GFX9 GPUs require PCI Express 3.0 with PCIe atomics in the default ROCm configuration.
In particular, the CPU and every active PCIe point between the CPU and GPU require support for PCIe gen 3 and PCIe atomics.
The CPU root must indicate PCIe AtomicOp Completion capabilities and any intermediate switch must indicate PCIe AtomicOp Routing capabilities.

Current CPUs which support PCIe Gen3 + PCIe Atomics are: 
  * AMD Ryzen CPUs;
  * AMD Ryzen APUs;
  * AMD Ryzen Threadripper CPUs
  * AMD EPYC CPUs;  
  * Intel Xeon E7 v3 or newer CPUs;
  * Intel Xeon E5 v3 or newer CPUs; 
  * Intel Xeon E3 v3 or newer CPUs;
  * Intel Core i7 v4, Core i5 v4, Core i3 v4 or newer CPUs (i.e. Haswell family or newer).
  * Some Ivy Bridge-E systems

Beginning with ROCm 1.8, we have relaxed the requirements for PCIe Atomics on GFX9 GPUs such as Vega 10.
We have similarly opened up more options for number of PCIe lanes.
GFX9 GPUs can now be run on CPUs without PCIe atomics and on older PCIe generations such as gen 2.
This is not supported on GPUs below GFX9, e.g. GFX8 cards in Fiji and Polaris families.

If you are using any PCIe switches in your system, please note that PCIe Atomics are only supported on some switches, such as Broadcom PLX.
When you install your GPUs, make sure you install them in a fully PCIe Gen3 x16 or x8, x4 or x1 slot attached either directly to the CPU's Root I/O controller or via a PCIe switch directly attached to the CPU's Root I/O controller.

In our experience, many issues stem from trying to use consumer motherboards which provide physical x16 connectors that are electrically connected as e.g. PCIe Gen2 x4, PCIe slots connected via the Southbridge PCIe I/O controller, or PCIe slots connected through a PCIe switch that does
not support PCIe atomics.

If you attempt to run ROCm on a system without proper PCIe atomic support, you may see an error in the kernel log (`dmesg`):
```
kfd: skipped device 1002:7300, PCI rejects atomics
```

Experimental support for our Hawaii (GFX7) GPUs (Radeon R9 290, R9 390, FirePro W9100, S9150, S9170)
does not require or take advantage of PCIe Atomics. However, we still recommend that you use a CPU
from the list provided above for compatibility purposes.

#### Not supported or very limited support under ROCm 
###### Limited support 

* ROCm 2.0.x should support PCIe Gen2 enabled CPUs such as the AMD Opteron, Phenom, Phenom II, Athlon, Athlon X2, Athlon II and older Intel Xeon and Intel Core Architecture and Pentium CPUs. However, we have done very limited testing on these configurations, since our test farm has been catering to CPU listed above. This is where we need community support; if you find problems on such setups, please report these issues.
 * Thunderbolt 1, 2, and 3 enabled breakout boxes should now be able to work with ROCm. Thunderbolt 1 and 2 are PCIe Gen2 based, and thus are only supported with GPUs that do not require PCIe Gen 3 atomics (i.e. Vega 10). However, we have done no testing on this configuration and would need comunity support due to limited access to this type of equipment 

###### Not supported 

* "Tonga", "Iceland", "Polaris 12", and "Vega M" GPUs are not supported in ROCm 2.0.x
* We do not support GFX8-class GPUs (Fiji, Polaris, etc.) on CPUs that do not have PCIe Gen 3 with PCIe atomics.
  * As such, do not support AMD Carrizo and Kaveri APUs as hosts for such GPUs..
  * Thunderbolt 1 and 2 enabled GPUs are not supported by GFX8 GPUs on ROCm. Thunderbolt 1 & 2 are PCIe Gen2 based.
* AMD Carrizo based APUs have limited support due to OEM & ODM's choices when it comes to some key configuration parameters. In particular, we have observed that Carrizo laptops, AIOs, and desktop systems showed inconsistencies in exposing and enabling the System BIOS parameters required by the ROCm stack. Before purchasing a Carrizo system for ROCm, please verify that the BIOS provides an option for enabling IOMMUv2 and that the system BIOS properly exposes the correct CRAT table - please inquire with the OEM about the latter.
 * AMD Merlin/Falcon Embedded System is not currently supported by the public repo.
 * AMD Raven Ridge APU are currently not supported as GPU targets

### New features and enhancements in ROCm 2.0

#### Adds support for RHEL 7.6 / CentOS 7.6 and Ubuntu 18.04.1

#### Adds support for Vega 7nm

#### Introduces MIVisionX
* A comprehensive computer vision and machine intelligence libraries, utilities and applications bundled into a single toolkit.

#### Improvements to ROCm Libraries
* rocSPARSE & hipSPARSE 
* rocBLAS with improved DGEMM efficiency on Vega 7nm

#### MIOpen
* This release contains general bug fixes and an updated performance database
* Group convolutions backwards weights performance has been improved
* RNNs now support fp16

#### Tensorflow multi-gpu and Tensorflow FP16 support for Vega 7nm
* TensorFlow v1.12 is enabled with fp16 support

#### PyTorch/Caffe2 with Vega 7nm Support
* fp16 support is enabled
* Several bug fixes and performance enhancements
* Known Issue: breaking changes are introduced in ROCm 2.0 which are not addressed upstream yet. Meanwhile, please continue to use ROCm fork at https://github.com/ROCmSoftwarePlatform/pytorch

#### Improvements to ROCProfiler tool
* Support for Vega 7nm

#### Support for hipStreamCreateWithPriority
* Creates a stream with the specified priority. It creates a stream on which enqueued kernels have a different priority for execution compared to kernels enqueued on normal priority streams. The priority could be higher or lower than normal priority streams.

#### OpenCL 2.0 support
* ROCm 2.0 introduces full support for kernels written in the OpenCL 2.0 C language on certain devices and systems.  Applications can detect this support by calling the “clGetDeviceInfo” query function with “parame_name” argument set to “CL_DEVICE_OPENCL_C_VERSION”.  In order to make use of OpenCL 2.0 C language features, the application must include the option “-cl-std=CL2.0” in options passed to the runtime API calls responsible for compiling or building device programs.  The complete specification for the OpenCL 2.0 C language can be obtained using the following link: https://www.khronos.org/registry/OpenCL/specs/opencl-2.0-openclc.pdf 

#### Improved Virtual Addressing (48 bit VA) management for Vega 10 and later GPUs
* Fixes Clang AddressSanitizer and potentially other 3rd-party memory debugging tools with ROCm
* Small performance improvement on workloads that do a lot of memory management
* Removes virtual address space limitations on systems with more VRAM than system memory

#### Kubernetes support
 
### New features and enhancements in ROCm 1.9.2
#### RDMA(MPI) support on Vega 7nm
* Support ROCnRDMA based on Mellanox InfiniBand

#### Improvements to HCC
* Improved link time optimization

#### Improvements to ROCProfiler tool
* General bug fixes and implemented versioning APIs

### New features and enhancements in ROCm 1.9.2
#### RDMA(MPI) support on Vega 7nm
* Support ROCnRDMA based on Mellanox InfiniBand

#### Improvements to HCC
* Improved link time optimization

#### Improvements to ROCProfiler tool
* General bug fixes and implemented versioning APIs

#### Critical bug fixes

### New features and enhancements in ROCm 1.9.1
#### Added DPM support to Vega 7nm
* Dynamic Power Management feature is enabled on Vega 7nm.
 
#### Fix for 'ROCm profiling' that used to fail with a “Version mismatch between HSA runtime and libhsa-runtime-tools64.so.1” error

### New features and enhancements in ROCm 1.9.0

#### Preview for Vega 7nm
* Enables developer preview support for Vega 7nm

#### System Management Interface
* Adds support for the ROCm SMI (System Management Interface) library, which provides monitoring and management capabilities for AMD GPUs.

#### Improvements to HIP/HCC
* Support for gfx906
* Added deprecation warning for C++AMP.  This will be the last version of HCC supporting C++AMP.
* Improved optimization for global address space pointers passing into a GPU kernel
* Fixed several race conditions in the HCC runtime
* Performance tuning to the unpinned copy engine
* Several codegen enhancement fixes in the compiler backend

#### Preview for rocprof Profiling Tool
Developer preview (alpha) of profiling tool rocProfiler. It includes a command-line front-end, `rpl_run.sh`, which enables:
* Cmd-line tool for dumping public per kernel perf-counters/metrics and kernel timestamps
* Input file with counters list and kernels selecting parameters
* Multiple counters groups and app runs supported
* Output results in CSV format

The tool can be installed from the `rocprofiler-dev` package. It will be installed into: /opt/rocm/bin/rpl_run.sh

#### Preview for rocr Debug Agent rocr_debug_agent
The ROCr Debug Agent is a library that can be loaded by ROCm Platform Runtime to provide the following functionality:
* Print the state for wavefronts that report memory violation or upon executing a "s_trap 2" instruction.
* Allows SIGINT (`ctrl c`) or SIGTERM (`kill -15`) to print wavefront state of aborted GPU dispatches.
* It is enabled on Vega10 GPUs on ROCm1.9.

The ROCm1.9 release will install the ROCr Debug Agent library at /opt/rocm/lib/librocr_debug_agent64.so


#### New distribution support 

* Binary package support for Ubuntu 18.04

#### ROCm 1.9 is ABI compatible with KFD in upstream Linux kernels. 
Upstream Linux kernels support the following GPUs in these releases:
4.17: Fiji, Polaris 10, Polaris 11
4.18: Fiji, Polaris 10, Polaris 11, Vega10

Some ROCm features are not available in the upstream KFD:
* More system memory available to ROCm applications
* Interoperability between graphics and compute
* RDMA
* IPC

To try ROCm with an upstream kernel, install ROCm as normal, but do not install the rock-dkms package. Also add a udev rule to control /dev/kfd permissions:

    echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules


### New features as of ROCm 1.8.3

* ROCm 1.8.3 is a minor update meant to fix compatibility issues on Ubuntu releases running kernel 4.15.0-33

### New features as of ROCm 1.8.2

#### DKMS driver installation

 * Debian packages are provided for DKMS on Ubuntu
 * RPM packages are provided for CentOS/RHEL 7.4 and 7.5 support
 * See the [ROCT-Thunk-Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/roc-1.8.x) and [ROCK-Kernel-Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/roc-1.8.x) for additional documentation on driver setup

#### New distribution support 

 * Binary package support for Ubuntu 16.04 and 18.04
 * Binary package support for CentOS 7.4 and 7.5
 * Binary package support for RHEL 7.4 and 7.5
 
#### Improved OpenMPI via UCX support 

 * UCX support for OpenMPI
 * ROCm RDMA

### The latest ROCm platform - ROCm 2.0

The latest tested version of the drivers, tools, libraries and source code for
the ROCm platform have been released and are available under the roc-2.0.0 or rocm-2.0.x tag
of the following GitHub repositories:

* [ROCK-Kernel-Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/roc-2.0.x)
* [ROCR-Runtime](https://github.com/RadeonOpenCompute/ROCR-Runtime/tree/roc-2.0.x)
* [ROCT-Thunk-Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/roc-2.0.x)
* [ROC-smi](https://github.com/RadeonOpenCompute/ROC-smi/tree/roc-2.0.x)
* [HCC compiler](https://github.com/RadeonOpenCompute/hcc/tree/roc-2.0.x)
* [compiler-runtime](https://github.com/RadeonOpenCompute/compiler-rt/tree/roc-2.0.x)
* [HIP](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/tree/roc-2.0.x)
* [HIP-Examples](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP-Examples/tree/roc-2.0.x)
* [atmi](https://github.com/RadeonOpenCompute/atmi/tree/0.3.7)

Additionally, the following mirror repositories that support the HCC compiler
are also available on GitHub, and frozen for the rocm-2.0.x release:

* [llvm](https://github.com/RadeonOpenCompute/llvm/tree/roc-2.0.x)
* [ldd](https://github.com/RadeonOpenCompute/lld/tree/roc-2.0.x)
* [hcc-clang-upgrade](https://github.com/RadeonOpenCompute/hcc-clang-upgrade/tree/roc-2.0.x)
* [ROCm-Device-Libs](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/tree/roc-2.0.x)

#### Supported Operating Systems - New operating systems available

The ROCm 2.0.x platform supports the following operating systems:
 * Ubuntu 16.04.x & 18.04.x (Version 16.04.3 and newer or kernels 4.13 and newer)
 * CentOS 7.4 & 7.5 & 7.6 (Using devtoolset-7 runtime support)
 * RHEL 7.4 & 7.5 & 7.6 (Using devtoolset-7 runtime support)

### Installing from AMD ROCm repositories

AMD is hosting both Debian and RPM repositories for the ROCm 2.0.x packages at this time.

The packages in the Debian repository have been signed to ensure package integrity.

#### Ubuntu Support - installing from a Debian repository

##### First make sure your system is up to date 

```shell
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot
```

##### Add the ROCm apt repository

For Debian based systems, like Ubuntu, configure the Debian ROCm repository as
follows:

```shell
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
```
The gpg key might change, so it may need to be updated when installing a new release. 
If the key signature verification is failed while update, please re-add the key from 
ROCm apt repository. The current rocm.gpg.key is not available in a standard key ring 
distribution, but has the following sha1sum hash:

f7f8147431c75e505c58a6f3a3548510869357a6  rocm.gpg.key

##### Install

Next, update the apt repository list and install the rocm package:

>**Warning**: Before proceeding, make sure to completely
>[uninstall any previous ROCm package](https://github.com/RadeonOpenCompute/ROCm#removing-pre-release-packages):

```shell
sudo apt update
sudo apt install rocm-dkms
```

###### Next set your permissions 

With move to upstreaming the KFD driver and the support of DKMS,  for all Console aka headless user, you will need to add all  your users to the  'video" group by setting the Unix permissions

Configure 
Ensure that your user account is a member of the "video" group prior to using the ROCm driver. You can find which groups you are a member of with the following command:

```shell
groups
```

To add yourself to the video group you will need the sudo password and can use the following command:

```shell
sudo usermod -a -G video $LOGNAME 
``` 

You may want to ensure that any future users you add to your system are put into the "video" group by default. To do that, you can run the following commands:
```shell
echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
```

Once complete, reboot your system.

Upon Reboot run the following commands to verify that the ROCm installation was successful. If you see your GPUs listed by both of these commands, you should be ready to go!
```shell
/opt/rocm/bin/rocminfo 
/opt/rocm/opencl/bin/x86_64/clinfo 
``` 

Note that, to make running ROCm programs easier, you may wish to put the ROCm libraries in your LD_LIBRARY_PATH environment variable and the ROCm binaries in your PATH.
```shell
echo 'export LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:$LD_LIBRARY_PATH' | sudo tee -a /etc/profile.d/rocm.sh
echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/x86_64' | sudo tee -a /etc/profile.d/rocm.sh
```

If you have an [Install Issue](https://rocm.github.io/install_issues.html) please read this FAQ .

###### Performing an OpenCL-only Installation of ROCm

Some users may want to install a subset of the full ROCm installation. In particular, if you are trying to install on a system with a limited amount of storage space, or which will only run a small collection of known applications, you may want to install only the packages that are required to run OpenCL applications. To do that, you can run the following installation command **instead** of the command to install `rocm-dkms`.

```shell
sudo apt-get install dkms rock-dkms rocm-opencl
```

###### Upon restart, to test your OpenCL instance 

Build and run Hello World OCL app.

HelloWorld sample:

```shell
 wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cpp
 wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cl
```

 Build it using the default ROCm OpenCL include and library locations:

```shell
g++ -I /opt/rocm/opencl/include/ ./HelloWorld.cpp -o HelloWorld -L/opt/rocm/opencl/lib/x86_64 -lOpenCL
```

 Run it:

 ```shell
 ./HelloWorld
```

##### How to un-install from Ubuntu 16.04 or Ubuntu 18.04

To un-install the entire rocm development package execute:

```shell
sudo apt autoremove rocm-dkms
```

##### Installing development packages for cross compilation

It is often useful to develop and test on different systems. In this scenario,
you may prefer to avoid installing the ROCm Kernel to your development system.

In this case, install the development subset of packages:

```shell
sudo apt update
sudo apt install rocm-dev
```

>**Note:** To execute ROCm enabled apps you will require a system with the full
>ROCm driver stack installed

##### Removing pre-release packages
It is recommended to [remove previous rocm installations](https://github.com/RadeonOpenCompute/ROCm#how-to-un-install-from-ubuntu-1604-or-ubuntu-1804) before installing the latest version to ensure a smooth installation.

If you installed any of the ROCm pre-release packages from github, they will
need to be manually un-installed:

```shell
sudo apt purge hsakmt-roct
sudo apt purge hsakmt-roct-dev
sudo apt purge compute-firmware
sudo apt purge $(dpkg -l | grep 'kfd\|rocm' | grep linux | grep -v libc | awk '{print $2}')
```

If possible, we would recommend starting with a fresh OS install.

#### CentOS/RHEL 7 (7.4, 7.5, 7.6) Support

Support for CentOS/RHEL 7 has been added in ROCm 1.8, but requires a special 
runtime environment provided by the RHEL Software Collections and additional
dkms support packages to properly install in run.

##### Preparing RHEL 7 (7.4, 7.5, 7.6) for installation

RHEL is a subscription based operating system, and must enable several external
repositories to enable installation of the devtoolset-7 environment and the DKMS
support files. These steps are not required for CentOS.

First, the subscription for RHEL must be enabled and attached to a pool id. Please
see Obtaining an RHEL image and license page for instructions on registering your
system with the RHEL subscription server and attaching to a pool id.


Second, enable the following repositories:

```shell
sudo subscription-manager repos --enable rhel-server-rhscl-7-rpms
sudo subscription-manager repos --enable rhel-7-server-optional-rpms
sudo subscription-manager repos --enable rhel-7-server-extras-rpms
```

Third, enable additional repositories by downloading and installing the epel-release-latest-7 repository RPM:

```shell
sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

##### Install and setup Devtoolset-7

To setup the Devtoolset-7 environment, follow the instructions on this page:

https://www.softwarecollections.org/en/scls/rhscl/devtoolset-7/

Note that devtoolset-7 is a Software Collections package, and is not supported by AMD.

##### Prepare CentOS/RHEL (7.4, 7.5, 7.6) for DKMS Install

Installing kernel drivers on CentOS/RHEL 7.4/7.5/7.6 requires dkms tool being installed:

```shell
sudo yum install -y epel-release
sudo yum install -y dkms kernel-headers-`uname -r` kernel-devel-`uname -r`
```


##### Installing ROCm on the system

It is recommended to [remove previous rocm installations](https://github.com/RadeonOpenCompute/ROCm#how-to-un-install-rocm-from-centosrhel-74-75-and-76) before installing the latest version to ensure a smooth installation.

At this point ROCm can be installed on the target system. Create a /etc/yum.repos.d/rocm.repo file with the following contents:

```shell
[ROCm]
name=ROCm
baseurl=http://repo.radeon.com/rocm/yum/rpm
enabled=1
gpgcheck=0
```

The repo's URL should point to the location of the repositories repodata database. Install ROCm components using these commands:

```shell
sudo yum install rocm-dkms
```

The rock-dkms component should be installed and the /dev/kfd device should be available on reboot.

Ensure that your user account is a member of the "video" or "wheel" group prior to using the ROCm driver.
You can find which groups you are a member of with the following command:

```shell
groups
```

To add yourself to the video (or wheel) group you will need the sudo password and can use the
following command:

```shell
sudo usermod -a -G video $LOGNAME 
```

Current release supports CentOS/RHEL 7.4, 7.5, 7.6. If users want to update the OS version, they should completely remove ROCm packages before updating to the latest version of the OS, to avoid DKMS related issues.

###### Performing an OpenCL-only Installation of ROCm

Some users may want to install a subset of the full ROCm installation. In particular, if you are trying to install on a system with a limited amount of storage space, or which will only run a small collection of known applications, you may want to install only the packages that are required to run OpenCL applications. To do that, you can run the following installation command **instead** of the command to install `rocm-dkms`.

```shell
sudo yum install rock-dkms rocm-opencl
```

##### Compiling applications using hcc, hip, etc.

To compile applications or samples, please use gcc-7.2 provided by the devtoolset-7 environment.
To do this, compile all applications after running this command: 

```shell
scl enable devtoolset-7 bash
```
##### How to un-install ROCm from CentOS/RHEL 7.4, 7.5 and 7.6

To un-install the entire rocm development package execute:

```shell
sudo yum autoremove rocm-dkms
```

### Known Issues / Workarounds

#### HCC: removed support for C++AMP

#### HipCaffe is supported on single GPU configurations

#### The ROCm SMI library calls to rsmi_dev_power_cap_set() and rsmi_dev_power_profile_set() will not work for all but the first gpu in multi-gpu set ups.

### Closed source components

The ROCm platform relies on a few closed source components to provide functionality
such as HSA image support. These components are only available through the ROCm
repositories, and will either be deprecated or become open source components in the
future. These components are made available in the following packages:

*  hsa-ext-rocr-dev

### Getting ROCm source code

Modifications can be made to the ROCm 2.0 components by modifying the open
source code base and rebuilding the components. Source code can be cloned from
each of the GitHub repositories using git, or users can use the repo command
and the ROCm 2.0 manifest file to download the entire ROCm 2.0 source code.

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
repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-2.0.0
repo sync
```
These series of commands will pull all of the open source code associated with
the ROCm 2.0 release. Please ensure that ssh-keys are configured for the
target machine on GitHub for your GitHub ID.

* OpenCL Runtime and Compiler will be submitted to the Khronos Group, prior to
  the final release, for conformance testing.
