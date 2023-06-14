# All Reference Material

## ROCm Software Groups

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} [HIP](./hip)
HIP is both AMD's GPU programming language extension and the GPU runtime.

- {doc}`hip:.doxygen/docBin/html/index`
- [Examples](https://github.com/amd/rocm-examples/tree/develop/HIP-Basic)

:::

:::{grid-item-card} [Math Libraries](./gpu_libraries/math)
HIP Math Libraries support the following domains:

- [Linear Algebra Libraries](./gpu_libraries/linear_algebra)
- [Fast Fourier Transforms](./gpu_libraries/fft)
- [Random Numbers](./gpu_libraries/rand)

:::

:::{grid-item-card} [C++ Primitive Libraries](./gpu_libraries/c++_primitives)
ROCm template libraries for C++ primitives and algorithms are as follows:

- {doc}`rocPRIM <rocprim:index>`
- {doc}`rocThrust <rocthrust:index>`
- {doc}`hipCUB <hipcub:index>`

:::

:::{grid-item-card} [Communication Libraries](gpu_libraries/communication)
Inter and intra-node communication is supported by the following projects:

- {doc}`RCCL <rccl:index>`

:::

:::{grid-item-card} [AI Libraries](./ai_tools)
Libraries related to AI.

- {doc}`MIOpen <miopen:index>`
- {doc}`Composable Kernel <composable-kernel:index>`
- {doc}`MIGraphX <migraphx:index>`

:::

:::{grid-item-card} [Computer Vision](./computer_vision)
Computer vision related projects.

- {doc}`MIVisionX <mivisionx:README>`
- {doc}`rocAL <rocal:README>`

:::

:::{grid-item-card} [OpenMP](openmp/openmp)

- [OpenMP Support Guide](openmp/openmp)

:::

:::{grid-item-card} [Compilers and Tools](compilers)

- [ROCmCC](/reference/rocmcc/rocmcc)
- {doc}`ROCgdb <rocgdb:index>`
- {doc}`ROCProfiler <rocprofiler:rocprof>`
- {doc}`ROCTracer <roctracer:index>`

:::

:::{grid-item-card} [Management Tools](management_tools)

- AMD SMI
- ROCm SMI
- ROCm Data Center Tool

:::

:::{grid-item-card} [Validation Tools](validation_tools)

- {doc}`ROCm Validation Suite <rocm-validation-suite:index>`
- {doc}`TransferBench <transferbench:index>`

:::

:::{grid-item-card} [GPU Architectures](gpu_arch)

- [AMD Instinct MI200](./gpu_arch/mi250.md)
- [AMD Instinct MI100](./gpu_arch/mi100.md)

:::

:::::
