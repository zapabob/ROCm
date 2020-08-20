
# AMD ROCm Release Notes v3.7.0

This page describes the features, fixed issues, and information about downloading and installing the ROCm software.
It also covers known issues and deprecated features in this release.

- [Supported Operating Systems and Documentation Updates](#Supported-Operating-Systems-and-Documentation-Updates)
  * [Supported Operating Systems](#Supported-Operating-Systems)
  * [AMD ROCm Documentation Updates](#AMD-ROCm-Documentation-Updates)
   
- [What\'s New in This Release](#Whats-New-in-This-Release)
  * [AOMP Enhancements](#AOMP-Enhancements)
  * [Compatibility with NVIDIA Communications Collective Library v2\.7 API](#Compatibility-with-NVIDIA-Communications-Collective-Library-v27-API)
  * [Singular Value Decomposition of Bi\-diagonal Matrices](#Singular-Value-Decomposition-of-Bi-diagonal-Matrices)
  * [rocSPARSE_gemmi\() Operations for Sparse Matrices](#rocSPARSE_gemmi-Operations-for-Sparse-Matrices)
    
 
- [Known Issues](#Known-Issues)

- [Deploying ROCm](#Deploying-ROCm)
 
- [Hardware and Software Support](#Hardware-and-Software-Support)

- [Machine Learning and High Performance Computing Software Stack for AMD GPU](#Machine-Learning-and-High-Performance-Computing-Software-Stack-for-AMD-GPU)
  * [ROCm Binary Package Structure](#ROCm-Binary-Package-Structure)
  * [ROCm Platform Packages](#ROCm-Platform-Packages)
  


# Supported Operating Systems 

## Support for Ubuntu 20.04 


In this release, AMD ROCm extends support to Ubuntu 20.04, including dual-kernel.

## List of Supported Operating Systems

The AMD ROCm v3.7.x platform is designed to support the following operating systems:

* Ubuntu 20.04 and 18.04.4 (Kernel 5.3)	
* CentOS 7.8 & RHEL 7.8 (Kernel 3.10.0-1127) (Using devtoolset-7 runtime support)
* CentOS 8.2 & RHEL 8.2 (Kernel 4.18.0 ) (devtoolset is not required)
* SLES 15 SP1

## Fresh Installation of AMD ROCm v3.7 Recommended
A fresh and clean installation of AMD ROCm v3.7 is recommended. An upgrade from previous releases to AMD ROCm v3.7 is not supported.

For more information, refer to the AMD ROCm Installation Guide at:
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

**Note**: AMD ROCm release v3.3 or prior releases are not fully compatible with AMD ROCm v3.5 and higher versions. You must perform a fresh ROCm installation if you want to upgrade from AMD ROCm v3.3 or older to 3.5 or higher versions and vice-versa.


# AMD ROCm Documentation Updates

## AMD ROCm Installation Guide 

The AMD ROCm Installation Guide in this release includes:

* Updated Supported Environments
* HIP Installation Instructions

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html


## AMD ROCm - HIP Documentation Updates

### Texture and Surface Functions
The documentation for Texture and Surface functions is updated and available at:

https://rocmdocs.amd.com/en/latest/Programming_Guides/Kernel_language.html

### Warp Shuffle Functions
The documentation for Warp Shuffle functions is updated and available at:

https://rocmdocs.amd.com/en/latest/Programming_Guides/Kernel_language.html

### Compiler Defines and Environment Variables
The documentation for the updated HIP Porting Guide is available at:

https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-porting-guide.html#hip-porting-guide


## AMD ROCm Debug Agent

ROCm Debug Agent Library 

https://rocmdocs.amd.com/en/latest/ROCm_Tools/rocm-debug-agent.html


## General AMD ROCm Documentatin Links

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

## AOMP ENHANCEMENTS

AOMP is a scripted build of LLVM. It supports OpenMP target offload on AMD GPUs. Since AOMP is a Clang/LLVM compiler, it also supports GPU offloading with HIP, CUDA, and OpenCL.

The following enhancements are made for AOMP in this release: 
* OpenMP 5.0 is enabled by default. You can use -fopenmp-version=45 for OpenMP 4.5 compliance
* Restructured to include the ROCm compiler
* B=Bitcode search path using hip policy HIP_DEVICE_LIB_PATH and hip-devic-lib command line option to enable global_free for kmpc_impl_free

Restructured hostrpc, including:
* Replaced hostcall register functions with handlePayload(service, payload). Note, handlPayload has a simple switch to call the correct service handler function.
* Removed the WITH_HSA macro
* Moved the hostrpc stubs and host fallback functions into a single library and the include file. This enables the stubs openmp cpp source instead of hip and reorganizes the directory openmp/libomptarget/hostrpc.
* Moved hostrpc_invoke.cl to DeviceRTLs/amdgcn.
* Generalized the vargs processing in printf to work for any vargs function to execute on the host, including a vargs function that uses a function pointer.
* Reorganized files, added global_allocate and global_free.
* Fixed llvm TypeID enum to match the current upstream llvm TypeID.
* Moved strlen_max function inside the declare target #ifdef _DEVICE_GPU in hostrpc.cpp to resolve linker failure seen in pfspecifier_str smoke test.
* Fixed AOMP_GIT_CHECK_BRANCH in aomp_common_vars to not block builds in Red Hat if the repository is on a specific commit hash.
* Simplified and reduced the size of openmp host runtime
* Switched to default OpenMP 5.0

For more information, see https://github.com/ROCm-Developer-Tools/aomp
     

## ROCm COMMUNICATIONS COLLECTIVE LIBRARY

### Compatibility with NVIDIA Communications Collective Library v2\.7 API

ROCm Communications Collective Library (RCCL) is now compatible with the NVIDIA Communications Collective Library (NCCL) v2.7 API.

RCCL (pronounced "Rickle") is a stand-alone library of standard collective communication routines for GPUs, implementing all-reduce, all-gather, reduce, broadcast, reduce-scatter, gather, scatter, and all-to-all. There is also initial support for direct GPU-to-GPU send and receive operations. It has been optimized to achieve high bandwidth on platforms using PCIe, xGMI as well as networking using InfiniBand Verbs or TCP/IP sockets. RCCL supports an arbitrary number of GPUs installed in a single node or multiple nodes, and can be used in either single- or multi-process (e.g., MPI) applications.

The collective operations are implemented using ring and tree algorithms and have been optimized for throughput and latency. For best performance, small operations can be either batched into larger operations or aggregated through the API.

For more information about RCCL APIs and compatibility with NCCL v2.7, see
https://rccl.readthedocs.io/en/develop/index.html


## Singular Value Decomposition of Bi\-diagonal Matrices

Rocsolver_bdsqr now computes the Singular Value Decomposition (SVD) of bi-diagonal matrices. It is an auxiliary function for the SVD of general matrices (function rocsolver_gesvd). 

BDSQR computes the singular value decomposition (SVD) of a n-by-n bidiagonal matrix B.

The SVD of B has the following form:

B = Ub * S * Vb'
where 
•	S is the n-by-n diagonal matrix of singular values of B
•	the columns of Ub are the left singular vectors of B
•	the columns of Vb are its right singular vectors

The computation of the singular vectors is optional; this function accepts input matrices U (of size nu-by-n) and V (of size n-by-nv) that are overwritten with U*Ub and Vb’*V. If nu = 0 no left vectors are computed; if nv = 0 no right vectors are computed.

Optionally, this function can also compute Ub’*C for a given n-by-nc input matrix C.

PARAMETERS

•	[in] handle: rocblas_handle.

•	[in] uplo: rocblas_fill.

Specifies whether B is upper or lower bidiagonal.

•	[in] n: rocblas_int. n >= 0.

The number of rows and columns of matrix B.

•	[in] nv: rocblas_int. nv >= 0. 

The number of columns of matrix V.

•	[in] nu: rocblas_int. nu >= 0. 

The number of rows of matrix U.

•	[in] nc: rocblas_int. nu >= 0. 

The number of columns of matrix C.

•	[inout] D: pointer to real type. Array on the GPU of dimension n.

On entry, the diagonal elements of B. On exit, if info = 0, the singular values of B in decreasing order; if info > 0, the diagonal elements of a bidiagonal matrix orthogonally equivalent to B.

•	[inout] E: pointer to real type. Array on the GPU of dimension n-1.

On entry, the off-diagonal elements of B. On exit, if info > 0, the off-diagonal elements of a bidiagonal matrix orthogonally equivalent to B (if info = 0 this matrix converges to zero).

•	[inout] V: pointer to type. Array on the GPU of dimension ldv*nv.

On entry, the matrix V. On exit, it is overwritten with Vb’*V. (Not referenced if nv = 0).

•	[in] ldv: rocblas_int. ldv >= n if nv > 0, or ldv >=1 if nv = 0.

Specifies the leading dimension of V.

•	[inout] U: pointer to type. Array on the GPU of dimension ldu*n.

On entry, the matrix U. On exit, it is overwritten with U*Ub. (Not referenced if nu = 0).

•	[in] ldu: rocblas_int. ldu >= nu.

Specifies the leading dimension of U.

•	[inout] C: pointer to type. Array on the GPU of dimension ldc*nc.

On entry, the matrix C. On exit, it is overwritten with Ub’*C. (Not referenced if nc = 0).

•	[in] ldc: rocblas_int. ldc >= n if nc > 0, or ldc >=1 if nc = 0.

Specifies the leading dimension of C.

•	[out] info: pointer to a rocblas_int on the GPU.

If info = 0, successful exit. If info = i > 0, i elements of E have not converged to zero.

For more information, see
https://rocsolver.readthedocs.io/en/latest/userguide_api.html#rocsolver-type-bdsqr


### rocSPARSE_gemmi\() Operations for Sparse Matrices

This enhancement provides a dense matrix sparse matrix multiplication using the CSR storage format.
rocsparse_gemmi multiplies the scalar αα with a dense m×km×k matrix AA and the sparse k×nk×n matrix BB defined in the CSR storage format, and adds the result to the dense m×nm×n matrix CC that is multiplied by the scalar ββ, such that
C:=α⋅op(A)⋅op(B)+β⋅CC:=α⋅op(A)⋅op(B)+β⋅C
with

op(A)=⎧⎩⎨⎪⎪A,AT,AH,if trans_A == rocsparse_operation_noneif trans_A == rocsparse_operation_transposeif trans_A == rocsparse_operation_conjugate_transposeop(A)={A,if trans_A == rocsparse_operation_noneAT,if trans_A == rocsparse_operation_transposeAH,if trans_A == rocsparse_operation_conjugate_transpose

and

op(B)=⎧⎩⎨⎪⎪B,BT,BH,if trans_B == rocsparse_operation_noneif trans_B == rocsparse_operation_transposeif trans_B == rocsparse_operation_conjugate_transposeop(B)={B,if trans_B == rocsparse_operation_noneBT,if trans_B == rocsparse_operation_transposeBH,if trans_B == rocsparse_operation_conjugate_transpose
Note: This function is non-blocking and executed asynchronously with the host. It may return before the actual computation has finished.

For more information and examples, see
https://rocsparse.readthedocs.io/en/master/usermanual.html#rocsparse-gemmi
 

# Known Issues 
The following are the known issues in this release.

## (AOMP) ‘Undefined Hidden Symbol’ Linker Error Causes Compilation Failure in HIP

The HIP example device_lib fails to compile due to unreferenced symbols with Link Time Optimization resulting in ‘undefined hidden symbol’ errors. 

This issue is under investigation and there is no known workaround at this time.


## MIGraphX Fails for fp16 Datatype
The MIGraphX functionality does not work for the fp16 datatype.  

The following workaround is recommended: 

Use the AMD ROCm v3.3 of MIGraphX 

Or

Build MIGraphX v3.7 from the source using AMD ROCm v3.3

## Missing Google Test Installation May Cause RCCL Unit Test Compilation Failure
Users of the RCCL install.sh script may encounter an RCCL unit test compilation error. It is recommended to use CMAKE directly instead of install.sh to compile RCCL. Ensure Google Test 1.10+ is available in the CMAKE search path.


As a workaround, use the latest RCCL from the GitHub development branch at:
https://github.com/ROCmSoftwarePlatform/rccl/pull/237


## Issue with Peer-to-Peer Transfers 
Using peer-to-peer (P2P) transfers on systems without the hardware P2P assistance may produce incorrect results.

Ensure the hardware supports peer-to-peer transfers and enable the peer-to-peer setting in the hardware to resolve this issue. 


## Partial Loss of Tracing Events for Large Applications
An internal tracing buffer allocation issue can cause a partial loss of some tracing events for large applications.

As a workaround, rebuild the roctracer/rocprofiler libraries from the GitHub ‘roc-3.7’ branch at:
•	https://github.com/ROCm-Developer-Tools/rocprofiler
•	https://github.com/ROCm-Developer-Tools/roctracer


## GPU Kernel C++ Names Not Demangled
GPU kernel C++ names in the profiling traces and stats produced by ‘—hsa-trace’ option are not demangled.

As a workaround, users may choose to demangle the GPU kernel C++ names as required.


## ‘rocprof’ option ‘--parallel-kernels’ Not Supported in This Release

‘rocprof’ option ‘--parallel-kernels’ is available in the options list, however,  it is not fully validated and supported in this release.

## Random Soft Hang Observed When Running ResNet-Based Models

A random soft hang is observed when running ResNet-based models for a loop run of more than 25 to 30 hours.  The issue is observed on both PyTorch and TensorFlow frameworks.
You can terminate the unresponsive process to temporarily resolve the issue.

There is no known workaround at this time.



# Deploying ROCm
AMD hosts both Debian and RPM repositories for the ROCm v3.7.x packages. 

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

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#machine-learning-and-high-performance-computing-software-stack-for-amd-gpu-v3-5-0
