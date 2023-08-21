# AMD ROCm™ Platform

ROCm is an open-source stack, composed primarily of open-source software (OSS), designed for
graphics processing unit (GPU) computation. ROCm consists of a collection of drivers, development
tools, and APIs that enable GPU programming from low-level kernel to end-user applications.

With ROCm, you can customize your GPU software to meet your specific needs. You can develop,
collaborate, test, and deploy your applications in a free, open-source, integrated, and secure software
ecosystem. ROCm is particularly well-suited to GPU-accelerated high-performance computing (HPC),
artificial intelligence (AI), scientific computing, and computer aided design (CAD).

ROCm is powered by AMD’s
[Heterogeneous-computing Interface for Portability (HIP)](https://github.com/ROCm-Developer-Tools/HIP),
an OSS C++ GPU programming environment and its corresponding runtime. HIP allows ROCm
developers to create portable applications on different platforms by deploying code on a range of
platforms, from dedicated gaming GPUs to exascale HPC clusters.

ROCm supports programming models, such as OpenMP and OpenCL, and includes all necessary OSS
compilers, debuggers, and libraries. ROCm is fully integrated into machine learning (ML) frameworks,
such as PyTorch and TensorFlow.

## ROCm Documentation

The ROCm Documentation site is [rocm.docs.amd.com](https://rocm.docs.amd.com).

Source code for the documentation is located in the docs folder of most repositories that are part of
ROCm.

This repository contains the manifest file for ROCm releases, changelogs, and release information.
The file `default.xml` contains information for all repositories and the associated commit used to build
the current ROCm release.

The `default.xml` file uses the repo Manifest Format.

The develop branch of this repository contains content for the next ROCm release.

### How to build documentation via Sphinx

```bash
cd docs

pip3 install -r sphinx/requirements.txt

python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

## Older ROCm Releases

For release information for older ROCm releases, refer to
[`CHANGELOG.md`](./CHANGELOG.md).
