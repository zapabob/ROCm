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