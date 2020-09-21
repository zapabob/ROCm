
# AMD ROCm Release Notes v3.8.0

This page describes the features, fixed issues, and information about downloading and installing the ROCm software.
It also covers known issues in this release.

- [Supported Operating Systems and Documentation Updates](#Supported-Operating-Systems-and-Documentation-Updates)
  * [Supported Operating Systems](#Supported-Operating-Systems)
  * [AMD ROCm Documentation Updates](#AMD-ROCm-Documentation-Updates)
   
- [What\'s New in This Release](#Whats-New-in-This-Release)
  * [Hipfort-Interface for GPU Kernel Libraries](#Hipfort-Interface-for-GPU-Kernel-Libraries)
  * [ROCm Data Center Tool](#ROCm-Data-Center-Tool)
  * [Error-Correcting Code Fields in ROCm Data Center Tool](#Error-Correcting-Code-Fields-in-ROCm-Data-Center-Tool)
  * [Static Linking Libraries](#Static-Linking-Libraries)
    
- [Fixed Defects](#Fixed-Defects)

- [Known Issues](#Known-Issues)

- [Deploying ROCm](#Deploying-ROCm)
 
- [Hardware and Software Support](#Hardware-and-Software-Support)

- [Machine Learning and High Performance Computing Software Stack for AMD GPU](#Machine-Learning-and-High-Performance-Computing-Software-Stack-for-AMD-GPU)
  * [ROCm Binary Package Structure](#ROCm-Binary-Package-Structure)
  * [ROCm Platform Packages](#ROCm-Platform-Packages)
  


# Supported Operating Systems 

## Support for Vega 7nm Workstation

This release extends support to the Vega 7nm Workstation (Vega20 GL-XE) version.

## List of Supported Operating Systems

The AMD ROCm platform is designed to support the following operating systems:

* Ubuntu 20.04 (5.4 and 5.6-oem) and 18.04.5 (Kernel 5.4)	
* CentOS 7.8 & RHEL 7.8 (Kernel 3.10.0-1127) (Using devtoolset-7 runtime support)
* CentOS 8.2 & RHEL 8.2 (Kernel 4.18.0 ) (devtoolset is not required)
* SLES 15 SP1

## Fresh Installation of AMD ROCm v3.8 Recommended
A fresh and clean installation of AMD ROCm v3.8 is recommended. An upgrade from previous releases to AMD ROCm v3.8 is not supported.

For more information, refer to the AMD ROCm Installation Guide at:
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

**Note**: AMD ROCm release v3.3 or prior releases are not fully compatible with AMD ROCm v3.5 and higher versions. You must perform a fresh ROCm installation if you want to upgrade from AMD ROCm v3.3 or older to 3.5 or higher versions and vice-versa.

**Note**: *render group* is required only for Ubuntu v20.04. For all other ROCm supported operating systems, continue to use *video group*.

* For ROCm v3.5 and releases thereafter,the *clinfo* path is changed to -  */opt/rocm/opencl/bin/clinfo*.

* For ROCm v3.3 and older releases, the *clinfo* path remains unchanged -  */opt/rocm/opencl/bin/x86_64/clinfo*.


# AMD ROCm Documentation Updates

## AMD ROCm Installation Guide 

The AMD ROCm Installation Guide in this release includes:

* Updated Supported Environments
* HIP Installation Instructions
* Tensorflow ROCm Port: Basic Installations on RHEL v8.2

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

## AMD ROCm - HIP Documentation Updates

* HIP Repository Information

For more information, see 

https://rocmdocs.amd.com/en/latest/Programming_Guides/Programming-Guides.html#hip-repository-information

## ROCm Data Center Tool User Guide

* Error-Correction Codes Field and Output Documentation

For more information, refer to the AMD ROCm Data Center User Guide at

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_ROCm_DataCenter_Tool_User_Guide.pdf

## General AMD ROCm Documentation Links

Access the following links for more information:

* For AMD ROCm documentation, see 

  https://rocmdocs.amd.com/en/latest/

* For installation instructions on supped platforms, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

* For AMD ROCm binary structure, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#build-amd-rocm

* For AMD ROCm Release History, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#amd-rocm-version-history



# What\'s New in This Release

## Hipfort-Interface for GPU Kernel Libraries

Hipfort is an interface library for accessing GPU Kernels. It provides support to the AMD ROCm architecture from within the Fortran programming language. Currently, the gfortran and HIP-Clang compilers support hipfort. Note, the gfortran compiler belongs to the GNU Compiler Collection (GCC). While hipfc wrapper calls hipcc for the non-fortran kernel source, gfortran is used for FORTRAN applications that call GPU kernels.

The hipfort interface library is meant for Fortran developers with a focus on gfortran users. 

For information on HIPFort installation and examples, see
https://github.com/ROCmSoftwarePlatform/hipfort
  

## ROCm Data Center Tool 

The ROCm™ Data Center Tool™ simplifies the administration and addresses key infrastructure challenges in AMD GPUs in cluster and datacenter environments. The important features of this tool are:

* GPU telemetry  

* GPU statistics for jobs 

* Integration with third-party tools 

* Open source 

The ROCm Data Center Tool can be used in the standalone mode if all components are installed. The same set of features is also available in a library format that can be used by existing management tools. 

![ScreenShot](https://github.com/Rmalavally/ROCm/blob/master/RDCComponentsrevised.png)


Refer to the ROCm Data Center Tool™ User Guide for more details on the different modes of operation.  

NOTE: The ROCm Data Center User Guide is intended to provide an overview of ROCm Data Center Tool features and how system administrators and Data Center (or HPC) users can administer and configure AMD GPUs. The guide also provides an overview of its components and open source developer handbook. 

For installation information on different distributions, refer to the ROCm Data Center User Guide at

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_ROCm_DataCenter_Tool_User_Guide.pdf


### Error Correcting Code Fields in ROCm Data Center Tool

The ROCm Data Center (RDC) tool is enhanced to provide counters to track correctable and uncorrectable errors. While a single bit per word error can be corrected, double bit per word errors cannot be corrected. 

The RDC tool now helps monitor and protect undetected memory data corruption. If the system is using ECC- enabled memory, the ROCm Data Center tool can report the error counters to monitor the status of the memory. 

![ScreenShot](https://github.com/Rmalavally/ROCm/blob/master/forweb.PNG)

## Static Linking Libraries 

The underlying libraries of AMD ROCm are dynamic and are called shared objects (.so) in Linux.
The AMD ROCm v3.8 release includes the capability to build static ROCm libraries and link to the applications statically. CMake target files enable linking an application statically to ROCm libraries and each component exports the required dependencies for linking. The static libraries are called Archives (.a) in Linux.

This release also comprises of the requisite changes required for all the components to work in a static environment. The components have been successfully tested for basic functionalities like *rocminfo /rocm_bandwidth_test* and archives.

In the AMD ROCm v3.8 release, the following libraries support static linking: 

![ScreenShot](https://github.com/Rmalavally/ROCm/blob/master/staticlinkinglib.PNG)

# Fixed Defects
The following defects are fixed in this release:

* GPU Kernel C++ Names Not Demangled
* MIGraphX Fails for fp16 Datatype
* Issue with Peer-to-Peer Transfers
* ‘rocprof’ option ‘--parallel-kernels’ Not Supported in this Release

# Known Issues 

## Undefined Reference Issue in Statically Linked Libraries

Libraries and applications statically linked using flags -rtlib=compiler-rt, such as rocBLAS, have an implicit dependency on gcc_s not captured in their CMAKE configuration.  

Client applications may require linking with an additional library -lgcc_s to resolve the undefined reference to symbol '_Unwind_Resume@@GCC_3.0'.

## MIGraphX Pooling Operation Fails for Some Models

MIGraphX does not work for some models with pooling operations and the following error appears:

*‘test_gpu_ops_test FAILED’*

This issue is currently under investigation and there is no known workaround currently. 

## MIVisionX Installation Error on CentOS/RHEL8.2 and SLES 15

Installing ROCm on MIVisionX results in the following error on CentOS/RHEL8.2 and SLES 15:

*"Problem: nothing provides opencv needed"*

As a workaround, install opencv before installing MIVisionX.


# Deploying ROCm
AMD hosts both Debian and RPM repositories for the ROCm v3.8.x packages. 

For more information on ROCM installation on all platforms, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

# Hardware and Software Support
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
However, they are not enabled in the HIP runtime, and may not work due to motherboard or OEM hardware limitations.
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
* AMD "Carrizo" and "Bristol Ridge" APUs are enabled to run OpenCL, but do not yet support HIP or our libraries built on top of these compilers and runtimes.
  * As of ROCm 2.1, "Carrizo" and "Bristol Ridge" require the use of upstream kernel drivers.
  * In addition, various "Carrizo" and "Bristol Ridge" platforms may not work due to OEM and ODM choices when it comes to key configurations parameters such as inclusion of the required CRAT tables and IOMMU configuration parameters in the system BIOS.
  * Before purchasing such a system for ROCm, please verify that the BIOS provides an option for enabling IOMMUv2 and that the system BIOS properly exposes the correct CRAT table. Inquire with your vendor about the latter.
* AMD "Raven Ridge" APUs are enabled to run OpenCL, but do not yet support HIP or our libraries built on top of these compilers and runtimes.
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

For an updated version of the software stack for AMD GPU, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#software-stack-for-amd-gpu
