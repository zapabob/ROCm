# Reference material

## ROCm Software Groups

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} [HIP](./hip)
HIP is both AMD's GPU programming language extension and the GPU runtime.

- {doc}`HIP <hip:index>`
- [HIP Examples](https://github.com/amd/rocm-examples/tree/develop/HIP-Basic)
- {doc}`HIPIFY <hipify:index>`

:::

:::{grid-item-card} [Math Libraries](./libraries/gpu_libraries/math)
HIP Math Libraries support the following domains:

- [Linear Algebra Libraries](./libraries/gpu_libraries/linear_algebra)
- [Fast Fourier Transforms](./libraries/gpu_libraries/fft)
- [Random Numbers](./libraries/gpu_libraries/rand)

:::

:::{grid-item-card} [C++ Primitive Libraries](./libraries/gpu_libraries/c++_primitives)
ROCm template libraries for C++ primitives and algorithms are as follows:

- {doc}`rocPRIM <rocprim:index>`
- {doc}`rocThrust <rocthrust:index>`
- {doc}`hipCUB <hipcub:index>`
- {doc}`hipTensor <hiptensor:index>`

:::

:::{grid-item-card} [Communication Libraries](./libraries/gpu_libraries/communication)
Inter and intra-node communication is supported by the following projects:

- {doc}`RCCL <rccl:index>`

:::

:::{grid-item-card} [Artificial intelligence](../rocm_ai/rocm_ai)
Libraries related to AI.

- {doc}`MIOpen <miopen:index>`
- {doc}`Composable Kernel <composable_kernel:index>`
- {doc}`MIGraphX <amdmigraphx:index>`

:::

:::{grid-item-card} [Computer Vision](./computer_vision)
Computer vision related projects.

- {doc}`MIVisionX <mivisionx:README>`
- {doc}`rocAL <rocal:README>`

:::

:::{grid-item-card} [OpenMP](openmp/openmp)

- [OpenMP Support Guide](openmp/openmp)

:::

:::{grid-item-card} [Compilers and Tools](compilers_tools/index)

- [ROCmCC](./rocmcc/rocmcc)
- {doc}`ROCdbgapi <rocdbgapi:index>`
- {doc}`ROCgdb <rocgdb:index>`
- {doc}`ROCProfiler <rocprofiler:rocprof>`
- {doc}`ROCTracer <roctracer:index>`

:::

:::{grid-item-card} [Management Tools](./compilers_tools/management_tools)

- {doc}`AMD SMI <amdsmi:index>`
- {doc}`ROCm SMI <rocm_smi_lib:index>`
- {doc}`ROCm Data Center Tool <rdc:index>`

:::

:::{grid-item-card} [Validation Tools](./compilers_tools/validation_tools)

- {doc}`ROCm Validation Suite <rocmvalidationsuite:index>`
- {doc}`TransferBench <transferbench:index>`

:::

:::{grid-item-card} GPU Architectures

- [AMD Instinct MI200](../conceptual/gpu_arch/mi250.md)
- [AMD Instinct MI100](../conceptual/gpu_arch/mi100.md)

:::

:::::
