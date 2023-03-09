 GPU and OS Support

## OS Support

ROCm supports the operating systems listed below.
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
|GPU               |Architecture    |Product|[LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Linux                                | Windows |
|:----------------:|:--------------:|:----:|:--------------------------------------------------------------------:|:------------------------------------:|:-------:|
|Instinct™ MI250X  | CDNA2          |All |gfx90a                                                               |Supported                                  |Unsupported  |
|Instinct™ MI250   | CDNA2          |All |gfx90a                                                               |Supported                                  |Unsupported  |
|Instinct™ MI210   | CDNA2          |All |gfx90a                                                               |Supported                             |Unsupported   |
|Instinct™ MI100   | CDNA           |All|gfx908                                                               |Supported                             |Unsupported  |
|Instinct™ MI50    | Vega           |All|gfx906                                                               |Supported                             |Unsupported  |


:::

:::{tab-item} Radeon Pro™
:sync: radeonpro

[Use Radeon Pro Driver](https://www.amd.com/en/support/linux-drivers)
|GPU               |Architecture    |Product|[LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Linux                                | Windows |
|:----------------:|:--------------:|:----:|:--------------------------------------------------------------------:|:------------------------------------:|:-------:|
|Radeon™ Pro W6800 | RDNA2          |All |gfx1030                                                              |Supported                            |Supported|
|Radeon™ Pro V620  | RDNA2          |All|gfx1030                                                              |Supported                            |Unsupported|
|Radeon™ RX 6900 XT| RDNA2          |HIP SDK|gfx1030                                                              |Supported                             |Supported|
|Radeon™ RX 6600   | RDNA2          |HIP|gfx1031                                                              |Supported|Supported|
|Radeon™ R9 Fury   | Fiji           |All|gfx803                                                               |Community                            |Unsupported|

:::

:::{tab-item} Radeon™
:sync: radeon

[Use Radeon Pro Driver](https://www.amd.com/en/support/linux-drivers)
|GPU               |Architecture    |Product|[LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Linux                                | Windows |
|:----------------:|:--------------:|:----:|:--------------------------------------------------------------------:|:------------------------------------:|:-------:|
|Radeon™ RX 6900 XT| RDNA2          |HIP SDK|gfx1030                                                              |Supported                             |Supported|
|Radeon™ RX 6600   | RDNA2          |HIP|gfx1031                                                              |Supported|Supported|
|Radeon™ R9 Fury   | Fiji           |All|gfx803                                                               |Community                            |Unsupported|

:::



::::



### Products in ROCm
ROCm software support varies by GPU type and Operating System. ROCm ecosystem products are three software stack enablement levels that correspond as described below:

- All includes all software that is part of the ROCm ecosystem. Please see [article](link) for details of ROCm.
- HIP SDK includes the HIP Runtime and a selection of GPU libraries for compute. Please see [article](link) for details of HIP SDK.
- HIP enables the use of the HIP Runtime only. 


### GPU Support Levels

GPU support levels in ROCm:

- Supported - AMD enables these GPUs in our software distributions for the corresponding ROCm product.
- Unsupported - This configuration is not enabled in our software distributions. 
- Deprecated - Support will be removed in a future release. 
- Community - AMD does not enable these GPUs in our software distributions but end users are free to enable these GPUs themselves.


## CPU Support

ROCm requires CPUs that support PCIe™ Atomics. Modern CPUs after the release of
1st generation AMD Zen CPU and Intel™ Haswell support PCIe Atomics.
