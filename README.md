## Are You Ready to ROCK?
The ROCm Platform bringing a rich foundation to advanced computing by better
integrating the CPU and GPU to solve real-world problems.

On April 25th, 2016, we delivered ROCm 1.0 built around three core foundation
elements:

Open Hetrogenous Computing Platform (Linux(R) Driver and Runtime Stack)
optimized for HPC & Ultra-scale class computing Heterogeneous C and C++
Single Source to better address the whole system computation not just a GPU
device HIP acknowledging the need for platform choice when utilizing GPU
computing API

Using our knowledge of the HSA Standards and, more importantly, the HSA
Runtime we have been able to successfully extended support to the dGPU with
critical features for NUMA class acceleration. As a result, the ROCK driver is
composed of several components based on our efforts to develop the
Heterogeneous System Architecture for APUs, including the new AMDGPU driver,
the Kernel Fusion Driver (KFD), the HSA+ Runtime and an LLVM based compilation
stack for the building of key language support. This support starts with AMD’s
Fiji Family of dGPU, and has expanded to include the Hawaii dGPU Family in
ROCm 1.2.

### Overview and Installation Instructions
For an overview of the ROCm stack, installation instructions, and other supporting
documentation, please refer to https://radeonopencompute.github.io

### The Latest ROCm Platform - ROCm 1.3
The latest tested version of the drivers, tools, libraries and source code for
the ROCm platform have been released and are available under the roc-1.3.0 tag.
The repo tool can be used to checkout the full software stack.

#### Installing repo
Google's repo tool allows you to manage multiple git repositories
simultaneously. You can install it by executing the following commands:

```shell
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
```
Note: make sure ~/bin exists and it is part of your PATH

#### Cloning the code
```shell
mkdir ROCm && cd ROCm
repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-1.3.0
repo sync
```

#### Closed Source Components
The ROCm platform relies on a few closed source components to provide legacy
functionality like HSAIL finalization and debugging/profiling support. These
components are only available through the ROCm repositories, and will either be
deprecated or become open source components in the future. These components are
made available in the following packages:

*  hsa-ext-rocr-dev
