# AMD ROCm™ Platform

ROCm™ is an open-source stack for GPU computation. ROCm is primarily Open-Source
Software (OSS) that allows developers the freedom to customize and tailor their
GPU software for their own needs while collaborating with a community of other
developers, and helping each other find solutions in an agile, flexible, rapid
and secure manner.

ROCm is a collection of drivers, development tools and APIs enabling GPU
programming from the low-level kernel to end-user applications. ROCm is powered
by AMD’s Heterogeneous-computing Interface for Portability (HIP), an OSS C++ GPU
programming environment and its corresponding runtime. HIP allows ROCm
developers to create portable applications on different platforms by deploying
code on a range of platforms, from dedicated gaming GPUs to exascale HPC
clusters. ROCm supports programming models such as OpenMP and OpenCL, and
includes all the necessary OSS compilers, debuggers and libraries. ROCm is fully
integrated into ML frameworks such as PyTorch and TensorFlow. ROCm can be
deployed in many ways, including through the use of containers such as Docker,
Spack, and your own build from source.

ROCm’s goal is to allow our users to maximize their GPU hardware investment.
ROCm is designed to help develop, test and deploy GPU accelerated HPC, AI,
scientific computing, CAD, and other applications in a free, open-source,
integrated and secure software ecosystem.

This repository contains the manifest file for ROCm™ releases, changelogs, and
release information. The file default.xml contains information for all
repositories and the associated commit used to build the current ROCm release.

The default.xml file uses the repo Manifest format.

The develop branch of this repository contains content for the next
ROCm release.

## ROCm Documentation

ROCm Documentation is available online at
[rocm.docs.amd.com](https://rocm.docs.amd.com). Source code for the documenation
is located in the docs folder of most repositories that are part of ROCm.

### How to build documentation via Sphinx

```bash
cd docs

pip3 install -r sphinx/requirements.txt

python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

## Older ROCm™ Releases

For release information for older ROCm™ releases, refer to
[CHANGELOG](./CHANGELOG.md).
