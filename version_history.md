## ROCm Version History
This file contains archived version history information for the [ROCm project](https://github.com/RadeonOpenCompute/ROCm)

### Current ROCm Version: 2.2
- [New features and enhancements in ROCm 2.2](#new-features-and-enhancements-in-rocm-22)
- [New features and enhancements in ROCm 2.1](#new-features-and-enhancements-in-rocm-21)
- [New features and enhancements in ROCm 2.0](#new-features-and-enhancements-in-rocm-20)
- [New features and enhancements in ROCm 1.9.2](#new-features-and-enhancements-in-rocm-192)
- [New features and enhancements in ROCm 1.9.2](#new-features-and-enhancements-in-rocm-192-1)
- [New features and enhancements in ROCm 1.9.1](#new-features-and-enhancements-in-rocm-191)
- [New features and enhancements in ROCm 1.9.0](#new-features-and-enhancements-in-rocm-190)
- [New features as of ROCm 1.8.3](#new-features-as-of-rocm-183)
- [New features as of ROCm 1.8](#new-features-as-of-rocm-18)
- [New Features as of ROCm 1.7](#new-features-as-of-rocm-17)
- [New Features as of ROCm 1.5](#new-features-as-of-rocm-15)

### New features and enhancements in ROCm 2.2

#### rocSparse Optimization on Vega20
Cache usage optimizations for csrsv (sparse triangular solve), coomv
(SpMV in COO format) and ellmv (SpMV in ELL format) are available.

#### DGEMM and DTRSM Optimization
Improved DGEMM performance for reduced matrix sizes (k=384, k=256)

#### Caffe2
Added support for multi-GPU training

### New features and enhancements in ROCm 2.1

#### RocTracer v1.0 preview release – 'rocprof' HSA runtime tracing and statistics support -
Supports HSA API tracing and HSA asynchronous GPU activity including kernels execution and memory copy
     
#### Improvements to ROCM-SMI tool -
Added support to show real-time PCIe bandwidth usage via the -b/--showbw flag
       
#### DGEMM Optimizations -
Improved DGEMM performance for large square and reduced matrix sizes (k=384, k=256)

### New features and enhancements in ROCm 2.0

#### Adds support for RHEL 7.6 / CentOS 7.6 and Ubuntu 18.04.1

#### Adds support for Vega 7nm, Polaris 12 GPUs

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

The tool can be installed from the `rocprofiler-dev` package. It will be installed into: `/opt/rocm/bin/rpl_run.sh`

#### Preview for rocr Debug Agent rocr_debug_agent
The ROCr Debug Agent is a library that can be loaded by ROCm Platform Runtime to provide the following functionality:
* Print the state for wavefronts that report memory violation or upon executing a "s_trap 2" instruction.
* Allows SIGINT (`ctrl c`) or SIGTERM (`kill -15`) to print wavefront state of aborted GPU dispatches.
* It is enabled on Vega10 GPUs on ROCm1.9.

The ROCm1.9 release will install the ROCr Debug Agent library at `/opt/rocm/lib/librocr_debug_agent64.so`


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

To try ROCm with an upstream kernel, install ROCm as normal, but do not install the rock-dkms package. Also add a udev rule to control `/dev/kfd` permissions:

```
    echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules
```

### New features as of ROCm 1.8.3

* ROCm 1.8.3 is a minor update meant to fix compatibility issues on Ubuntu releases running kernel 4.15.0-33

### New features as of ROCm 1.8

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

### New Features as of ROCm 1.7

#### DKMS driver installation

 * New driver installation uses Dynamic Kernel Module Support (DKMS)
 * Only amdkfd and amdgpu kernel modules are installed to support AMD hardware
 * Currently only Debian packages are provided for DKMS (no Fedora suport available)
 * See the [ROCT-Thunk-Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/roc-1.7.x) and [ROCK-Kernel-Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/roc-1.7.x) for additional documentation on driver setup

### New Features as of ROCm 1.5

#### Developer preview of the new OpenCL 1.2 compatible language runtime and compiler

 * OpenCL 2.0 compatible kernel language support with OpenCL 1.2 compatible
   runtime 
 * Supports offline ahead of time compilation today;
   during the Beta phase we will add in-process/in-memory compilation. 

#### Binary Package support for Ubuntu 16.04

#### Binary Package support for Fedora 24 is not currently available

#### Dropping binary package support for Ubuntu 14.04, Fedora 23
 
#### IPC support 

