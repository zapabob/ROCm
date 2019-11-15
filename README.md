
### ROCm - Machine Learning and High Performance Computing Software Stack for AMD GPU

### ROCm Version: Version 2.10

  * [ROCm Binary Package Structure](#rocm-binary-package-structure)


### Links to Drivers, Tools, Libraries and Source Code for the ROCm Platform

The latest supported version of the drivers, tools, libraries and source code for the ROCm platform have been released and are available from the following GitHub repositories:

* ROCm Core Components
  - [ROCk Kernel Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/roc-2.9.0)
  - [ROCr Runtime](https://github.com/RadeonOpenCompute/ROCR-Runtime/tree/roc-2.9.0)
  - [ROCt Thunk Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/roc-2.9.0)
* ROCm Support Software
  - [ROCm SMI](https://github.com/RadeonOpenCompute/ROC-smi/tree/roc-2.9.0)
  - [ROCm cmake](https://github.com/RadeonOpenCompute/rocm-cmake/tree/roc-2.9.0)
  - [rocminfo](https://github.com/RadeonOpenCompute/rocminfo/tree/roc-2.9.0)
  - [ROCm Bandwidth Test](https://github.com/RadeonOpenCompute/rocm_bandwidth_test/tree/roc-2.9.0)
* ROCm Development Tools
  - [HCC compiler](https://github.com/RadeonOpenCompute/hcc/tree/roc-hcc-2.9.0)
  - [HIP](https://github.com/ROCm-Developer-Tools/HIP/tree/roc-2.9.0)
  - [ROCm Device Libraries](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/tree/roc-hcc-2.9.0)
  - ROCm OpenCL, which is created from the following components:
    - [ROCm OpenCL Runtime](http://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/tree/roc-2.9.0)
    - [ROCm OpenCL Driver](http://github.com/RadeonOpenCompute/ROCm-OpenCL-Driver/tree/roc-2.9.0)
  - The ROCm OpenCL compiler, which is created from the following components:
      - [ROCm LLVM OCL](http://github.com/RadeonOpenCompute/llvm/tree/roc-ocl-2.9.0)
      - [ROCm LLVM HCC](http://github.com/RadeonOpenCompute/llvm/tree/roc-hcc-2.9.0)
      - [ROCm Clang](http://github.com/RadeonOpenCompute/clang/tree/roc-2.9.0)
      - [ROCm lld OCL](http://github.com/RadeonOpenCompute/lld/tree/roc-ocl-2.9.0)
      - [ROCm lld HCC](http://github.com/RadeonOpenCompute/lld/tree/roc-hcc-2.9.0)
      - [ROCm Device Libraries](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/tree/roc-2.9.x)
  - [ROCM Clang-OCL Kernel Compiler](https://github.com/RadeonOpenCompute/clang-ocl/tree/roc-2.9.0)
  - [Asynchronous Task and Memory Interface (ATMI)](https://github.com/RadeonOpenCompute/atmi/tree/rocm_2.9.0)
  - [ROCr Debug Agent](https://github.com/ROCm-Developer-Tools/rocr_debug_agent/tree/roc-2.9.0)
  - [ROCm Code Object Manager](https://github.com/RadeonOpenCompute/ROCm-CompilerSupport/tree/roc-2.9.0)
  - [ROC Profiler](https://github.com/ROCm-Developer-Tools/rocprofiler/tree/roc-2.9.0)
  - [ROC Tracer](https://github.com/ROCm-Developer-Tools/roctracer/tree/roc-2.9.x)
  - [Radeon Compute Profiler](https://github.com/GPUOpen-Tools/RCP/tree/3a49405)
  - Example Applications:
    - [HCC Examples](https://github.com/ROCm-Developer-Tools/HCC-Example-Application/tree/ffd65333)
    - [HIP Examples](https://github.com/ROCm-Developer-Tools/HIP-Examples/tree/roc-2.9.0)
* ROCm Libraries
  - [rocBLAS](https://github.com/ROCmSoftwarePlatform/rocBLAS/tree/rocm-2.9)
  - [hipBLAS](https://github.com/ROCmSoftwarePlatform/hipBLAS/tree/rocm-2.9)
  - [rocFFT](https://github.com/ROCmSoftwarePlatform/rocFFT/tree/rocm-2.9)
  - [rocRAND](https://github.com/ROCmSoftwarePlatform/rocRAND/tree/2.9.0)
  - [rocSPARSE](https://github.com/ROCmSoftwarePlatform/rocSPARSE/tree/rocm-2.9)
  - [hipSPARSE](https://github.com/ROCmSoftwarePlatform/hipSPARSE/tree/rocm-2.9)
  - [rocALUTION](https://github.com/ROCmSoftwarePlatform/rocALUTION/tree/rocm-2.9)
  - [MIOpenGEMM](https://github.com/ROCmSoftwarePlatform/MIOpenGEMM/tree/6275a879)
  - [MIOpen](https://github.com/ROCmSoftwarePlatform/MIOpen/tree/roc-2.9.0)
  - [rocThrust](https://github.com/ROCmSoftwarePlatform/rocThrust/tree/2.9.0)
  - [ROCm SMI Lib](https://github.com/RadeonOpenCompute/rocm_smi_lib/tree/roc-2.9.0)
  - [RCCL](https://github.com/ROCmSoftwarePlatform/rccl/tree/2.9.0)
  - [MIVisionX](https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/tree/1.3.0)
  - [hipCUB](https://github.com/ROCmSoftwarePlatform/hipCUB/tree/2.9.0)



#### ROCm Binary Package Structure

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
       |--hsa-rocr-dev
       |--hsa-ext-rocr-dev
       |--hsakmt-roct
       |--hsakmt-roct-dev
       |--rocm-cmake
       |--rocm-device-libs
       |--hcc
       |--hip_base
       |--hip_doc
       |--hip_hcc
       |--hip_samples
       |--rocm-smi
       |--hsa-amd-aqlprofile
       |--comgr
       |--rocr_debug_agent
       \--rocm-utils
          |--rocminfo
          \--rocm-clang-ocl # This will cause OpenCL to be installed

  rocm-libs
    |--rocalution
    |--hipblas
    |--rocblas
    |--rocfft
    |--rocrand
    |--hipsparse
    \--rocsparse
```

These meta-packages are not required but may be useful to make it easier to install ROCm on most systems.

Note:Some users may want to skip certain packages. For instance, a user that wants to use the upstream kernel drivers (rather than those supplied by AMD) may want to skip the `rocm-dkms` and `rock-dkms` packages, and instead directly install `rocm-dev`.

Similarly, a user that only wants to install OpenCL support instead of HCC and HIP may want to skip the `rocm-dkms` and `rocm-dev` packages. Instead, they could directly install `rock-dkms`, `rocm-opencl`, and `rocm-opencl-dev` and their dependencies.

Features and enhancements introduced in previous versions of ROCm can be found in [version_history.md](version_history.md)
