
New AMD ROCm Information Portal ROCm v4.5 and Above
-----------------------------------------------------

Beginning ROCm release v5.0, AMD ROCm documentation has a new portal at https://docs.amd.com  This portal consists of ROCm documentation v4.5 and above.

For documentation prior to ROCm v4.5, you may continue to access https://rocmdocs.amd.com.


# AMD ROCm™ v5.0 Release Notes


# ROCm Installation Updates

This document describes the features, fixed issues, and information about downloading and installing the AMD ROCm™ software.

It also covers known issues and deprecations in this release.

## Notice for Open-source and Closed-source ROCm Repositories in Future Releases

To make a distinction between open-source and closed-source components, all ROCm repositories will consist of sub-folders in future releases.

- All open-source components will be placed in the `base-url/<rocm-ver>/main` sub-folder
- All closed-source components will reside in the `base-url/<rocm-ver>/proprietary`  sub-folder

## List of Supported Operating Systems

The AMD ROCm platform supports the following operating systems:

| **OS-Version (64-bit)** | **Kernel Versions** |
| --- | --- |
| CentOS 8.3 | 4.18.0-193.el8 |
| CentOS 7.9 | 3.10.0-1127 |
| RHEL 8.5 | 4.18.0-348.7.1.el8\_5.x86\_64 |
| RHEL 8.4 | 4.18.0-305.el8.x86\_64 |
| RHEL 7.9 | 3.10.0-1160.6.1.el7 |
| SLES 15 SP3 | 5.3.18-59.16-default |
| Ubuntu 20.04.3 | 5.8.0 LTS / 5.11 HWE |
| Ubuntu 18.04.5 [5.4 HWE kernel] | 5.4.0-71-generic |

### Support for RHEL v8.5

This release extends support for RHEL v8.5.

### Supported GPUs

#### Radeon Pro V620 and W6800 Workstation GPUs

This release extends ROCm support for Radeon Pro V620 and W6800 Workstation GPUs.

- SRIOV virtualization support for Radeon Pro V620
- KVM Hypervisor (1VF support only) on Ubuntu Host OS with Ubuntu, CentOs, and RHEL Guest
- Support for ROCm-SMI in an SRIOV environment. For more details, refer to the ROCm SMI API documentation.

**Note:** Radeon Pro v620 is not supported on SLES.

## ROCm Installation Updates for ROCm v5.0

This release has the following ROCm installation enhancements.

### Support for Kernel Mode Driver

In this release, users can install the kernel-mode driver using the Installer method. Some of the ROCm-specific use cases that the installer currently supports are:

- OpenCL (ROCr/KFD based) runtime
- HIP runtimes
- ROCm libraries and applications
- ROCm Compiler and device libraries
- ROCr runtime and thunk
- Kernel-mode driver

### Support for Multi-version ROCm Installation and Uninstallation

Users now can install multiple ROCm releases simultaneously on a system using the newly introduced installer script and package manager install mechanism.

Users can also uninstall multi-version ROCm releases using the `amdgpu-uninstall` script and package manager.

### Support for Updating Information on Local Repositories

In this release, the `amdgpu-install` script automates the process of updating local repository information before proceeding to ROCm installation.

### Support for Release Upgrades

Users can now upgrade the existing ROCm installation to specific or latest ROCm releases.

For more details, refer to the AMD ROCm Installation Guide v5.0.

# AMD ROCm V5.0 Documentation Updates

## New AMD ROCm Information Portal – ROCm v4.5 and Above

Beginning ROCm release v5.0, AMD ROCm documentation has a new portal at https://docs.amd.com. This portal consists of ROCm documentation v4.5 and above.

For documentation prior to ROCm v4.5, you may continue to access https://rocmdocs.amd.com.

## Documentation Updates for ROCm 5.0

### Deployment Tools

#### ROCm Data Center Tool Documentation Updates

- ROCm Data Center Tool User Guide
- ROCm Data Center Tool API Guide

#### ROCm System Management Interface Updates

- System Management Interface Guide
- System Management Interface API Guide

#### ROCm Command Line Interface Updates

- Command Line Interface Guide

### Machine Learning/AI Documentation Updates

- Deep Learning Guide
- MIGraphX API Guide
- MIOpen API Guide
- MIVisionX API Guide

### ROCm Libraries Documentation Updates

- hipSOLVER User Guide
- RCCL User Guide
- rocALUTION User Guide
- rocBLAS User Guide
- rocFFT User Guide
- rocRAND User Guide
- rocSOLVER User Guide
- rocSPARSE User Guide
- rocThrust User Guide

### Compilers and Tools

#### ROCDebugger Documentation Updates

- ROCDebugger User Guide
- ROCDebugger API Guide

#### ROCTracer

- ROCTracer User Guide
- ROCTracer API Guide

#### Compilers

- AMD Instinct High Performance Computing and Tuning Guide
- AMD Compiler Reference Guide

#### HIPify Documentation

- HIPify User Guide
- HIP Supported CUDA API Reference Guide

#### ROCm Debug Agent

- ROCm Debug Agent Guide
- System Level Debug Guide
- ROCm Validation Suite

### Programming Models Documentation

#### HIP Documentation

- HIP Programming Guide
- HIP API Guide
- HIP FAQ Guide

#### OpenMP Documentation

- OpenMP Support Guide

### ROCm Glossary

- ROCm Glossary – Terms and Definitions

## AMD ROCm Legacy Documentation Links – ROCm v4.3 and Prior

- For AMD ROCm documentation, see

https://rocmdocs.amd.com/en/latest/

