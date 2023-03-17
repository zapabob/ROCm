# Linear Solvers

:::::{grid} 1 1 2 2
:gutter: 1

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
