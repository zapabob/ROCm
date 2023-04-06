# Package Manager Integration (Linux)

This section provides information about the required meta-packages for the
following AMD ROCm programming models:

- Heterogeneous-Computing Interface for Portability (HIP)
- OpenCL™
- OpenMP™

## ROCm Package Naming Conventions

A meta-package is a grouping of related packages and dependencies used to
support a specific use case.

**Example:** Running HIP applications

All meta-packages exist in both versioned and non-versioned forms.

- Non-versioned packages – For a single-version installation of the ROCm stack
- Versioned packages – For multiversion installations of the ROCm stack

```{figure-md} package-naming

<img src="../../data/understand/installing_linux/image.002.png" alt="">

ROCm Release Package Naming
```

{numref}`package-naming` demonstrates the single and multiversion ROCm packages' naming
structure, including examples for various Linux distributions. See terms below:

_Module_ - It is the part of the package that represents the name of the ROCm
component.

**Example:** The examples mentioned in the image represent the ROCm HIP module.

_Module version_ - It is the version of the library released in that package. It
should increase with a newer release.

_Release version_ - It shows the ROCm release version when the package was
released.

**Example:** 50400 points to the ROCm 5.4.0 release.

_Build id_ - It represents the jenkins build number for that release.

_Arch_ - It shows the architecture for which the package was created.

_Distro_ - It describes the distribution for which the package was created. It is
valid only for rpm packages.

**Example:** el8 represents RHEL 8.x packages.

## Components of ROCm Programming Models

{numref}`meta-packages` demonstrates the high-level layered architecture of ROCm
programming models and their meta-packages. All meta-packages are a combination
of required packages and libraries.

**Example:**

- rocm-hip-runtime is used to deploy on supported machines to execute HIP
applications.
- rocm-hip-sdk contains runtime components to deploy and execute HIP
applications.

```{figure-md} meta-packages

<img src="../../data/understand/installing_linux/image.003.png" alt="">

ROCm Meta Packages
```

```{note}
_rocm-llvm_ is not a meta-package but a single package that installs the ROCm
clang compiler files.
```

```{table} Meta-packages and Their Descriptions
:name: meta-package-desc
| **Meta-packages**          | **Description**                                                                                                                           |
|:--------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------:|
| **rocm-language-runtime**  | installs the ROCm runtime                                                                                                                 |
| **rocm-hip-runtime**       | installs packages necessary to run an application written in HIP for the AMD platform                                                     |
| **rocm-opencl-runtime**    | installs packages required to run OpenCL-based applications on the AMD platform                                                           |
| **rocm-hip-runtime-devel** | contains packages to develop an application on HIP or port it from CUDA                                                                   |
| **rocm-opencl-sdk**        | installs packages required to develop applications in OpenCL for the AMD platform                                                         |
| **rocm-hip-libraries**     | installs HIP libraries optimized for AMD platforms                                                                                        |
| **rocm-hip-sdk**           | installs packages necessary to develop/port applications using HIP and libraries for AMD platforms                                        |
| **rocm-developer-tools**   | installs packages required to debug and profile HIP-based applications                                                                    |
| **rocm-ml-sdk**            | installs packages necessary to develop and run Machine Learning applications with Machine Learning primitives optimized for AMD platforms |
| **rocm-ml-libraries**      | installs packages for key Machine Learning libraries, specifically MIOpen                                                                 |
| **rocm-openmp-sdk**        | installs packages necessary to develop OpenMP-based applications for AMD platforms                                                        |
| **rocm-openmp-runtime**    | installs packages necessary to run OpenMP-based applications for AMD platforms                                                            |
```

## Packages in ROCm Programming Models

This section discusses the available meta-packages and their packages. The
following image visualizes the meta-packages and their associated packages in a
ROCm programming model.

```{figure-md} assoc-packages

<img src="../../data/understand/installing_linux/image.004.png" alt="">

Associated Packages
```

- Meta-packages can include another meta-package.
- rocm-core package is common across all the meta-packages.
- Meta-packages and associated packages are represented in the same color.

```{note}
{numref}`assoc-packages` is for informational purposes only, as the individual
packages in a meta-package are subject to change. Install meta-packages, and not
individual packages, to avoid conflicts.
```
