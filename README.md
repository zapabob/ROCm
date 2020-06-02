# AMD ROCm Release Notes v3.5.0
This page describes the features, fixed issues, and information about downloading and installing the ROCm software.
It also covers known issues and deprecated features in the ROCm v3.5.0 release.

- [Supported Operating Systems and Documentation Updates](#Supported-Operating-Systems-and-Documentation-Updates)
  * [Supported Operating Systems](#Supported-Operating-Systems)
  * [Documentation Updates](#Documentation-Updates)
   
- [What\'s New in This Release](#Whats-New-in-This-Release)
  * [Upgrading to This Release](#Upgrading-to-This-Release)
  * [Heterogeneous-Compute Interface for Portability](#Heterogeneous-Compute-Interface-for-Portability)
  * [Radeon Open Compute Common Language Runtime](#Radeon-Open-Compute-Common-Language-Runtime)
  * [OpenCL Runtime](#OpenCL-Runtime)
  * [AMD ROCm GNU Debugger ROCgdb](#AMD-ROCm-GNU-Debugger-ROCgdb)
  * [AMD ROCm Debugger API Library](#AMD-ROCm-Debugger-API-Library)
  * [rocProfiler Dispatch Callbacks Start/Stop API](#rocProfiler-Dispatch-Callbacks-Start-Stop-API)
  * [ROCm Communications Collective Library](#ROCm-Communications-Collective-Library)
  * [NVIDIA Communications Collective Library Version Compatibility](#NVIDIA-Communications-Collective-Library-Version-Compatibility)
  * [MIOpen - Optional Kernel Package Installation](#MIOpen-Optional-Kernel-Package-Installation)
  * [New SMI Event Interface and Library](#New-SMI-Event-Interface-and-Library)
  * [API for CPU Affinity](#API-for-CPU-Affinity)
  * [Radeon Performance Primitives Library](#Radeon-Performance-Primitives-Library)
  
  
- [Fixed Issues](#Fixed-Issues)

- [Known Issues](#Known-Issues)

- [Deprecations](#Deprecations)
  * [Heterogeneous Compute Compiler](#Heterogeneous-Compute-Compiler)

- [Deploying ROCm](#Deploying-ROCm)
 
- [Hardware and Software Support](#Hardware-and-Software-Support)

- [Machine Learning and High Performance Computing Software Stack for AMD GPU](#Machine-Learning-and-High-Performance-Computing-Software-Stack-for-AMD-GPU)
  * [ROCm Binary Package Structure](#ROCm-Binary-Package-Structure)
  * [ROCm Platform Packages](#ROCm-Platform-Packages)

# Supported Operating Systems and Documentation Updates

## Supported Operating Systems 

The AMD ROCm v3.5.x platform is designed to support the following operating systems:

* Ubuntu 16.04.6(Kernel 4.15) and 18.04.4(Kernel 5.3)
* CentOS 7.7 (Kernel 3.10-1062) and RHEL 7.8(Kernel 3.10.0-1127)(Using devtoolset-7 runtime support)
* SLES 15 SP1
* CentOS and RHEL 8.1(Kernel 4.18.0-147)


## Documentation Updates

### HIP-Clang Compile

* [HIP FAQ - Transition from HCC to HIP-Clang](https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-FAQ.html#hip-faq)
* [HIP-Clang Porting Guide](https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-porting-guide.html#hip-porting-guide)
* [HIP - Glossary of Terms](https://rocmdocs.amd.com/en/latest/ROCm_Glossary/ROCm-Glossary.html)

### AMD ROCDebugger (ROCgdb)

* [ROCgdb User Guide](https://github.com/RadeonOpenCompute/ROCm/blob/master/gdb.pdf)
* [ROCgdbapi Guide](https://github.com/RadeonOpenCompute/ROCm/blob/master/amd-dbgapi.pdf)

### AMD ROCm Systems Management Interface

* [System Management Interface Event API Guide](https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_SMI_Manual.pdf)

### AMD ROCm Deep Learning

* [MIOpen API](https://github.com/ROCmSoftwarePlatform/MIOpen)

### AMD ROCm Glossary of Terms

* [Updated Glossary of Terms and Definitions](https://rocmdocs.amd.com/en/latest/ROCm_Glossary/ROCm-Glossary.html)

### General AMD ROCm Documentatin Links

Access the following links for more information on:

* For AMD ROCm documentation, see 

  https://rocmdocs.amd.com/en/latest/

* For installation instructions on supported platforms, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

* For AMD ROCm binary structure, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#machine-learning-and-high-performance-computing-software-stack-for-amd-gpu-v3-3-0

* For AMD ROCm Release History, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#amd-rocm-version-history


# What\'s New in This Release

## Upgrading to This Release

You must perform a fresh and a clean AMD ROCm install to successfully upgrade from v3.3 to v3.5. The following changes apply in this release: 

* HCC is deprecated and replaced with the HIP-Clang compiler
* HIP-HCC runtime is changed to Radeon Open Compute Common Language Runtime (HIP-ROCClr)
* In the v3.5 release, the firmware is separated from the kernel package. The difference is as    follows:
     * v3.5 release has two separate rock-dkms and rock-dkms-firmware packages
     * v3.3 release had the firmware as part of the rock-dkms package
     

## rocProf Command Line Tool Python Requirement
SQLite3 is a required Python module for the rocprof command-line tool.  You can install the SQLite3 Python module using the pip utility and set env var ROCP_PYTHON_VERSION to the Python version, which includes the SQLite3 module.



## Heterogeneous-Compute Interface for Portability

In this release, the Heterogeneous Compute Compiler (HCC) compiler is deprecated and the HIP-Clang compiler is introduced for compiling Heterogeneous-Compute Interface for Portability (HIP) programs.

NOTE: The HCC environment variables will be gradually deprecated in subsequent releases.

The majority of the codebase for the HIP-Clang compiler has been upstreamed to the Clang trunk. The HIP-Clang implementation has undergone a strict code review by the LLVM/Clang community and comprehensive tests consisting of LLVM/Clang build bots. These reviews and tests resulted in higher productivity, code quality, and lower cost of maintenance.

![ScreenShot](HIPClang2.png)

For most HIP applications, the transition from HCC to HIP-Clang is transparent and efficient as the HIPCC and HIP cmake files automatically choose compilation options for HIP-Clang and hide the difference between the HCC and HIP-Clang code. However, minor changes may be required as HIP-Clang has a stricter syntax and semantic checks compared to HCC.

NOTE: Native HCC language features are no longer supported.

## Radeon Open Compute Common Language Runtime
In this release,  the HIP runtime API is implemented on top of Radeon Open Compute Common Language Runtime (ROCclr). ROCclr is an abstraction layer that provides the ability to interact with different runtime backends such as ROCr.

## OpenCL Runtime
The following OpenCL runtime changes are made in this release:

* AMD ROCm OpenCL Runtime extends support to OpenCL2.2
* The developer branch is changed from master to master-next

## AMD ROCm GNU Debugger (ROCgdb)
The AMD ROCm Debugger (ROCgdb) is the AMD ROCm source-level debugger for Linux based on the GNU Debugger (GDB). It enables heterogeneous debugging on the AMD ROCm platform of an x86-based host architecture along with AMD GPU architectures and supported by the AMD Debugger API Library (ROCdbgapi).

The AMD ROCm Debugger is installed by the rocm-gdb package. The rocm-gdb package is part of the rocm-dev meta-package, which is in the rocm-dkms package.

The current AMD ROCm Debugger (ROCgdb) is an initial prototype that focuses on source line debugging. Note, symbolic variable debugging capabilities are not currently supported.

You can use the standard GDB commands for both CPU and GPU code debugging. For more information about ROCgdb, refer to the ROCgdb User Guide, which is installed at:

* /opt/rocm/share/info/gdb.info as a texinfo file
* /opt/rocm/share/doc/gdb/gdb.pdf as a PDF file

The AMD ROCm Debugger User Guide is available as a PDF at:

https://github.com/RadeonOpenCompute/ROCm/blob/master/gdb.pdf
 
For more information about GNU Debugger (GDB), refer to the GNU Debugger (GDB) web site at: http://www.gnu.org/software/gdb


## AMD ROCm Debugger API Library 

The AMD ROCm Debugger API Library (ROCdbgapi) implements an AMD GPU debugger application programming interface (API) that provides the support necessary for a client of the library to control the execution and inspect the state of AMD GPU devices.

The following AMD GPU architectures are supported:
* Vega 10 
* Vega 7nm

The AMD ROCm Debugger API Library is installed by the rocm-dbgapi package. The rocm-gdb package is part of the rocm-dev meta-package, which is in the rocm-dkms package.
The AMD ROCm Debugger API Specification is available as a PDF at:

https://github.com/RadeonOpenCompute/ROCm/blob/master/amd-dbgapi.pdf

## rocProfiler Dispatch Callbacks Start Stop API

In this release, a new rocprofiler start/stop API is added to enable/disable GPU kernel HSA dispatch callbacks. The callback can be registered with the 'rocprofiler_set_hsa_callbacks' API. The API helps you eliminate some profiling performance impact by invoking the profiler only for kernel dispatches of interest. This optimization will result in significant performance gains.

The API provides the following functions:
* *hsa_status_t rocprofiler_start_queue_callbacks();* is used to start profiling
* *hsa_status_t rocprofiler_stop_queue_callbacks();* is used to stop profiling. 

For more information on kernel dispatches, see the HSA Platform System Architecture Specification guide at http://www.hsafoundation.com/standards/.

## ROCm Communications Collective Library 
The ROCm Communications Collective Library (RCCL) consists of the following enhancements:
* Re-enable target 0x803
* Build time improvements for the HIP-Clang compiler

### NVIDIA Communications Collective Library Version Compatibility
AMD RCCL is now compatible with NVIDIA Communications Collective Library (NCCL) v2.6.4 and provides the following features: 
* Network interface improvements with API v3
* Network topology detection 
* Improved CPU type detection
* Infiniband adaptive routing support

## MIOpen - Optional Kernel Package Installation
MIOpen provides an optional pre-compiled kernel package to reduce startup latency. 

NOTE: The installation of this package is optional. MIOpen will continue to function as expected even if you choose to not install the pre-compiled kernel package. This is because MIOpen compiles the kernels on the target machine once the kernel is run. However, the compilation step may significantly increase the startup time for different operations.

To install the kernel package for your GPU architecture, use the following command:

*apt-get install miopen-kernels-<arch>-<num cu>*
 
* <arch> is the GPU architecture. For example, gfx900, gfx906
* <num cu> is the number of CUs available in the GPU. For example, 56 or 64 
 

## New SMI Event Interface and Library

An SMI event interface is added to the kernel and ROCm SMI  lib for system administrators to get notified when specific events occur. On the kernel side, AMDKFD_IOC_SMI_EVENTS input/output control is enhanced to allow notifications propagation to user mode through the event channel. 

On the ROCm SMI lib side, APIs are added to set an event mask and receive event notifications with a timeout option. Further, ROCm SMI API details can be found in the PDF generated by Doxygen from source or by referring to the rocm_smi.h header file (see the rsmi_event_notification_* functions).

For the more details about ROCm SMI API, see 

https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_SMI_Manual.pdf

## API for CPU Affinity
A new API is introduced for aiding applications to select the appropriate memory node for a given accelerator(GPU). 

The API for CPU affinity has the following signature:

*rsmi_status_t rsmi_topo_numa_affinity_get(uint32_t dv_ind, uint32_t *numa_node);*

This API takes as input, device index (dv_ind), and returns the NUMA node (CPU affinity), stored at the location pointed by numa_node pointer, associated with the device.

Non-Uniform Memory Access (NUMA) is a computer memory design used in multiprocessing, where the memory access time depends on the memory location relative to the processor. 

## Radeon Performance Primitives Library
The new Radeon Performance Primitives (RPP) library is a comprehensive high-performance computer vision library for AMD (CPU and GPU) with the HIP and OpenCL backend. The target operating system is Linux.

![ScreenShot](RPP.png)

For more information about prerequisites and library functions, see 

https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/tree/master/docs

# Fixed Issues

## Device printf Support for HIP-Clang
HIP now supports the use of printf in the device code. The parameters and return value for the device-side printf follow the POSIX.1 standard, with the exception that the "%n" specifier is not supported. A call to printf blocks the calling wavefront until the operation is completely processed by the host. 

No host-side runtime calls by the application are needed to cause the output to appear. There is also no limit on the number of device-side calls to printf or the amount of data that is printed.

For more details, refer the HIP Programming Guide at:
https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-GUIDE.html#hip-guide

## Assertions in HIP Device Code  
Previously, a failing assertion caused early termination of kernels and the application to exit with a line number, file, and failing condition printed to the screen.
This issue is now fixed and the assert() and abort() functions are implemented for HIP device code. 
NOTE: There may be a performance impact in the use of device assertions in its current form. 

You may choose to disable the assertion in the production code. For example, to disable an assertion of:

*assert(foo != 0);*    

you may comment it out as:  

*//assert(foo != 0);*

NOTE: Assertions are currently enabled by default. 

# Known Issues 
The following are the known issues in the v3.5 release.

## HIPify-Clang Installation Failure on CentOS/RHEL 

HIPify-Clang fails to install on CentOS/RHEL with the following error:

*file from install of hipify-clang conflicts with file from package hip-base*

**Workaround**: This is a known issue and the following workaround is recommended for a successful installation of HIPify-Clang on CentOS/RHEL:

* Download HIPify-Clang RPM. For example, *hipify-clang-11.0.0.x86_64.rpm*
* Perform a force install using the following command: 

  *sudo rpm -ivh --force hipify-clang-11.0.0.x86_64.rpm*


## Failure to Process Breakpoint before Queue Destroy Results in ROCm Debugger Error
When ROCgdb is in non-stop mode with an application that rapidly creates and destroys queues, a breakpoint may be reported that is not processed by the debugger before the queue is deleted. In some cases, this can result in the following error that prevents further debugging:

*[amd-dbgapi]: fatal error: kfd_queue_id 2 should have been reported as a NEW_QUEUE before next_pending_event failed (rc=-2)*

There are no known workarounds at this time.

## Failure to Process Breakpoint before Queue Destroy Results in ROCm Debugger API Error

When the ROCdbgapi library is used with an application that rapidly creates and destroys queues, a breakpoint may be reported that is not processed by the client before the queue is deleted. In some cases, this can result in a fatal error and the following error log message is produced:

*[amd-dbgapi]: fatal error: kfd_queue_id 2 should have been reported as a NEW_QUEUE before next_pending_event failed (rc=-2)*

There are no known workarounds at this time.

## rocThrust and hipCUB Unit Test Failures 

The following unit test failures have been observed due to known issues in the ROCclr runtime. 

rocThrust
* sort 
* sort_by_key

hipCUB
* BlockDiscontinuity 
* BlockExchange 
* BlockHistogram 
* BlockRadixSort
* BlockReduce 
* BlockScan

There are no known workarounds in the current release. 


## Multiple GPU Configuration Freezes with Imagenet Training and tf_cnn_benchmark on TensorFlow 

A random freeze has been observed with Imagenet training and tf_cnn_benchmark on TensorFlow when multiple GPU configurations are involved. 

There is no freeze observed with single GPUs.  

There are no known workarounds at this time.

## Issue with Running AMD ROCm v3.3 User Mode with AMD ROCm v3.5 DKMS Kernel Module

Running AMD ROCm v3.3 in the user mode with the AMD ROCm v3.5 DKMS kernel module will cause the following features to be broken:

* IPC import/export, cross memory copy (used by UCX and MPI)
* Experimental GDB support

**Resolution**: Install ROCm v3.5 Thunk (*Hsakmt*) when using ROCm 3.5 Kernel Fusion Driver (KFD).


## SQLite3 Library Not Found in ROCProfiler

The ROCProfiler tool appears to be broken when the SQLite3 library is not found.

**Resolution**: Install the SQLite3 Python module separately and ensure the environment variable is set to ROCP_PYTHON_VERSION to confirm the Python version, which includes the SQLite3 module.



# Deprecations 
Install ROCm v3.5 Thunk (Hsakmt) when using ROCm 3.5 Kernel Fusion Driver (KFD). You can access the Thunk package at:

https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface
## Heterogeneous Compute Compiler
In this release, the Heterogeneous Compute Compiler (HCC) compiler is deprecated and the HIP-Clang compiler is introduced for compiling Heterogeneous-Compute Interface for Portability (HIP) programs.

For more information, see HIP documentation at:
https://rocmdocs.amd.com/en/latest/Programming_Guides/Programming-Guides.html


## Deploying ROCm
AMD hosts both Debian and RPM repositories for the ROCm v3.5.x packages. 

For more information on ROCM installation on all platforms, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

## Hardware and Software Support
ROCm is focused on using AMD GPUs to accelerate computational tasks such as machine learning, engineering workloads, and scientific computing.
In order to focus our development efforts on these domains of interest, ROCm supports a targeted set of hardware configurations which are detailed further in this section.

#### Supported GPUs
Because the ROCm Platform has a focus on particular computational domains, we offer official support for a selection of AMD GPUs that are designed to offer good performance and price in these domains.

ROCm officially supports AMD GPUs that use following chips:

  * GFX8 GPUs
    * "Fiji" chips, such as on the AMD Radeon R9 Fury X and Radeon Instinct MI8
    * "Polaris 10" chips, such as on the AMD Radeon RX 580 and Radeon Instinct MI6
  * GFX9 GPUs
    * "Vega 10" chips, such as on the AMD Radeon RX Vega 64 and Radeon Instinct MI25
    * "Vega 7nm" chips, such as on the Radeon Instinct MI50, Radeon Instinct MI60 or AMD Radeon VII

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
However, they are not enabled in our HCC or HIP runtimes, and may not work due to motherboard or OEM hardware limitations.
As such, they are not yet officially supported targets for ROCm.

For a more detailed list of hardware support, please see [the following documentation](https://rocm.github.io/hardware.html).

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

* ROCm 2.9.x should support PCIe 2.0 enabled CPUs such as the AMD Opteron, Phenom, Phenom II, Athlon, Athlon X2, Athlon II and older Intel Xeon and Intel Core Architecture and Pentium CPUs. However, we have done very limited testing on these configurations, since our test farm has been catering to CPUs listed above. This is where we need community support. _If you find problems on such setups, please report these issues_.
* Thunderbolt 1, 2, and 3 enabled breakout boxes should now be able to work with ROCm. Thunderbolt 1 and 2 are PCIe 2.0 based, and thus are only supported with GPUs that do not require PCIe 3.1.0 atomics (e.g. Vega 10). However, we have done no testing on this configuration and would need community support due to limited access to this type of equipment.
* AMD "Carrizo" and "Bristol Ridge" APUs are enabled to run OpenCL, but do not yet support HCC, HIP, or our libraries built on top of these compilers and runtimes.
  * As of ROCm 2.1, "Carrizo" and "Bristol Ridge" require the use of upstream kernel drivers.
  * In addition, various "Carrizo" and "Bristol Ridge" platforms may not work due to OEM and ODM choices when it comes to key configurations parameters such as inclusion of the required CRAT tables and IOMMU configuration parameters in the system BIOS.
  * Before purchasing such a system for ROCm, please verify that the BIOS provides an option for enabling IOMMUv2 and that the system BIOS properly exposes the correct CRAT table. Inquire with your vendor about the latter.
* AMD "Raven Ridge" APUs are enabled to run OpenCL, but do not yet support HCC, HIP, or our libraries built on top of these compilers and runtimes.
  * As of ROCm 2.1, "Raven Ridge" requires the use of upstream kernel drivers.
  * In addition, various "Raven Ridge" platforms may not work due to OEM and ODM choices when it comes to key configurations parameters such as inclusion of the required CRAT tables and IOMMU configuration parameters in the system BIOS.
  * Before purchasing such a system for ROCm, please verify that the BIOS provides an option for enabling IOMMUv2 and that the system BIOS properly exposes the correct CRAT table. Inquire with your vendor about the latter.

##### Not supported

* "Tonga", "Iceland", "Vega M", and "Vega 12" GPUs are not supported in ROCm 2.9.x
* We do not support GFX8-class GPUs (Fiji, Polaris, etc.) on CPUs that do not have PCIe 3.0 with PCIe atomics.
  * As such, we do not support AMD Carrizo and Kaveri APUs as hosts for such GPUs.
  * Thunderbolt 1 and 2 enabled GPUs are not supported by GFX8 GPUs on ROCm. Thunderbolt 1 & 2 are based on PCIe 2.0.

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



## Machine Learning and High Performance Computing Software Stack for AMD GPU

ROCm Version 3.3.0

### ROCm Binary Package Structure

 ROCm is a collection of software ranging from drivers and runtimes to libraries and developer tools.
In AMD's package distributions, these software projects are provided as a separate packages.
This allows users to install only the packages they need, if they do not wish to install all of ROCm.
These packages will install most of the ROCm software into `/opt/rocm/` by default.

The packages for each of the major ROCm components are:

* ROCm Core Components
  - ROCk Kernel Driver: `rock-dkms`
  - ROCr Runtime: `hsa-rocr-dev`, `hsa-ext-rocr-dev`
  - ROCt Thunk Interface: `hsakmt-roct`, `hsakmt-roct-dev`
* ROCm Support Software
  - ROCm SMI: `rocm-smi`
  - ROCm cmake: `rocm-cmake`
  - rocminfo: `rocminfo`
  - ROCm Bandwidth Test: `rocm_bandwidth_test`
* ROCm Development Tools
  - HCC compiler: `hcc`
  - HIP: `hip_base`, `hip_doc`, `hip_hcc`, `hip_samples`
  - ROCm Device Libraries: `rocm-device-libs`
  - ROCm OpenCL: `rocm-opencl`, `rocm-opencl-devel` (on RHEL/CentOS), `rocm-opencl-dev` (on Ubuntu)
  - ROCM Clang-OCL Kernel Compiler: `rocm-clang-ocl`
  - Asynchronous Task and Memory Interface (ATMI): `atmi`
  - ROCr Debug Agent: `rocr_debug_agent`
  - ROCm Code Object Manager: `comgr`
  - ROC Profiler: `rocprofiler-dev`
  - ROC Tracer: `roctracer-dev`
  - Radeon Compute Profiler: `rocm-profiler`
* ROCm Libraries
  - rocALUTION: `rocalution`
  - rocBLAS: `rocblas`
  - hipBLAS: `hipblas`
  - hipCUB: `hipCUB`
  - rocFFT: `rocfft`
  - rocRAND: `rocrand`
  - rocSPARSE: `rocsparse`
  - hipSPARSE: `hipsparse`
  - ROCm SMI Lib: `rocm_smi_lib64`
  - rocThrust: `rocThrust`
  - MIOpen: `MIOpen-HIP` (for the HIP version), `MIOpen-OpenCL` (for the OpenCL version)
  - MIOpenGEMM: `miopengemm`
  - MIVisionX: `mivisionx`
  - RCCL: `rccl`

To make it easier to install ROCm, the AMD binary repositories provide a number of meta-packages that will automatically install multiple other packages.
For example, `rocm-dkms` is the primary meta-package that is used to install most of the base technology needed for ROCm to operate.
It will install the `rock-dkms` kernel driver, and another meta-package (`rocm-dev`) which installs most of the user-land ROCm core components, support software, and development tools.

The `rocm-utils` meta-package will install useful utilities that, while not required for ROCm to operate, may still be beneficial to have.
Finally, the `rocm-libs` meta-package will install some (but not all) of the libraries that are part of ROCm.

The chain of software installed by these meta-packages is illustrated below

```
  rocm-dkms
    |--rock-dkms
    \--rocm-dev
       |--comgr
       |--hcc
       |--hip_base
       |--hip_doc
       |--hip_hcc
       |--hip_samples
       |--hsakmt-roct
       |--hsakmt-roct-dev
       |--hsa-amd-aqlprofile
       |--hsa-ext-rocr-dev
       |--hsa-rocr-dev
       |--rocm-cmake
       |--rocm-device-libs
       |--rocm-smi
       |--rocprofiler-dev
       |--rocr_debug_agent
       \--rocm-utils
          |--rocminfo
          \--rocm-clang-ocl # This will cause OpenCL to be installed

  rocm-libs
    |--hipblas
    |--hipcub
    |--hipsparse
    |--rocalution
    |--rocblas
    |--rocfft
    |--rocprim
    |--rocrand
    |--rocsparse
    \--rocthrust
```

These meta-packages are not required but may be useful to make it easier to install ROCm on most systems.

Note:Some users may want to skip certain packages. For instance, a user that wants to use the upstream kernel drivers (rather than those supplied by AMD) may want to skip the `rocm-dkms` and `rock-dkms` packages, and instead directly install `rocm-dev`.

Similarly, a user that only wants to install OpenCL support instead of HCC and HIP may want to skip the `rocm-dkms` and `rocm-dev` packages. Instead, they could directly install `rock-dkms`, `rocm-opencl`, and `rocm-opencl-dev` and their dependencies.


### ROCm Platform Packages

Drivers, ToolChains, Libraries, and Source Code 

The latest supported version of the drivers, tools, libraries and source code for the ROCm platform have been released and are available from the following GitHub repositories:

#### ROCm Core Components
  - [ROCk Kernel Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/roc-3.3.0)
  - [ROCr Runtime](https://github.com/RadeonOpenCompute/ROCR-Runtime/tree/rocm-3.3.0)
  - [ROCT Thunk Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/roc-3.3.0)  

  
#### ROCm Support Software
  - [ROCm SMI](https://github.com/RadeonOpenCompute/ROC-smi/tree/roc-3.3.0)
  - [ROCm cmake](https://github.com/RadeonOpenCompute/rocm-cmake/tree/rocm-3.3.0)
  - [rocminfo](https://github.com/RadeonOpenCompute/rocminfo/tree/rocm-3.3.0)
  - [ROCm Bandwidth Test](https://github.com/RadeonOpenCompute/rocm_bandwidth_test/tree/rocm-3.3.0)
  
#### ROCm Development ToolChain
  - [HCC compiler](https://github.com/RadeonOpenCompute/hcc/tree/rocm-3.3.0)
  
  - [HIP](https://github.com/ROCm-Developer-Tools/HIP/tree/rocm-3.3.0)
  
  - [ROCm Device Libraries HCC](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/tree/roc-ocl-3.3.0)
  
  - [ROCm OpenCL Runtime](http://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/tree/roc-3.3.0)
   
  - [ROCm LLVM OCL](http://github.com/RadeonOpenCompute/llvm-project/tree/rocm-ocl-3.3.0)   
      
  - [ROCm Device Libraries OCL](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/tree/rocm-ocl-3.3.0)
      
  - [ROCM Clang-OCL Kernel Compiler](https://github.com/RadeonOpenCompute/clang-ocl/tree/rocm-3.3.0)
  
  - [Asynchronous Task and Memory Interface (ATMI)](https://github.com/RadeonOpenCompute/atmi/tree/rocm-3.3.0)
  
  - [ROCr Debug Agent](https://github.com/ROCm-Developer-Tools/rocr_debug_agent/tree/roc-3.3.0)
  
  - [ROCm Code Object Manager](https://github.com/RadeonOpenCompute/ROCm-CompilerSupport/tree/rocm-3.3.0)
  
  - [ROC Profiler](https://github.com/ROCm-Developer-Tools/rocprofiler/tree/roc-3.3.0)
  
  - [ROC Tracer](https://github.com/ROCm-Developer-Tools/roctracer/tree/roc-3.3.0)
  
  - [AOMP](https://github.com/ROCm-Developer-Tools/aomp/tree/roc-3.3.0)
  
  - [Radeon Compute Profiler](https://github.com/GPUOpen-Tools/RCP/tree/3a49405)
  
  - [ROCmValidationSuite](https://github.com/ROCm-Developer-Tools/ROCmValidationSuite/tree/roc-3.3.0)
  
  - Example Applications:
    - [HCC Examples](https://github.com/ROCm-Developer-Tools/HCC-Example-Application/tree/ffd65333)
    
    - [HIP Examples](https://github.com/ROCm-Developer-Tools/HIP-Examples/tree/rocm-3.3.0)
    
#### ROCm Libraries

  - [rocBLAS](https://github.com/ROCmSoftwarePlatform/rocBLAS/tree/rocm-3.3.0)
  
  - [hipBLAS](https://github.com/ROCmSoftwarePlatform/hipBLAS/tree/rocm-3.3.0)
  
  - [rocFFT](https://github.com/ROCmSoftwarePlatform/rocFFT/tree/rocm-3.3)
  
  - [rocRAND](https://github.com/ROCmSoftwarePlatform/rocRAND/tree/rocm-3.3.0)
  
  - [rocSPARSE](https://github.com/ROCmSoftwarePlatform/rocSPARSE/tree/rocm-3.3.0)
  
  - [hipSPARSE](https://github.com/ROCmSoftwarePlatform/hipSPARSE/tree/rocm-3.3.0)
  
  - [rocALUTION](https://github.com/ROCmSoftwarePlatform/rocALUTION/tree/rocm-3.3.0)
  
  - [MIOpenGEMM](https://github.com/ROCmSoftwarePlatform/MIOpenGEMM/tree/b51a125)
  
  - [MIOpen](https://github.com/ROCmSoftwarePlatform/MIOpen/tree/roc-3.3.0)
  
  - [rocThrust](https://github.com/ROCmSoftwarePlatform/rocThrust/tree/rocm-3.3.0)
  
  - [ROCm SMI Lib](https://github.com/RadeonOpenCompute/rocm_smi_lib/tree/rocm-3.3.0)
  
  - [RCCL](https://github.com/ROCmSoftwarePlatform/rccl/tree/rocm-3.3.0)
  
  - [MIVisionX](https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/commit/755e7a08d5299a95c42def092af7c736d5eda90c)
  
  - [MIVisionX] https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/tree/1.7)
  
  - [hipCUB](https://github.com/ROCmSoftwarePlatform/hipCUB/tree/rocm-3.3.0)
  
  - [AMDMIGraphX](https://github.com/ROCmSoftwarePlatform/AMDMIGraphX/commit/d1e945dabce0078d44c78de67b00232b856e18bc)


Features and enhancements introduced in previous versions of ROCm can be found in [version_history.md](version_history.md)
