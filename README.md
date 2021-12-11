

# AMD ROCm™ v4.5.2 Release Notes 

This document describes the features, fixed issues, and information about downloading and installing the AMD ROCm™ software. It also covers known issues and deprecations in this release.

## INSTALLATION GUIDE UPDATES FOR ROCM V4.5.2 

In this release, users have the option to install the kernel mode driver using the Installer method. Some of the ROCm-specific use cases that the installer currently supports are:    

- OpenCL (ROCr/KFD based) runtime  

- HIP runtimes  

- ROCm libraries and applications  

- ROCm Compiler and device libraries  

- ROCr runtime and thunk  

- Kernel mode driver  

For more details, refer to the AMD ROCm Installation Guide v4.5.2 at, 

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html


## HIP ENHANCEMENTS


The ROCm v4.5.2 release consists of the following HIP enhancement. 

### Changes to the roc-obj-ls Tool 

The roc-obj-ls tool is corrected in ROCm v4.5.2, and the command roc-obj-ls <exe> | roc-obj-extract is no longer the preferred syntax.   

Use the roc-obj tool with the following correct command:  

```   

        roc-obj <exe> 
 
 ```   

For example, 

Extract all ROCm code objects from a list of executables 
 
 ```   

       roc-obj <executable>... 
 
 ```   

Extract all ROCm code objects from a list of executables, and disassemble them 
 
 ```   

       roc-obj --disassemble <executable>... 
 
       # or 

       roc-obj -d <executable>... 

 ```   

Extract all ROCm code objects from a list of executables into dir/ 
 
 ```   

       roc-obj --outdir dir/ <executable>... 

       # or 

       roc-obj -o dir/ <executable>... 

 ```   

Extract only ROCm code objects matching regex over Target ID 
 
 ```   

       roc-obj --target-id gfx9 <executable>... 

        # or 

       roc-obj -t gfx9 <executable>... 

```    

For more information, refer to the HIP Programming Guide at:  

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_Programming_Guide.pdf


 ## OPENMP DEFECT FIX

Previously, ROCProfiler crashed when the following ROCProfiler options were used in OpenMP programs: 

* --stats  

* --hsa-trace 

This issue is fixed in the OpenMP plugin by ensuring that the contents of a kernel dispatch packet are not accessed after publishing it. The issue is also fixed in ROCTracer by ensuring that the registered exit function is called before the runtime library is closed. 
 
 

# AMD ROCm™ v4.5 Release Notes 

This document describes the features, fixed issues, and information about downloading and installing the AMD ROCm™ software. It also covers known issues and deprecations in this release.

