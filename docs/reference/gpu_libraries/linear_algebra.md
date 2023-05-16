# Linear Algebra Libraries

ROCm libraries for linear algebra are as follows:

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} [rocBLAS](https://rocmdocs.amd.com/projects/rocBLAS/en/develop/)
`rocBLAS` is an AMD GPU optimized library for BLAS (Basic Linear Algebra Subprograms).

- [Documentation](https://rocmdocs.amd.com/projects/rocBLAS/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocBLAS)

:::

:::{grid-item-card} [hipBLAS](https://rocmdocs.amd.com/projects/hipBLAS/en/develop/)
`hipBLAS` is a compatibility layer for GPU accelerated BLAS optimized for AMD GPUs
via `rocBLAS` and `rocSOLVER`. `hipBLAS` allows for a common interface for other GPU
BLAS libraries.

- [Documentation](https://rocmdocs.amd.com/projects/hipBLAS/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipBLAS/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} [hipBLASLt](https://rocmdocs.amd.com/projects/hipBLASLt/en/develop/)
`hipBLASLt` is a library that provides general matrix-matrix operations with a
flexible API and extends functionalities beyond traditional BLAS library.
`hipBLASLt` is exposed APIs in HIP programming language with an underlying
optimized generator as a back-end kernel provider.

- [Documentation](https://rocmdocs.amd.com/projects/hipBLASLt/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipBLASLt/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} [rocALUTION](https://rocmdocs.amd.com/projects/rocALUTION/en/develop/)
`rocALUTION` is a sparse linear algebra library with focus on exploring
fine-grained parallelism on top of AMD's ROCm runtime and toolchains, targeting
modern CPU and GPU platforms.

- [Documentation](https://rocmdocs.amd.com/projects/rocALUTION/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocALUTION/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} [rocWMMA](https://rocmdocs.amd.com/projects/rocWMMA/en/develop/)
`rocWMMA` provides an API to break down mixed precision matrix multiply-accumulate
(MMA) problems into fragments and distributes these over GPU wavefronts.

- [Documentation](https://rocmdocs.amd.com/projects/rocWMMA/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocWMMA/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} [rocSOLVER](https://rocmdocs.amd.com/projects/rocSOLVER/en/develop/)
`rocSOLVER` provides a subset of LAPACK (Linear Algebra Package) functionality on the ROCm platform.

- [Documentation](https://rocmdocs.amd.com/projects/rocSOLVER/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocSOLVER/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} [hipSOLVER](https://rocmdocs.amd.com/projects/hipSOLVER/en/develop/)
`hipSOLVER` is a LAPACK marshalling library supporting both `rocSOLVER` and `cuSOLVER`
as backends whilst exporting a unified interface.

- [Documentation](https://rocmdocs.amd.com/projects/hipSOLVER/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipSOLVER/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} [rocSPARSE](https://rocmdocs.amd.com/projects/rocSOLVER/en/develop/)
`rocSPARSE` is a library to provide BLAS for sparse computations.

- [Documentation](https://rocmdocs.amd.com/projects/rocSOLVER/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocSOLVER/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} [hipSPARSE](https://rocmdocs.amd.com/projects/hipSOLVER/en/develop/)
`hipSPARSE` is a marshalling library to provide sparse BLAS functionality,
supporting both `rocSPARSE` and `cuSPARSE` as backends.

- [Documentation](https://rocmdocs.amd.com/projects/hipSOLVER/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipSOLVER/blob/develop/CHANGELOG.md)

:::

:::::