- For installation instructions on supported platforms, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

- For AMD ROCm binary structure, see

https://rocmdocs.amd.com/en/latest/Installation_Guide/Software-Stack-for-AMD-GPU.html

- For AMD ROCm release history, see

https://rocmdocs.amd.com/en/latest/Current_Release_Notes/ROCm-Version-History.html

# What's New in This Release

## HIP Enhancements

The ROCm v5.0 release consists of the following HIP enhancements.

### HIP Installation Guide Updates

The HIP Installation Guide is updated to include building HIP from source on the NVIDIA platform.

Refer to the HIP Installation Guide v5.0 for more details.

### Managed Memory Allocation

Managed memory, including the `__managed__` keyword, is now supported in the HIP combined host/device compilation. Through unified memory allocation, managed memory allows data to be shared and accessible to both the CPU and GPU using a single pointer. The allocation is managed by the AMD GPU driver using the Linux Heterogeneous Memory Management (HMM) mechanism. The user can call managed memory API hipMallocManaged to allocate a large chunk of HMM memory, execute kernels on a device, and fetch data between the host and device as needed.

**Note:** In a HIP application, it is recommended to do a capability check before calling the managed memory APIs. For example,

```c
int managed_memory = 0;
HIPCHECK(hipDeviceGetAttribute(&managed_memory, hipDeviceAttributeManagedMemory, p_gpuDevice));

if (!managed_memory) {
  printf ("info: managed memory access not supported on the device %d\n Skipped\n", p_gpuDevice);
} else {
  HIPCHECK(hipSetDevice(p_gpuDevice));
  HIPCHECK(hipMallocManaged(&Hmm, N * sizeof(T)));
  . . .
}
```

**Note:** The managed memory capability check may not be necessary; however, if HMM is not supported, managed malloc will fall back to using system memory. Other managed memory API calls will, then, have

Refer to the HIP API documentation for more details on managed memory APIs.

For the application, see [hipMallocManaged.cpp](https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-4.5.x/tests/src/runtimeApi/memory/hipMallocManaged.cpp)

## New Environment Variable

The following new environment variable is added in this release:

| **Environment Variable** | **Value** | **Description** |
| --- | --- | --- |
| **HSA\_COOP\_CU\_COUNT** | 0 or 1 (default is 0) | Some processors support more compute units than can reliably be used in a cooperative dispatch. Setting the environment variable HSA\_COOP\_CU\_COUNT to 1 will cause ROCr to return the correct CU count for cooperative groups through the HSA\_AMD\_AGENT\_INFO\_COOPERATIVE\_COMPUTE\_UNIT\_COUNT attribute of hsa\_agent\_get\_info(). Setting HSA\_COOP\_CU\_COUNT to other values, or leaving it unset, will cause ROCr to return the same CU count for the attributes HSA\_AMD\_AGENT\_INFO\_COOPERATIVE\_COMPUTE\_UNIT\_COUNT and HSA\_AMD\_AGENT\_INFO\_COMPUTE\_UNIT\_COUNT. Future ROCm releases will make HSA\_COOP\_CU\_COUNT=1 the default.
 |

## ROCm Math and Communication Libraries