- Supported Operating Environments and Documentation Updates
  * [Supported Operating Environments](#Supported-Operating-Environments)
  * [ROCm Installation Updates](#ROCm-Installation-Updates)
  * [AMD ROCm Documentation Updates](#AMD-ROCm-Documentation-Updates)

   
- What\'s New in This Release
  * [HIP Enhancements](#HIP-Enhancements)
  * [Unified Memory Support in ROCm](#Unified-Memory-Support-in-ROCm)
  * [System Management Interface](#System-Management-Interface) 
  * [ROCm Math and Communication Libraries](#ROCm-Math-and-Communication-Libraries)
  * [OpenMP Enhancements](#OpenMP-Enhancements)   

- Known Issues in This Release
  * [Known Issues in This Release](#Known-Issues-in-This-Release)

- Deprecations in This Release
  * [Deprecations](#Deprecations)

- [Hardware and Software Support](#Hardware-and-Software-Support)

- [Machine Learning and High Performance Computing Software Stack for AMD GPU](#Machine-Learning-and-High-Performance-Computing-Software-Stack-for-AMD-GPU)
  * [ROCm Binary Package Structure](#ROCm-Binary-Package-Structure)
  * [ROCm Platform Packages](#ROCm-Platform-Packages)
  



# ROCm Installation Updates

This document describes the features, fixed issues, and information
about downloading and installing the AMD ROCm™ software.

It also covers known issues and deprecations in this release.

## Supported Operating Environments

The AMD ROCm platform supports the following operating systems:

| OS                | Kernel              |
| ---               | ---                 |
| SLES15 SP3        | 5.3.18-24.49        |
| RHEL 7.9          | 3.10.0-1160.6.1.el7 |
| CentOS 7.9        | 3.10.0-1127         |
| RHEL 8.4          | 4.18.0-193.1.1.el8  |
| CentOS 8.3        | 4.18.0-193.el8      |
| Ubuntu 18.04.5    | 5.4.0-71-generic    |
| Ubuntu 20.04.3HWE | 5.8.0-48-generic    |



## Enhanced Installation Process for ROCm v4.5

In addition to the installation method using the native Package Manager, AMD ROCm v4.5 introduces added methods to install ROCm. With this
release, the ROCm installation uses the *amdgpu-install* and *amdgpu-uninstall* scripts. 

The *amdgpu-install* script streamlines the installation process by:

-   Abstracting the distribution-specific package installation logic

-   Performing the repository set-up

-   Allowing user to specify the use case and automating the installation of all the required packages,

-   Performing post-install checks to verify whether the installation was performed successfully

-   Installing the uninstallation script

The *amdgpu-uninstall* script allows the removal of the entire ROCm stack by using a single command.

Some of the ROCm-specific use cases that the installer currently supports are:

-   OpenCL (ROCr/KFD based) runtime

-   HIP runtimes

-   ROCm libraries and applications

-   ROCm Compiler and device libraries

-   ROCr runtime and thunk

**Note:** Graphics use cases are not supported in this release.

For more details, refer to the AMD ROCm Installation Guide v4.5 at,

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html


# AMD ROCm Documentation Updates 

## AMD ROCm Installation Guide 

The AMD ROCm Installation Guide in this release includes the following
updates:

-   New - Installation Guide for ROCm v4.5

    https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html


## AMD Instinct™ High Performance Computing and Tuning

- New - AMD Instinct™ High Performance Computing and Tuning Guide 

   https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD%20Instinct%E2%84%A2High%20Performance%20Computing%20and%20Tuning%20Guide.pdf
   
   
## HIP Documentation

-  HIP installation instructions

   https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP-Installation.html

-   HIP Programming Guide

    https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_Programming_Guide.pdf

-   HIP API Guide

    https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD-HIP-API-4.5.pdf

-   HIP-Supported CUDA API Reference Guide

    https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_Supported_CUDA_API_Reference_Guide.pdf

-   AMD ROCm Compiler Reference Guide

    https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_Compiler_Reference_Guide_v4.5.pdf

-   HIP FAQ

    <https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-FAQ.html#hip-faq>
   

## System Interface Management

-   System Interface Management (SMI)

    https://rocmdocs.amd.com/en/latest/ROCm_System_Managment/ROCm-System-Managment.html
    

## AMD ROCm Data Center Tool

- AMD ROCm Data Center Tool API Guide

  https://github.com/RadeonOpenCompute/ROCm/blob/master/RDC_API_Manual_4.5.pdf
  
- AMD ROCm Data Center Tool User Guide

  https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_ROCm_DataCenter_Tool_User_Guide_v4.5.pdf

## ROCm SMI API Guide

-   ROCm SMI API Guide

    https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCm_SMI_Manual_4.5.pdf

## ROC Debugger User and API Guide 

-   ROCDebugger User Guide

    https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCDebugger_User_Guide.pdf

-   Debugger API Guide

    https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCDebugger_API_Guide.pdf
    
## OpenMP Documentation

- Updated OpenMP documentation 

  https://rocmdocs.amd.com/en/latest/Programming_Guides/openmp_support.html
  

## AMD ROCm General Documentation Links

-   For AMD ROCm documentation, see

    https://rocmdocs.amd.com/en/latest/

-   For installation instructions on supported platforms, see

    https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

-   For AMD ROCm binary structure, see

    https://rocmdocs.amd.com/en/latest/Installation_Guide/Software-Stack-for-AMD-GPU.html

-   For AMD ROCm release history, see

    https://rocmdocs.amd.com/en/latest/Current_Release_Notes/ROCm-Version-History.html


# What's New in This Release 

## HIP Enhancements

The ROCm v4.5 release consists of the following HIP enhancements:

### HIP Direct Dispatch

The conventional producer-consumer model where the host thread(producer) enqueues commands to a command queue (per stream), which is then
processed by a separate, per-stream worker thread (consumer) created by the runtime, is no longer applicable.

In this release, for Direct Dispatch, the runtime directly queues a packet to the AQL queue (user mode queue to GPU) in Dispatch and some of
the synchronization. This new functionality indicates the total latency of the HIP Dispatch API and the latency to launch the first wave on the
GPU.

In addition, eliminating the threads in runtime has reduced the variance in the dispatch numbers as the thread scheduling delays and
atomics/locks synchronization latencies are reduced.

This feature can be disabled by setting the following environment variable,

```     
     AMD_DIRECT_DISPATCH=0

```

### Support for HIP Graph 

ROCm v4.5 extends support for HIP Graph. For details, refer to the HIP API Guide at

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD-HIP-API-4.5.pdf

### Enhanced *launch_bounds* Check Error Log Message 

When a kernel is launched with HIP APIs, for example, hipModuleLaunchKernel(), HIP validates to check that input kernel
dimension size is not larger than specified launch_bounds.

If exceeded, HIP returns launch failure if AMD_LOG_LEVEL is set with the proper value. Users can find more information in the error log message,
including launch parameters of kernel dim size, launch bounds, and the name of the faulting kernel. It is helpful to figure out the faulting
kernel. Besides, the kernel dim size and launch bounds values will also assist in debugging such failures.

For more details, refer to the HIP Programming Guide at

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_Programming_Guide.pdf


### HIP Runtime Compilation

HIP now supports runtime compilation (hipRTC), the usage of which will provide the possibility of optimizations and performance improvement
compared with other APIs via regular offline static compilation. 

hipRTC APIs accept HIP source files in character string format as input parameters and create handles of programs by compiling the HIP source
files without spawning separate processes.

For more details on hipRTC APIs, refer to the HIP API Guide at

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD-HIP-API-4.5.pdf

### New Flag for Backwards Compatibility on float/double atomicAdd Function

In the ROCm4.5 release, a new compilation flag is introduced as an option in the CMAKE file. This flag ensures backwards compatibility in
float/double atomicAdd functions.

```   
     \_\_HIP_USE_CMPXCHG_FOR_FP_ATOMICS
```   

This compilation flag is not set("0") by default, so the HIP runtime uses the current float/double atomicAdd functions.

If this compilation flag is set to "1" with the CMAKE option, the existing float/double atomicAdd functions is used for compatibility with
compilers that do not support floating point atomics.

```  
     D\_\_HIP_USE_CMPXCHG_FOR_FP_ATOMICS=1
```  
For details on how to build the HIP runtime, refer to the HIP Programming Guide at

https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_Programming_Guide.pdf



### Updated HIP Version Definition

The HIP version definition is updated as follows:

```  
     HIP_VERSION=HIP_VERSION_MAJOR * 10000000 + HIP_VERSION_MINOR *
     100000 + HIP_VERSION_PATCH)
```  

The HIP version can be queried from the following HIP API call,

```  
     hipRuntimeGetVersion(&runtimeVersion);
```  

The version returned is always greater than the versions in the previous ROCm releases.

**Note:** The version definition of the HIP runtime is different from that of CUDA. The function returns the HIP runtime version on the AMD
platform, while on the NVIDIA platform, it returns the CUDA runtime version. There is no mapping or a correlation between the HIP and CUDA
versions.



### Planned HIP Enhancements and Fixes

#### Changes to hiprtc implementation to match nvrtc behavior

In this release, there are changes to the *hiprtc* implementation to
match the *nvrtc* behavior.

**Impact:** Applications can no longer explicitly include HIP runtime header files. Minor code changes are required to remove the HIP runtime
header files.

#### HIP device attribute enumeration

In a future release, there will be a breaking change in the HIP device attribute enumeration. Enum values are being rearranged to accommodate
future enhancements and additions.

**Impact:** This will require users to rebuild their applications. No code changes are required.

#### Changes to behavior of hipGetLastError() and hipPeekAtLastError() to match CUDA behavior available

In a later release, changes to behavior of hipGetLastError() and hipPeekAtLastError() to match CUDA behavior will be available.

**Impact:** Applications relying on the previous behavior will be impacted and may require some code changes.

## Unified Memory Support in ROCm

Unified memory allows applications to map and migrate data between CPU and GPU seamlessly without explicitly copying it between different
allocations. This enables a more complete implementation of *hipMallocManaged*, *hipMemAdvise*, *hipMemPrefetchAsync* and related
APIs. Without unified memory, these APIs only support system memory. With unified memory, the driver can automatically migrate such memory to
GPU memory for faster access.

### Supported Operating Systems and Versions

This feature is only supported on recent Linux kernels. Currently, it works on Ubuntu versions with 5.6 or newer kernels and the DKMS driver
from ROCm. Current releases of RHEL and SLES do not support this feature yet. Future releases of those distributions will add support for this.
The unified memory feature is also supported in the KFD driver included with upstream kernels starting from Linux 5.14.

Unified memory only works on GFXv9 and later GPUs, including Vega10 and MI100. Fiji, Polaris and older GPUs are not supported. To check whether
unified memory is enabled, look in the kernel log for this message:

```  
     \$ dmesg \| grep \"HMM registered"
```  

If unified memory is enabled, there should be a message like "HMM registered xyzMB device memory". If unified memory is not supported on
your GPU or kernel version, this message is missing.

### Unified Memory Support and XNACK

Unified memory support comes in two flavours, XNACK-enabled and XNACK-disabled. XNACK refers to the ability of the GPU to handle page
faults gracefully and retry a memory access. In XNACK-enabled mode, the GPU can handle retry after page-faults, which enables mapping and
migrating data on demand, as well as memory overcommitment. In XNACK-disabled mode, all memory must be resident and mapped in the GPU
page tables when the GPU is executing application code. Any migrations involve temporary preemption of the GPU queues by the driver. Both page
fault handling and preemptions, happen automatically and are transparent to the applications.

XNACK-enabled mode only has experimental support. XNACK-enabled mode requires compiling shader code differently. By default, the ROCm
compiler builds code that works in both modes. Code can be optimized for one specific mode with compiler options:

OpenCL:

```  
     clang \... -mcpu=gfx908:xnack+:sramecc- \... // xnack on, sramecc off\
     clang \... -mcpu=gfx908:xnack-:sramecc+ \... // xnack off, sramecc on
```  

HIP:
```  
     clang \... \--cuda-gpu-arch=gfx906:xnack+ \... // xnack on\
     clang \... \--cuda-gpu-arch=gfx906:xnack- \... // xnack off
```  
Not all the math libraries included in ROCm support XNACK-enabled mode on current hardware. Applications will fail to run if their shaders are
compiled in the incorrect mode.

On current hardware, the XNACK mode can be chosen at boot-time by a module parameter amdgpu.noretry. The default is XNACK-disabled
(amdgpu.noretry=1).

## System Management Interface 

### Enhanced ROCm SMI --setpoweroverdrive Functionality

The ROCm System Management Interface (SMI) *--setpoweroverdrive* functionality is used to lower the power cap on a device without needing
to enable the OverDrive functionality in the driver. Similarly, even with the OverDrive driver functionality enabled, it is possible to
request a lower power cap than the card's default.

Currently, any use of the *--setpoweroverdrive* functionality in rocm-smi prints an out-of-spec warning to the screen and requires the
user to agree that using this functionality potentially voids their warranty. However, this warning should only be printed when users are
trying to set the power cap to higher than the card's default, which requires the OverDrive driver functionality to be enabled.

For example:

The default power cap is 225.0W before any changes.

```

     \[atitest\@rhel85 smi\]\$ ./rocm_smi.py --resetpoweroverdrive
     ======================= ROCm System Management Interface =======================

     ========================== Reset GPU Power OverDrive ===========================

     GPU\[0\] : Successfully reset Power OverDrive to: 225W
     ============================ End of ROCm SMI Log ============================

     Now, after using --setpoweroverdrive to lower the power cap to 123
     watts:

     \[atitest\@rhel85 smi\]\$ ./rocm_smi.py --setpoweroverdrive 123
     ======================= ROCm System Management Interface =======================

     =========================== Set GPU Power OverDrive ============================

     GPU\[0\] : Successfully set power to: 123W
     ======================= End of ROCm SMI Log ==============================

     Setting a power cap lower than the default of 225.0W (in this case,
     123W) does not give a warning.

     To verify that the power is set to the correct value:

     \[atitest\@rhel85 smi\]\$ ./rocm_smi.py --showmaxpower
     ======================= ROCm System Management Interface =======================

     ======================== Power Cap ===================================

     GPU\[0\] : Max Graphics Package Power (W): 123.0
     ========================End of ROCm SMI Log ==============================
```


## OpenMP Enhancements

The ROCm installation includes an LLVM-based implementation, which fully supports OpenMP 4.5 standard and a subset of the OpenMP 5.0 standard.
Fortran and C/C++ compilers and corresponding runtime libraries are included. Along with host APIs, the OpenMP compilers support offloading
code and data onto GPU devices.

For more information, refer to

<https://rocmdocs.amd.com/en/latest/Programming_Guides/openmp_support.html>

## ROCm Math and Communication Libraries

In this release, ROCm Math and Communication Libraries consists of the
following enhancements and fixes:

| Library   | Changes                                                  |
| ---       | ---                                                      |
| rocBLAS | **Optimizations** <ul><li>Improved performance of non-batched and batched syr for all sizes and data types</li><li>Improved performance of non-batched and batched hemv for all sizes and data types</li><li>Improved performance of non-batched and batched symv for all sizes and data types</li><li>Improved memory utilization in rocblas-bench, rocblas-test gemm functions, increasing possible runtime sizes.</li></ul>**Changes** <ul><li>Update from C++14 to C++17.</li>  <li>Packaging split into a runtime package (called rocblas) and a development package (called rocblas-dev for .deb packages, and rocblas-devel for .rpm packages). The development package depends on runtime. The runtime package suggests the development package for all supported OSes except CentOS 7 to aid in the transition. The 'suggest' feature in packaging is introduced as a deprecated feature and will be removed in a future ROCm release.</li></ul> **Fixed**<ul><li>For function geam avoid overflow in offset calculation.</li>  <li> For function syr avoid overflow in offset calculation.</li> <li>For function gemv (Transpose-case) avoid overflow in offset calculation.</li> <li>For functions ssyrk and dsyrk, allow conjugate-transpose case to match legacy BLAS. Behavior is the same as the transpose case.</li></ul> |
| hipBLAS| **Added**<ul><li>More support for hipblas-bench</li></ul>**Fixed**<ul><li>Avoid large offset overflow for gemv and hemv in hipblas-test</li></ul>**Changed**<ul><li>Packaging split into a runtime package called hipblas and a development package called hipblas-devel. The development package depends on runtime. The runtime package suggests the development package for all supported OSes except CentOS 7 to aid in the transition. The 'suggests' feature in packaging is a transitional feature and will be removed in a future rocm release.</li></ul> |
| rocFFT | **Optimizations**<ul><li>Optimized SBCC kernels of length 52, 60, 72, 80, 84, 96, 104, 108, 112, 160, 168, 208, 216, 224, 240 with new kernel generator.</li></ul>**Added**<ul><li>Split 2D device code into separate libraries.</li> </ul>**Changed**<ul><li>Packaging split into a runtime package called rocfft and a development package called rocfft-devel. The development package depends on runtime. The runtime package suggests the development package for all supported OSes except CentOS 7 to aid in the transition. The suggests feature in packaging is introduced as a deprecated feature and will be removed in a future rocm release.</li></ul>**Fixed**<ul><li>Fixed a few validation failures of even-length R2C inplace. 2D, 3D cubics sizes such as 100^2 (or ^3), 200^2 (or ^3), 256^2 (or ^3)...etc. We don't combine the three kernels (stockham-r2c-transpose). We only combine two kernels (r2c-transpose) instead.</li></ul> |
| hipFFT | **Changed**  <ul><li>Packaging split into a runtime package called hipfft and a development package called hipfft-devel. The development package depends on runtime. The runtime package suggests the development package for all supported OSes except CentOS 7 to aid in the transition. The 'suggests' feature in packaging is a transitional feature and will be removed in a future rocm release.</li></ul> |
| rocSPARSE | **Added** <ul><li>Triangular solve for multiple right-hand sides using BSR format</li> <li>SpMV for BSRX format</li> <li>SpMM in CSR format enhanced to work with transposed A</li> <li>Matrix coloring for CSR matrices </li><li>Added batched tridiagonal solve (gtsv_strided_batch)</li></ul> **Improved** <ul><li>Fixed a bug with gemvi on Navi21 </li><li>Optimization for pivot based gtsv</li></ul> |
| hipSPARSE | **Added** <ul><li>Triangular solve for multiple right-hand sides using BSR format</li> <li>SpMV for BSRX format</li> <li>SpMM in CSR format enhanced to work with transposed A</li> <li>Matrix coloring for CSR matrices </li>  <li>Added batched tridiagonal solve (gtsv_strided_batch)</li></ul> **Improved** <ul><li>Fixed a bug with gemvi on Navi21</li> <li>Optimization for pivot based gtsv</li></ul> |
| rocALUTION | **Changed** <ul><li>Packaging split into a runtime package called rocalution and a development package called rocalution-devel. The development package depends on runtime. The runtime package suggests the development package for all supported OSes except CentOS 7 to aid in the transition. The 'suggests' feature in packaging is a transitional feature and will be removed in a future rocm release.</li></ul> **Improved** <ul><li>(A)MG solving phase optimization</li></ul> |
| rocTHRUST | **Changed**  <ul><li>Packaging changed to a development package (called rocthrust-dev for .deb packages, and rocthrust-devel for .rpm packages). As rocThrust is a header-only library, there is no runtime package. To aid in the transition, the development package sets the "provides" field to provide the package rocthrust, so that existing packages depending on rocthrust can continue to work. The 'provides' feature is a transitional feature and will be removed in a future ROCm release.</li></ul> |
| rocSOLVER | **Added** <ul><li>RQ factorization routines:</li><li>GERQ2, GERQF (with batched and strided_batchedversions)</li>  <li>Linear solvers for general square systems:</li> <li>GESV (with batched and strided_batched versions)</li><li>Linear solvers for symmetric/hermitian positive definite systems:</li> <li>POTRS (with batched and strided_batched versions)</li> <li>POSV (with batched and strided_batched versions) </li> <li>Inverse of symmetric/hermitian positive definite matrices:</li><li>POTRI (with batched and strided_batched versions)</li> <li>General matrix inversion without pivoting:  </li>  <li>GETRI_NPVT (with batched and strided_batched versions)</li> <li>GETRI_NPVT_OUTOFPLACE (with batched and  strided_batched versions)</li></ul>**Optimized**<ul><li>Improved performance of LU factorization (especially for large matrix sizes)</li> <li>Changed</li>  <li>Raised reference LAPACK version used for rocSOLVER test and benchmark clients to v3.9.1</li>  <li>Minor CMake improvements for users building from source without install.sh:</li> <li>Removed fmt::fmt from rocsolver\'s public usage requirements</li> <li>Enabled small-size optimizations by default </li>  <li>Split packaging into a runtime package ('rocsolver') and a development package ('rocsolver-devel'). The development package depends on the runtime package. To aid in the transition, the runtime package suggests the development package (except on CentOS 7). This use of the 'suggests feature' is transitional and will be removed in a future ROCm release.</li></ul> **Fixed** <ul><li>Use of the GCC / Clang __attribute__((deprecated(...))) extension is now guarded by compiler detection macros. |
| hipSOLVER | The following functions were added in this release:<ul><li>gesv</li><ul><li>hipsolverSSgesv_bufferSize, hipsolverDDgesv_bufferSize, hipsolverCCgesv_bufferSize, hipsolverZZgesv_bufferSize</li><li>hipsolverSSgesv, hipsolverDDgesv, hipsolverCCgesv, hipsolverZZgesv</li></ul><li>potrs</li><ul><li>hipsolverSpotrs_bufferSize, hipsolverDpotrs_bufferSize, hipsolverCpotrs_bufferSize, hipsolverZpotrs_bufferSize</li><li>hipsolverSpotrs, hipsolverDpotrs, hipsolverCpotrs, hipsolverZpotrs</li></ul><li>potrsBatched</li><ul><li>hipsolverSpotrsBatched_bufferSize, hipsolverDpotrsBatched_bufferSize, hipsolverCpotrsBatched_bufferSize, hipsolverZpotrsBatched_bufferSize</li><li>hipsolverSpotrsBatched, hipsolverDpotrsBatched, hipsolverCpotrsBatched, hipsolverZpotrsBatched</li></ul><li>potri</li><ul><li>hipsolverSpotri_bufferSize, hipsolverDpotri_bufferSize, hipsolverCpotri_bufferSize, hipsolverZpotri_bufferSize</li><li>hipsolverSpotri, hipsolverDpotri, hipsolverCpotri, hipsolverZpotri</li></ul></ul></li></ul> |
| RCCL | **Added** <ul><li>Compatibility with NCCL 2.9.9 </li></ul>**Changed**  <ul><li>Packaging split into a runtime package called rccl and a development package called rccl-devel. The development package depends on runtime. The runtime package suggests the development package for all supported OSes except CentOS 7 to aid in the transition. The 'suggests' feature in packaging is a tranistional feature and will be removed in a future rocm release.</li></ul> |
| hipCUB | **Changed**  <ul><li>Packaging changed to a development package (called hipcub-dev for .deb packages, and hipcub-devel for .rpm packages). As hipCUB is a header-only library, there is no runtime package. To aid in the transition, the development package sets the "provides" field to provide the package hipcub, so that existing packages depending on hipcub can continue to work. This provides feature is introduced as a deprecated feature and will be removed in a future ROCm release.</li></ul> |
| rocPRIM| **Added** <ul><li>bfloat16 support added.</li></ul> **Changed**  <ul><li>Packaging split into a runtime package called rocprim and a development package called rocprim-devel. The development package depends on runtime. The runtime package suggests the development package for all supported OSes except CentOS 7 to aid in the transition. The suggests feature in packaging is introduced as a deprecated feature and will be removed in a future rocm release.</li> <li>As rocPRIM is a header-only library, the runtime package is an empty placeholder used to aid in the transition. This package is also a deprecated feature and will be removed in a future rocm release.</li></ul> **Deprecated** <ul><li>The warp_size() function is now deprecated; please switch to host_warp_size() and device_warp_size() for host and device references respectively.</li></ul> |
| rocRAND| **Changed**  <ul><li>Packaging split into a runtime package called rocrand and a development package called rocrand-devel. The development package depends on runtime. The runtime package suggests the development package for all supported OSes except CentOS 7 to aid in the transition. The suggests feature in packaging is introduced as a deprecated feature and will be removed in a future rocm release.</li></ul> **Fixed** <ul><li>Fix for mrg_uniform_distribution_double generating incorrect range of values</li> <li>Fix for order of state calls for log_normal, normal, and uniform</li></ul> **Known issues**  <ul><li>kernel_xorwow test is failing for certain GPU architectures.</li></ul> |

For more information about ROCm Libraries, refer to the documentation at

<https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html>

# Known Issues in This Release 

The following are the known issues in this release.

## clinfo and rocminfo Do Not Display Marketing Name

clinfo and rocminfo display a blank field for Marketing Name. 

This is due to a missing package that is not yet available from ROCm. This package will be distributed in future ROCm releases.

## Compiler Support for Function Pointers and Virtual Functions

A known issue in the compiler support for function pointers and virtual functions on the GPU may cause undefined behavior due to register
corruption. 

A temporary workaround is to compile the affected application with this option:

```
     -mllvm -amdgpu-fixed-function-abi=1
     
 ```

**Note:** This is an internal compiler flag and may be removed without notice once the issue is addressed in a future release.


## Debugger Process Exit May Cause ROCgdb Internal Error

If the debugger process exits during debugging, ROCgdb may report internal errors. This issue occurs as it attempts to access the AMD GPU
state for the exited process. To recover, users must restart ROCgdb.
 
As a workaround, users can set breakpoints to prevent the debugged process from exiting. For example, users can set breakpoints at the last
statement of the main function and in the abort() and exit() functions. This temporary solution allows the application to be re-run without
restarting ROCgdb.

This issue is currently under investigation and will be fixed in a future release.

For more information, refer to the ROCgdb User Guide at,

https://github.com/RadeonOpenCompute/ROCm/blob/master/ROCDebugger_User_Guide.pdf

## Cache Issues with ROCProfiler

When the same kernel is launched back-to-back multiple times on a GPU, a cache flush is executed each time the kernel finishes when profiler data is collected. The cache flush is inserted by ROCprofiler for each kernel. This prevents kernel from being cached, instead it is being read each time it is launched. As a result the cache hit rate from rocprofiler is reported as 0% or very low.

This issue is under investigation and will be fixed in a future release. 

## Stability Issue on LAMMPS-KOKKOS Applications

On mGPU machines, lammps-kokkos applications experience a stability issue (AMD Instinct MI100™). 

As a workaround, perform a Translation LookAside Buffer (TLB) flush. 

The issue is under active investigation and will be resolved in a future release.



# Deprecations

## AMD Instinct MI25 End of Life

ROCm release v4.5 is the final release to support AMD Instinct MI25. AMD Instinct MI25 has reached End of Life (EOL). ROCm 4.5 represents the
last certified release for software and driver support. AMD will continue to provide technical support and issue resolution for AMD
Instinct MI25 on ROCm v4.5 for a period of 12 months from the software GA date. 

## Planned Deprecation for Code Object Versions 2 and 3 

With the ROCm v4.5 release, the generation of code object versions 2 and 3 is being deprecated and may be removed in a future release. This deprecation notice does not impact support for the execution of AMD GPU code object versions.

The -mcode-object-version Clang option can be used to instruct the compiler to generate a specific AMD GPU code object version. In ROCm v4.5, the compiler can generate AMD GPU code object version 2, 3, and 4, with version 4 being the default if not specified. 



# Deploying ROCm

AMD hosts both Debian and RPM repositories for the ROCm packages. 

For more information on ROCM installation on all platforms, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html


# Machine Learning and High Performance Computing Software Stack for AMD GPU

For an updated version of the software stack for AMD GPU, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Software-Stack-for-AMD-GPU.html



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

The information presented in this document is for informational purposes only and may contain technical inaccuracies, omissions, and typographical errors.  The information contained herein is subject to change and may be rendered inaccurate for many reasons, including but not limited to product and roadmap changes, component and motherboard versionchanges, new  model and/or product releases, product differences between differing manufacturers, software changes, BIOS flashes, firmware upgrades, or the like. Any computer system has risks of security vulnerabilities that cannot be completely prevented or mitigated.AMD  assumes  no  obligation  to  update  or  otherwise  correct  or  revise  this  information.  However, AMD reserves the right to revise this information and to make changes from time to time to the content hereof without obligation of AMD to notify any person of such revisions or changes.THIS INFORMATION IS PROVIDED ‘AS IS.” AMD MAKES NO REPRESENTATIONS OR WARRANTIES WITH RESPECT  TO  THE  CONTENTS  HEREOF  AND  ASSUMES  NO  RESPONSIBILITY  FOR  ANY  INACCURACIES, ERRORS, OR OMISSIONS THAT MAY APPEAR IN THIS INFORMATION. AMD SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR ANY PARTICULAR PURPOSE.  IN NO EVENT WILL AMD BE LIABLE TO ANY PERSON FOR ANY RELIANCE, DIRECT, INDIRECT, SPECIAL,  OR  OTHER  CONSEQUENTIAL  DAMAGES  ARISING  FROM  THE  USE  OF  ANY  INFORMATION CONTAINED HEREIN, EVEN IF AMD IS EXPRESSLY ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.AMD,  the  AMD  Arrow  logo, and combinations thereof are trademarks of Advanced Micro Devices, Inc.Other product names  used  in  this  publication  are  for  identification  purposes  only  and  may  be  trademarks  of  their respective  companies.
©[2021]Advanced Micro Devices, Inc.All rights reserved.

## Third-party Disclaimer
Third-party content is licensed to you directly by the third party that owns the content and is not licensed to you by AMD.  ALL LINKED THIRD-PARTY CONTENT IS PROVIDED “AS IS” WITHOUT A WARRANTY OF ANY KIND.  USE OF SUCH THIRD-PARTY CONTENT IS DONE AT YOUR SOLE DISCRETION AND UNDER NO CIRCUMSTANCES WILL AMD BE LIABLE TO YOU FOR ANY THIRD-PARTY CONTENT.  YOU ASSUME ALL RISK AND ARE SOLELY RESPONSIBLE FOR ANY DAMAGES THAT MAY ARISE FROM YOUR USE OF THIRD-PARTY CONTENT. 






