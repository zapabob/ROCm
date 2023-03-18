# Linear Algebra Libraries

ROCm libraries for linear algebra are as follows:

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} hipBLAS
hipBLAS is a compatiblity layer for GPU accelerated BLAS optimized for AMD GPUs
via rocBLAS and rocSOLVER. hipBLAS allows for a common interface for other GPU
BLAS libraries.

- [API Reference Manual](https://rocmdocs.amd.com/projects/hipBLAS/en/rtd/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipBLAS/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} rocBLAS
rocBLAS is an AMD GPU optimized library for BLAS.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocBLAS/en/rtd/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocBLAS)

:::

:::{grid-item-card} rocSPARSE
rocSPARSE is a sparse matrix solver for AMD GPU backends.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocSPARSE/en/rtd/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocSPARSE/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} hipSPARSE
hipSPARSE is sparse matrix solver library that support AMD and NVIDIA GPU backends.

- [API Reference Manual](https://rocmdocs.amd.com/projects/hipSPARSE/en/rtd/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipSPARSE/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} rocALUTION
rocBLAS is an AMD GPU optimized library for BLAS.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocALUTION/en/rtd/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocALUTION/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} rocWMMA
AMD's C++ library for accelerating mixed-precision matrix multiply-accumulate (MMA)
operations leveraging AMD GPU hardware.

- [API Reference Manual](https://docs.amd.com/bundle/rocWMMA-release-rocm-rel-5.2/page/API_Reference_Guide.html)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocWMMA/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/ROCmSoftwarePlatform/rocWMMA/tree/develop/samples)

:::

:::{grid-item-card} rocSOLVER
rocSOLVER is a work-in-progress implementation of a subset of LAPACK functionality on the ROCm platform.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocSOLVER/en/rtd/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocSOLVER/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/ROCmSoftwarePlatform/rocSOLVER/tree/develop/clients/samples)

:::

:::{grid-item-card} hipSOLVER
hipSOLVER is a LAPACK marshalling library, with multiple supported backends. It sits between the
application and a 'worker' LAPACK library, marshalling inputs into the backend library and marshalling
results back to the application.

- [API Reference Manual](https://rocmdocs.amd.com/projects/hipSOLVER/en/rtd/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipSOLVER/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/ROCmSoftwarePlatform/hipSOLVER/tree/develop/clients/samples)

:::

:::::
