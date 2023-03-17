# Matrix Multiplication

ROCm libraries for BLAS are as follows:

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

:::{grid-item-card} Tensile
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems and general N-dimensional tensor contractions on a GPU.
The Tensile library is mainly used as backend library to rocBLAS. Tensile acts as the
performance backbone for a wide variety of 'compute' applications running on AMD GPUs.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocBLAS/en/rtd/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocBLAS)

:::

:::{grid-item-card} rocWMMA
AMD's C++ library for accelerating mixed-precision matrix multiply-accumulate (MMA)
operations leveraging AMD GPU hardware.

- [API Reference Manual](https://docs.amd.com/bundle/rocWMMA-release-rocm-rel-5.2/page/API_Reference_Guide.html)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocWMMA/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/ROCmSoftwarePlatform/rocWMMA/tree/develop/samples)

:::

:::::