| **Library** | **Changes** |
| --- | --- |
| **rocBLAS** | **Added** <ul><li>Added rocblas\_get\_version\_string\_size convenience function</li><li>Added rocblas\_xtrmm\_outofplace, an out-of-place version of rocblas\_xtrmm</li><li>Added hpl and trig initialization for gemm\_ex to rocblas-bench</li><li>Added source code gemm. It can be used as an alternative to Tensile for debugging and development</li><li>Added option `ROCM_MATHLIBS_API_USE_HIP_COMPLEX` to opt-in to use hipFloatComplex and hipDoubleComplex</li></ul> **Optimizations** <ul><li>Improved performance of non-batched and batched single-precision GER for size m > 1024. Performance enhanced by 5-10% measured on a MI100 (gfx908) GPU.</li><li>Improved performance of non-batched and batched HER for all sizes and data types. Performance enhanced by 2-17% measured on a MI100 (gfx908) GPU.</li></ul> **Changed** <ul><li>Instantiate templated rocBLAS functions to reduce size of librocblas.so</li><li>Removed static library dependency on msgpack</li><li>Removed boost dependencies for clients</li></ul> **Fixed** <ul><li>Option to install script to build only rocBLAS clients with a pre-built rocBLAS library</li><li>Correctly set output of nrm2\_batched\_ex and nrm2\_strided\_batched\_ex when given bad input</li><li>Fix for dgmm with side == rocblas\_side\_left and a negative incx</li><li>Fixed out-of-bounds read for small trsm</li><li>Fixed numerical checking for tbmv\_strided\_batched</li></ul> |
| | |
| **hipBLAS** | **Added** <ul><li>Added rocSOLVER functions to hipblas-bench</li><li>Added option `ROCM_MATHLIBS_API_USE_HIP_COMPLEX` to opt-in to use hipFloatComplex and hipDoubleComplex</li><li>Added compilation warning for future trmm changes</li><li>Added documentation to hipblas.h</li><li>Added option to forgo pivoting for getrf and getri when ipiv is nullptr</li><li>Added code coverage option</li></ul> **Fixed** <ul><li>Fixed use of incorrect `HIP_PATH` when building from source.</li><li>Fixed windows packaging</li><li>Allowing negative increments in hipblas-bench</li><li>Removed boost dependency</li></ul> |
| | |
| **rocFFT** | **Changed** <ul><li>Enabled runtime compilation of single FFT kernels > length 1024.</li><li>Re-aligned split device library into 4 roughly equal libraries.</li><li>Implemented the FuseShim framework to replace the original OptimizePlan</li><li>Implemented the generic buffer-assignment framework. The buffer assignment is no longer performed by each node. A generic algorithm is designed to test and pick the best assignment path. With the help of FuseShim, more kernel-fusions are achieved.</li><li>Do not read the imaginary part of the DC and Nyquist modes for even-length complex-to-real transforms.</li></ul> **Optimizations** <ul><li>Optimized twiddle-conjugation; complex-to-complex inverse transforms have similar performance to foward transforms now.</li><li>Improved performance of single-kernel small 2D transforms.</li></ul> |
| | |
| **hipFFT** | **Fixed** <ul><li>Fixed incorrect reporting of rocFFT version.</li></ul> **Changed** <ul><li>Unconditionally enabled callback functionality. On the CUDA backend, callbacks only run correctly when hipFFT is built as a static library, and is linked against the static cuFFT library.</li></ul> |
| | |
| **rocSPARSE** | **Added** <ul><li>csrmv, coomv, ellmv, hybmv for (conjugate) transposed matricescsrmv for symmetric matrices</li></ul> **Changed** <ul><li>spmm\_ex is now deprecated and will be removed in the next major release</li></ul> **Improved** <ul><li>Optimization for gtsv</li></ul> |
| | |
| **hipSPARSE** | **Added** <ul><li>Added (conjugate) transpose support for csrmv, hybmv and spmv routines</li></ul> |
| | |
| **rocALUTION** | **Changed** <ul><li>Removed deprecated GlobalPairwiseAMG class, please use PairwiseAMG instead.</li></ul> **Improved** <ul><li>Improved documentation</li></ul> |
| | |
| **rocTHRUST** | **Updates** <ul><li>Updated to match upstream Thrust 1.13.0</li><li>Updated to match upstream Thrust 1.14.0</li><li>Added async scan</li></ul> **Changed** <ul><li>Scan algorithms: inclusive\_scan now uses the input-type as accumulator-type, exclusive\_scan uses initial-value-type. This particularly changes behaviour of small-size input types with large-size output types (e.g. short input, int output). And low-res input with high-res output (e.g. float input, double output)</li></ul> |
| | |
| **rocSOLVER** | **Added** <ul><li>Symmetric matrix factorizations: <ul><li>LASYF</li><li>SYTF2, SYTRF (with batched and strided\_batched versions)</li></ul><li>Added rocsolver\_get\_version\_string\_size to help with version string queries</li><li>Added rocblas\_layer\_mode\_ex and the ability to print kernel calls in the trace and profile logs</li><li>Expanded batched and strided\_batched sample programs.</li></ul> **Optimizations** <ul><li>Improved general performance of LU factorization</li><li>Increased parallelism of specialized kernels when compiling from source, reducing build times on multi-core systems.</li></ul> **Changed** <ul><li>The rocsolver-test client now prints the rocSOLVER version used to run the tests, rather than the version used to build them</li><li>The rocsolver-bench client now prints the rocSOLVER version used in the benchmark</li></ul> **Fixed** <ul><li>Added missing stdint.h include to rocsolver.h</li></ul> |
| | |
| **hipSOLVER** | **Added** <ul><li>Added SYTRF functions: hipsolverSsytrf\_bufferSize, hipsolverDsytrf\_bufferSize, hipsolverCsytrf\_bufferSize, hipsolverZsytrf\_bufferSize, hipsolverSsytrf, hipsolverDsytrf, hipsolverCsytrf, hipsolverZsytrf</li></ul> **Fixed** <ul><li>Fixed use of incorrect `HIP_PATH` when building from source</li></ul> |
| | |
| **RCCL** | **Added** <ul><li>Compatibility with NCCL 2.10.3</li></ul> **Known issues** <ul><li>Managed memory is not currently supported for clique-based kernels</li></ul> |
| | |
| **hipCUB** | **Fixed** <ul><li>Added missing includes to hipcub.hpp</li></ul> **Added** <ul><li>Bfloat16 support to test cases (device\_reduce & device\_radix\_sort)</li><li>Device merge sort</li><li>Block merge sort</li><li>API update to CUB 1.14.0</li></ul> **Changed** <ul><li>The SetupNVCC.cmake automatic target selector select all of the capabalities of all available card for NVIDIA backend.</li></ul> |
| | |
| **rocPRIM** | **Fixed** <ul><li>Enable bfloat16 tests and reduce threshold for bfloat16</li><li>Fix device scan limit\_size feature</li><li>Non-optimized builds no longer trigger local memory limit errors</li></ul> **Added** <ul><li>Scan size limit feature</li><li>Reduce size limit feature</li><li>Transform size limit feature</li><li>Add block\_load\_striped and block\_store\_striped</li><li>Add gather\_to\_blocked to gather values from other threads into a blocked arrangement</li><li>The block sizes for device merge sorts initial block sort and its merge steps are now separate in its kernel config (the block sort step supports multiple items per thread)</li></ul> **Changed** <ul><li>size\_limit for scan, reduce and transform can now be set in the config struct instead of a parameter</li><li>device\_scan and device\_segmented\_scan: inclusive\_scan now uses the input-type as accumulator-type, exclusive\_scan uses initial-value-type. This particularly changes behaviour of small-size input types with large-size output types (e.g. short input, int output) and low-res input with high-res output (e.g. float input, double output)</li><li>Revert old Fiji workaround, because the issue was solved at compiler side</li><li>Update README cmake minimum version number</li><li>Block sort support multiple items per thread. Currently only powers of two block sizes, and items per threads are supported and only for full blocks</li><li>Bumped the minimum required version of CMake to 3.16</li></ul> **Known issues** <ul><li>Unit tests may soft hang on MI200 when running in hipMallocManaged mode.</li><li>device\_segmented\_radix\_sort, device\_scan unit tests failing for HIP on WindowsReduceEmptyInput cause random failure with bfloat16</li><li>Managed memory is not currently supported for clique-based kernels</li></ul> |

