# AMD ROCm™ Platform - Powering Your GPU Computational Needs

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
:::{dropdown} [Deploy ROCm](deploy)

- {doc}`/deploy/linux/index`
- {doc}`/deploy/quick_start_windows`
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
