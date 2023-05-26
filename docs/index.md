# AMD ROCm™ Documentation

:::::{grid} 1 1 3 3
:gutter: 1

::::{grid-item}
:::{dropdown} [What is ROCm?](rocm)
ROCm is an open-source stack for GPU computation. ROCm is primarily
Open-Source Software (OSS) that allows developers the freedom to customize and
tailor their GPU software for their own needs while collaborating with a
community of other developers, and helping each other find solutions in an
agile, flexible, rapid and secure manner. [more...](rocm)

::::

::::{grid-item}
:::{dropdown} Deploy ROCm

- {doc}`/deploy/linux/index`
- {doc}`/deploy/docker`

:::
::::

::::{grid-item}
:::{dropdown} [Release Info](release)

- [Release Notes](release)
- [GPU and OS Support](release/gpu_os_support)
- [Known Issues](https://github.com/RadeonOpenCompute/ROCm/labels/Verified%20Issue)
- [Compatibility](release/compatibility)
- [Licensing](release/licensing)

:::
::::

:::::

::::{grid} 1 2 2 2
:class-container: rocm-doc-grid

:::{grid-item-card}
:padding: 2
[APIs and Reference](reference/all)
^^^

- [Compilers and Development Tools](reference/compilers)
- [HIP](reference/hip)
- [OpenMP](reference/openmp/openmp)
- [Math Libraries](reference/gpu_libraries/math)
- [C++ Primitives Libraries](reference/gpu_libraries/c++_primitives)
- [Communication Libraries](reference/gpu_libraries/communication)
- [AI Libraries](reference/ai_tools)
- [Computer Vision](reference/computer_vision)
- [Management Tools](reference/management_tools)
- [Validation Tools](reference/validation_tools)

:::

:::{grid-item-card}
:padding: 2
[Understand ROCm](understand/all)
^^^

- [Compiler Disambiguation](understand/compiler_disambiguation)
- [Using CMake](understand/cmake_packages)
- [Linux Folder Structure Reorganization](understand/file_reorg)
- [GPU Isolation Techniques](understand/gpu_isolation)
- [GPU Architecture](understand/gpu_arch)

:::

:::{grid-item-card}
:padding: 2
[How to Guides](how_to/all)
^^^

- [System Tuning for Various Architectures](how_to/tuning_guides/index)
- [GPU Aware MPI](how_to/gpu_aware_mpi)
- [Setting up for Deep Learning with ROCm](how_to/deep_learning_rocm)
  - [Magma Installation](how_to/magma_install/magma_install)
  - [PyTorch Installation](how_to/pytorch_install/pytorch_install)
  - [TensorFlow Installation](how_to/tensorflow_install/tensorflow_install)
- [System Level Debugging](how_to/system_debugging.md)

:::

:::{grid-item-card}
:padding: 2
[Tutorials & Examples](examples/all)
^^^

- [Examples](https://github.com/amd/rocm-examples)
- [ML, DL, and AI](examples/machine_learning/all)
  - [](examples/machine_learning/pytorch_inception)
  - [](examples/machine_learning/migraphx_optimization)

:::
::::