## System Management Interface

### Clock Throttling for GPU Events

This feature lists GPU events as they occur in real-time and can be used with _kfdtest_ to produce _vm\_fault_ events for testing.

The command can be called with either &quot; `-e` or `--showevents` like this:

    -e [EVENT [EVENT ...]], --showevents [EVENT [EVENT ...]]  Show event list

Where `EVENT` is any list combination of `VM_FAULT`, `THERMAL_THROTTLE`, or `GPU_RESET` and is NOT case sensitive.

**Note:** If no event arguments are passed, all events will be watched by default.

#### CLI Commands

```
$ rocm-smi --showevents vm_fault thermal_throttle gpu_reset

======================= ROCm System Management Interface =======================
================================= Show Events ==================================
press 'q' or 'ctrl + c' to quit
DEVICE		TIME		TYPE		DESCRIPTION	

============================= End of ROCm SMI Log ==============================
```

(Run kfdtest in another window to test for vm\_fault events.)

**Note:** Unlike other rocm-smi CLI commands, this command does not quit unless specified by the user. Users may press either `q` or `ctrl + c` to quit.

### Display XGMI Bandwidth Between Nodes

The _rsmi\_minmax\_bandwidth\_get_ API reads the HW Topology file and displays bandwidth (min-max) between any two NUMA nodes in a matrix format.

The Command Line Interface (CLI) command can be called as follows:

```
$ rocm-smi --shownodesbw

======================= ROCm System Management Interface =======================
================================== Bandwidth ===================================
GPU0 GPU1 GPU2 GPU3 GPU4 GPU5 GPU6 GPU7
GPU0 N/A 50000-200000 50000-50000 0-0 0-0 0-0 50000-100000 0-0
GPU1 50000-200000 N/A 0-0 50000-50000 0-0 50000-50000 0-0 0-0
GPU2 50000-50000 0-0 N/A 50000-200000 50000-100000 0-0 0-0 0-0
GPU3 0-0 50000-50000 50000-200000 N/A 0-0 0-0 0-0 50000-50000
GPU4 0-0 0-0 50000-100000 0-0 N/A 50000-200000 50000-50000 0-0
GPU5 0-0 50000-50000 0-0 0-0 50000-200000 N/A 0-0 50000-50000
GPU6 50000-100000 0-0 0-0 0-0 50000-50000 0-0 N/A 50000-200000
GPU7 0-0 0-0 0-0 50000-50000 0-0 50000-50000 50000-200000 N/A
Format: min-max; Units: mps
============================= End of ROCm SMI Log ==============================
```

The sample output above shows the maximum theoretical xgmi bandwidth between 2 numa nodes,

**Note:** "0-0" min-max bandwidth indicates devices are not connected directly.

### P2P Connection Status

The _rsmi\_is\_p2p\_accessible_ API returns "True" if P2P can be implemented between two nodes, and returns "False" if P2P cannot be implemented between the two nodes.

The Command Line Interface command can be called as follows:

    rocm-smi --showtopoaccess

Sample Output:

```
$ rocm-smi --showtopoaccess
======================= ROCm System Management Interface =======================
===================== Link accessibility between two GPUs ======================
GPU0 GPU1
GPU0 True True
GPU1 True True
============================= End of ROCm SMI Log ==============================
```

# Breaking Changes

## Runtime Breaking Change

Re-ordering of the enumerated type in hip\_runtime\_api.h to better match NV.  See below for the difference in enumerated types.

ROCm software will be affected if any of the defined enums listed below are used in the code.  Applications built with ROCm v5.0 enumerated types will work with a ROCm 4.5.2 driver. However, an undefined behavior error will occur with a ROCm v4.5.2 application that uses these enumerated types with a ROCm 5.0 runtime.

