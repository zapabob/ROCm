
# AMD ROCm™ Release Notes v3.10.0

This page describes the features, fixed issues, and information about downloading and installing the ROCm software.
It also covers known issues in this release.

- [Supported Operating Systems and Documentation Updates](#Supported-Operating-Systems-and-Documentation-Updates)
  * [Supported Operating Systems](#Supported-Operating-Systems)
  * [ROCm Installation Updates](#ROCm-Installation-Updates)
  * [AMD ROCm Documentation Updates](#AMD-ROCm-Documentation-Updates)
   
- [What\'s New in This Release](#Whats-New-in-This-Release)
  * [ROCm Data Center Tool](#ROCm-Data-Center-Tool)
  * [ROCm System Management Information](#ROCm-System-Management-Information)
  * [ROCm Math and Communication Libraries](#ROCm-Math-and-Communication-Libraries)
  * [ROCM AOMP Enhancements](#ROCm-AOMP-Enhancements)
    
- [Fixed Defects](#Fixed-Defects)

- [Known Issues](#Known-Issues)

- [Deprecations](#Deprecations)

- [Deploying ROCm](#Deploying-ROCm)
 
- [Hardware and Software Support](#Hardware-and-Software-Support)

- [Machine Learning and High Performance Computing Software Stack for AMD GPU](#Machine-Learning-and-High-Performance-Computing-Software-Stack-for-AMD-GPU)
  * [ROCm Binary Package Structure](#ROCm-Binary-Package-Structure)
  * [ROCm Platform Packages](#ROCm-Platform-Packages)
  


# Supported Operating Systems 

## List of Supported Operating Systems

The AMD ROCm platform is designed to support the following operating systems:

* Ubuntu 20.04.1 (5.4 and 5.6-oem) and 18.04.5 (Kernel 5.4)	

* CentOS 7.8 & RHEL 7.8 (Kernel 3.10.0-1127) (Using devtoolset-7 runtime support)

* CentOS 8.2 & RHEL 8.2 (Kernel 4.18.0 ) (devtoolset is not required)

* SLES 15 SP2

 
# ROCm Installation Updates

## Fresh Installation of AMD ROCm v3.10 Recommended
A fresh and clean installation of AMD ROCm v3.10 is recommended. An upgrade from previous releases to AMD ROCm v3.10 is not supported.

For more information, refer to the AMD ROCm Installation Guide at:
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

**Note**: AMD ROCm release v3.3 or prior releases are not fully compatible with AMD ROCm v3.5 and higher versions. You must perform a fresh ROCm installation if you want to upgrade from AMD ROCm v3.3 or older to 3.5 or higher versions and vice-versa.

**Note**: *render group* is required only for Ubuntu v20.04. For all other ROCm supported operating systems, continue to use *video group*.

* For ROCm v3.5 and releases thereafter,the *clinfo* path is changed to -  */opt/rocm/opencl/bin/clinfo*.

* For ROCm v3.3 and older releases, the *clinfo* path remains unchanged -  */opt/rocm/opencl/bin/x86_64/clinfo*.

**Note**: After an operating system upgrade, AMD ROCm may upgrade automatically and result in an error. This is because AMD ROCm does not support upgrades currently. You must uninstall and reinstall AMD ROCm after an operating system upgrade.


## ROCm MultiVersion Installation Update

With the AMD ROCm v3.10 release, the following ROCm multi-version installation changes apply:

The meta packages rocm-dkms<version> are now deprecated for multi-version ROCm installs. For example, rocm-dkms3.7.0, rocm-dkms3.8.0.
 
* Multi-version installation of ROCm should be performed by installing rocm-dev<version> using   each of the desired ROCm versions. For example, rocm-dev3.7.0, rocm-dev3.8.0, rocm-dev3.9.0.   
* Version files must be created for each multi-version rocm <= 3.10.0

    * command: echo <version> | sudo tee /opt/rocm-<version>/.info/version

    * example: echo 3.9.0 | sudo tee /opt/rocm-3.10.0/.info/version

* The rock-dkms loadable kernel modules should be installed using a single rock-dkms package. 

* ROCm v3.10 and above will not set any *ldconfig* entries for ROCm libraries for multi-version installation.  Users must set *LD_LIBRARY_PATH* to load the ROCm library version of choice.


**NOTE**: The single version installation of the ROCm stack remains the same. The rocm-dkms package can be used for single version installs and is not deprecated at this time.



# AMD ROCm Documentation Updates

## AMD ROCm Installation Guide 

The AMD ROCm Installation Guide in this release includes:

* Updated Supported Environments
* Installation Instructions for v3.10
* HIP Installation Instructions

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html


## ROCm SMI API Documentation Updates 

* System DMA (SDMA) Utilization API 

* ROCm-SMI Command Line Interface

* Enhanced ROCm SMI Library for Events


For the updated ROCm SMI API Guide, see 

https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_SMI_API_Guide_v3.10.pdf


## ROCm Data Center Tool User Guide

The ROCm Data Center Tool User Guide includes the following enhancements:

* ROCm Data Center Tool Python Binding

* Prometheus plugin integration

For more information, refer to the ROCm Data Center Tool User Guide at:

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_ROCm_DataCenter_Tool_User_Guide.pdf

For ROCm Data Center APIs, see

https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_Data_Center_API_Guide.pdf


## AMD ROCm - HIP Documentation Updates

* HIP FAQ  

For more information, refer to

https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-FAQ.html#hip-faq


## General AMD ROCm Documentation Links

Access the following links for more information:

* For AMD ROCm documentation, see 

  https://rocmdocs.amd.com/en/latest/

* For installation instructions on supped platforms, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

* For AMD ROCm binary structure, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#software-stack-for-amd-gpu 

* For AMD ROCm Release History, see

  https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#amd-rocm-version-history



# What\'s New in This Release

## ROCm DATA CENTER TOOL 

The following enhancements are made to the ROCm Data Center Tool.

### Prometheus Plugin for ROCm Data Center Tool

The ROCm Data Center (RDC) Tool now provides the Prometheus plugin, a Python client to collect the telemetry data of the GPU. 
The RDC uses Python binding for Prometheus and the collected plugin. The Python binding maps the RDC C APIs to Python using ctypes. The functions supported by C APIs can also be used in the Python binding.

For installation instructions, refer to the 

### Python Binding

The ROCm Data Center (RDC) Tool now uses PyThon Binding for Prometheus and collectd plugins. PyThon binding maps the RDC C APIs to PyThon using ctypes. All the functions supported by C APIs can also be used in PyThon binding. A generic PyThon class RdcReader is created to simplify the usage of the RDC:

* Users can only specify the fields they want to monitor. RdcReader creates groups and fieldgroups, watches the fields, and fetches the fields. 

* The RdcReader can support both the Embedded and Standalone mode. Standalone mode can be used with and without authentication.

* In the Standalone mode, the RdcReader can automatically reconnect to rdcd when connection is lost.When rdcd is restarted, the previously created group and fieldgroup may lose. The RdcReader can re-create them and watch the fields after a reconnect. 

* If the client is restarted, RdcReader can detect the groups and fieldgroups created previously, and, therefore, can avoid recreating them.

* Users can pass the unit converter if they do not want to use the RDC default unit.

See the following sample program to monitor the power and GPU utilization using the RdcReader:

```

from RdcReader import RdcReader
from RdcUtil import RdcUtil
from rdc_bootstrap import *
 
default_field_ids = [
        rdc_field_t.RDC_FI_POWER_USAGE,
        rdc_field_t.RDC_FI_GPU_UTIL
]
 
class SimpleRdcReader(RdcReader):
    def __init__(self):
        RdcReader.__init__(self,ip_port=None, field_ids = default_field_ids, update_freq=1000000)
    def handle_field(self, gpu_index, value):
        field_name = self.rdc_util.field_id_string(value.field_id).lower()
        print("%d %d:%s %d" % (value.ts, gpu_index, field_name, value.value.l_int))
 
if __name__ == '__main__':
    reader = SimpleRdcReader()
    while True:
        time.sleep(1)
        reader.process()
        
 ```

For more information about RDC Python binding and the Prometheus plugin integration, refer to the ROCm Data Center Tool User Guide at



## ROCm SYSTEM MANAGEMENT INFORMATION 

### System DMA (SDMA) Utilization

Per-process, the SDMA usage is exposed via the ROCm SMI library. The structure rsmi_process_info_t is extended to include sdma_usage. sdma_usage is a 64-bit value that counts the duration (in microseconds) for which the SDMA engine was active during that process's lifetime. 

For example, see the rsmi_compute_process_info_by_pid_get() API below.

```

/**
* @brief This structure contains information specific to a process.
*/
  typedef struct {
      - - -,
      uint64_t sdma_usage; // SDMA usage in microseconds
  } rsmi_process_info_t;
  rsmi_status_t
      rsmi_compute_process_info_by_pid_get(uint32_t pid,
          rsmi_process_info_t *proc);

```

### ROCm-SMI Command Line Interface

The SDMA usage per-process is available using the following command,

```
$ rocm-smi –showpids

```

For more information, see the ROCm SMI API guide at,

https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_SMI_API_Guide_v3.10.pdf


### Enhanced ROCm SMI Library for Events

ROCm-SMI library clients can now register to receive the following events: 

* GPU PRE RESET: This reset event is sent to the client just before a GPU is going to be RESET.

* GPU POST RESET: This reset event is sent to the client after a successful GPU RESET.

* GPU THERMAL THROTTLE: This Thermal throttling event is sent if GPU clocks are throttled.

For more information, refer to the ROCm SMI API Guide at:

https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_SMI_API_Guide_v3.10.pdf


### ROCm SMI – Command Line Interface Hardware Topology

This feature provides a matrix representation of the GPUs present in a system by providing information of the manner in which the nodes are connected. This is represented in terms of weights, hops, and link types between two given GPUs. It also provides the numa node and the CPU affinity associated with every GPU.

![Screenshot](https://github.com/Rmalavally/ROCm/blob/master/images/CLI1.PNG)

![Screenshot](https://github.com/Rmalavally/ROCm/blob/master/images/CLI2.PNG)


## ROCm MATH and COMMUNICATION LIBRARIES

### New rocSOLVER APIs
The following new rocSOLVER APIs are added in this release:

![Screenshot](https://github.com/Rmalavally/ROCm/blob/master/images/rocsolverAPI.PNG)

For more information, refer to 

https://rocsolver.readthedocs.io/en/latest/userguide_api.html

### RCCL Alltoallv Support in PyTorch

The AMD ROCm v3.10 release includes a new API for ROCm Communication Collectives Library (RCCL). This API sends data from all to all ranks and each rank provides arrays of input/output data counts and offsets. 

For details about the functions and parameters, see 

https://rccl.readthedocs.io/en/master/allapi.html

## ROCm AOMP ENHANCEMENTS

### AOMP Release 11.11-0

The source code base for this release is the upstream LLVM 11 monorepo release/11.x sources with the hash value 

*176249bd6732a8044d457092ed932768724a6f06*

This release includes fixes to the internal Clang math headers:

* This set of changes applies to clang internal headers to support OpenMP C, C++, and FORTRAN and for HIP C. This establishes consistency between NVPTX and AMDGCN offloading and between OpenMP, HIP, and CUDA. OpenMP uses function variants and header overlays to define device versions of functions. This causes clang LLVM IR codegen to mangled names of variants in both the definition and callsites of functions defined in the internal clang headers. These changes apply to headers found in the installation subdirectory lib/clang/11.0.0/include.

* These changes temporarily eliminate the use of the libm bitcode libraries for C and C++. Although math functions are now defined with internal clang headers, a bitcode library of the C functions defined in the headers is still built for FORTRAN toolchain linking because FORTRAN cannot use c math headers. This bitcode library is installed in lib/libdevice/libm-.bc. The source build of this bitcode library is done with the aomp-extras repository and the component built script build_extras.sh. In the future, we will introduce across the board changes to eliminate massive header files for math libraries and replace them with linking to bitcode libraries.

* Added support for -gpubnames in Flang Driver

* Added an example category for Kokkos. The Kokkos example makefile detects if Kokkos is installed and, if not, it builds Kokkos from the Web. Refer to the script kokkos_build.sh in the bin directory on how to build Kokkos. Kokkos now builds cleanly with the OpenMP backend for simple test cases. 

* Fixed hostrpc cmake race condition in the build of openmp

* Add a fatal error if missing -Xopenmp-target or -march options when -fopenmp-targets is specified. However, we do forgive this requirement for offloading to host when there is only a single target and that target is the host.

* Fix a bug in InstructionSimplify pass where a comparison of two constants of different sizes found in the optimization pass. This fixes issue #182 which was causing kokkos build failure.

* Fix openmp error message output for no_rocm_device_lib, was asserting.

* Changed linkage on constant per-kernel symbols from external to weaklinkageonly to prevent duplicate symbols when building kokkos.



# Fixed Defects

The following defects are fixed in this release:

* HIPfort failed to be installed

* rocm-smi does not work as-is in 3.9, instead prints a reference to documentation

* *--showtopo*, weight and hop count shows wrong data

* Unable to install RDC on CentOS/RHEL 7.8/8.2 & SLES

* Unable to install mivisionx with error "Problem: nothing provides opencv needed"


# Known Issues 

The following are the known issues in this release.

## Upgrade to AMD ROCm v3.10 Not Supported

An upgrade from previous releases to AMD ROCm v3.10 is not supported. A fresh and clean installation of AMD ROCm v3.10 is recommended. 


# Deprecations

This section describes deprecations and removals in AMD ROCm.

## WARNING: COMPILER-GENERATED CODE OBJECT VERSION 2 DEPRECATION 

Compiler-generated code object version 2 is no longer supported and will be removed shortly. AMD ROCm users must plan for the code object version 2 deprecation immediately. 

Support for loading code object version 2 is also being deprecated with no announced removal release.


# Deploying ROCm

AMD hosts both Debian and RPM repositories for the ROCm v3.10.x packages. 

For more information on ROCM installation on all platforms, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

# Hardware and Software Support
ROCm is focused on using AMD GPUs to accelerate computational tasks such as machine learning, engineering workloads, and scientific computing.
In order to focus our development efforts on these domains of interest, ROCm supports a targeted set of hardware configurations which are detailed further in this section.

#### Supported GPUs
Because the ROCm Platform has a focus on particular computational domains, we offer official support for a selection of AMD GPUs that are designed to offer good performance and price in these domains.

**Note:** The integrated GPUs of Ryzen are not officially supported targets for ROCm.

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
