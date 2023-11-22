# AMD ROCm Software

ROCm is an open-source stack, composed primarily of open-source software, designed for graphics
processing unit (GPU) computation. ROCm consists of a collection of drivers, development tools, and
APIs that enable GPU programming from low-level kernel to end-user applications.

With ROCm, you can customize your GPU software to meet your specific needs. You can develop,
collaborate, test, and deploy your applications in a free, open source, integrated, and secure software
ecosystem. ROCm is particularly well-suited to GPU-accelerated high-performance computing (HPC),
artificial intelligence (AI), scientific computing, and computer aided design (CAD).

ROCm is powered by AMD’s
[Heterogeneous-computing Interface for Portability (HIP)](https://github.com/ROCm-Developer-Tools/HIP),
an open-source software C++ GPU programming environment and its corresponding runtime. HIP
allows ROCm developers to create portable applications on different platforms by deploying code on a
range of platforms, from dedicated gaming GPUs to exascale HPC clusters.

ROCm supports programming models, such as OpenMP and OpenCL, and includes all necessary open
source software compilers, debuggers, and libraries. ROCm is fully integrated into machine learning
(ML) frameworks, such as PyTorch and TensorFlow.

## ROCm documentation

This repository contains the manifest file for ROCm releases, changelogs, and release information.

The `default.xml` file contains information for all repositories and the associated commit used to build
the current ROCm release; `default.xml` uses the Manifest Format repository.

Source code for our documentation is located in the `/docs` folder of most ROCm repositories. The
`develop` branch of our repositories contains content for the next ROCm release.

The ROCm documentation homepage is [rocm.docs.amd.com](https://rocm.docs.amd.com).

### Building our documentation

For a quick-start build, use the following code. For more options and detail, refer to
[Building documentation](./contribute/building.md).

```bash
cd docs

pip3 install -r sphinx/requirements.txt

python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

## Older ROCm releases

For release information for older ROCm releases, refer to
[`CHANGELOG`](./CHANGELOG.md).