```c
typedef enum hipDeviceAttribute_t {
  hipDeviceAttributeMaxThreadsPerBlock, // Maximum number of threads per block.
  hipDeviceAttributeMaxBlockDimX, // Maximum x-dimension of a block.
  hipDeviceAttributeMaxBlockDimY, // Maximum y-dimension of a block.
  hipDeviceAttributeMaxBlockDimZ, // Maximum z-dimension of a block.
  hipDeviceAttributeMaxGridDimX, // Maximum x-dimension of a grid.
  hipDeviceAttributeMaxGridDimY, // Maximum y-dimension of a grid.
  hipDeviceAttributeMaxGridDimZ, // Maximum z-dimension of a grid.
  hipDeviceAttributeMaxSharedMemoryPerBlock, // Maximum shared memory available per block in bytes.
  hipDeviceAttributeTotalConstantMemory, // Constant memory size in bytes.
  hipDeviceAttributeWarpSize, // Warp size in threads.
  hipDeviceAttributeMaxRegistersPerBlock, // Maximum number of 32-bit registers available to a
                                          // thread block. This number is shared by all thread
                                          // blocks simultaneously resident on a
                                          // multiprocessor.
  hipDeviceAttributeClockRate, // Peak clock frequency in kilohertz.
  hipDeviceAttributeMemoryClockRate, // Peak memory clock frequency in kilohertz.
  hipDeviceAttributeMemoryBusWidth, // Global memory bus width in bits.
  hipDeviceAttributeMultiprocessorCount, // Number of multiprocessors on the device.
  hipDeviceAttributeComputeMode, // Compute mode that device is currently in.
  hipDeviceAttributeL2CacheSize, // Size of L2 cache in bytes. 0 if the device doesn't have L2
                                 // cache.
  hipDeviceAttributeMaxThreadsPerMultiProcessor, // Maximum resident threads per
                                                 // multiprocessor.
  hipDeviceAttributeComputeCapabilityMajor, // Major compute capability version number.
  hipDeviceAttributeComputeCapabilityMinor, // Minor compute capability version number.
  hipDeviceAttributeConcurrentKernels, // Device can possibly execute multiple kernels
                                       // concurrently.
  hipDeviceAttributePciBusId, // PCI Bus ID.
  hipDeviceAttributePciDeviceId, // PCI Device ID.
  hipDeviceAttributeMaxSharedMemoryPerMultiprocessor, // Maximum Shared Memory Per
                                                      // Multiprocessor.
  hipDeviceAttributeIsMultiGpuBoard, // Multiple GPU devices.
  hipDeviceAttributeIntegrated, // iGPU
  hipDeviceAttributeCooperativeLaunch, // Support cooperative launch
  hipDeviceAttributeCooperativeMultiDeviceLaunch, // Support cooperative launch on multiple devices
  hipDeviceAttributeMaxTexture1DWidth, // Maximum number of elements in 1D images
  hipDeviceAttributeMaxTexture2DWidth, // Maximum dimension width of 2D images in image elements
  hipDeviceAttributeMaxTexture2DHeight, // Maximum dimension height of 2D images in image elements
  hipDeviceAttributeMaxTexture3DWidth, // Maximum dimension width of 3D images in image elements
  hipDeviceAttributeMaxTexture3DHeight, // Maximum dimensions height of 3D images in image elements
  hipDeviceAttributeMaxTexture3DDepth, // Maximum dimensions depth of 3D images in image elements
  hipDeviceAttributeCudaCompatibleBegin = 0,
  hipDeviceAttributeHdpMemFlushCntl, // Address of the HDP\_MEM\_COHERENCY\_FLUSH\_CNTL register
  hipDeviceAttributeHdpRegFlushCntl, // Address of the HDP\_REG\_COHERENCY\_FLUSH\_CNTL register
  hipDeviceAttributeEccEnabled = hipDeviceAttributeCudaCompatibleBegin, // Whether ECC support is enabled.
  hipDeviceAttributeAccessPolicyMaxWindowSize, // Cuda only. The maximum size of the window policy in bytes.
  hipDeviceAttributeAsyncEngineCount, // Cuda only. Asynchronous engines number.
  hipDeviceAttributeCanMapHostMemory, // Whether host memory can be mapped into device address space
  hipDeviceAttributeCanUseHostPointerForRegisteredMem, // Cuda only. Device can access host registered memory
  // at the same virtual address as the CPU
  hipDeviceAttributeClockRate, // Peak clock frequency in kilohertz.
  hipDeviceAttributeComputeMode, // Compute mode that device is currently in.
  hipDeviceAttributeComputePreemptionSupported, // Cuda only. Device supports Compute Preemption.
  hipDeviceAttributeConcurrentKernels, // Device can possibly execute multiple kernels concurrently.
  hipDeviceAttributeConcurrentManagedAccess, // Device can coherently access managed memory concurrently with the CPU
  hipDeviceAttributeCooperativeLaunch, // Support cooperative launch
  hipDeviceAttributeCooperativeMultiDeviceLaunch, // Support cooperative launch on multiple devices
  hipDeviceAttributeDeviceOverlap, // Cuda only. Device can concurrently copy memory and execute a kernel.
                                   // Deprecated. Use instead asyncEngineCount.
  hipDeviceAttributeDirectManagedMemAccessFromHost, // Host can directly access managed memory on
                                                    // the device without migration
  hipDeviceAttributeGlobalL1CacheSupported, // Cuda only. Device supports caching globals in L1
  hipDeviceAttributeHostNativeAtomicSupported, // Cuda only. Link between the device and the host supports native atomic operations
  hipDeviceAttributeIntegrated, // Device is integrated GPU
  hipDeviceAttributeIsMultiGpuBoard, // Multiple GPU devices.
  hipDeviceAttributeKernelExecTimeout, // Run time limit for kernels executed on the device
  hipDeviceAttributeL2CacheSize, // Size of L2 cache in bytes. 0 if the device doesn&#39;t have L2 cache.
  hipDeviceAttributeLocalL1CacheSupported, // caching locals in L1 is supported
  hipDeviceAttributeLuid, // Cuda only. 8-byte locally unique identifier in 8 bytes. Undefined on TCC and non-Windows platforms
  hipDeviceAttributeLuidDeviceNodeMask, // Cuda only. Luid device node mask. Undefined on TCC and non-Windows platforms
  hipDeviceAttributeComputeCapabilityMajor, // Major compute capability version number.
  hipDeviceAttributeManagedMemory, // Device supports allocating managed memory on this system
  hipDeviceAttributeMaxBlocksPerMultiProcessor, // Cuda only. Max block size per multiprocessor
  hipDeviceAttributeMaxBlockDimX, // Max block size in width.
  hipDeviceAttributeMaxBlockDimY, // Max block size in height.
  hipDeviceAttributeMaxBlockDimZ, // Max block size in depth.
  hipDeviceAttributeMaxGridDimX, // Max grid size in width.
  hipDeviceAttributeMaxGridDimY, // Max grid size in height.
  hipDeviceAttributeMaxGridDimZ, // Max grid size in depth.
  hipDeviceAttributeMaxSurface1D, // Maximum size of 1D surface.
  hipDeviceAttributeMaxSurface1DLayered, // Cuda only. Maximum dimensions of 1D layered surface.
  hipDeviceAttributeMaxSurface2D, // Maximum dimension (width, height) of 2D surface.
  hipDeviceAttributeMaxSurface2DLayered, // Cuda only. Maximum dimensions of 2D layered surface.
  hipDeviceAttributeMaxSurface3D, // Maximum dimension (width, height, depth) of 3D surface.
  hipDeviceAttributeMaxSurfaceCubemap, // Cuda only. Maximum dimensions of Cubemap surface.
  hipDeviceAttributeMaxSurfaceCubemapLayered, // Cuda only. Maximum dimension of Cubemap layered surface.
  hipDeviceAttributeMaxTexture1DWidth, // Maximum size of 1D texture.
  hipDeviceAttributeMaxTexture1DLayered, // Cuda only. Maximum dimensions of 1D layered texture.
  hipDeviceAttributeMaxTexture1DLinear, // Maximum number of elements allocatable in a 1D linear texture.
                                        // Use cudaDeviceGetTexture1DLinearMaxWidth() instead on Cuda.
  hipDeviceAttributeMaxTexture1DMipmap, // Cuda only. Maximum size of 1D mipmapped texture.
  hipDeviceAttributeMaxTexture2DWidth, // Maximum dimension width of 2D texture.
  hipDeviceAttributeMaxTexture2DHeight, // Maximum dimension hight of 2D texture.
  hipDeviceAttributeMaxTexture2DGather, // Cuda only. Maximum dimensions of 2D texture if gather operations performed.
  hipDeviceAttributeMaxTexture2DLayered, // Cuda only. Maximum dimensions of 2D layered texture.
  hipDeviceAttributeMaxTexture2DLinear, // Cuda only. Maximum dimensions (width, height, pitch) of 2D textures bound to pitched memory.
  hipDeviceAttributeMaxTexture2DMipmap, // Cuda only. Maximum dimensions of 2D mipmapped texture.
  hipDeviceAttributeMaxTexture3DWidth, // Maximum dimension width of 3D texture.
  hipDeviceAttributeMaxTexture3DHeight, // Maximum dimension height of 3D texture.
  hipDeviceAttributeMaxTexture3DDepth, // Maximum dimension depth of 3D texture.
  hipDeviceAttributeMaxTexture3DAlt, // Cuda only. Maximum dimensions of alternate 3D texture.
  hipDeviceAttributeMaxTextureCubemap, // Cuda only. Maximum dimensions of Cubemap texture
  hipDeviceAttributeMaxTextureCubemapLayered, // Cuda only. Maximum dimensions of Cubemap layered texture.
  hipDeviceAttributeMaxThreadsDim, // Maximum dimension of a block
  hipDeviceAttributeMaxThreadsPerBlock, // Maximum number of threads per block.
  hipDeviceAttributeMaxThreadsPerMultiProcessor, // Maximum resident threads per multiprocessor.
  hipDeviceAttributeMaxPitch, // Maximum pitch in bytes allowed by memory copies
  hipDeviceAttributeMemoryBusWidth, // Global memory bus width in bits.
  hipDeviceAttributeMemoryClockRate, // Peak memory clock frequency in kilohertz.
  hipDeviceAttributeComputeCapabilityMinor, // Minor compute capability version number.
  hipDeviceAttributeMultiGpuBoardGroupID, // Cuda only. Unique ID of device group on the same multi-GPU board
  hipDeviceAttributeMultiprocessorCount, // Number of multiprocessors on the device.
  hipDeviceAttributeName, // Device name.
  hipDeviceAttributePageableMemoryAccess, // Device supports coherently accessing pageable memory
                                          // without calling hipHostRegister on it
  hipDeviceAttributePageableMemoryAccessUsesHostPageTables, // Device accesses pageable memory via the host&#39;s page tables
  hipDeviceAttributePciBusId, // PCI Bus ID.
  hipDeviceAttributePciDeviceId, // PCI Device ID.
  hipDeviceAttributePciDomainID, // PCI Domain ID.
  hipDeviceAttributePersistingL2CacheMaxSize, // Cuda11 only. Maximum l2 persisting lines capacity in bytes
  hipDeviceAttributeMaxRegistersPerBlock, // 32-bit registers available to a thread block. This number is shared
                                          // by all thread blocks simultaneously resident on a multiprocessor.
  hipDeviceAttributeMaxRegistersPerMultiprocessor, // 32-bit registers available per block.
  hipDeviceAttributeReservedSharedMemPerBlock, // Cuda11 only. Shared memory reserved by CUDA driver per block.
  hipDeviceAttributeMaxSharedMemoryPerBlock, // Maximum shared memory available per block in bytes.
  hipDeviceAttributeSharedMemPerBlockOptin, // Cuda only. Maximum shared memory per block usable by special opt in.
  hipDeviceAttributeSharedMemPerMultiprocessor, // Cuda only. Shared memory available per multiprocessor.
  hipDeviceAttributeSingleToDoublePrecisionPerfRatio, // Cuda only. Performance ratio of single precision to double precision.
  hipDeviceAttributeStreamPrioritiesSupported, // Cuda only. Whether to support stream priorities.
  hipDeviceAttributeSurfaceAlignment, // Cuda only. Alignment requirement for surfaces
  hipDeviceAttributeTccDriver, // Cuda only. Whether device is a Tesla device using TCC driver
  hipDeviceAttributeTextureAlignment, // Alignment requirement for textures
  hipDeviceAttributeTexturePitchAlignment, // Pitch alignment requirement for 2D texture references bound to pitched memory;
  hipDeviceAttributeTotalConstantMemory, // Constant memory size in bytes.
  hipDeviceAttributeTotalGlobalMem, // Global memory available on devicice.
  hipDeviceAttributeUnifiedAddressing, // Cuda only. An unified address space shared with the host.
  hipDeviceAttributeUuid, // Cuda only. Unique ID in 16 byte.
  hipDeviceAttributeWarpSize, // Warp size in threads.
  hipDeviceAttributeMaxPitch, // Maximum pitch in bytes allowed by memory copies
  hipDeviceAttributeTextureAlignment, //Alignment requirement for textures
  hipDeviceAttributeTexturePitchAlignment, //Pitch alignment requirement for 2D texture references bound to pitched memory;
  hipDeviceAttributeKernelExecTimeout, //Run time limit for kernels executed on the device
  hipDeviceAttributeCanMapHostMemory, //Device can map host memory into device address space
  hipDeviceAttributeEccEnabled, //Device has ECC support enabled
  hipDeviceAttributeCudaCompatibleEnd = 9999,
  hipDeviceAttributeAmdSpecificBegin = 10000,
  hipDeviceAttributeCooperativeMultiDeviceUnmatchedFunc, // Supports cooperative launch on multiple
                                                         // devices with unmatched functions
  hipDeviceAttributeCooperativeMultiDeviceUnmatchedGridDim, // Supports cooperative launch on multiple
                                                            // devices with unmatched grid dimensions
  hipDeviceAttributeCooperativeMultiDeviceUnmatchedBlockDim, // Supports cooperative launch on multiple
                                                             // devices with unmatched block dimensions
  hipDeviceAttributeCooperativeMultiDeviceUnmatchedSharedMem, // Supports cooperative launch on multiple
                                                              // devices with unmatched shared memories
  hipDeviceAttributeAsicRevision, // Revision of the GPU in this device
  hipDeviceAttributeManagedMemory, // Device supports allocating managed memory on this system
  hipDeviceAttributeDirectManagedMemAccessFromHost, // Host can directly access managed memory on
                                                    //  the device without migration
  hipDeviceAttributeConcurrentManagedAccess, // Device can coherently access managed memory
                                             // concurrently with the CPU
  hipDeviceAttributePageableMemoryAccess, // Device supports coherently accessing pageable memory
                                          // without calling hipHostRegister on it
  hipDeviceAttributePageableMemoryAccessUsesHostPageTables, // Device accesses pageable memory via
                                                            // the host's page tables
  hipDeviceAttributeCanUseStreamWaitValue // '1' if Device supports hipStreamWaitValue32() and
                                          // hipStreamWaitValue64(), '0' otherwise.
  hipDeviceAttributeClockInstructionRate = hipDeviceAttributeAmdSpecificBegin, // Frequency in khz of the timer used by the device-side "clock"
  hipDeviceAttributeArch, // Device architecture
  hipDeviceAttributeMaxSharedMemoryPerMultiprocessor, // Maximum Shared Memory PerMultiprocessor.
  hipDeviceAttributeGcnArch, // Device gcn architecture
  hipDeviceAttributeGcnArchName, // Device gcnArch name in 256 bytes
  hipDeviceAttributeHdpMemFlushCntl, // Address of the HDP_MEM_COHERENCY_FLUSH_CNTL register
  hipDeviceAttributeHdpRegFlushCntl, // Address of the HDP_REG_COHERENCY_FLUSH_CNTL register
  hipDeviceAttributeCooperativeMultiDeviceUnmatchedFunc, // Supports cooperative launch on multiple
                                                         // devices with unmatched functions
  hipDeviceAttributeCooperativeMultiDeviceUnmatchedGridDim, // Supports cooperative launch on multiple
                                                            // devices with unmatched grid dimensions
  hipDeviceAttributeCooperativeMultiDeviceUnmatchedBlockDim, // Supports cooperative launch on multiple
                                                             // devices with unmatched block dimensions
  hipDeviceAttributeCooperativeMultiDeviceUnmatchedSharedMem, // Supports cooperative launch on multiple
                                                              // devices with unmatched shared memories
  hipDeviceAttributeIsLargeBar, // Whether it is LargeBar
  hipDeviceAttributeAsicRevision, // Revision of the GPU in this device
  hipDeviceAttributeCanUseStreamWaitValue, // '1' if Device supports hipStreamWaitValue32() and
                                           // hipStreamWaitValue64() , '0' otherwise.
  hipDeviceAttributeAmdSpecificEnd = 19999,
  hipDeviceAttributeVendorSpecificBegin = 20000,   // Extended attributes for vendors
} hipDeviceAttribute_t;
```

