# GPU and OS Support (Windows)

(supported_skus)=

## Supported SKUs

AMD ROCm™ Platform supports the following Windows SKU.

| Distribution        |Processor Architectures| Validated update   |
|---------------------|-----------------------|--------------------|
| Windows 10          | x86-64                | 22H2 (GA)          |
| Windows 11          | x86-64                | 22H2 (GA)          |
| Windows Server 2022 | x86-64                |                    |

## GPU Support Table

::::{tab-set}

:::{tab-item} Radeon Pro™
:sync: radeonpro

| Name | Architecture |[LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Runtime | HIP SDK |
|:----:|:------------:|:--------------------------------------------------------------------:|:-------:|:----------------:|
| AMD Radeon™ Pro W7900   | RDNA3  | gfx1100 | ✅ | ✅ |
| AMD Radeon™ Pro W7800   | RDNA3  | gfx1100 | ✅ | ✅ |
| AMD Radeon™ Pro W6800   | RDNA2  | gfx1030 | ✅ | ✅ |
| AMD Radeon™ Pro W6600   | RDNA2  | gfx1032 | ✅ | ❌ |
| AMD Radeon™ Pro W5500   | RDNA1  | gfx1012 | ❌ | ❌ |
| AMD Radeon™ Pro VII     | GCN5.1 | gfx906  | ❌ | ❌ |

:::

:::{tab-item} Radeon™
:sync: radeon

| Name | Architecture | [LLVM Target](https://www.llvm.org/docs/AMDGPUUsage.html#processors) | Runtime | HIP SDK |
|:----:|:------------:|:--------------------------------------------------------------------:|:-------:|:----------------:|
| AMD Radeon™ RX 7900 XTX | RDNA3  | gfx1100 | ✅ | ✅ |
| AMD Radeon™ RX 7900 XT  | RDNA3  | gfx1100 | ✅ | ✅ |
| AMD Radeon™ RX 7600     | RDNA3  | gfx1100 | ✅ | ✅ |
| AMD Radeon™ RX 6950 XT  | RDNA2  | gfx1030 | ✅ | ✅ |
| AMD Radeon™ RX 6900 XT  | RDNA2  | gfx1030 | ✅ | ✅ |
| AMD Radeon™ RX 6800 XT  | RDNA2  | gfx1030 | ✅ | ✅ |
| AMD Radeon™ RX 6800     | RDNA2  | gfx1030 | ✅ | ✅ |
| AMD Radeon™ RX 6750     | RDNA2  | gfx1032 | ✅ | ❌ |
| AMD Radeon™ RX 6700 XT  | RDNA2  | gfx1032 | ✅ | ❌ |
| AMD Radeon™ RX 6700     | RDNA2  | gfx1032 | ✅ | ❌ |
| AMD Radeon™ RX 6650 XT  | RDNA2  | gfx1032 | ✅ | ❌ |
| AMD Radeon™ RX 6600 XT  | RDNA2  | gfx1032 | ✅ | ❌ |
| AMD Radeon™ RX 6600     | RDNA2  | gfx1032 | ✅ | ❌ |

:::

::::

### Component Support

ROCm components are described in the [reference](../reference/all) page. Support
on Windows is provided with two levels on enablement.

- **Runtime**: Runtime enables the use of the HIP/OpenCL runtimes only.
- **HIP SDK**: Runtime plus additional components refer to libraries found under
  [Math Libraries](../reference/gpu_libraries/math.md) and
  [C++ Primitive Libraries](../reference/gpu_libraries/c%2B%2B_primitives.md).
  Some [Math Libraries](../reference/gpu_libraries/math.md) are Linux exclusive,
  please check the library details.

### Support Status

- ✅: **Supported** - AMD enables these GPUs in our software distributions for
  the corresponding ROCm product.
- ⚠️: **Deprecated** - Support will be removed in a future release.
- ❌: **Unsupported** - This configuration is not enabled in our software
  distributions.

## CPU Support

ROCm requires CPUs that support PCIe™ Atomics. Modern CPUs after the release of
1st generation AMD Zen CPU and Intel™ Haswell support PCIe Atomics.
