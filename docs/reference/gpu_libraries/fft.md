# Fast Fourier Transforms

ROCm libraries for FFT are as follows:

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} hipFFT
hipFFT is a compatiblity layer for GPU accelerated FFT optimized for AMD GPUs
using rocFFT. hipFFT allows for a common interface for other non AMD GPU
FFT libraries.

- [Changelog](https://github.com/ROCmSoftwarePlatform/hipFFT/blob/develop/CHANGELOG.md)
- [API Reference Manual](https://rocmdocs.amd.com/projects/hipFFT/en/rtd/)

:::

:::{grid-item-card} rocFFT
rocFFT is an AMD GPU optimized library for FFT.

- [Changelog](https://github.com/ROCmSoftwarePlatform/rocFFT/blob/develop/CHANGELOG.md)
- [API Reference Manual](https://rocmdocs.amd.com/projects/hipFFT/en/rtd/)
- [Examples](https://github.com/amd/rocm-examples/tree/develop/Libraries/rocFFT)

:::

:::::
