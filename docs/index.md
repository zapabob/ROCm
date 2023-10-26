# AMD ROCm™ documentation

Welcome to the ROCm docs home page! If you're new to ROCm, you can review the following
resources to learn more about our products and what we support:

* [What is ROCm?](./what-is-rocm.md)
* [What's new?](about/whats-new/whats-new)
* [Release notes](./about/release-notes.md)

Our documentation is organized into the following categories:

::::{grid} 1 2 2 2
:class-container: rocm-doc-grid

:::{grid-item-card}
:padding: 2
**Installation**

Installation guides
^^^

* Linux
  * [Quick-start (Linux)](./install/linux/install-quick.md)
  * [Linux install guide](./install/linux/install.md)
  * [Package manager integration](./install/linux/package-manager-integration.md)
* Windows
  * [Quick-start (Windows)](./install/windows/install-quick.md)
  * [Windows install guide](./install/windows/install.md)
  * [Application deployment guidelines](./install/windows/windows-app-deployment-guidelines.md)
* [Deploy ROCm Docker containers](./install/docker.md)
* [PyTorch for ROCm](./install/pytorch-install.md)
* [TensorFlow for ROCm](./install/tensorflow-install.md)
* [MAGMA for ROCm](./install/magma-install.md)
* [ROCm & Spack](./install/spack-intro.md)

:::

:::{grid-item-card}
:padding: 2
**Compatibility & Support**

ROCm compatibility information
^^^

* [Linux (GPU & OS)](./about/compatibility/linux-support.md)
* [Windows (GPU & OS)](./about/compatibility/windows-support.md)
* [Third-party](./about/compatibility/3rd-party-support-matrix.md)
* [User/kernel space](./about/compatibility/user-kernel-space-compat-matrix.md)
* [Docker](./about/compatibility/docker-image-support-matrix.rst)
* [OpenMP](./about/compatibility/openmp.md)

:::

:::{grid-item-card}
:padding: 2
**How-to**

Task-oriented walkthroughs
^^^

* [System tuning for various architectures](./how-to/tuning-guides.md)
  * [MI100](./how-to/tuning-guides/mi100.md)
  * [MI200](./how-to/tuning-guides/mi200.md)
  * [RDNA2](./how-to/tuning-guides/w6000-v620.md)
* [Setting up for deep learning with ROCm](./how-to/deep-learning-rocm.md)
* [GPU-enabled MPI](./how-to/gpu-enabled-mpi.md)
* [System level debugging](./how-to/system-debugging.md)
* [GitHub examples](https://github.com/amd/rocm-examples)

:::

:::{grid-item-card}
:padding: 2
**Reference**

Collated information
^^^

* [API Libraries](./reference/library-index.md)

:::

:::{grid-item-card}
:padding: 2
**Conceptual**

Topic overviews & background information
^^^

* [GPU architecture](./conceptual/gpu-arch.md)
  * [MI100](./conceptual/gpu-arch/mi100.md)
  * [MI200](./conceptual/gpu-arch/mi200-performance-counters.md)
  * [MI250](./conceptual/gpu-arch/mi250.md)
* [GPU memory](./conceptual/gpu-memory.md)
* [Compiler disambiguation](./conceptual/compiler-disambiguation.md)
* [File structure (Linux FHS)](./conceptual/file-reorg.md)
* [GPU isolation techniques](./conceptual/gpu-isolation.md)
* [LLVN ASan](./conceptual/using-gpu-sanitizer.md)
* [Using CMake](./conceptual/cmake-packages.rst)
* [ROCm & PCIe atomics](./conceptual/More-about-how-ROCm-uses-PCIe-Atomics.rst)
* [Inception v3 with PyTorch](./conceptual/ai-pytorch-inception.md)
* [Inference optimization with MIGraphX](./conceptual/ai-migraphx-optimization.md)
* [OpenMP support in ROCm](./about/compatibility/openmp.md)

:::

::::

We welcome collaboration! If you'd like to contribute to our documentation, you can find instructions
on our [Contribute to ROCm docs](./contribute/index.md) page. Known issues are listed on
[GitHub](https://github.com/RadeonOpenCompute/ROCm/labels/Verified%20Issue).

Licensing information for all ROCm components is listed on our [Licensing](./about/license.md) page.
