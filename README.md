# AMD ROCm™ v4.1 Release Notes 
This document describes the features, fixed issues, and information about downloading and installing the AMD ROCm™ software. It also covers known issues and deprecations in the AMD ROCm v4.1 release.

- [Supported Operating Systems and Documentation Updates](#Supported-Operating-Systems-and-Documentation-Updates)
  * [Supported Operating Systems](#Supported-Operating-Systems)
  * [ROCm Installation Updates](#ROCm-Installation-Updates)
  * [AMD ROCm Documentation Updates](#AMD-ROCm-Documentation-Updates)

- [Driver Compatibility Issue in This Release](#Driver-Compatibility-Issue-in-This-Release)
   
- [What\'s New in This Release](#Whats-New-in-This-Release)
  * [TargetID for Multiple Configurations](#TargetID-for-Multiple-Configurations)
  * [ROCm Data Center Tool](#ROCm-Data-Center-Tool)
  * [ROCm Math and Communication Libraries](#ROCm-Math-and-Communication-Libraries)
  * [HIP Enhancements](#HIP-Enhancements)
  * [OpenMP Enhancements and Fixes](#OpenMP-Enhancements-and-Fixes)
  * [MIOpen Tensile Integration](#MIOpen-Tensile-Integration)

    
- [Known Issues](#Known-Issues)

- [Deprecations](#Deprecations)

  * [Compiler Generated Code Object Version 2 Deprecation ](#Compiler-Generated-Code-Object-Version-2-Deprecation)

- [Deploying ROCm](#Deploying-ROCm)
 
- [Hardware and Software Support](#Hardware-and-Software-Support)

- [Machine Learning and High Performance Computing Software Stack for AMD GPU](#Machine-Learning-and-High-Performance-Computing-Software-Stack-for-AMD-GPU)
  * [ROCm Binary Package Structure](#ROCm-Binary-Package-Structure)
  * [ROCm Platform Packages](#ROCm-Platform-Packages)
  



## ROCm Installation Updates 

### List of Supported Operating Systems

The AMD ROCm platform is designed to support the following operating systems:

* Ubuntu 20.04.1 (5.4 and 5.6-oem) and 18.04.5 (Kernel 5.4)	
* CentOS 7.9 (3.10.0-1127) & RHEL 7.9 (3.10.0-1160.6.1.el7) (Using devtoolset-7 runtime support)
* CentOS 8.3 (4.18.0-193.el8) and RHEL 8.3 (4.18.0-193.1.1.el8) (devtoolset is not required)
* SLES 15 SP2

### FRESH INSTALLATION OF AMD ROCM V4.1 RECOMMENDED

A complete uninstallation of previous ROCm versions is required before installing a new version of ROCm. An upgrade from previous releases to AMD ROCm v4.1 is not supported. For more information, refer to the AMD ROCm Installation Guide at

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

**Note**: AMD ROCm release v3.3 or prior releases are not fully compatible with AMD ROCm v3.5 and higher versions. You must perform a fresh ROCm installation if you want to upgrade from AMD ROCm v3.3 or older to 3.5 or higher versions and vice-versa.

**Note**: *render* group is required only for Ubuntu v20.04. For all other ROCm supported operating systems, continue to use video group. 

* For ROCm v3.5 and releases thereafter, the clinfo path is changed to /opt/rocm/opencl/bin/clinfo. 

* For ROCm v3.3 and older releases, the clinfo path remains /opt/rocm/opencl/bin/x86_64/clinfo. 
 
### ROCM MULTI-VERSION INSTALLATION UPDATE

With the AMD ROCm v4.1 release, the following ROCm multi-version installation changes apply:

The meta packages rocm-dkms<version> are now deprecated for multi-version ROCm installs.  For example, rocm-dkms3.7.0, rocm-dkms3.8.0.
 
* Multi-version installation of ROCm should be performed by installing rocm-dev<version> using each of the desired ROCm versions. For example, rocm-dev3.7.0, rocm-dev3.8.0, rocm-dev3.9.0.   

* Version files must be created for each multi-version rocm <= 4.1.0

 * Command: echo <version> | sudo tee /opt/rocm-<version>/.info/version

 * Example: echo 4.1.0 | sudo tee /opt/rocm-4.1.0/.info/version

* The rock-dkms loadable kernel modules should be installed using a single rock-dkms package. 

* ROCm v3.9 and above will not set any ldconfig entries for ROCm libraries for multi-version installation.  Users must set LD_LIBRARY_PATH to load the ROCm library version of choice.

**NOTE**: The single version installation of the ROCm stack remains the same. The rocm-dkms package can be used for single version installs and is not deprecated at this time.



# Driver Compatibility Issue in This Release

In certain scenarios, the ROCm 4.1 run-time and userspace environment are not compatible with ROCm v4.0 and older driver implementations for 7nm-based (Vega 20) hardware (MI50 and MI60). 

To mitigate issues, the ROCm v4.1 or newer userspace prevents running older drivers for these GPUs.

Users are notified in the following scenarios:

* Bare Metal 
* Containers
 
## Bare Metal

In the bare-metal environment, the following error message displays in the console: 

*“HSA Error: Incompatible kernel and userspace, Vega 20 disabled. Upgrade amdgpu.”*

To test the compatibility, run the ROCm v4.1 version of rocminfo using the following instruction: 

*/opt/rocm-4.1.0/bin/rocminfo 2>&1 | less*

## Containers

A container (built with error detection for this issue) using a ROCm v4.1 or newer run-time is initiated to execute on an older kernel. The container fails to start and the following warning appears:

*Error: Incompatible ROCm environment. The Docker container requires the latest kernel driver to operate correctly.
Upgrade the ROCm kernel to v4.1 or newer, or use a container tagged for v4.0.1 or older.*

To inspect the version of the installed kernel driver,  run either: 

* dpkg --status rock-dkms [Debian-based]

or

* rpm -ql rock-dkms [RHEL, SUSE, and others]

To install or update the driver, follow the installation instructions at:

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html


# AMD ROCm Documentation Updates

## AMD ROCm Installation Guide 

The AMD ROCm Installation Guide in this release includes:

* Supported Environments

* Installation Instructions for v4.1

* HIP Installation Instructions 

For more information, refer to the ROCm documentation website at:

https://rocmdocs.amd.com/en/latest/


## AMD ROCm - HIP Documentation Updates

* HIP Programming Guide v4.1 

  https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_Programming_Guide_v4.1.pdf

* HIP API Guide v4.1

  https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_API_Guide_v4.1.pdf
  

* HIP-Supported CUDA API Reference Guide v4.1

  https://github.com/RadeonOpenCompute/ROCm/blob/master/HIP_Supported_CUDA_API_Reference_Guide_v4.1.pdf

* HIP FAQ  

  For more information, refer to

  https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-FAQ.html#hip-faq


## ROCm Data Center User and API Guide

* ROCm Data Center Tool User Guide

   - Grafana Plugin Integration

  For more information, refer to the ROCm Data Center User Guide at,

  https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_ROCm_DataCenter_Tool_User_Guide_v4.1.pdf
  

* ROCm Data Center Tool API Guide

  For more information, refer to the ROCm Data Center API Guide at,

  https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_Data_Center_Tool_API_Manual_4.1.pdf


## ROCm SMI API Documentation Updates 

* ROCm SMI API Guide 

  For more information, refer to the ROCm SMI API Guide at,

  https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_SMI_API_GUIDE_v4.1.pdf
  
## ROC Debugger User and API Guide 

* ROC Debugger User Guide 

  https://github.com/RadeonOpenCompute/ROCm/blob/master/Debugging%20with%20ROCGDB%20User%20Guide%20v4.1.pdf
  

* Debugger API Guide 

  https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD-Debugger%20API%20Guide%20v4.1.pdf


## General AMD ROCm Documentation Links

Access the following links for more information:

* For AMD ROCm documentation, see 

  https://rocmdocs.amd.com/en/latest/

* For installation instructions on supped platforms, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

* For AMD ROCm binary structure, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Software-Stack-for-AMD-GPU.html
  

* For AMD ROCm Release History, see

 https://rocmdocs.amd.com/en/latest/Current_Release_Notes/ROCm-Version-History.html



# What\'s New in This Release

## TARGETID FOR MULTIPLE CONFIGURATIONS

The new TargetID functionality allows compilations to specify various configurations of the supported hardware. 

Previously, ROCm supported only a single configuration per target. 

With the TargetID enhancement, ROCm supports configurations for Linux, PAL and associated configurations such as XNACK. This feature addresses configurations for the same target in different modes and allows applications to build executables that specify the supported configurations, including the option to be agnostic for the desired setting.


### New Code Object Format Version for TargetID

* A new clang option -mcode-object-version can be used to request the legacy code object version 3 or code object version 2. For more information, refer to

  https://llvm.org/docs/AMDGPUUsage.html#elf-code-object

* A new clang --offload-arch= option is introduced to specify the offload target architecture(s) for the HIP language.

* The clang --offload-arch= and -mcpu options accept a new Target ID syntax. This allows both the processor and target feature settings to be specified. For more details, refer to

  https://llvm.org/docs/AMDGPUUsage.html#amdgpu-target-id

    - If a target feature is not specified, it defaults to a new concept of "any". The compiler, then, produces code, 
      which executes on a target configured for either value of the setting impacting the overall performance. 
      
      It is recommended to explicitly specify the setting for more efficient performance. 

    - In particular, the setting for XNACK now defaults to produce less performant code than previous ROCm releases.

    - The legacy clang -mxnack, -mno-xnack, -msram-ecc, and -mno-sram-ecc options are deprecated. They are still 
      supported, however, they will be removed in a future release. 

    - The new Target ID syntax renames the SRAM ECC feature from sram-ecc to sramecc.

* The clang offload bundler uses the new offload hipv4 for HIP code object version 4. For more information, see 
https://clang.llvm.org/docs/ClangOffloadBundler.html

* ROCm v4.1 corrects code object loading to enforce target feature settings of the code object to match the setting of the agent. It also corrects the recording of target feature settings in the code object. As a consequence, the legacy code objects may no longer load due to mismatches.

* gfx802, gfx803, and gfx805 do not support the XNACK target feature in the ROCm v4.1 release.


### New Code Object Tools

AMD ROCm v4.1 provides new code object tools *roc-obj-ls* and *roc-obj-extract*. These tools allow for the listing and extraction of AMD GPU ROCm code objects that are embedded in HIP executables and shared objects. Each tool supports a --help option that provides more information. 

Refer to the HIP Programming Guide v4.1 for additional information and examples.

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_Programming_Guide_v4.1.pdf

**Note**

The extractkernel tool in previous AMD ROCm releases has been removed from the AMD ROCm v4.1 release 
and will no longer be  supported.

**Note**
 
 The roc-obj-ls and roc-obj-extract tools may generate an error about the following missing Perl modules: 

* File::Which
* File::BaseDir
* File::Copy
* URI::Encode

This error is due to the missing dependencies in the hip-base installer package.  As a workaround, you may use the 
following instructions to install the Perl modules:  

*Ubuntu*
     
     apt-get install libfile-which-perl libfile-basedir-perl libfile-copy-recursive-perl liburi-encode-perl
   
*CentOS*
            
      yum install “ perl(File::Which) perl(File::BaseDir) perl(File::Copy) perl(URI::Encode)



## ROCm Data Center Tool 

### Grafana Integration

The ROCm Data Center (RDC) Tool is enhanced with the Grafana plugin. Grafana is a common monitoring stack used for storing and visualizing time series data. Prometheus acts as the storage backend, and Grafana is used as the interface for analysis and visualization. Grafana has a plethora of visualization options and can be integrated with Prometheus for the ROCm Data Center (RDC) dashboard. 

For more information about Grafana integration and installation, refer to the ROCm Data Center Tool User guide at:

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_ROCm_DataCenter_Tool_User_Guide_v4.1.pdf



## ROCm Math and Communication Libraries 

### rocSPARSE

rocSPARSE extends support for:

* gebsrmm
* gebsrmv
* gebsrsv
* coo2dense and dense2coo
* generic API including axpby, gather, scatter, rot, spvv, spmv, spgemm, sparsetodense, densetosparse
* mixed indexing types in matrix formats

For more information, see 

https://rocsparse.readthedocs.io/en/latest/


### rocSOLVER

rocSOLVER extends support for:

* Eigensolver routines for symmetric/hermitian matrices:
  - STERF, STEQR
  
* Linear solvers for general non-square systems:
  - GELS (API added with batched and strided_batched versions. Only the overdetermined non-transpose case is implemented in 
    this release. Other cases will return rocblas_status_not_implemented status for now.)
    
* Extended test coverage for functions returning information

* Changelog file

* Tridiagonalization routines for symmetric and hermitian matrices:
  - LATRD
  - SYTD2, SYTRD (with batched and strided_batched versions)
  - HETD2, HETRD (with batched and strided_batched versions)
  
* Sample code and unit test for unified memory model/Heterogeneous Memory Management (HMM)

For more information, see

https://rocsolver.readthedocs.io/en/latest/

### hipCUB

The new iterator DiscardOutputIterator in hipCUB represents a special kind of pointer that ignores values written to it upon dereference.  It is useful for ignoring the output of certain algorithms without wasting memory capacity or bandwidth.  DiscardOutputIterator may also be used to count the size of an algorithm's output, which was not known previously.

For more information, see

https://hipcub.readthedocs.io/en/latest/


## HIP Enhancements

### Support for hipEventDisableTiming Flag

HIP now supports the hipEventDisableTiming flag for hipEventCreateWithFlags. Note, events created with this flag do not record profiling data and provide optimal performance when used for synchronization.

### Cooperative Group Functions

Cooperative Groups defines, synchronizes, and communicates between groups of threads and blocks for efficiency and ease of management. HIP now supports the following kernel language Cooperative Groups types and functions:

![Screenshot](https://github.com/Rmalavally/ROCm/blob/master/images/CG1.PNG)
![Screenshot](https://github.com/Rmalavally/ROCm/blob/master/images/CG2.PNG)
![Screenshot](https://github.com/Rmalavally/ROCm/blob/master/images/CG3.PNG)


###  Support for Extern Shared Declarations

Previously, it was required to declare dynamic shared memory using the HIP_DYNAMIC_SHARED macro for accuracy as using static shared memory in the same kernel could result in overlapping memory ranges and data-races.
Now, the HIP-Clang compiler provides support for extern shared declarations, and the HIP_DYNAMIC_SHARED option is no longer required. 

You may use the standard extern definition:

    extern __shared__ type var[];


## OpenMP Enhancements and Fixes

This release includes the following OpenMP changes:

* Usability Enhancements
* Fixes to Internal Clang Math Headers
* OpenMP Defect Fixes

### Usability Enhancements

* OMPD updates for flang
* To support OpenMP debugging, the selected OpenMP runtime sources are included in lib-debug/src/openmp. The ROCgdb debugger 
  will find these automatically.
* Threadsafe hsa plugin for libomptarget
* Support multiple devices with malloc and hostrpc
* Improve hostrpc version check
* Add max reduction offload feature to flang
* Integration of changes to support HPC Toolkit
* Support for fprintf
* Initial support for GPU malloc and Free. The internal (device rtl) is required for GPU malloc and Free for nested parallelism.  
  GPU malloc and Free are now replaced, which improves the device memory footprint.
* Increase detail of debug printing controlled by LIBOMPTARGET_KERNEL_TRACE environment variable
* Add support for -gpubnames in Flang Driver
* Increase detail of debug printing controlled by LIBOMPTARGET_KERNEL_TRACE environment variable
* Add support for -gpubnames in Flang Driver

###  Fixes to Internal Clang Math Headers

This release includes a set of changes applied to Clang internal headers to support OpenMP C, C++, FORTRAN, and HIP C. This establishes consistency between NVPTX and AMDGCN offloading, and OpenMP, HIP, and CUDA. OpenMP uses function variants and header overlays to define device versions of functions. This causes Clang LLVM IR codegen to mangle names of variants in both the definition and callsites of functions defined in the internal Clang headers. The changes apply to headers found in the installation subdirectory lib/clang/11.0.0/include.

The changes also temporarily eliminate the use of the libm bitcode libraries for C and C++. Although math functions are now defined with internal clang headers, a bitcode library of the C functions defined in the headers is still built for the FORTRAN toolchain linking. This is because FORTRAN cannot use C math headers. This bitcode library is installed in lib/libdevice/libm-.bc. The source build of the bitcode library is implemented with the aomp-extras repository and the component-built script build_extras.sh. 

### OpenMP Defect Fixes

The following OpenMP defects are fixed in this release:

* Openmpi configuration issue with real16. 
* [flang] The AOMP 11.7-1 Fortran compiler claims to support the -isystem flag, but ignores it.
* [flang] producing internal compiler error when the character is used with KIND.
* [flang] openmp map clause on complex allocatable expressions !$omp target data map( chunk%tiles(1)%field%density0).
* Add a fatal error if missing -Xopenmp-target or -march options when -fopenmp-targets is specified. However, this requirement is not 
  applicable for offloading to the host when there is only a single target and that target is the host.
* Openmp error message output for no_rocm_device_lib was asserting.
* Linkage on constant per-kernel symbols from external to weaklinkageonly to prevent duplicate symbols when building kokkos.
* Add environment variables ROCM_LLD_ARGS ROCM_LINK_ARGS ROCM_SELECT_ARGS to test driver options without compiler rebuild.  
* Fix problems with device math functions being ambiguous, especially the pow function.ix aompcc to accept file type cxx. 
* Fix a latent race between host runtime and devicertl.

## MIOPEN TENSILE INTEGRATION

MIOpenTensile provides host-callable interfaces to the Tensile library and supports the HIP programming model. You may use the Tensile feature in the HIP backend by setting the building environment variable value to ON.

    MIOPEN_USE_MIOPENTENSILE=ON

MIOpenTensile is an open-source collaboration tool where external entities can submit source pull requests (PRs) for updates. MIOpenTensile maintainers review and approve the PRs using standard open-source practices. 

For more information about the sources and the build system, see

https://github.com/ROCmSoftwarePlatform/MIOpenTensile


# Known Issues 

The following are the known issues in this release.

## Upgrade to AMD ROCm v4.1 Not Supported

An upgrade from previous releases to AMD ROCm v4.1 is not supported. A complete uninstallation of previous ROCm versions is required before installing a new version of ROCm.

## Performance Impact for Kernel Launch Bound Attribute

Kernels without the *__launch_bounds__* attribute assume the default maximum threads per block value. In the previous ROCm release, this value was 256. In the ROCm v4.1 release, it is changed to 1024. The objective of this change ensures the actual threads per block value used to launch a kernel, by default, are always within the launch bounds, thus, establishing the correctness of HIP programs. 

**NOTE**: Using the above-mentioned approach may incur performance degradation in certain cases. Users must add a minimum launch bound to each kernel, which covers all possible threads per block values used to launch that kernel for correctness and performance. 

The recommended workaround to recover the performance is to add *--gpu-max-threads-per-block=256* to the compilation options for HIP programs.

## Issue with Passing a Subset of GPUs in a Multi-GPU System

ROCm support for passing individual GPUs via the docker --device flag in a Docker run command has a known issue when passing a subset of GPUs in a multi-GPU system. The command runs without any warning or error notification. However, all GPU executable run outputs are randomly corrupted. 

Using GPU targeting via the Docker command is not recommended for users of ROCm 4.1. There is no workaround for this issue currently. 

## Performance Impact for LDS-Bound Kernels

The compiler in ROCm v4.1 generates LDS load and stores instructions that incorrectly assume equal performance between aligned and misaligned accesses. While this does not impact code correctness, it may result in sub-optimal performance.

This issue is under investigation, and there is no known workaround at this time.


# Deprecations

This section describes deprecations and removals in AMD ROCm.

## Compiler Generated Code Object Version 2 Deprecation 

Compiler-generated code object version 2 is no longer supported and has been completely removed. Support for loading code object version 2 is also deprecated with no announced removal release.


# Deploying ROCm

AMD hosts both Debian and RPM repositories for the ROCm packages. 

For more information on ROCM installation on all platforms, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html


# Machine Learning and High Performance Computing Software Stack for AMD GPU

For an updated version of the software stack for AMD GPU, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#software-stack-for-amd-gpu



# Hardware and Software Support
ROCm is focused on using AMD GPUs to accelerate computational tasks such as machine learning, engineering workloads, and scientific computing.
In order to focus our development efforts on these domains of interest, ROCm supports a targeted set of hardware configurations which are detailed further in this section.

**Note:** The AMD ROCm™ open software platform is a compute stack for headless system deployments. GUI-based software applications are currently not supported.

#### Supported GPUs
Because the ROCm Platform has a focus on particular computational domains, we offer official support for a selection of AMD GPUs that are designed to offer good performance and price in these domains.

**Note:** The integrated GPUs of Ryzen are not officially supported targets for ROCm.

ROCm officially supports AMD GPUs that use following chips:

* GFX9 GPUs

  - "Vega 10" chips, such as on the AMD Radeon RX Vega 64 and Radeon Instinct MI25
  
  - "Vega 7nm" chips, such as on the Radeon Instinct MI50, Radeon Instinct MI60 or AMD Radeon VII, Radeon Pro VII

* CDNA GPUs

  - MI100 chips such as on the AMD Instinct™ MI100


ROCm is a collection of software ranging from drivers and runtimes to libraries and developer tools.
Some of this software may work with more GPUs than the "officially supported" list above, though AMD does not make any official claims of support for these devices on the ROCm software platform.

The following list of GPUs are enabled in the ROCm software, though full support is not guaranteed:

  * GFX8 GPUs
    * "Polaris 11" chips, such as on the AMD Radeon RX 570 and Radeon Pro WX 4100
    * "Polaris 12" chips, such as on the AMD Radeon RX 550 and Radeon RX 540
  * GFX7 GPUs
    * "Hawaii" chips, such as the AMD Radeon R9 390X and FirePro W9100

As described in the next section, GFX8 GPUs require PCI Express 3.0 (PCIe 3.0) with support for PCIe atomics. This requires both CPU and motherboard support. GFX9 GPUs require PCIe 3.0 with support for PCIe atomics by default, but they can operate in most cases without this capability.

The integrated GPUs in AMD APUs are not officially supported targets for ROCm.
As described [below](#limited-support), "Carrizo", "Bristol Ridge", and "Raven Ridge" APUs are enabled in our upstream drivers and the ROCm OpenCL runtime.
However, they are not enabled in the HIP runtime, and may not work due to motherboard or OEM hardware limitations.
As such, they are not yet officially supported targets for ROCm.

For a more detailed list of hardware support, please see [the following documentation](https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units).

#### Supported CPUs
As described above, GFX8 GPUs require PCIe 3.0 with PCIe atomics in order to run ROCm.
In particular, the CPU and every active PCIe point between the CPU and GPU require support for PCIe 3.0 and PCIe atomics.
The CPU root must indicate PCIe AtomicOp Completion capabilities and any intermediate switch must indicate PCIe AtomicOp Routing capabilities.

Current CPUs which support PCIe Gen3 + PCIe Atomics are:

  * AMD Ryzen CPUs
  * The CPUs in AMD Ryzen APUs
  * AMD Ryzen Threadripper CPUs
  * AMD EPYC CPUs
  * Intel Xeon E7 v3 or newer CPUs
  * Intel Xeon E5 v3 or newer CPUs
  * Intel Xeon E3 v3 or newer CPUs
  * Intel Core i7 v4, Core i5 v4, Core i3 v4 or newer CPUs (i.e. Haswell family or newer)
  * Some Ivy Bridge-E systems

Beginning with ROCm 1.8, GFX9 GPUs (such as Vega 10) no longer require PCIe atomics.
We have similarly opened up more options for number of PCIe lanes.
GFX9 GPUs can now be run on CPUs without PCIe atomics and on older PCIe generations, such as PCIe 2.0.
This is not supported on GPUs below GFX9, e.g. GFX8 cards in the Fiji and Polaris families.

If you are using any PCIe switches in your system, please note that PCIe Atomics are only supported on some switches, such as Broadcom PLX.
When you install your GPUs, make sure you install them in a PCIe 3.1.0 x16, x8, x4, or x1 slot attached either directly to the CPU's Root I/O controller or via a PCIe switch directly attached to the CPU's Root I/O controller.

In our experience, many issues stem from trying to use consumer motherboards which provide physical x16 connectors that are electrically connected as e.g. PCIe 2.0 x4, PCIe slots connected via the Southbridge PCIe I/O controller, or PCIe slots connected through a PCIe switch that does
not support PCIe atomics.

If you attempt to run ROCm on a system without proper PCIe atomic support, you may see an error in the kernel log (`dmesg`):
```
kfd: skipped device 1002:7300, PCI rejects atomics
```

Experimental support for our Hawaii (GFX7) GPUs (Radeon R9 290, R9 390, FirePro W9100, S9150, S9170)
does not require or take advantage of PCIe Atomics. However, we still recommend that you use a CPU
from the list provided above for compatibility purposes.

#### Not supported or limited support under ROCm

##### Limited support

* ROCm 4.x should support PCIe 2.0 enabled CPUs such as the AMD Opteron, Phenom, Phenom II, Athlon, Athlon X2, Athlon II and older Intel Xeon and Intel Core Architecture and Pentium CPUs. However, we have done very limited testing on these configurations, since our test farm has been catering to CPUs listed above. This is where we need community support. _If you find problems on such setups, please report these issues_.
* Thunderbolt 1, 2, and 3 enabled breakout boxes should now be able to work with ROCm. Thunderbolt 1 and 2 are PCIe 2.0 based, and thus are only supported with GPUs that do not require PCIe 3.1.0 atomics (e.g. Vega 10). However, we have done no testing on this configuration and would need community support due to limited access to this type of equipment.
* AMD "Carrizo" and "Bristol Ridge" APUs are enabled to run OpenCL, but do not yet support HIP or our libraries built on top of these compilers and runtimes.
  * As of ROCm 2.1, "Carrizo" and "Bristol Ridge" require the use of upstream kernel drivers.
  * In addition, various "Carrizo" and "Bristol Ridge" platforms may not work due to OEM and ODM choices when it comes to key configurations parameters such as inclusion of the required CRAT tables and IOMMU configuration parameters in the system BIOS.
  * Before purchasing such a system for ROCm, please verify that the BIOS provides an option for enabling IOMMUv2 and that the system BIOS properly exposes the correct CRAT table. Inquire with your vendor about the latter.
* AMD "Raven Ridge" APUs are enabled to run OpenCL, but do not yet support HIP or our libraries built on top of these compilers and runtimes.
  * As of ROCm 2.1, "Raven Ridge" requires the use of upstream kernel drivers.
  * In addition, various "Raven Ridge" platforms may not work due to OEM and ODM choices when it comes to key configurations parameters such as inclusion of the required CRAT tables and IOMMU configuration parameters in the system BIOS.
  * Before purchasing such a system for ROCm, please verify that the BIOS provides an option for enabling IOMMUv2 and that the system BIOS properly exposes the correct CRAT table. Inquire with your vendor about the latter.

##### Not supported

* "Tonga", "Iceland", "Vega M", and "Vega 12" GPUs are not supported.
* We do not support GFX8-class GPUs (Fiji, Polaris, etc.) on CPUs that do not have PCIe 3.0 with PCIe atomics.
  * As such, we do not support AMD Carrizo and Kaveri APUs as hosts for such GPUs.
  * Thunderbolt 1 and 2 enabled GPUs are not supported by GFX8 GPUs on ROCm. Thunderbolt 1 & 2 are based on PCIe 2.0.

In the default ROCm configuration, GFX8 and GFX9 GPUs require PCI Express 3.0 with PCIe atomics. The ROCm platform leverages these advanced capabilities to allow features such as user-level submission of work from the host to the GPU. This includes PCIe atomic Fetch and Add, Compare and Swap, Unconditional Swap, and AtomicOp Completion.

#### ROCm support in upstream Linux kernels

As of ROCm 1.9.0, the ROCm user-level software is compatible with the AMD drivers in certain upstream Linux kernels.
As such, users have the option of either using the ROCK kernel driver that are part of AMD's ROCm repositories or using the upstream driver and only installing ROCm user-level utilities from AMD's ROCm repositories.

These releases of the upstream Linux kernel support the following GPUs in ROCm:
 * 4.17: Fiji, Polaris 10, Polaris 11
 * 4.18: Fiji, Polaris 10, Polaris 11, Vega10
 * 4.20: Fiji, Polaris 10, Polaris 11, Vega10, Vega 7nm

The upstream driver may be useful for running ROCm software on systems that are not compatible with the kernel driver available in AMD's repositories.
For users that have the option of using either AMD's or the upstreamed driver, there are various tradeoffs to take into consideration:

|   | Using AMD's `rock-dkms` package | Using the upstream kernel driver |
| ---- | ------------------------------------------------------------| ----- |
| Pros | More GPU features, and they are enabled earlier | Includes the latest Linux kernel features |
|      | Tested by AMD on supported distributions | May work on other distributions and with custom kernels |
|      | Supported GPUs enabled regardless of kernel version | |
|      | Includes the latest GPU firmware | |
| Cons | May not work on all Linux distributions or versions | Features and hardware support varies depending on kernel version |
|      | Not currently supported on kernels newer than 5.4 | Limits GPU's usage of system memory to 3/8 of system memory (before 5.6). For 5.6 and beyond, both DKMS and upstream kernels allow use of 15/16 of system memory. |
|      |   | IPC and RDMA capabilities are not yet enabled |
|      |   | Not tested by AMD to the same level as `rock-dkms` package |
|      |   | Does not include most up-to-date firmware |


# Disclaimer

AMD®, the AMD Arrow logo, AMD Instinct™, Radeon™, ROCm® and combinations thereof are trademarks of Advanced Micro Devices, Inc.

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

PCIe® is a registered trademark of PCI-SIG Corporation. Other product names used in this publication are for identification purposes only and may be trademarks of their respective companies.  

Google®  is a registered trademark of Google LLC.

Ubuntu and the Ubuntu logo are registered trademarks of Canonical Ltd.

Other product names used in this publication are for identification purposes only and may be trademarks of their respective companies.

