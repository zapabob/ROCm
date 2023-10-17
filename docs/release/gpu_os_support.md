# GPU and OS Support (Linux)

(supported_distributions)=

## Supported Linux Distributions

AMD ROCm™ Platform supports the following Linux distributions.

::::{tab-set}

:::{tab-item} Supported

| Distribution | Processor Architectures | Validated Kernel | Support |
| :----------- | :---------------------: | :--------------: | ------: |
| CentOS 7.9     | x86-64 | 3.10    | ✅ |
| RHEL 7.9       | x86-64 | 3.10    | ✅ |
| RHEL 8.7       | x86-64 | 4.18    | ✅ |
| RHEL 8.8       | x86-64 | 4.18    | ✅ |
| RHEL 9.1       | x86-64 | 5.14    | ✅ |
| RHEL 9.2       | x86-64 | 5.14    | ✅ |
| SLES 15 SP4    | x86-64 | 5.14.21 | ✅ |
| SLES 15 SP5    | x86-64 | 5.14.21 | ✅ |
| Ubuntu 20.04.5 | x86-64 | 5.15    | ✅ |
| Ubuntu 20.04.6 | x86-64 | 5.15    | ✅ |
| Ubuntu 22.04.2 | x86-64 | 5.19    | ✅ |
| Ubuntu 22.04.3 | x86-64 | 6.2     | ✅ |

:::{versionadded} 5.7.0

- Ubuntu 22.04.3 support was added.

:::

:::{tab-item} Unsupported

| Distribution | Processor Architectures | Validated Kernel | Support |
| :----------- | :---------------------: | :--------------: | ------: |
| RHEL 9.0       | x86-64 | 5.14               | ❌ |
| RHEL 8.6       | x86-64 | 5.14               | ❌ |
| SLES 15 SP3    | x86-64 | 5.3                | ❌ |
| Ubuntu 22.04.0 | x86-64 | 5.15 LTS, 5.17 OEM | ❌ |
| Ubuntu 20.04.4 | x86-64 | 5.13 HWE, 5.13 OEM | ❌ |
| Ubuntu 22.04.1 | x86-64 | 5.15 LTS           | ❌ |

:::

::::

- ✅: **Supported** - AMD performs full testing of all ROCm components on distro
  GA image.
- ❌: **Unsupported** - AMD no longer performs builds and testing on these
  previously supported distro GA images.

## Virtualization Support

ROCm supports virtualization for select GPUs only as shown below.

| Hypervisor     | Version  | GPU   | Validated Guest OS (validated kernel)                                            |
|----------------|----------|-------|----------------------------------------------------------------------------------|
| VMWare         | ESXi 8   | MI250 | Ubuntu 20.04 (`5.15.0-56-generic`)                                               |
| VMWare         | ESXi 8   | MI210 | Ubuntu 20.04 (`5.15.0-56-generic`), SLES 15 SP4 (`5.14.21-150400.24.18-default`) |
| VMWare         | ESXi 7   | MI210 | Ubuntu 20.04 (`5.15.0-56-generic`), SLES 15 SP4 (`5.14.21-150400.24.18-default`) |

## Linux Supported GPUs

The table below shows supported GPUs for Instinct™, Radeon Pro™ and Radeon™
GPUs. Please click the tabs below to switch between GPU product lines. If a GPU
is not listed on this table, the GPU is not officially supported by AMD.

:::::{tab-set}

::::{tab-item} AMD Instinct™
:sync: instinct

| Product Name | Architecture | [LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) |Support |
|:------------:|:------------:|:--------------------------------------------------------------------:|:-------:|
| AMD Instinct™ MI250X | CDNA2  | gfx90a | ✅ |
| AMD Instinct™ MI250  | CDNA2  | gfx90a | ✅ |
| AMD Instinct™ MI210  | CDNA2  | gfx90a | ✅ |
| AMD Instinct™ MI100  | CDNA   | gfx908 | ✅ |
| AMD Instinct™ MI50   | GCN5.1 | gfx906 | ✅ |
| AMD Instinct™ MI25   | GCN5.0 | gfx900 | ❌ |

::::

::::{tab-item} Radeon Pro™
:sync: radeonpro

:::{note}
See {doc}`Radeon Software for Linux compability matrix <radeon:docs/compatibility>`
for those using select RDNA™ 3 GPU with graphical applications and ROCm.
:::

| Name | Architecture |[LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Support|
|:----:|:------------:|:--------------------------------------------------------------------:|:-------:|
| AMD Radeon™ Pro W7900   | RDNA3  | gfx1100 | ✅ (Ubuntu 22.04 only)|
| AMD Radeon™ Pro W6800   | RDNA2  | gfx1030 | ✅ |
| AMD Radeon™ Pro V620    | RDNA2  | gfx1030 | ✅ |
| AMD Radeon™ Pro VII     | GCN5.1 | gfx906  | ✅ |
::::

::::{tab-item} Radeon™
:sync: radeonpro

:::{note}
See {doc}`Radeon Software for Linux compatibility <radeon:docs/compatibility>`
for those using select RDNA™ 3 GPU with graphical applications and ROCm.
:::

| Name | Architecture    |[LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Support|
|:----:|:---------------:|:--------------------------------------------------------------------:|:-------:|
| AMD Radeon™ RX 7900 XTX | RDNA3 | gfx1100  | ✅ (Ubuntu 22.04 only)|
| AMD Radeon™ VII        | GCN5.1 | gfx906  | ✅ |

::::

:::::

### Support Status

- ✅: **Supported** - AMD enables these GPUs in our software distributions for
  the corresponding ROCm product.
- ⚠️: **Deprecated** - Support will be removed in a future release.
- ❌: **Unsupported** - This configuration is not enabled in our software
  distributions.

## CPU Support

ROCm requires CPUs that support PCIe™ Atomics. Modern CPUs after the release of
1st generation AMD Zen CPU and Intel™ Haswell support PCIe Atomics.
