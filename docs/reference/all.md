# All Reference Material

## ROCm Software Groups
:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} HIP Runtime
The HIP Runtime is used to enable GPU acceleration for all HIP language based products.

- [HIP Runtime API Manual](https://rocmdocs.amd.com/projects/hipBLAS/en/rtd/)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/HIP-Basic)

:::

:::{grid-item-card} [Math Libraries](./gpu_libraries/math)
HIP Math Libraries support the following domains:

- [Matrix Multiplication](./gpu_libraries/blas)
- [Fast Fourier Transforms](./gpu_libraries/fft)
- [Random Numbers](./gpu_libraries/rand)
- [Linear Solvers](./gpu_libraries/solver)
- [Sparse Matrix Solvers](./gpu_libraries/sparse)

:::

:::{grid-item-card} [C++ Primitives](./gpu_libraries/c++_primitives)
ROCm template libraries for C++ primitives and algorithms are as follows:

- [rocPRIM](https://rocprim.readthedocs.io/en/latest/)
- [rocThrust](https://rocthrust.readthedocs.io/en/latest/)
- [hipCUB](https://hipcub.readthedocs.io/en/latest/)

:::

:::{grid-item-card} [Communication Libraries](gpu_libraries/communication)
Inter and intra node communication is supported by the following projects:

- [RCCL](https://rocmdocs.amd.com/projects/rccl/en/latest/)


:::

:::{grid-item-card} MIOpen
AMD's library for high performance machine learning primitives. 

- [API Reference Manual](https://rocmdocs.amd.com/projects/MIOpen/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/MIOpen/blob/develop/CHANGELOG.md)


:::

:::{grid-item-card} MIGraphX
AMD's graph optimization engine. 

- [API Reference Manual](https://rocmdocs.amd.com/projects/AMDMIGraphX/en/develop/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/MIGraphX/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} [Computer Vision](./computer_vision)
Computer vision related projects.

- [MIVisionX](https://rocmdocs.amd.com/projects/MIVisionX/en/develop)
- [rocAL](https://rocmdocs.amd.com/projects/rocAL/en/develop)

:::


:::::