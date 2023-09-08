# C++ Primitive Libraries

ROCm template libraries for algorithms are as follows:

:::::{grid} 1 1 3 3
:gutter: 1

:::{grid-item-card} {doc}`rocPRIM <rocprim:index>`
rocPRIM is an AMD GPU optimized template library of algorithm primitives, like
transforms, reductions, scans, etc. It also serves as a common back-end for
similar libraries found inside ROCm.

- {doc}`Documentation <rocprim:index>`
- [GitHub](https://github.com/ROCmSoftwarePlatform/rocPRIM/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocPRIM/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocPRIM)

:::

:::{grid-item-card} {doc}`rocThrust <rocthrust:index>`
rocThrust is a template library of algorithm primitives with a Thrust-compatible
interface. Their CPU back-ends are identical, while the GPU back-end calls into
rocPRIM.

- {doc}`Documentation <rocthrust:index>`
- [GitHub](https://github.com/ROCmSoftwarePlatform/rocThrust)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocThrust/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocThrust)

:::

:::{grid-item-card} {doc}`hipCUB <hipcub:index>`
hipCUB is a template library of algorithm primitives with a CUB-compatible
interface. It's back-end is rocPRIM.

- {doc}`Documentation <hipcub:index>`
- [GitHub](https://github.com/ROCmSoftwarePlatform/hipCUB)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipCUB/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/hipCUB)

:::

:::{grid-item-card} {doc}`hipTensor <hiptensor:index>`
hipTensor is AMD's C++ library for accelerating tensor primitives
based on the composable kernel library,
through general purpose kernel languages, like HIP C++.

- {doc}`Documentation <hiptensor:index>`
- [GitHub](https://github.com/ROCmSoftwarePlatform/hipTensor)

:::

:::::