# Known Issues in This Release

## Incorrect dGPU Behavior When Using AMDVBFlash Tool

The AMDVBFlash tool, used for flashing the VBIOS image to dGPU, does not communicate with the ROM Controller specifically when the driver is present. This is because the driver, as part of its runtime power management feature, puts the dGPU to a sleep state.

As a workaround, users can run `amdgpu.runpm=0`, which temporarily disables the runtime power management feature from the driver and dynamically changes some power control-related sysfs files.

## Issue with START Timestamp in ROCProfiler

Users may encounter an issue with the enabled timestamp functionality for monitoring one or multiple counters. ROCProfiler outputs the following four timestamps for each kernel:

- Dispatch
- Start
- End
- Complete

**Issue**

This defect is related to the Start timestamp functionality, which incorrectly shows an earlier time than the Dispatch timestamp.

To reproduce the issue,

1. Enable timing using the `--timestamp on` flag.
2. Use the `-i` option with the input filename that contains the name of the counter(s) to monitor.
3. Run the program.
4. Check the output result file.

**Current behavior**

BeginNS is lower than DispatchNS, which is incorrect.

**Expected behavior**

The correct order is:

_Dispatch < Start < End < Complete_

Users cannot use ROCProfiler to measure the time spent on each kernel because of the incorrect timestamp with counter collection enabled.

