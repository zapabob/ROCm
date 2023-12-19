# Release notes for AMD ROCm™ 6.0

ROCm 6.0 is a major release with new performance optimizations, expanded frameworks and library
support, and improved developer experience. This includes initial enablement of the AMD Instinct™
MI300 series. Future releases will further enable and optimize this new platform. Key features include:

* Improved performance in areas like lower precision math and attention layers.
* New hipSPARSELt library accelerates AI workloads via AMD's sparse matrix core technique.
* Upstream support is now available for popular AI frameworks like TensorFlow, JAX, and PyTorch.
* New support for libraries, such as DeepSpeed, ONNX-RT, and CuPy.
* Prepackaged HPC and AI containers on AMD Infinity Hub, with improved documentation and
  tutorials on the [AMD ROCm Docs](https://rocm.docs.amd.com) site.
* Consolidated developer resources and training on the new
  [AMD ROCm Developer Hub](https://www.amd.com/en/developer/resources/rocm-hub.html).

The following section provide a release overview for ROCm 6.0. For additional details, you can refer to
the [Changelog](https://rocm.docs.amd.com/en/develop/about/CHANGELOG.html). We list known
issues on [GitHub](https://github.com/ROCm/ROCm/issues).

## OS and GPU support changes

ROCm 6.0 enables the use of MI300A and MI300X Accelerators with a limited operating systems
support. Future releases will add additional OS's to match our general offering.

| Operating Systems | MI300A | MI300X |
|:---:|:---:|:---:|
| Ubuntu 22.04.3 | Supported | Supported |
| RHEL 8.9 | Supported |  |
| SLES15 SP5 | Supported |  |

For older generations of supported Instinct products we've added the following operating systems:

* RHEL 9.3
* RHEL 8.9

Note: For ROCm 6.2 and beyond, we've planned for end-of-support (EoS) for the following operating
systems:

* Ubuntu 20.04.5
* SLES 15 SP4
* RHEL/CentOS 7.9

## New ROCm meta package

We've added a new ROCm meta package for easy installation of all ROCm core packages, tools, and
libraries. For example, the following command will install the full ROCm package: `apt-get install rocm`
(Ubuntu), or `yum install rocm` (RHEL).

## Filesystem Hierarchy Standard

ROCm 6.0 fully adopts the Filesystem Hierarchy Standard (FHS) reorganization goals. We've removed
the backward compatibility support for old file locations.

## Compiler location change

* The installation path of LLVM has been changed from `/opt/rocm-<rel>/llvm` to
  `/opt/rocm-<rel>/lib/llvm`. For backward compatibility, a symbolic link is provided to the old
  location and will be removed in a future release.
* The installation path of the device library bitcode has changed from `/opt/rocm-<rel>/amdgcn` to
  `/opt/rocm-<rel>/lib/llvm/lib/clang/<ver>/lib/amdgcn`. For backward compatibility, a symbolic link
  is provided and will be removed in a future release.

## Documentation

CMake support has been added for documentation in the
[ROCm repository](https://github.com/RadeonOpenCompute/ROCm).

## AMD Instinct™ MI50 end-of-support notice

AMD Instinct MI50, Radeon Pro VII, and Radeon VII products (collectively gfx906 GPUs) enters
maintenance mode in ROCm 6.0.

As outlined in [5.6.0](https://rocm.docs.amd.com/en/docs-5.6.0/release.html), ROCm 5.7 was the
final release for gfx906 GPUs in a fully supported state.

  * Henceforth, no new features and performance optimizations will be supported for the gfx906 GPUs.
  * Bug fixes and critical security patches will continue to be supported for the gfx906 GPUs until Q2
    2024 (end of maintenance \[EOM] will be aligned with the closest ROCm release).
  * Bug fixes will be made up to the next ROCm point release.
  * Bug fixes will not be backported to older ROCm releases for gfx906.
  * Distribution and operating system updates will continue per the ROCm release cadence for gfx906
    GPUs until EOM.

## ROCm projects

The following sections contains project-specific release notes for ROCm 6.0. For additional details, you
can refer to the [Changelog](https://rocm.docs.amd.com/en/develop/about/CHANGELOG.html).

### AMD SMI

* **Integrated the E-SMI (EPYC-SMI) library**.
    You can now query CPU-related information directly through AMD SMI. Metrics include power,
    energy, performance, and other system details.

* **Added support for gfx942 metrics**.
    You can now query MI300 device metrics to get real-time information. Metrics include power,
    temperature, energy, and performance.

### HIP

* **New features to improve resource interoperability**.
  * For external resource interoperability, we've added new structs and enums.
  * We've added new members to HIP struct `hipDeviceProp_t` for surfaces, textures, and device
    identifiers.

* **Changes impacting backward compatibility**.
    There are several changes impacting backward compatibility: we changed some struct members and
    some enum values, and removed some deprecated flags. For additional information, please refer to
    the Changelog.

### hipCUB

* **Additional CUB API support**.
    The hipCUB backend is updated to CUB and Thrust 2.1.

### HIPIFY

* **Enhanced CUDA2HIP document generation**.
    API versions are now listed in the CUDA2HIP documentation. To see if the application binary
    interface (ABI) has changed, refer to the
    [*C* column](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/tables/CUDA_Runtime_API_functions_supported_by_HIP.html)
    in our API documentation.

* **Hipified rocSPARSE**.
    We've implemented support for the direct hipification of additional cuSPARSE APIs into rocSPARSE
    APIs under the `--roc` option. This covers a major milestone in the roadmap towards complete
    cuSPARSE-to-rocSPARSE hipification.

### hipRAND

* **Official release**.
    hipRAND is now a *standalone project*--it's no longer available as a submodule for rocRAND.

### hipTensor

* **Added architecture support**.
    We've added contraction support for gfx942 architectures, and f32 and f64 data
    types.

* **Upgraded testing infrastructure**.
    hipTensor will now support dynamic parameter configuration with input YAML config.

### MIGraphX

* **Added TorchMIGraphX**.
    We introduced a Dynamo backend for Torch, which allows PyTorch to use MIGraphX directly
    without first requiring a model to be converted to the ONNX model format. With a single line of
    code, PyTorch users can utilize the performance and quantization benefits provided by MIGraphX.

* **Boosted overall performance with rocMLIR**.
    We've integrated the rocMLIR library for ROCm-supported RDNA and CDNA GPUs. This
    technology provides MLIR-based convolution and GEMM kernel generation.

* **Added INT8 support across the MIGraphX portfolio**.
    We now support the INT8 data type. MIGraphX can perform the quantization or ingest
    prequantized models. INT8 support extends to the MIGraphX execution provider for ONNX Runtime.

### ROCgdb

* **Added support for additional GPU architectures**.
  * Navi 3 series: gfx1100, gfx1101, and gfx1102.
  * MI300 series: gfx942.

### rocm-smi-lib

* **Improved accessibility to GPU partition nodes**.
    You can now view, set, and reset the compute and memory partitions. You'll also get notifications of
    a GPU busy state, which helps you avoid partition set or reset failure.

* **Upgraded GPU metrics version 1.4**.
    The upgraded GPU metrics binary has an improved metric version format with a content version
    appended to it. You can read each metric within the binary without the full `rsmi_gpu_metric_t` data
    structure.

* **Updated GPU index sorting**.
    We made GPU index sorting consistent with other ROCm software tools by optimizing it to use
    `Bus:Device.Function` (BDF) instead of the card number.

### ROCm Compiler

* **Added kernel argument optimization on gfx942**.
    With the new feature, you can preload kernel arguments into Scalar General-Purpose Registers
    (SGPRs) rather than pass them in memory. This feature is enabled with a compiler option, which also
    controls the number of arguments to pass in SGPRs. For more information, see:
    [https://llvm.org/docs/AMDGPUUsage.html#preloaded-kernel-arguments](https://llvm.org/docs/AMDGPUUsage.html#preloaded-kernel-arguments)

* **Improved register allocation at -O0**.
    We've improved the register allocator used at -O0 to avoid compiler crashes (when the signature is
    'ran out of registers during register allocation').

* **Improved generation of debug information**.
    We've improved compile time when generating debug information for certain corner cases. We've
    also improved the compiler to eliminate compiler crashes when generating debug information.

### ROCmValidationSuite

* **Added GPU and operating system support**.
    We added support for MI300X GPU in GPU Stress Test (GST).

### Roc Profiler

* **Added option to specify desired Roc Profiler version**.
    You can now use rocProfV1 or rocProfV2 by specifying your desired version, as the legacy rocProf
    (`rocprofv1`) provides the option to use the latest version (`rocprofv2`).

* **Automated the ISA dumping process by Advance Thread Tracer**.
    Advance Thread Tracer (ATT) no longer depends on user-supplied Instruction Set Architecture (ISA)
    and compilation process (using ``hipcc --save-temps``) to dump ISA from the running kernels.

* **Added ATT support for parallel kernels**.
    The automatic ISA dumping process also helps ATT successfully parse multiple kernels running in
    parallel, and provide cycle-accurate occupancy information for multiple kernels at the same time.

### ROCr

* **Support for SDMA link aggregation**.
    If multiple XGMI links are available when making SDMA copies between GPUs, the copy is
    distributed over multiple links to increase peak bandwidth.

### rocThrust

* **Added Thrust 2.1 API support**.
    rocThrust backend is updated to Thrust and CUB 2.1.

### rocWMMA

* **Added new architecture support**.
    We added support for gfx942 architectures.

* **Added data type support**.
    We added support for f8, bf8, xf32 data types on supporting architectures, and for bf16 in the HIP RTC
    environment.

* **Added support for the PyTorch kernel plugin**.
    We added awareness of `__HIP_NO_HALF_CONVERSIONS__` to support PyTorch users.

### TransferBench (beta)

* **Improved ordering control**.
    You can now set the thread block size (`BLOCK_SIZE`) and the thread block order (`BLOCK_ORDER`)
    in which thread blocks from different transfers are run when using a single stream.

* **Added comprehensive reports**.
    We modified individual transfers to report X Compute Clusters (XCC) ID when `SHOW_ITERATIONS`
    is set to 1.

* **Improved accuracy in result validation**.
    You can now validate results for each iteration instead of just once for all iterations.
