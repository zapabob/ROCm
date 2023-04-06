# AMD ROCm Documentation

Welcome to AMD ROCm's documentation!

:::::{grid} 1 1 2 2
:gutter: 1

::::{grid-item}
:::{dropdown} [Release Info](release)

- [Release Notes](release)
- [GPU and OS Support](release/gpu_os_support)
- [Known Issues](https://github.com/RadeonOpenCompute/ROCm/labels/Verified%20Issue)
- [Compatibility](release/compatibility)
- [Licensing](release/licensing)

:::
::::

::::{grid-item}
:::{dropdown} [Deploy ROCm](deploy)

- [Quick Start (Linux)](how_to/quick_start_linux)
- [Quick Start (Windows)](how_to/quick_start_windows)
- [Docker](deploy/docker)
- [Basic Installation Guide](deploy/install)
- [Multi-ROCm Installation](deploy/multi.md)
- [Spack](deploy/spack)
- [Build from source](deploy/build_source)

:::
::::

:::::

::::{grid} 1 2 2 2
:class-container: rocm-doc-grid

:::{grid-item-card}
:padding: 2
[APIs and Reference](reference/all)
^^^

- [HIP](reference/hip)
- [Math Libraries](reference/gpu_libraries/math)
- [C++ Primitives](reference/gpu_libraries/c++_primitives)
- [Communication Libraries](reference/gpu_libraries/communication)
- [AI Libraries](reference/ai_tools)
- [Computer Vision](reference/computer_vision)
- [OpenMP](reference/openmp/openmp)
- [Compilers and Tools](reference/compilers)
- [Management Tools](reference/management_tools)
- [Validation Tools](reference/validation_tools)
- [GPU Architecture](reference/gpu_arch)

:::

:::{grid-item-card}
:padding: 2
Understand ROCm
^^^

- [Installation (Linux)](understand/installing_linux)
- [Compiler Disambiguation](understand/compiler_disambiguation)
- [ISV Deployment Guide (Windows)](understand/isv_deployment_win)
- [Using CMake](understand/cmake_packages)
- [ROCm File Reorganization White Paper](understand/file_reorg)

:::

:::{grid-item-card}
:padding: 2
How to Guides
^^^

- [How to Isolate GPUs in Docker?](how_to/docker_gpu_isolation)
- [Setting up for Deep Learning with ROCm](how_to/deep_learning_rocm)
  - [Magma Installation](how_to/magma_install/magma_install)
  - [PyTorch Installation](how_to/pytorch_install/pytorch_install)
  - [TensorFlow Installation](how_to/tensorflow_install/tensorflow_install)
- [System Level Debugging](how_to/system_debugging.md)

:::

:::{grid-item-card}
:padding: 2
Examples
^^^

- [ROCm Examples](https://github.com/amd/rocm-examples)
- [AMD lab notes](https://github.com/amd/amd-lab-notes)
- [AI/ML/Inferencing](examples/ai_ml_inferencing)
  - [Inception V3 with PyTorch](examples/inception_casestudy/inception_casestudy)

:::
::::