**Recommended Workaround**

Users are recommended to collect kernel execution timestamps without monitoring counters, as follows:

1. Enable timing using the `--timestamp on` flag, and run the application.
2. Rerun the application using the `-i` option with the input filename that contains the name of the counter(s) to monitor, and save this to a different output file using the `-o` flag.
3. Check the output result file from step 1.
4. The order of timestamps correctly displays as:

_DispathNS < BeginNS < EndNS < CompleteNS_

1. Users can find the values of the collected counters in the output file generated in step 2.

## Radeon Pro V620 and W6800 Workstation GPUs

### No Support for SMI and ROCDebugger on SRIOV

System Management Interface (SMI) and ROCDebugger are not supported in the SRIOV environment on any GPU. For more information, refer to the Systems Management Interface documentation.

# Deprecations and Warnings in This Release

## ROCm Libraries Changes – Deprecations and Deprecation Removal

- The hipfft.h header is now provided only by the hipfft package.  Up to ROCm 5.0, users would get hipfft.h in the rocfft package too.
- The GlobalPairwiseAMG class is now entirely removed, users should use the PairwiseAMG class instead.
- The rocsparse\_spmm signature in 5.0 was changed to match that of rocsparse\_spmm\_ex.  In 5.0, rocsparse\_spmm\_ex is still present, but deprecated.  Signature diff for rocsparse\_spmm

