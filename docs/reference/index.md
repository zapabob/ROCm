# Reference material

## ROCm software groups

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card}
**[HIP](./hip.md)**

HIP is both AMD's GPU programming language extension and the GPU runtime.

* [HIP Examples](https://github.com/amd/rocm-examples/tree/develop/HIP-Basic)
* {doc}`HIPIFY <hipify:index>`

:::

:::{grid-item-card}
**[Math libraries](./libraries/gpu-libraries/math.md)**

HIP Math Libraries support the following domains:

* [Linear Algebra Libraries](./libraries/gpu-libraries/math-linear-algebra.md)
* [Fast Fourier transforms (FFTs)](./libraries/gpu-libraries/math-fft.md)
* [Random Numbers](./libraries/gpu-libraries/rand.md)

:::

:::{grid-item-card}
**[C++ primitive libraries](./libraries/gpu-libraries/c++primitives.md)**

ROCm template libraries for C++ primitives and algorithms are as follows:

* {doc}`rocPRIM <rocprim:index>`
* {doc}`rocThrust <rocthrust:index>`
* {doc}`hipCUB <hipcub:index>`
* {doc}`hipTensor <hiptensor:index>`

:::

:::{grid-item-card} [Communication libraries](./libraries/gpu-libraries/communication.md)
Inter and intra-node communication is supported by the following projects:

* {doc}`RCCL <rccl:index>`

:::

:::{grid-item-card}
**Artificial intelligence**

Libraries related to artificial intelligence.

* {doc}`MIOpen <miopen:index>`
* {doc}`Composable Kernel <composable_kernel:index>`
* {doc}`MIGraphX <amdmigraphx:index>`
* {doc}`MIVisionX <mivisionx:README>`
* {doc}`ROCm Augmentation Library (rocAL) <rocal:README>`
:::

:::{grid-item-card}
**[OpenMP](./openmp/openmp.md)**

* [OpenMP support guide](./openmp/openmp.md)

:::

:::{grid-item-card}
**[Compilers and tools](./compilers-tools/index.md)**

* [ROCmCC](./rocmcc/rocmcc.md)
* {doc}`ROCdbgapi <rocdbgapi:index>`
* {doc}`ROCgdb <rocgdb:index>`
* {doc}`ROCProfiler <rocprofiler:rocprof>`
* {doc}`ROCTracer <roctracer:index>`

:::

:::{grid-item-card}
**[Management tools](./compilers-tools/management-tools.md)**

* {doc}`AMD SMI <amdsmi:index>`
* {doc}`ROCm SMI <rocm_smi_lib:index>`
* {doc}`ROCm Data Center Tool <rdc:index>`

:::

:::{grid-item-card}
**[Validation tools](./compilers-tools/validation-tools.md)**

* {doc}`ROCm Validation Suite <rocmvalidationsuite:index>`
* {doc}`TransferBench <transferbench:index>`

:::

:::{grid-item-card} **GPU architectures**

* [AMD Instinct MI200](../conceptual/gpu-arch/mi250.md)
* [AMD Instinct MI100](../conceptual/gpu-arch/mi100.md)

:::

:::::
