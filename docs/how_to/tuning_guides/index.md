# Tuning Guides

Use case-specific system setup and tuning guides.

## High Performance Computing

High Performance Computing (HPC) workloads have unique requirements. The default
hardware and BIOS configurations for OEM platforms may not provide optimal
performance for HPC workloads. To enable optimal HPC settings on a per-platform
and per-workload level, this guide calls out:

- BIOS settings that can impact performance
- Hardware configuration best practices
- Supported versions of operating systems
- Workload-specific recommendations for optimal BIOS and operating system
  settings

There is also a discussion on the AMD Instinct™ software development
environment, including information on how to install and run the DGEMM, STREAM,
HPCG, and HPL benchmarks. This guidance provides a good starting point but is
not exhaustively tested across all compilers.

Prerequisites to understanding this document and to performing tuning of HPC
applications include:

- Experience in configuring servers
- Administrative access to the server's Management Interface (BMC)
- Administrative access to the operating system
- Familiarity with the OEM server's BMC (strongly recommended)
- Familiarity with the OS specific tools for configuration, monitoring, and
  troubleshooting (strongly recommended)

This document provides guidance on tuning systems with various AMD Instinct™
accelerators for HPC workloads. This document is not an all-inclusive guide, and
some items referred to may have similar, but different, names in various OEM
systems (for example, OEM-specific BIOS settings). This document also provides
suggestions on items that should be the initial focus of additional,
application-specific tuning.

This document is based on the AMD EPYC™ 7003-series processor family (former
codename "Milan").

While this guide is a good starting point, developers are encouraged to perform
their own performance testing for additional tuning.

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} AMD Instinct™ MI200
This chapter goes through how to configure your AMD Instinct™ MI200 accelerated
compute nodes to get the best performance out of them.

- [Instruction Set Architecture](https://www.amd.com/system/files/TechDocs/instinct-mi200-cdna2-instruction-set-architecture.pdf)
- [Whitepaper](https://www.amd.com/system/files/documents/amd-cdna2-white-paper.pdf)
- [Guide](./mi200.md)

:::

:::{grid-item-card} AMD Instinct™ MI100
This chapter briefly reviews hardware aspects of the AMD Instinct™ MI100
accelerators and the CDNA™ 1 architecture that is the foundation of these GPUs.

- [Instruction Set Architecture](https://www.amd.com/system/files/TechDocs/instinct-mi100-cdna1-shader-instruction-set-architecture%C2%A0.pdf)
- [Whitepaper](https://www.amd.com/system/files/documents/amd-cdna-whitepaper.pdf)
- [Guide](./mi100.md)

:::

:::::

## Workstation

Workstation workloads, much like High Performance Computing have a unique set of
requirements, a blend of both graphics and compute, certification, stability and
the list continues.

The document covers specific software requirements and processes needed to use
these GPUs for Single Root I/O Virtualization (SR-IOV) and Machine Learning
(ML).

The main purpose of this document is to help users utilize the RDNA 2 GPUs to
their full potential.

:::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} AMD Radeon™ PRO W6000 and V620
This chapter describes the AMD GPUs with RDNA™ 2 architecture, namely AMD Radeon
PRO W6800 and AMD Radeon PRO V620

- [AMD RDNA2 Instruction Set Architecture](https://www.amd.com/system/files/TechDocs/rdna2-shader-instruction-set-architecture.pdf)
- [Whitepaper](https://www.amd.com/system/files/documents/rdna2-explained-radeon-pro-W6000.pdf)
- [Guide](./w6000_v620.md)

:::

:::::
