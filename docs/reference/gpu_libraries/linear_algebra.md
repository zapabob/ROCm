# Linear Algebra Libraries

ROCm libraries for linear algebra are as follows:

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} rocBLAS
rocBLAS is an AMD GPU optimized library for BLAS.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocBLAS/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocBLAS)

:::

:::{grid-item-card} hipBLAS
hipBLAS is a compatiblity layer for GPU accelerated BLAS optimized for AMD GPUs
via rocBLAS and rocSOLVER. hipBLAS allows for a common interface for other GPU
BLAS libraries.

- [API Reference Manual](https://rocmdocs.amd.com/projects/hipBLAS/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipBLAS/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} hipBLASLt
hipBLASLt is a library that provides general matrix-matrix operations with a flexible API and extends funtionalities beyond traditional BLAS library. hipBLASLt is exposed APIs in HIP programming language with an underlying optimized generator as a backend kernel provider.

- [API Reference Manual](https://rocmdocs.amd.com/projects/hipBLASLt/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipBLASLt/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} rocALUTION
rocALUTION is a sparse linear algebra library with focus on exploring fine-grained parallelism on top of AMD’s Radeon Open Compute ROCm runtime and toolchains, targeting modern CPU and GPU platforms.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocALUTION/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocALUTION/blob/develop/CHANGELOG.md)

:::

:::::