### _rocsparse\_spmm_ in 5.0

```c
rocsparse_status rocsparse_spmm(rocsparse_handle            handle,
                                rocsparse_operation         trans_A,
                                rocsparse_operation         trans_B,
                                const void*                 alpha,
                                const rocsparse_spmat_descr mat_A,
                                const rocsparse_dnmat_descr mat_B,
                                const void*                 beta,
                                const rocsparse_dnmat_descr mat_C,
                                rocsparse_datatype          compute_type,
                                rocsparse_spmm_alg          alg,
                                rocsparse_spmm_stage        stage,
                                size_t*                     buffer_size,
                                void*                       temp_buffer);
```

### _rocsparse\_spmm_ in 4.0

```c
rocsparse_status rocsparse_spmm(rocsparse_handle            handle,
                                rocsparse_operation         trans_A,
                                rocsparse_operation         trans_B,
                                const void*                 alpha,
                                const rocsparse_spmat_descr mat_A,
                                const rocsparse_dnmat_descr mat_B,
                                const void*                 beta,
                                const rocsparse_dnmat_descr mat_C,
                                rocsparse_datatype          compute_type,
                                rocsparse_spmm_alg          alg,
                                size_t*                     buffer_size,
                                void*                       temp_buffer);
```

## HIP API Deprecations and Warnings

### Warning - Arithmetic Operators of HIP Complex and Vector Types

In this release, arithmetic operators of HIP complex and vector types are deprecated.

- As alternatives to arithmetic operators of HIP complex types, users can use arithmetic operators of std::complex types.
- As alternatives to arithmetic operators of HIP vector types, users can use the operators of the native clang vector type associated with the data member of HIP vector types.

During the deprecation, two macros `__HIP_ENABLE_COMPLEX_OPERATORS` and `__HIP_ENABLE_VECTOR_OPERATORS` are provided to allow users to conditionally enable arithmetic operators of HIP complex or vector types.

Note, the two macros are mutually exclusive and, by default, set to off.

The arithmetic operators of HIP complex and vector types will be removed in a future release.

Refer to the HIP API Guide for more information.

### Refactor of HIPCC/HIPCONFIG

In prior ROCm releases, by default, the hipcc/hipconfig Perl scripts were used to identify and set target compiler options, target platform, compiler, and runtime appropriately.

In ROCm v5.0, hipcc.bin and hipconfig.bin have been added as the compiled binary implementations of the hipcc and hipconfig. These new binaries are currently a work-in-progress, considered, and marked as experimental. ROCm plans to fully transition to hipcc.bin and hipconfig.bin in the a future ROCm release. The existing hipcc and hipconfig Perl scripts are renamed to hipcc.pl and hipconfig.pl respectively. New top-level hipcc and hipconfig Perl scripts are created, which can switch between the Perl script or the compiled binary based on the environment variable `HIPCC_USE_PERL_SCRIPT`.

In ROCm 5.0, by default, this environment variable is set to use hipcc and hipconfig through the Perl scripts.

Subsequently, Perl scripts will no longer be available in ROCm in a future release.

## Warning - Compiler-Generated Code Object Version 4 Deprecation

Support for loading compiler-generated code object version 4 will be deprecated in a future release with no release announcement and replaced with code object 5 as the default version.

The current default is code object version 4.

## Warning - MIOpenTensile Deprecation

MIOpenTensile will be deprecated in a future release.


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

    kfd: skipped device 1002:7300, PCI rejects atomics

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
