# Linear Algebra Libraries

ROCm libraries for linear algebra are as follows:

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} {doc}`rocBLAS <rocblas:index>`
`rocBLAS` is an AMD GPU optimized library for BLAS (Basic Linear Algebra Subprograms).

- {doc}`Documentation <rocblas:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocBLAS)

:::

:::{grid-item-card} {doc}`hipBLAS <hipblas:index>`
`hipBLAS` is a compatibility layer for GPU accelerated BLAS optimized for AMD GPUs
via `rocBLAS` and `rocSOLVER`. `hipBLAS` allows for a common interface for other GPU
BLAS libraries.

- {doc}`Documentation <hipblas:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipBLAS/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} {doc}`hipBLASLt <hipblaslt:index>`
`hipBLASLt` is a library that provides general matrix-matrix operations with a
flexible API and extends functionalities beyond traditional BLAS library.
`hipBLASLt` is exposed APIs in HIP programming language with an underlying
optimized generator as a back-end kernel provider.

- {doc}`Documentation <hipblaslt:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipBLASLt/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} {doc}`rocALUTION <rocalution:index>`
`rocALUTION` is a sparse linear algebra library with focus on exploring
fine-grained parallelism on top of AMD's ROCm runtime and toolchains, targeting
modern CPU and GPU platforms.

- {doc}`Documentation <rocalution:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocALUTION/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} {doc}`rocWMMA <rocwmma:index>`
`rocWMMA` provides an API to break down mixed precision matrix multiply-accumulate
(MMA) problems into fragments and distributes these over GPU wavefronts.

- {doc}`Documentation <rocwmma:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocWMMA/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} {doc}`rocSOLVER <rocsolver:index>`
`rocSOLVER` provides a subset of LAPACK (Linear Algebra Package) functionality on the ROCm platform.

- {doc}`Documentation <rocsolver:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocSOLVER/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} {doc}`hipSOLVER <hipsolver:index>`
`hipSOLVER` is a LAPACK marshalling library supporting both `rocSOLVER` and `cuSOLVER`
as backends whilst exporting a unified interface.

- {doc}`Documentation <hipsolver:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipSOLVER/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} {doc}`rocSPARSE <rocsparse:index>`
`rocSPARSE` is a library to provide BLAS for sparse computations.

- {doc}`Documentation <rocsparse:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocSOLVER/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} {doc}`hipSPARSE <hipsparse:index>`
`hipSPARSE` is a marshalling library to provide sparse BLAS functionality,
supporting both `rocSPARSE` and `cuSPARSE` as backends.

- {doc}`Documentation <hipsparse:index>`
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipSOLVER/blob/develop/CHANGELOG.md)

:::

:::::
