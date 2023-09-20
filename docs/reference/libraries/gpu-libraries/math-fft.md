# Fast Fourier transforms

ROCm libraries for fast Fourier transforms (FFTs) are as follows:

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} {doc}`rocFFT <rocfft:index>`

rocFFT is an AMD GPU optimized library for FFT.

* [GitHub](https://github.com/ROCmSoftwarePlatform/rocFFT)
* [Changelog](https://github.com/ROCmSoftwarePlatform/rocFFT/blob/develop/CHANGELOG.md)

:::

:::{grid-item-card} {doc}`hipFFT <hipfft:index>`

hipFFT is a compatibility layer for GPU accelerated FFT optimized for AMD GPUs
using rocFFT. hipFFT allows for a common interface for other non AMD GPU
FFT libraries.

* [GitHub](https://github.com/ROCmSoftwarePlatform/hipFFT)
* [Changelog](https://github.com/ROCmSoftwarePlatform/hipFFT/blob/develop/CHANGELOG.md)

:::

:::::
