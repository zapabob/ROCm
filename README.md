# AMD ROCm Release Notes v2.10
This document describes the features, fixed issues, and information about downloading and installing the ROCm software.
It also covers known issues and deprecated features in the ROCm v2.10 release.

## What Is ROCm?
ROCm is designed to be a universal platform for gpu-accelerated computing. This modular design allows hardware vendors to build drivers that support the ROCm framework. ROCm is also designed to integrate multiple programming languages and makes it easy to add support for other languages. 

ROCm is built from open source software. Subject to the applicable license, you can download the source code, modify and rebuild the ROCm components. To ensure you are downloading the correct source code versions, the ROCm repository provides a repo manifest file called default.xml. 

Note: You can also clone the source code for individual ROCm components from the GitHub repositories.

### ROCm Components
The following components for the ROCm platform are released and available for the v2.10 release:
•	Drivers
•	Tools
•	Libraries
•	Source Code

You can access the latest supported version of drivers, tools, libraries, and source code for the ROCm platform at the following location:
https://github.com/RadeonOpenCompute/ROCm

### Supported Operating Systems
The ROCm v2.10.x platform is designed to support the following operating systems:
•	SLES 15 SP1 
•	Ubuntu 16.04.6(Kernel 4.15) and 18.04.3(Kernel 5.0)
•	CentOS 7.6 (Using devtoolset-7 runtime support)
•	RHEL 7.6 (Using devtoolset-7 runtime support)

For details about deploying the ROCm v2.10.x on these operating systems, see the Deploying ROCm section later in the document.

### Important ROCm Links
Access the following links for more information on:
•	ROCm documentation, see 
https://rocm-documentation.readthedocs.io/en/latest/index.html

•	ROCm binary structure, see
https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md#rocm-binary-package-structure

•	Common ROCm installation issues, see
https://rocm.github.io/install_issues.html

•	Instructions to install PyTorch after ROCm is installed – https://rocm-documentation.readthedocs.io/en/latest/Deep_learning/Deep-learning.html#pytorch

Note: These instructions reference the rocm/pytorch:rocm2.9_ubuntu16.04_py2.7_pytorch image. However, you can substitute the Ubuntu 18.04 image listed at https://hub.docker.com/r/rocm/pytorch/tags

## What’s New in Version 2.10
### rocBLAS - Support for Complex GEMM in AMD Radeon Pro Vega 20 
The rocBLAS library is a gpu-accelerated implementation of the standard Basic Linear Algebra Subroutines (BLAS). rocBLAS is designed to enable you to develop algorithms, including high performance computing, image analysis, and machine learning.
In the AMD ROCm release v2.10, support is extended to the General Matrix Multiply (GEMM) routine for multiple small matrices processed simultaneously for rocBLAS in AMD Radeon Pro Vega 20.  Both single and double precision, CGEMM and ZGEMM, are now supported in rocBLAS.

### Support for SLES 15 SP1
In the AMD ROCm v2.10 release, support is added for SUSE Linux® Enterprise Server (SLES) 15 SP1. SLES is a modular operating system for both multimodal and traditional IT.
Note: The SUSE Linux® Enterprise Server is a licensed platform. Ensure you have registered and have a license key prior to installation. Use the following SUSE command line to apply your license:
SUSEConnect -r < Key>

#### SLES 15 SP1 
The following section tells you how to perform an install and uninstall ROCm on SLES 15 SP 1. 
Run the following commands once for a fresh install on the operating system:
sudo usermod -a -G video  $LOGNAME
sudo usermod  -a -G sudo $LOGNAME
sudo reboot


### Code Marker Support for rocProfiler and rocTracer Libraries
Code markers provide the external correlation ID for the calling thread. This function indicates that the calling thread is entering and leaving an external API region.
•	The rocProfiler library enables you to profile performance counters and derived metrics. This library supports GFX8/GFX9 and provides a hardware-specific low-level performance analysis interface for profiling of GPU compute applications. The profiling includes hardware performance counters with complex performance metrics.

•	The rocTracer library provides a specific runtime profiler to trace API and asynchronous activity. The API provides functionality for registering the runtimes API callbacks and the asynchronous activity records pool support.

•	rocTX provides a C API for code markup for performance profiling and supports annotation of code ranges and ASCII markers.


## Fixed Issues
Fixed Issues in the v2.10 Release
### Running TensorFlow and PyTorch Frameworks Consecutively Results in the Memory Access Fault error 
Issue: Running the TensorFlow and PyTorch frameworks in quick succession results in a Memory Access Fault error.

Resolution: This issue is resolved, and the error no longer appears.

### Issue with the Docker Container Environment Variable Setting
Issue: Applications fail when the docker container is launched on the NUMA system without the ‘security-opt seccomp=unconfined’ setting.

Resolution: Configure the “–security-opt seccomp=unconfined” variable setting to avoid this issue.



## Machine Learning and High Performance Computing Software Stack for AMD GPU

ROCm Version 2.10

### ROCm Binary Package Structure

  * [ROCm Binary Package Structure](#rocm-binary-package-structure)


### ROCm Platform - Links to Drivers, Tools, Libraries and Source Code 

The latest supported version of the drivers, tools, libraries and source code for the ROCm platform have been released and are available from the following GitHub repositories:

 #### ROCm Core Components
  - [ROCk Kernel Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/roc-2.9.0)
  - [ROCr Runtime](https://github.com/RadeonOpenCompute/ROCR-Runtime/tree/roc-2.9.0)
  - [ROCt Thunk Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/roc-2.9.0)  

  
#### ROCm Support Software
  - [ROCm SMI](https://github.com/RadeonOpenCompute/ROC-smi/tree/roc-2.9.0)
  - [ROCm cmake](https://github.com/RadeonOpenCompute/rocm-cmake/tree/roc-2.9.0)
  - [rocminfo](https://github.com/RadeonOpenCompute/rocminfo/tree/roc-2.9.0)
  - [ROCm Bandwidth Test](https://github.com/RadeonOpenCompute/rocm_bandwidth_test/tree/roc-2.9.0)
  
#### ROCm Development Tools
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
    
#### ROCm Libraries
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
