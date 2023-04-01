# Math Libraries

AMD provides various math domain and support libraries as part of the ROCm.

## rocLIB vs. hipLIB

Several libraries are prefixed with either "roc" or "hip".
The rocLIB variants (such as rocRAND, rocBLAS) are tested and optimized for AMD hardware using supported toolchains.
The hipLIB variants (such as hipRAND, hipBLAS) are compatibility layers that provide an interface akin to their
cuLIB (such as cuRAND, cuBLAS) variants while performing static dispatching of API calls to the appropriate
vendor libraries as their back-ends. Due to their static dispatch nature, support for either vendor is decided
at compile-time of the hipLIB in question. For dynamic dispatch between vendor implementations, refer to the
[Orochi](https://github.com/GPUOpen-LibrariesAndSDKs/Orochi) library.

:::{grid-item-card} [Linear Algebra Libraries](linear_algebra)

- [rocBLAS](https://rocmdocs.amd.com/projects/rocBLAS/en/develop/)
- [hipBLAS](https://rocmdocs.amd.com/projects/hipBLAS/en/develop/)
- [hipBLASLt](https://rocmdocs.amd.com/projects/hipBLASLt/en/develop/)
- [rocALUTION](https://rocmdocs.amd.com/projects/rocALUTION/en/develop/)
- [rocWMMA](https://rocmdocs.amd.com/projects/rocWMMA/en/develop/)
- [rocSOLVER](https://rocmdocs.amd.com/projects/rocSOLVER/en/develop/)
- [hipSOLVER](https://rocmdocs.amd.com/projects/hipSOLVER/en/develop/)
- [rocSPARSE](https://rocmdocs.amd.com/projects/rocSPARSE/en/develop/)
- [hipSPARSE](https://rocmdocs.amd.com/projects/hipSPARSE/en/develop/)

:::

:::{grid-item-card} [Fast Fourier Transforms](fft)

- [rocFFT](https://rocmdocs.amd.com/projects/rocFFT/en/develop/)
- [hipFFT](https://rocmdocs.amd.com/projects/hipFFT/en/develop/)

:::

:::{grid-item-card} [Random Numbers](rand)

- [rocRAND](https://rocmdocs.amd.com/projects/rocRAND/en/develop/)
- [hipRAND](https://rocmdocs.amd.com/projects/hipRAND/en/develop/)

:::
