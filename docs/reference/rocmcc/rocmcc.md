# Introduction to Compiler Reference Guide

ROCmCC is a Clang/LLVM-based compiler. It is optimized for high-performance computing on AMD GPUs and CPUs and supports various heterogenous programming models such as HIP, OpenMP, and OpenCL.

ROCmCC is made available via two packages: rocm-llvm and rocm-llvm-alt. The differences are shown in this table:

| <b>Table 1. rocm-llvm vs. rocm-llvm-alt</b>|
| rocm-llvm | rocm-llvm-alt |
| ----------- | ----------- |
| Installed by default when ROCm™ itself is installed | An optional package |
| Provides an open-source compiler | Provides an additional closed-source compiler for users interested in additional CPU optimizations not available in rocm-llvm |

For more details, follow this table:

| <b>Table 2. Details Table</b>|
| For | See |
| ----------- | ----------- |
| The latest usage information for AMD GPU |[https://llvm.org/docs/AMDGPUUsage.html](https://llvm.org/docs/AMDGPUUsage.html) |
|Usage information for a specific ROCm release | [https://llvm.org/docs/AMDGPUUsage.html] (https://llvm.org/docs/AMDGPUUsage.html)|
| Source code for rocm-llvm | [https://github.com/RadeonOpenCompute/llvm-project](https://github.com/RadeonOpenCompute/llvm-project) |



