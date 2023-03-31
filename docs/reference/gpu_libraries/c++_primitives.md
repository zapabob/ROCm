# C++ Primitive Libraries
ROCm template libraries for algorithms are as follows:

:::::{grid} 1 1 3 3
:gutter: 1

:::{grid-item-card} rocPRIM
rocPRIM is an AMD GPU optimized template library of algorithm primitives, like
transforms, reductions, scans, etc. It also serves as a common back-end for
similar libraries found inside ROCm.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocPRIM/en/latest/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocPRIM/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocPRIM)

:::

:::{grid-item-card} rocThrust
rocThrust is a template library of algorithm primitives with a Thrust-compatible
interface. Their CPU back-ends are identical, while the GPU back-end calls into
rocPRIM.

- [API Reference Manual](https://rocmdocs.amd.com/projects/rocThrust/en/latest/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/rocThrust/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocThrust)

:::

:::{grid-item-card} hipCUB
hipCUB is a template library of algorithm primitives with a CUB-compatible
interface. It's back-end is rocPRIM.

- [API Reference Manual](https://rocmdocs.amd.com/projects/hipCUB/en/latest/)
- [Changelog](https://github.com/ROCmSoftwarePlatform/hipCUB/blob/develop/CHANGELOG.md)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/hipCUB)

:::

:::::
