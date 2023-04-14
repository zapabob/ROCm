# GPU and OS Support

## OS Support

AMD ROCm™ Platform supports the operating systems listed below.

| OS                 | Validated Kernel   |
|:------------------:|:------------------:|
| RHEL 9.1           | `5.14`             |
| RHEL 8.6 to 8.7    | `4.18`             |
| SLES 15 SP4        |                    |
| Ubuntu 20.04.5 LTS | `5.15`             |
| Ubuntu 22.04.1 LTS | `5.15`, OEM `5.17` |

## Virtualization Support

ROCm supports virtualization for select GPUs only as shown below.

| Hypervisor     | Version  | GPU   | Validated Guest OS (validated kernel)                                            |
|:--------------:|:--------:|:-----:|:--------------------------------------------------------------------------------:|
| VMWare         |ESXi 8    | MI250 | `Ubuntu 20.04 (5.15.0-56-generic)`                                               |
| VMWare         |ESXi 8    | MI210 | `Ubuntu 20.04 (5.15.0-56-generic)`, `SLES 15 SP4 (5.14.21-150400.24.18-default)` |
| VMWare         |ESXi 7    | MI210 | `Ubuntu 20.04 (5.15.0-56-generic)`, `SLES 15 SP4( 5.14.21-150400.24.18-default)` |

## GPU Support Table

::::{tab-set}

:::{tab-item} Instinct™
:sync: instinct
Use Driver Shipped with ROCm
| GPU               | Architecture    | Product | [LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Linux                                | Windows     |
|:-----------------:|:---------------:|:-------:|:--------------------------------------------------------------------:|:------------------------------------:|:-----------:|
| AMD Instinct™ MI250X  | CDNA2           | Full    | gfx90a                                                               | Supported                            | Unsupported |
| AMD Instinct™ MI250   | CDNA2           | Full    | gfx90a                                                               | Supported                            | Unsupported |
| AMD Instinct™ MI210   | CDNA2           | Full    | gfx90a                                                               | Supported                            | Unsupported |
| AMD Instinct™ MI100   | CDNA            | Full    | gfx908                                                               | Supported                            | Unsupported |
| AMD Instinct™ MI50    | Vega            | Full    | gfx906                                                               | Supported                            | Unsupported |

:::

:::{tab-item} Radeon Pro™
:sync: radeonpro

[Use Radeon Pro Driver](https://www.amd.com/en/support/linux-drivers)
| GPU               | Architecture    | SW Level | [LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Linux                                | Windows     |
|:-----------------:|:---------------:|:--------:|:--------------------------------------------------------------------:|:------------------------------------:|:-----------:|
| AMD Radeon™ Pro W6800 | RDNA2           | Full     | gfx1030                                                              | Supported                            | Supported   |
| AMD Radeon™ Pro V620  | RDNA2           | Full     | gfx1030                                                              | Supported                            | Unsupported |

:::

:::{tab-item} Radeon™
:sync: radeon

[Use Radeon Pro Driver](https://www.amd.com/en/support/linux-drivers)
| GPU                | Architecture   | SW Level   | [LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Linux                                | Windows     |
|:------------------:|:--------------:|:----------:|:--------------------------------------------------------------------:|:------------------------------------:|:-----------:|
| AMD Radeon™ RX 6900 XT | RDNA2          |HIP SDK     | gfx1030                                                              | Supported                            | Supported   |
| AMD Radeon™ RX 6600    | RDNA2          |HIP Runtime | gfx1031                                                              | Supported                            | Supported   |
| AMD Radeon™ VII        | Vega           |Full        | gfx906                                                               | Supported                            | Unsupported   |
| AMD Radeon™ R9 Fury    | Fiji           |Full        | gfx803                                                               | Community                            | Unsupported |


:::

::::

### Software Enablement Level

::::{tab-set}

:::{tab-item} AMD Instinct™
:sync: instinct

Instinct™ accelerators support the full stack available in ROCm. Instinct™ 
accelerators are Linux only.

:::

:::{tab-item} AMD Radeon Pro™
:sync: radeonpro

ROCm software support varies by GPU type and Operating System. ROCm ecosystem
products are three software stack enablement levels that correspond as
described below:

- Full includes all software that is part of the ROCm ecosystem. Please see
  [article](link) for details of ROCm.
- HIP SDK includes the HIP Runtime and a selection of GPU libraries for compute.
  Please see [article](link) for details of HIP SDK.
- HIP Runtime enables the use of the HIP Runtime only.

:::

:::{tab-item} AMD Radeon™
:sync: radeon
ROCm software support varies by GPU type and Operating System. ROCm ecosystem
products are three software stack enablement levels that correspond as described
below:

- Full includes all software that is part of the ROCm ecosystem. Please see
  [article](link) for details of ROCm.
- HIP SDK includes the HIP Runtime and a selection of GPU libraries for compute.
  Please see [article](link) for details of HIP SDK.
- HIP enables the use of the HIP Runtime only.
:::

::::

### Support Status

::::{tab-set}

:::{tab-item} Instinct™
:sync: instinct

- Supported - AMD enables these GPUs in our software distributions for the
  corresponding ROCm product.
- Unsupported - This configuration is not enabled in our software distributions.
- Deprecated - Support will be removed in a future release.

:::

:::{tab-item} Radeon Pro™
:sync: radeonpro

GPU support levels for Radeon Pro™

- Supported - AMD enables these GPUs in our software distributions for the
  corresponding ROCm product.
- Unsupported - This configuration is not enabled in our software distributions.
- Deprecated - Support will be removed in a future release.
- Community - AMD does not enable these GPUs in our software distributions but
  end users are free to enable these GPUs themselves.

:::

:::{tab-item} Radeon™
:sync: radeon

Support levels for Radeon™ GPUs:

- Supported - AMD enables these GPUs in our software distributions for the
  corresponding ROCm product.
- Unsupported - This configuration is not enabled in our software distributions.
- Deprecated - Support will be removed in a future release.
- Community - AMD does not enable these GPUs in our software distributions but
  end users are free to enable these GPUs themselves.

:::

::::

## CPU Support

ROCm requires CPUs that support PCIe™ Atomics. Modern CPUs after the release of
1st generation AMD Zen CPU and Intel™ Haswell support PCIe Atomics.
