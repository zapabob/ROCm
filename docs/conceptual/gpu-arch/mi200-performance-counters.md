<head>
  <meta charset="UTF-8">
  <meta name="description" content="MI200 performance counters and metrics">
  <meta name="keywords" content="MI200, performance counters, counters, GRBM counters, GRBM,
  CPF counters, CPF, CPC counters, CPC, command processor counters, SPI counters, SPI, AMD, ROCm">
</head>

# MI200 performance counters and metrics
<!-- markdownlint-disable no-duplicate-header -->

This document lists and describes the hardware performance counters and derived metrics available on the AMD Instinct™ MI200 GPU. All the hardware basic counters and derived metrics are accessible via {doc}`ROCProfiler tool <rocprofiler:rocprofv1>`.

## MI200 performance counters list

See the category-wise listing of MI200 performance counters in the following tables.

:::{note}
Preliminary validation of all MI200 performance counters is in progress. Those with “*” appended to the names require further evaluation.
:::

### Graphics Register Bus Management (GRBM) counters

| Hardware Counter   | Unit   | Definition                                                                |
|:--------------------|:--------|:--------------------------------------------------------------------------|
| `GRBM_COUNT`       | Cycles | Number of free-running GPU cycles                                         |
| `GRBM_GUI_ACTIVE`  | Cycles | Number of GPU active cycles                                               |
| `GRBM_CP_BUSY`     | Cycles | Number of cycles any of the Command Processor (CP) blocks are busy                  |
| `GRBM_SPI_BUSY`    | Cycles | Number of cycles any of the Shader Processor Input (SPI) are busy in the shader engine(s) |
| `GRBM_TA_BUSY`     | Cycles | Number of cycles any of the Texture Addressing Unit (TA) are busy in the shader engine(s) |
| `GRBM_TC_BUSY`     | Cycles | Number of cycles any of the Texture Cache Blocks (TCP/TCI/TCA/TCC) are busy               |
| `GRBM_CPC_BUSY`    | Cycles | Number of cycles the Command Processor - Compute (CPC) is busy                            |
| `GRBM_CPF_BUSY`    | Cycles | Number of cycles the Command Processor - Fetcher (CPF) is busy                            |
| `GRBM_UTCL2_BUSY`  | Cycles | Number of cycles the Unified Translation Cache - Level 2 (UTCL2) block is busy            |
| `GRBM_EA_BUSY`     | Cycles | Number of cycles the Efficiency Arbiter (EA) block is busy                                |

### Command Processor (CP) counters

The CP counters are further classified into CP-Fetcher (CPF) and CP-Compute (CPC).

#### CPF counters

| Hardware Counter                     | Unit   | Definition                  |
|:--------------------------------------|:--------|:-------------------------------------------------------------|
| `CPF_CMP_UTCL1_STALL_ON_TRANSLATION` | Cycles | Number of cycles one of the Compute UTCL1s is stalled waiting on translation |
| `CPF_CPF_STAT_BUSY`                  | Cycles | Number of cycles CPF is busy                                                   |
| `CPF_CPF_STAT_IDLE*`               | Cycles | Number of cycles CPF is idle                                                   |
| `CPF_CPF_STAT_STALL`                 | Cycles | Number of cycles CPF is stalled                                                  |
| `CPF_CPF_TCIU_BUSY`                  | Cycles | Number of cycles CPF Texture Cache Interface Unit (TCIU) interface is busy                                    |
| `CPF_CPF_TCIU_IDLE`                  | Cycles | Number of cycles CPF TCIU interface is idle                                    |
| `CPF_CPF_TCIU_STALL*`              | Cycles | Number of cycles CPF TCIU interface is stalled waiting on free tags        |

#### CPC counters

| Hardware Counter                 | Unit   | Definition                                          |
|:---------------------------------|:-------|:---------------------------------------------------|
| `CPC_ME1_BUSY_FOR_PACKET_DECODE` | Cycles | Number of cycles CPC Micro Engine (ME1) is busy decoding packets                       |
| `CPC_UTCL1_STALL_ON_TRANSLATION` | Cycles | Number of cycles one of the UTCL1s is stalled waiting on translation |
| `CPC_CPC_STAT_BUSY`              | Cycles | Number of cycles CPC is busy                                            |
| `CPC_CPC_STAT_IDLE`              | Cycles | Number of cycles CPC is idle                                            |
| `CPC_CPC_STAT_STALL`             | Cycles | Number of cycles CPC is stalled                                         |
| `CPC_CPC_TCIU_BUSY`              | Cycles | Number of cycles CPC TCIU interface is busy                             |
| `CPC_CPC_TCIU_IDLE`              | Cycles | Number of cycles CPC TCIU interface is idle                             |
| `CPC_CPC_UTCL2IU_BUSY`           | Cycles | Number of cycles CPC UTCL2 interface is busy                            |
| `CPC_CPC_UTCL2IU_IDLE`           | Cycles | Number of cycles CPC UTCL2 interface is idle                            |
| `CPC_CPC_UTCL2IU_STALL`          | Cycles | Number of cycles CPC UTCL2 interface is stalled                 |
| `CPC_ME1_DC0_SPI_BUSY`           | Cycles | Number of cycles CPC ME1 Processor is busy                              |

### Shader Processor Input (SPI) counters

| Hardware Counter             | Unit        | Definition                                                   |
|:----------------------------|:-----------|:-----------------------------------------------------------|
| `SPI_CSN_BUSY`                 | Cycles      | Number of cycles with outstanding waves                      |
| `SPI_CSN_WINDOW_VALID`         | Cycles      | Number of cycles enabled by `perfcounter_start` event               |
| `SPI_CSN_NUM_THREADGROUPS`     | Workgroups  | Number of dispatched workgroups                        |
| `SPI_CSN_WAVE`                 | Wavefronts  | Number of dispatched wavefronts                        |
| `SPI_RA_REQ_NO_ALLOC`          | Cycles      | Number of Arb cycles with requests but no allocation |
|`SPI_RA_REQ_NO_ALLOC_CSN`       | Cycles      | Number of Arb cycles with Compute Shader, n-th pipe (CSn) requests but no CSn allocation |
| `SPI_RA_RES_STALL_CSN`         | Cycles      | Number of Arb stall cycles due to shortage of CSn pipeline slots |
| `SPI_RA_TMP_STALL_CSN*`      | Cycles      | Number of stall cycles due to shortage of temp space |
| `SPI_RA_WAVE_SIMD_FULL_CSN`    | SIMD-cycles | Accumulated number of Single Instruction Multiple Data (SIMDs) per cycle affected by shortage of wave slots for CSn wave dispatch   |
| `SPI_RA_VGPR_SIMD_FULL_CSN*` | SIMD-cycles | Accumulated number of SIMDs per cycle affected by shortage of VGPR slots for CSn wave dispatch  |
| `SPI_RA_SGPR_SIMD_FULL_CSN*` | SIMD-cycles | Accumulated number of SIMDs per cycle affected by shortage of SGPR slots for CSn wave dispatch    |
| `SPI_RA_LDS_CU_FULL_CSN`       | CUs         | Number of Compute Units (CUs) affected by shortage of LDS space for CSn wave dispatch   |
| `SPI_RA_BAR_CU_FULL_CSN*`    | CUs         | Number of CUs with CSn waves waiting at a BARRIER   |
| `SPI_RA_BULKY_CU_FULL_CSN*`  | CUs         | Number of CUs with CSn waves waiting for BULKY resource     |
| `SPI_RA_TGLIM_CU_FULL_CSN*`  | Cycles      | Number of CSn wave stall cycles due to restriction of `tg_limit` for thread group size    |
| `SPI_RA_WVLIM_STALL_CSN*`  | Cycles      | Number of cycles CSn is stalled due to WAVE_LIMIT            |
| `SPI_VWC_CSC_WR`               | Qcycles      | Number of quad-cycles taken to initialize Vector General Purpose Register (VGPRs) when launching waves |
| `SPI_SWC_CSC_WR`               | Qcycles      | Number of quad-cycles taken to initialize Vector General Purpose Register (SGPRs) when launching waves |

### Compute Unit (CU) counters

The CU counters are further classified into instruction mix, Matrix Fused Multiply Add (MFMA) operation counters, level counters, wavefront counters, wavefront cycle counters and Local Data Share (LDS) counters.

#### Instruction mix

| Hardware Counter        | Unit   | Definition                                                               |
|:-----------------------|:-----|:-----------------------------------------------------------------------|
| `SQ_INSTS`                | Instr | Number of instructions issued.                                              |
| `SQ_INSTS_VALU`           | Instr | Number of Vector Arithmetic Logic Unit (VALU) instructions including MFMA issued.                         |
| `SQ_INSTS_VALU_ADD_F16`   | Instr | Number of VALU Half Precision Floating Point (F16) ADD/SUB instructions issued.                            |
| `SQ_INSTS_VALU_MUL_F16`   | Instr | Number of VALU F16 Multiply instructions issued.                   |
| `SQ_INSTS_VALU_FMA_F16`   | Instr | Number of VALU F16 Fused Multiply Add (FMA)/ Multiply Add (MAD) instructions issued.                   |
| `SQ_INSTS_VALU_TRANS_F16` | Instr | Number of VALU F16 Transcendental instructions issued.                   |
| `SQ_INSTS_VALU_ADD_F32`   | Instr | Number of VALU Full Precision Floating Point (F32) ADD/SUB instructions issued.                 |
| `SQ_INSTS_VALU_MUL_F32`   | Instr | Number of VALU F32 Multiply instructions issued.                    |
| `SQ_INSTS_VALU_FMA_F32`   | Instr | Number of VALU F32 FMA/MAD instructions issued.                   |
| `SQ_INSTS_VALU_TRANS_F32` | Instr | Number of VALU F32 Transcendental instructions issued.                    |
| `SQ_INSTS_VALU_ADD_F64`   | Instr | Number of VALU F64 ADD/SUB instructions issued.                |
| `SQ_INSTS_VALU_MUL_F64`   | Instr | Number of VALU F64 Multiply instructions issued.                    |
| `SQ_INSTS_VALU_FMA_F64`   | Instr | Number of VALU F64 FMA/MAD instructions issued.                   |
| `SQ_INSTS_VALU_TRANS_F64` | Instr | Number of VALU F64 Transcendental instructions issued.                 |
| `SQ_INSTS_VALU_INT32`     | Instr | Number of VALU 32-bit integer instructions (signed or unsigned) issued.        |
| `SQ_INSTS_VALU_INT64`     | Instr | Number of VALU 64-bit integer instructions (signed or unsigned) issued.       |
| `SQ_INSTS_VALU_CVT`       | Instr | Number of VALU Conversion instructions issued.                   |
| `SQ_INSTS_VALU_MFMA_I8`   | Instr | Number of 8-bit Integer MFMA instructions issued.               |
| `SQ_INSTS_VALU_MFMA_F16`  | Instr | Number of F16 MFMA instructions issued.                                   |
| `SQ_INSTS_VALU_MFMA_BF16` | Instr | Number of Brain Floating Point - 16 (BF16) MFMA instructions issued.                                  |
| `SQ_INSTS_VALU_MFMA_F32`  | Instr | Number of F32 MFMA instructions issued.                                    |
| `SQ_INSTS_VALU_MFMA_F64`  | Instr | Number of F64 MFMA instructions issued.                               |
| `SQ_INSTS_MFMA`           | Instr | Number of MFMA instructions issued.                                  |
| `SQ_INSTS_VMEM_WR`        | Instr | Number of Vector Memory (VMEM) Write instructions (including FLAT) issued.                                  |
| `SQ_INSTS_VMEM_RD`        | Instr | Number of VMEM Read instructions (including FLAT) issued.  |
| `SQ_INSTS_VMEM`           | Instr | Number of VMEM instructions issued, including both FLAT and Buffer instructions. |
| `SQ_INSTS_SALU`           | Instr | Number of SALU instructions issued.                                        |
| `SQ_INSTS_SMEM`           | Instr | Number of Scalar Memory (SMEM) instructions issued.                                       |
| `SQ_INSTS_SMEM_NORM`      | Instr | Number of SMEM instructions normalized to match `smem_level` issued. |
| `SQ_INSTS_FLAT`           | Instr | Number of FLAT instructions issued.                                     |
| `SQ_INSTS_FLAT_LDS_ONLY`  | Instr | Number of FLAT instructions that read/write only from/to LDS issued. Works only if `EARLY_TA_DONE` is enabled.       |
| `SQ_INSTS_LDS`            | Instr | Number of Local Data Share (LDS) instructions issued (including FLAT).                                         |
| `SQ_INSTS_GDS`            | Instr | Number of Global Data Share (GDS) instructions issued.                                         |
| `SQ_INSTS_EXP_GDS`        | Instr | Number of EXP and GDS instructions excluding skipped export instructions issued.  |
| `SQ_INSTS_BRANCH`         | Instr | Number of Branch instructions issued.                                     |
| `SQ_INSTS_SENDMSG`        | Instr | Number of `SENDMSG` instructions including `s_endpgm` issued.                 |
| `SQ_INSTS_VSKIPPED*`    | Instr | Number of vector instructions skipped.                                 |

#### MFMA operation counters

| Hardware Counter             | Unit  | Definition                                      |
|:----------------------------|:-----|:----------------------------------------------|
| `SQ_INSTS_VALU_MFMA_MOPS_I8`   | IOP   | Number of 8-bit integer MFMA ops in the unit of 512 |
| `SQ_INSTS_VALU_MFMA_MOPS_F16`  | FLOP  | Number of F16 floating MFMA ops in the unit of 512  |
| `SQ_INSTS_VALU_MFMA_MOPS_BF16` | FLOP  | Number of BF16 floating MFMA ops in the unit of 512 |
| `SQ_INSTS_VALU_MFMA_MOPS_F32`  | FLOP  | Number of F32 floating MFMA ops in the unit of 512  |
| `SQ_INSTS_VALU_MFMA_MOPS_F64`  | FLOP  | Number of F64 floating MFMA ops in the unit of 512  |

#### Level counters

:::{note}
All level counters must be followed by `SQ_ACCUM_PREV_HIRES` counter to measure average latency.
:::

| Hardware Counter    | Unit  | Definition                             |
|:-------------------|:-----|:-------------------------------------|
| `SQ_ACCUM_PREV`       | Count | Accumulated counter sample value where accumulation takes place once every four cycles. |
| `SQ_ACCUM_PREV_HIRES` | Count | Accumulated counter sample value where accumulation takes place once every cycle. |
| `SQ_LEVEL_WAVES`      | Waves | Number of inflight waves. To calculate the wave latency, divide `SQ_ACCUM_PREV_HIRES` by `SQ_WAVE`.           |
| `SQ_INST_LEVEL_VMEM` | Instr | Number of inflight VMEM (including FLAT) instructions. To calculate the VMEM latency, divide `SQ_ACCUM_PREV_HIRES` by `SQ_INSTS_VMEM`.   |
| `SQ_INST_LEVEL_SMEM` | Instr | Number of inflight SMEM instructions. To calculate the SMEM latency, divide `SQ_ACCUM_PREV_HIRES` by `SQ_INSTS_SMEM_NORM`.    |
| `SQ_INST_LEVEL_LDS`  | Instr | Number of inflight LDS (including FLAT) instructions. To calculate the LDS latency, divide `SQ_ACCUM_PREV_HIRES` by `SQ_INSTS_LDS`.  |
| `SQ_IFETCH_LEVEL`     | Instr | Number of inflight instruction fetch requests from the cache. To calculate the instruction fetch latency, divide `SQ_ACCUM_PREV_HIRES` by `SQ_IFETCH`. |

#### Wavefront counters

| Hardware Counter     | Unit  | Definition                                                        |
|:--------------------|:-----|:----------------------------------------------------------------|
| `SQ_WAVES`             | Waves | Number of wavefronts dispatched to Sequencers (SQs), including both new and restored wavefronts  |
| `SQ_WAVES_SAVED*`    | Waves | Number of context-saved waves                  |
| `SQ_WAVES_RESTORED*` | Waves | Number of context-restored waves sent to SQs                  |
| `SQ_WAVES_EQ_64`       | Waves | Number of wavefronts with exactly 64 active threads sent to SQs    |
| `SQ_WAVES_LT_64`       | Waves | Number of wavefronts with less than 64 active threads sent to SQs  |
| `SQ_WAVES_LT_48`       | Waves | Number of wavefronts with less than 48 active threads sent to SQs  |
| `SQ_WAVES_LT_32`       | Waves | Number of wavefronts with less than 32 active threads sent to SQs  |
| `SQ_WAVES_LT_16`       | Waves | Number of wavefronts with less than 16 active threads sent to SQs  |

#### Wavefront cycle counters

| Hardware Counter         | Unit    | Definition                                                            |
|:------------------------|:-------|:--------------------------------------------------------------------|
| `SQ_CYCLES`                | Cycles  | Clock cycles.  |
| `SQ_BUSY_CYCLES`           | Cycles  | Number of cycles while SQ reports it to be busy.                       |
| `SQ_BUSY_CU_CYCLES`        | Qcycles | Number of quad-cycles each CU is busy.                                  |
| `SQ_VALU_MFMA_BUSY_CYCLES` | Cycles  | Number of cycles the MFMA ALU is busy.                                 |
| `SQ_WAVE_CYCLES`           | Qcycles | Number of quad-cycles spent by waves in the CUs.                       |
| `SQ_WAIT_ANY`              | Qcycles | Number of quad-cycles spent waiting for anything.                    |
| `SQ_WAIT_INST_ANY`         | Qcycles | Number of quad-cycles spent waiting for any instruction to be issued.         |
| `SQ_ACTIVE_INST_ANY`       | Qcycles | Number of quad-cycles spent by each wave to work on an instruction.   |
| `SQ_ACTIVE_INST_VMEM`      | Qcycles | Number of quad-cycles spent by the SQ instruction arbiter to work on a VMEM instruction.  |
| `SQ_ACTIVE_INST_LDS`       | Qcycles | Number of quad-cycles spent by the SQ instruction arbiter to work on an LDS instruction. |
| `SQ_ACTIVE_INST_VALU`      | Qcycles | Number of quad-cycles spent by the SQ instruction arbiter to work on a VALU instruction.  |
| `SQ_ACTIVE_INST_SCA`       | Qcycles | Number of quad-cycles spent by the SQ instruction arbiter to work on a SALU or SMEM instruction.  |
| `SQ_ACTIVE_INST_EXP_GDS`   | Qcycles | Number of quad-cycles spent by the SQ instruction arbiter to work on an EXPORT or GDS instruction.  |
| `SQ_ACTIVE_INST_MISC`      | Qcycles | Number of quad-cycles spent by the SQ instruction aribter to work on a BRANCH or `SENDMSG` instruction.  |
| `SQ_ACTIVE_INST_FLAT`      | Qcycles | Number of quad-cycles spent by the SQ instruction arbiter to work on a FLAT instruction.  |
| `SQ_INST_CYCLES_VMEM_WR`   | Qcycles | Number of quad-cycles  spent to send addr and cmd data for VMEM Write instructions.  |
| `SQ_INST_CYCLES_VMEM_RD`   | Qcycles | Number of quad-cycles  spent to send addr and cmd data for VMEM Read instructions.  |
| `SQ_INST_CYCLES_SMEM`      | Qcycles | Number of quad-cycles  spent to execute scalar memory reads.          |
| `SQ_INST_CYCLES_SALU`      | Qcycles  | Number of quad-cycles spent to execute non-memory read scalar operations.    |
| `SQ_THREAD_CYCLES_VALU`    | Cycles  | Number of thread-cycles spent to execute VALU operations. This is similar to `INST_CYCLES_VALU` but multiplied by the number of active threads.            |
| `SQ_WAIT_INST_LDS` | Qcycles | Number of quad-cycles spent waiting for LDS instruction to be issued.  |

#### LDS counters

| Hardware Counter           | Unit   | Definition                                                |
|:--------------------------|:------|:--------------------------------------------------------|
| `SQ_LDS_ATOMIC_RETURN`       | Cycles | Number of atomic return cycles in LDS                   |
| `SQ_LDS_BANK_CONFLICT`       | Cycles | Number of cycles LDS is stalled by bank conflicts     |
| `SQ_LDS_ADDR_CONFLICT*`    | Cycles | Number of cycles LDS is stalled by address conflicts     |
| `SQ_LDS_UNALIGNED_STALL*` | Cycles | Number of cycles LDS is stalled processing flat unaligned load/store ops |
| `SQ_LDS_MEM_VIOLATIONS*`   | Count  | Number of threads that have a memory violation in the LDS  |
| `SQ_LDS_IDX_ACTIVE` | Cycles | Number of cycles LDS is used for indexed operations  |

#### Miscellaneous counters

| Hardware Counter           | Unit   | Definition                                                |
|:--------------------------|:------|:--------------------------------------------------------|
| `SQ_IFETCH`        | Count   | Number of instruction fetch requests from `L1I` cache, in 32-byte width  |
| `SQ_ITEMS`         | Threads | Number of valid items per wave                                  |

### L1I and sL1D cache counters

| Hardware Counter             | Unit   | Definition                                                        |
|:----------------------------|:------|:----------------------------------------------------------------|
| `SQC_ICACHE_REQ`               | Req    | Number of `L1I` cache requests                                      |
| `SQC_ICACHE_HITS`              | Count  | Number of `L1I` cache hits                                   |
| `SQC_ICACHE_MISSES`            | Count  | Number of non-duplicate `L1I` cache misses including uncached requests                   |
| `SQC_ICACHE_MISSES_DUPLICATE`  | Count  | Number of duplicate `L1I` cache misses whose previous lookup miss on the same cache line is not fulfilled yet |
| `SQC_DCACHE_REQ`               | Req    | Number of `sL1D` cache requests                                  |
| `SQC_DCACHE_INPUT_VALID_READYB` | Cycles | Number of cycles while SQ input is valid but sL1D cache is not ready |
| `SQC_DCACHE_HITS`              | Count  | Number of `sL1D` cache hits                                |
| `SQC_DCACHE_MISSES`            | Count  | Number of non-duplicate `sL1D` cache misses including uncached requests                        |
| `SQC_DCACHE_MISSES_DUPLICATE`  | Count  | Number of duplicate `sL1D` cache misses                            |
| `SQC_DCACHE_REQ_READ_1`        | Req    | Number of constant cache read requests in a single DW  |
| `SQC_DCACHE_REQ_READ_2`        | Req    | Number of constant cache read requests in two DW      |
| `SQC_DCACHE_REQ_READ_4`        | Req    | Number of constant cache read requests in four DW  |
| `SQC_DCACHE_REQ_READ_8`        | Req    | Number of constant cache read requests in eight DW     |
| `SQC_DCACHE_REQ_READ_16`       | Req    | Number of constant cache read requests in 16 DW      |
| `SQC_DCACHE_ATOMIC*`         | Req    | Number of atomic requests                 |
| `SQC_TC_REQ`                   | Req    | Number of TC requests that were issued by instruction and constant caches  |
| `SQC_TC_INST_REQ`              | Req    | Number of instruction requests to the L2 cache            |
| `SQC_TC_DATA_READ_REQ`         | Req    | Number of data Read requests to the L2 cache                   |
| `SQC_TC_DATA_WRITE_REQ*`     | Req    | Number of data write requests to the L2 cache                    |
| `SQC_TC_DATA_ATOMIC_REQ*`    | Req    | Number of data atomic requests to the L2 cache              |
| `SQC_TC_STALL*`              | Cycles | Number of cycles while the valid requests to the L2 cache are stalled |

### Vector L1 cache subsystem

The vector L1 cache subsystem counters are further classified into Texture Addressing Unit (TA), Texture Data Unit (TD), vector L1D cache or Texture Cache per Pipe (TCP), and Texture Cache Arbiter (TCA) counters.

#### TA counters

| Hardware Counter                 | Unit   | Definition                                        |
|:--------------------------------|:------|:------------------------------------------------|
| `TA_TA_BUSY[n]`                       | Cycles | TA busy cycles. Value range for n: [0-15]. |
| `TA_TOTAL_WAVEFRONTS[n]`              | Instr  | Number of wavefronts processed by TA. Value range for n: [0-15].       |
| `TA_BUFFER_WAVEFRONTS[n]`             | Instr  | Number of buffer wavefronts processed by TA. Value range for n: [0-15].       |
| `TA_BUFFER_READ_WAVEFRONTS[n]`        | Instr  | Number of buffer read wavefronts processed by TA. Value range for n: [0-15].  |
| `TA_BUFFER_WRITE_WAVEFRONTS[n]`       | Instr  | Number of buffer write wavefronts processed by TA. Value range for n: [0-15]. |
| `TA_BUFFER_ATOMIC_WAVEFRONTS[n]`   | Instr  | Number of buffer atomic wavefronts processed by TA. Value range for n: [0-15]. |
| `TA_BUFFER_TOTAL_CYCLES[n]`           | Cycles | Number of buffer cycles (including read and write) issued to TC. Value range for n: [0-15].  |
| `TA_BUFFER_COALESCED_READ_CYCLES[n]`  | Cycles | Number of coalesced buffer read cycles issued to TC. Value range for n: [0-15].         |
| `TA_BUFFER_COALESCED_WRITE_CYCLES[n]` | Cycles | Number of coalesced buffer write cycles issued to TC. Value range for n: [0-15].         |
| `TA_ADDR_STALLED_BY_TC_CYCLES[n]`     | Cycles | Number of cycles TA address path is stalled by TC. Value range for n: [0-15]. |
| `TA_DATA_STALLED_BY_TC_CYCLES[n]`            | Cycles | Number of cycles TA data path is stalled by TC. Value range for n: [0-15].       |
| `TA_ADDR_STALLED_BY_TD_CYCLES[n]`  | Cycles | Number of cycles TA address path is stalled by TD. Value range for n: [0-15].     |
| `TA_FLAT_WAVEFRONTS[n]`               | Instr  | Number of flat opcode wavefronts processed by TA. Value range for n: [0-15].            |
| `TA_FLAT_READ_WAVEFRONTS[n]`          | Instr  | Number of flat opcode read wavefronts processed by TA. Value range for n: [0-15].        |
| `TA_FLAT_WRITE_WAVEFRONTS[n]`         | Instr  | Number of flat opcode write wavefronts processed by TA. Value range for n: [0-15].      |
| `TA_FLAT_ATOMIC_WAVEFRONTS[n]`        | Instr  | Number of flat opcode atomic wavefronts processed by TA. Value range for n: [0-15].      |

#### TD counters

| Hardware Counter         | Unit  | Definition                                           |
|:------------------------|:-----|:---------------------------------------------------|
| `TD_TD_BUSY[n]`               | Cycle | TD busy cycles while it is processing or waiting for data. Value range for n: [0-15].                            |
| `TD_TC_STALL[n]`              | Cycle | Number of cycles TD is stalled waiting for TC data. Value range for n: [0-15].   |
| `TD_SPI_STALL[n]`          | Cycle | Number of cycles TD is stalled by SPI. Value range for n: [0-15].      |
| `TD_LOAD_WAVEFRONT[n]`        | Instr |Number of wavefront instructions (read/write/atomic). Value range for n: [0-15]. |
| `TD_STORE_WAVEFRONT[n]`       | Instr | Number of write wavefront instructions. Value range for n: [0-15].|
| `TD_ATOMIC_WAVEFRONT[n]`      | Instr | Number of atomic wavefront instructions. Value range for n: [0-15]. |
| `TD_COALESCABLE_WAVEFRONT[n]` | Instr | Number of coalescable wavefronts according to TA. Value range for n: [0-15].     |

#### TCP counters

| Hardware Counter                    | Unit   | Definition                                                  |
|:-----------------------------------|:------|:----------------------------------------------------------|
| `TCP_GATE_EN1[n]`                        | Cycles | Number of cycles vL1D interface clocks are turned on. Value range for n: [0-15].    |
| `TCP_GATE_EN2[n]`                        | Cycles | Number of cycles vL1D core clocks are turned on. Value range for n: [0-15].  |
| `TCP_TD_TCP_STALL_CYCLES[n]`             | Cycles | Number of cycles TD stalls vL1D. Value range for n: [0-15].                           |
| `TCP_TCR_TCP_STALL_CYCLES[n]`            | Cycles | Number of cycles TCR stalls vL1D. Value range for n: [0-15].                           |
| `TCP_READ_TAGCONFLICT_STALL_CYCLES[n]`   | Cycles | Number of cycles tagram conflict stalls on a read. Value range for n: [0-15].          |
| `TCP_WRITE_TAGCONFLICT_STALL_CYCLES[n]`  | Cycles | Number of cycles tagram conflict stalls on a write. Value range for n: [0-15].         |
| `TCP_ATOMIC_TAGCONFLICT_STALL_CYCLES[n]` | Cycles | Number of cycles tagram conflict stalls on an atomic. Value range for n: [0-15].       |
| `TCP_PENDING_STALL_CYCLES[n]`            | Cycles | Number of cycles vL1D cache is stalled due to data pending from L2 Cache. Value range for n: [0-15]. |
| `TCP_TCP_TA_DATA_STALL_CYCLES` | Cycles | Number of cycles TCP stalls TA data interface. |
| `TCP_TA_TCP_STATE_READ[n]`               | Req    | Number of state reads. Value range for n: [0-15].    |
| `TCP_VOLATILE[n]`                     | Req    | Number of L1 volatile pixels/buffers from TA. Value range for n: [0-15].  |
| `TCP_TOTAL_ACCESSES[n]`                  | Req    | Number of vL1D accesses. Equals `TCP_PERF_SEL_TOTAL_READ`+`TCP_PERF_SEL_TOTAL_NONREAD`. Value range for n: [0-15].                    |
| `TCP_TOTAL_READ[n]`                      | Req    | Number of vL1D read accesses. Equals `TCP_PERF_SEL_TOTAL_HIT_LRU_READ` + `TCP_PERF_SEL_TOTAL_MISS_LRU_READ` + `TCP_PERF_SEL_TOTAL_MISS_EVICT_READ`. Value range for n: [0-15].    |
| `TCP_TOTAL_WRITE[n]`                     | Req    | Number of vL1D write accesses. `Equals TCP_PERF_SEL_TOTAL_MISS_LRU_WRITE`+ `TCP_PERF_SEL_TOTAL_MISS_EVICT_WRITE`. Value range for n: [0-15].     |
| `TCP_TOTAL_ATOMIC_WITH_RET[n]`           | Req    | Number of vL1D atomic requests with return. Value range for n: [0-15].       |
| `TCP_TOTAL_ATOMIC_WITHOUT_RET[n]`        | Req    | Number of vL1D atomic without return. Value range for n: [0-15].        |
| `TCP_TOTAL_WRITEBACK_INVALIDATES[n]`     | Count  | Total number of vL1D writebacks and invalidates. Equals `TCP_PERF_SEL_TOTAL_WBINVL1`+ `TCP_PERF_SEL_TOTAL_WBINVL1_VOL`+ `TCP_PERF_SEL_CP_TCP_INVALIDATE`+ `TCP_PERF_SEL_SQ_TCP_INVALIDATE_VOL`. Value range for n: [0-15].       |
| `TCP_UTCL1_REQUEST[n]`                   | Req    | Number of address translation requests to UTCL1. Value range for n: [0-15].            |
| `TCP_UTCL1_TRANSLATION_HIT[n]`           | Req    | Number of UTCL1 translation hits. Value range for n: [0-15].     |
| `TCP_UTCL1_TRANSLATION_MISS[n]`          | Req    | Number of UTCL1 translation misses. Value range for n: [0-15].    |
| `TCP_UTCL1_PERMISSION_MISS[n]`          | Req    | Number of UTCL1 permission misses. Value range for n: [0-15].       |
| `TCP_TOTAL_CACHE_ACCESSES[n]`            | Req    | Number of vL1D cache accesses including hits and misses. Value range for n: [0-15].     |
| `TCP_TCP_LATENCY[n]`                     | Cycles | Accumulated wave access latency to vL1D over all wavefronts. Value range for n: [0-15]. |
| `TCP_TCC_READ_REQ_LATENCY[n]`            | Cycles | Total vL1D to L2 request latency over all wavefronts for reads and atomics with return. Value range for n: [0-15]. |
| `TCP_TCC_WRITE_REQ_LATENCY[n]`           | Cycles | Total vL1D to L2 request latency over all wavefronts for writes and atomics without return. Value range for n: [0-15]. |
| `TCP_TCC_READ_REQ[n]`                    | Req    | Number of read requests to L2 cache. Value range for n: [0-15].      |
| `TCP_TCC_WRITE_REQ[n]`                   | Req    | Number of write requests to L2 cache. Value range for n: [0-15].                   |
| `TCP_TCC_ATOMIC_WITH_RET_REQ[n]`         | Req    | Number of atomic requests to L2 cache with return. Value range for n: [0-15].       |
| `TCP_TCC_ATOMIC_WITHOUT_RET_REQ[n]`      | Req    | Number of atomic requests to L2 cache without return. Value range for n: [0-15].    |
| `TCP_TCC_NC_READ_REQ[n]`                 | Req    | Number of NC read requests to L2 cache. Value range for n: [0-15].       |
| `TCP_TCC_UC_READ_REQ[n]`                 | Req    | Number of UC read requests to L2 cache. Value range for n: [0-15].          |
| `TCP_TCC_CC_READ_REQ[n]`                 | Req    | Number of CC read requests to L2 cache. Value range for n: [0-15].     |
| `TCP_TCC_RW_READ_REQ[n]`                 | Req    | Number of RW read requests to L2 cache. Value range for n: [0-15].       |
| `TCP_TCC_NC_WRITE_REQ[n]`                | Req    | Number of NC write requests to L2 cache. Value range for n: [0-15].         |
| `TCP_TCC_UC_WRITE_REQ[n]`                | Req    | Number of UC write requests to L2 cache. Value range for n: [0-15].         |
| `TCP_TCC_CC_WRITE_REQ[n]`                | Req    | Number of CC write requests to L2 cache. Value range for n: [0-15].         |
| `TCP_TCC_RW_WRITE_REQ[n]`                | Req    | Number of RW write requests to L2 cache. Value range for n: [0-15].         |
| `TCP_TCC_NC_ATOMIC_REQ[n]`               | Req    | Number of NC atomic requests to L2 cache. Value range for n: [0-15].        |
| `TCP_TCC_UC_ATOMIC_REQ[n]`               | Req    | Number of UC atomic requests to L2 cache. Value range for n: [0-15].      |
| `TCP_TCC_CC_ATOMIC_REQ[n]`               | Req    | Number of CC atomic requests to L2 cache. Value range for n: [0-15].      |
| `TCP_TCC_RW_ATOMIC_REQ[n]`               | Req    | Number of RW atomic requests to L2 cache. Value range for n: [0-15].       |

#### TCA counters

| Hardware Counter | Unit   | Definition                                  |
|:----------------|:------|:------------------------------------------|
| `TCA_CYCLE[n]`        | Cycles | Number of TCA cycles. Value range for n: [0-31].                               |
| `TCA_BUSY[n]`         | Cycles | Number of cycles TCA has a pending request. Value range for n: [0-31]. |

### L2 cache access counters

L2 Cache is also known as Texture Cache per Channel (TCC).

| Hardware Counter                 | Unit   | Definition                                                     |
|:--------------------------------|:------|:-------------------------------------------------------------|
| `TCC_CYCLE[n]`                        |Cycle   | Number of L2 cache free-running clocks. Value range for n: [0-31].               |
| `TCC_BUSY[n]`                         |Cycle   | Number of L2 cache busy cycles. Value range for n: [0-31].                                        |
| `TCC_REQ[n]`                          |Req     | Number of L2 cache requests of all types. This is measured at the tag block. This may be more than the number of requests arriving at the TCC, but it is a good indication of the total amount of work that needs to be performed. Value range for n: [0-31].      |
| `TCC_STREAMING_REQ[n]`             |Req     | Number of L2 cache streaming requests. This is measured at the tag block. Value range for n: [0-31]. |
| `TCC_NC_REQ[n]`                       |Req     | Number of NC requests. This is measured at the tag block. Value range for n: [0-31].   |
| `TCC_UC_REQ[n]`                       |Req     | Number of UC requests. This is measured at the tag block. Value range for n: [0-31].   |
| `TCC_CC_REQ[n]`                       |Req     | Number of CC requests. This is measured at the tag block. Value range for n: [0-31].   |
| `TCC_RW_REQ[n]`                       |Req     | Number of RW requests. This is measured at the tag block. Value range for n: [0-31].   |
| `TCC_PROBE[n]`                        |Req     | Number of probe requests. Value range for n: [0-31].  |
| `TCC_PROBE_ALL[n]`                 |Req     | Number of external probe requests with `EA_TCC_preq_all`== 1. Value range for n: [0-31].    |
| `TCC_READ[n]`                     |Req     | Number of L2 cache read requests. This includes compressed reads but not metadata reads. Value range for n: [0-31].   |
| `TCC_WRITE[n]`                    |Req     | Number of L2 cache write requests. Value range for n: [0-31].     |
| `TCC_ATOMIC[n]`                   |Req     | Number of L2 cache atomic requests of all types. Value range for n: [0-31]. |
| `TCC_HIT[n]`                          |Req     | Number of L2 cache hits. Value range for n: [0-31].      |
| `TCC_MISS[n]`                         |Req     | Number of L2 cache misses. Value range for n: [0-31].        |
| `TCC_WRITEBACK[n]`                    |Req     | Number of lines written back to the main memory, including writebacks of dirty lines and uncached write/atomic requests. Value range for n: [0-31]. |
| `TCC_EA_WRREQ[n]`                     |Req     | Number of 32-byte and 64-byte transactions going over the `TC_EA_wrreq` interface. Atomics may travel over the same interface and are generally classified as write requests. This does not include probe commands. Value range for n: [0-31].   |
| `TCC_EA_WRREQ_64B[n]`                 |Req     | Total number of 64-byte transactions (write or `CMPSWAP`) going over the `TC_EA_wrreq` interface. Value range for n: [0-31].  |
| `TCC_EA_WR_UNCACHED_32B[n]`           |Req     | Number of 32-byte write/atomic going over the `TC_EA_wrreq` interface due to uncached traffic. Note that CC mtypes can produce uncached requests, and those are included in this. A 64-byte request is counted as 2. Value range for n: [0-31].|
| `TCC_EA_WRREQ_STALL[n]`               | Cycles | Number of cycles a write request is stalled. Value range for n: [0-31].                 |
| `TCC_EA_WRREQ_IO_CREDIT_STALL[n]`  | Cycles | Number of cycles an EA write request is stalled due to the interface running out of IO credits. Value range for n: [0-31].  |
| `TCC_EA_WRREQ_GMI_CREDIT_STALL[n]` | Cycles | Number of cycles an EA write request is stalled due to the interface running out of GMI credits. Value range for n: [0-31].  |
| `TCC_EA_WRREQ_DRAM_CREDIT_STALL[n]`   | Cycles | Number of cycles an EA write request is stalled due to the interface running out of DRAM credits. Value range for n: [0-31]. |
| `TCC_TOO_MANY_EA_WRREQS_STALL[n]`  | Cycles | Number of cycles the L2 cache is unable to send an EA write request due to it reaching its maximum capacity of pending EA write requests. Value range for n: [0-31]. |
| `TCC_EA_WRREQ_LEVEL[n]`               | Req    | The accumulated number of EA write requests in flight. This is primarily intended to measure average EA write latency. Average write latency = `TCC_PERF_SEL_EA_WRREQ_LEVEL`/`TCC_PERF_SEL_EA_WRREQ`. Value range for n: [0-31].  |
| `TCC_EA_ATOMIC[n]`                    | Req    | Number of 32-byte or 64-byte atomic requests going over the `TC_EA_wrreq` interface. Value range for n: [0-31].           |
| `TCC_EA_ATOMIC_LEVEL[n]`              | Req    | The accumulated number of EA atomic requests in flight. This is primarily intended to measure average EA atomic latency. Average atomic latency = `TCC_PERF_SEL_EA_WRREQ_ATOMIC_LEVEL`/`TCC_PERF_SEL_EA_WRREQ_ATOMIC`. Value range for n: [0-31].  |
| `TCC_EA_RDREQ[n]`                     | Req    | Number of 32-byte or 64-byte read requests to EA. Value range for n: [0-31].   |
| `TCC_EA_RDREQ_32B[n]`                 | Req    | Number of 32-byte read requests to EA. Value range for n: [0-31].  |
| `TCC_EA_RD_UNCACHED_32B[n]`           | Req    | Number of 32-byte EA reads due to uncached traffic. A 64-byte request is counted as 2. Value range for n: [0-31]. |
| `TCC_EA_RDREQ_IO_CREDIT_STALL[n]`  | Cycles | Number of cycles there is a stall due to the read request interface running out of IO credits. Stalls occur irrespective of the need for a read to be performed. Value range for n: [0-31]. |
| `TCC_EA_RDREQ_GMI_CREDIT_STALL[n]` | Cycles | Number of cycles there is a stall due to the read request interface running out of GMI credits. Stalls occur irrespective of the need for a read to be performed. Value range for n: [0-31]. |
| `TCC_EA_RDREQ_DRAM_CREDIT_STALL[n]`   | Cycles | Number of cycles there is a stall due to the read request interface running out of DRAM credits. Stalls occur irrespective of the need for a read to be performed. Value range for n: [0-31]. |
| `TCC_EA_RDREQ_LEVEL[n]`               | Req    | The accumulated number of EA read requests in flight. This is primarily intended to measure average EA read latency. Average read latency = `TCC_PERF_SEL_EA_RDREQ_LEVEL`/`TCC_PERF_SEL_EA_RDREQ`. Value range for n: [0-31].    |
| `TCC_EA_RDREQ_DRAM[n]`                | Req    | Number of 32-byte or 64-byte EA read requests to High Bandwidth Memory (HBM). Value range for n: [0-31].   |
| `TCC_EA_WRREQ_DRAM[n]`                | Req    | Number of 32-byte or 64-byte EA write requests to HBM. Value range for n: [0-31].  |
| `TCC_TAG_STALL[n]`                    | Cycles | Number of cycles the normal request pipeline in the tag is stalled for any reason.  Normally, stalls of this nature are measured exactly at one point in the pipeline however in case of this counter, probes can stall the pipeline at a variety of places and there is no single point that can reasonably measure the total stalls accurately. Value range for n: [0-31]. |
| `TCC_NORMAL_WRITEBACK[n]`             | Req    | Number of writebacks due to requests that are not writeback requests. Value range for n: [0-31].    |
| `TCC_ALL_TC_OP_WB_WRITEBACK[n]`    | Req    | Number of writebacks due to all `TC_OP` writeback requests. Value range for n: [0-31].       |
| `TCC_NORMAL_EVICT[n]`                 | Req    | Number of evictions due to requests that are not invalidate or probe requests. Value range for n: [0-31].        |
| `TCC_ALL_TC_OP_INV_EVICT[n]`       | Req    | Number of evictions due to all `TC_OP` invalidate requests. Value range for n: [0-31].           |

## MI200 derived metrics list

| Derived Metric   | Description                                                                            |
|:----------------|:-------------------------------------------------------------------------------------|
| `ALUStalledByLDS` | Percentage of GPU time ALU units are stalled due to the LDS input queue being full or the output queue not being ready. Reduce this by reducing the LDS bank conflicts or the number of LDS accesses if possible. Value range: 0% (optimal) to 100% (bad). |
| `FetchSize` | Total kilobytes fetched from the video memory. This is measured with all extra fetches and any cache or memory effects taken into account. |
| `FlatLDSInsts`     | Average number of FLAT instructions that read from or write to LDS, executed per work item (affected by flow control). |
| `FlatVMemInsts`    | Average number of FLAT instructions that read from or write to the video memory, executed per work item (affected by flow control). Includes FLAT instructions that read from or write to scratch. |
| `GDSInsts` | Average number of GDS read/write instructions executed per work item (affected by flow control). |
| `GPUBusy` | Percentage of time GPU is busy. |
| `L2CacheHit`       | Percentage of fetch, write, atomic, and other instructions that hit the data in L2 cache. Value range: 0% (no hit) to 100% (optimal). |
| `LDSBankConflict`  | Percentage of GPU time LDS is stalled by bank conflicts. Value range: 0% (optimal) to 100% (bad). |
| `LDSInsts`         | Average number of LDS read/write instructions executed per work item (affected by flow control). Excludes FLAT instructions that read from or write to LDS. |
| `MemUnitBusy` | Percentage of GPU time the memory unit is active. The result includes the stall time (`MemUnitStalled`). This is measured with all extra fetches and writes and any cache or memory effects taken into account. Value range: 0% to 100% (fetch-bound). |
| `MemUnitStalled`   | Percentage of GPU time the memory unit is stalled. Try reducing the number or size of fetches and writes if possible. Value range: 0% (optimal) to 100% (bad). |
| `MemWrites32B`     | Total number of effective 32B write transactions to the memory.                      |
| `SALUBusy`         | Percentage of GPU time scalar ALU instructions are processed. Value range: 0% (bad) to 100% (optimal). |
| `SALUInsts` | Average number of scalar ALU instructions executed per work item (affected by flow control). |
| `SFetchInsts` | Average number of scalar fetch instructions from the video memory executed per work item (affected by flow control). |
| `TA_ADDR_STALLED_BY_TC_CYCLES_sum` | Total number of cycles TA address path is stalled by TC, over all TA instances. |
| `TA_ADDR_STALLED_BY_TD_CYCLES_sum` | Total number of cycles TA address path is stalled by TD, over all TA instances. |
| `TA_BUFFER_WAVEFRONTS_sum` | Total number of buffer wavefronts processed by all TA instances. |
| `TA_BUFFER_READ_WAVEFRONTS_sum` | Total number of buffer read wavefronts processed by all TA instances. |
| `TA_BUFFER_WRITE_WAVEFRONTS_sum` | Total number of buffer write wavefronts processed by all TA instances. |
| `TA_BUFFER_ATOMIC_WAVEFRONTS_sum` | Total number of buffer atomic wavefronts processed by all TA instances. |
| `TA_BUFFER_TOTAL_CYCLES_sum` | Total number of buffer cycles (including read and write) issued to TC by all TA instances. |
| `TA_BUFFER_COALESCED_READ_CYCLES_sum` | Total number of coalesced buffer read cycles issued to TC by all TA instances. |
| `TA_BUFFER_COALESCED_WRITE_CYCLES_sum` | Total number of coalesced buffer write cycles issued to TC by all TA instances. |
| `TA_BUSY_avr` | Average number of busy cycles over all TA instances. |
| `TA_BUSY_max` | Maximum number of TA busy cycles over all TA instances. |
| `TA_BUSY_min` | Minimum number of TA busy cycles over all TA instances. |
| `TA_DATA_STALLED_BY_TC_CYCLES_sum` | Total number of cycles TA data path is stalled by TC, over all TA instances. |
| `TA_FLAT_READ_WAVEFRONTS_sum` | Sum of flat opcode reads processed by all TA instances. |
| `TA_FLAT_WRITE_WAVEFRONTS_sum` | Sum of flat opcode writes processed by all TA instances. |
| `TA_FLAT_WAVEFRONTS_sum` | Total number of flat opcode wavefronts processed by all TA instances. |
| `TA_FLAT_READ_WAVEFRONTS_sum` | Total number of flat opcode read wavefronts processed by all TA instances. |
| `TA_FLAT_ATOMIC_WAVEFRONTS_sum` | Total number of flat opcode atomic wavefronts processed by all TA instances. |
| `TA_TA_BUSY_sum` | Total number of TA busy cycles over all TA instances. |
| `TA_TOTAL_WAVEFRONTS_sum` | Total number of wavefronts processed by all TA instances. |
| `TCA_BUSY_sum` | Total number of cycles TCA has a pending request, over all TCA instances. |
| `TCA_CYCLE_sum` | Total number of cycles over all TCA instances. |
| `TCC_ALL_TC_OP_WB_WRITEBACK_sum` | Total number of writebacks due to all TC_OP writeback requests, over all TCC instances. |
| `TCC_ALL_TC_OP_INV_EVICT_sum` | Total number of evictions due to all TC_OP invalidate requests, over all TCC instances. |
| `TCC_ATOMIC_sum` | Total number of L2 cache atomic requests of all types, over all TCC instances. |
| `TCC_BUSY_avr` | Average number of L2 cache busy cycles, over all TCC instances. |
| `TCC_BUSY_sum` | Total number of L2 cache busy cycles, over all TCC instances. |
| `TCC_CC_REQ_sum` | Total number of CC requests over all TCC instances. |
| `TCC_CYCLE_sum` | Total number of L2 cache free running clocks, over all TCC instances. |
| `TCC_EA_WRREQ_sum` | Total number of 32-byte and 64-byte transactions going over the TC_EA_wrreq interface, over all TCC instances. Atomics may travel over the same interface and are generally classified as write requests. This does not include probe commands. |
| `TCC_EA_WRREQ_64B_sum` | Total number of 64-byte transactions (write or `CMPSWAP`) going over the TC_EA_wrreq interface, over all TCC instances. |
| `TCC_EA_WR_UNCACHED_32B_sum` | Total Number of 32-byte write/atomic going over the TC_EA_wrreq interface due to uncached traffic, over all TCC instances. Note that CC mtypes can produce uncached requests, and those are included in this. A 64-byte request is counted as 2. |
| `TCC_EA_WRREQ_STALL_sum` | Total Number of cycles a write request is stalled, over all instances. |
| `TCC_EA_WRREQ_IO_CREDIT_STALL_sum` | Total number of cycles an EA write request is stalled due to the interface running out of IO credits, over all instances. |
| `TCC_EA_WRREQ_GMI_CREDIT_STALL_sum` | Total number of cycles an EA write request is stalled due to the interface running out of GMI credits, over all instances. |
| `TCC_EA_WRREQ_DRAM_CREDIT_STALL_sum` | Total number of cycles an EA write request is stalled due to the interface running out of DRAM credits, over all instances. |
| `TCC_EA_WRREQ_LEVEL_sum` | Total number of EA write requests in flight over all TCC instances. |
| `TCC_EA_RDREQ_LEVEL_sum` | Total number of EA read requests in flight over all TCC instances. |
| `TCC_EA_ATOMIC_sum` | Total Number of 32-byte or 64-byte atomic requests going over the TC_EA_wrreq interface, over all TCC instances. |
| `TCC_EA_ATOMIC_LEVEL_sum` | Total number of EA atomic requests in flight, over all TCC instances. |
| `TCC_EA_RDREQ_sum` | Total number of 32-byte or 64-byte read requests to EA, over all TCC instances. |
| `TCC_EA_RDREQ_32B_sum` | Total number of 32-byte read requests to EA, over all TCC instances. |
| `TCC_EA_RD_UNCACHED_32B_sum` | Total number of 32-byte EA reads due to uncached traffic, over all TCC instances. |
| `TCC_EA_RDREQ_IO_CREDIT_STALL_sum` | Total number of cycles there is a stall due to the read request interface running out of IO credits, over all TCC instances. |
| `TCC_EA_RDREQ_GMI_CREDIT_STALL_sum` | Total number of cycles there is a stall due to the read request interface running out of GMI credits, over all TCC instances. |
| `TCC_EA_RDREQ_DRAM_CREDIT_STALL_sum` | Total number of cycles there is a stall due to the read request interface running out of DRAM credits, over all TCC instances. |
| `TCC_EA_RDREQ_DRAM_sum` | Total number of 32-byte or 64-byte EA read requests to HBM, over all TCC instances. |
| `TCC_EA_WRREQ_DRAM_sum` | Total number of 32-byte or 64-byte EA write requests to HBM, over all TCC instances. |
| `TCC_HIT_sum` | Total number of L2 cache hits over all TCC instances. |
| `TCC_MISS_sum` | Total number of L2 cache misses over all TCC instances. |
| `TCC_NC_REQ_sum` | Total number of NC requests over all TCC instances. |
| `TCC_NORMAL_WRITEBACK_sum` | Total number of writebacks due to requests that are not writeback requests, over all TCC instances. |
| `TCC_NORMAL_EVICT_sum` | Total number of evictions due to requests that are not invalidate or probe requests, over all TCC instances. |
| `TCC_PROBE_sum` | Total number of probe requests over all TCC instances. |
| `TCC_PROBE_ALL_sum` | Total number of external probe requests with EA_TCC_preq_all== 1, over all TCC instances. |
| `TCC_READ_sum` | Total number of L2 cache read requests (including compressed reads but not metadata reads) over all TCC instances. |
| `TCC_REQ_sum` | Total number of all types of L2 cache requests over all TCC instances. |
| `TCC_RW_REQ_sum` | Total number of RW requests over all TCC instances. |
| `TCC_STREAMING_REQ_sum` | Total number of L2 cache streaming requests over all TCC instances. |
| `TCC_TAG_STALL_sum` | Total number of cycles the normal request pipeline in the tag is stalled for any reason, over all TCC instances. |
| `TCC_TOO_MANY_EA_WRREQS_STALL_sum` | Total number of cycles L2 cache is unable to send an EA write request due to it reaching its maximum capacity of pending EA write requests, over all TCC instances. |
| `TCC_UC_REQ_sum` | Total number of UC requests over all TCC instances. |
| `TCC_WRITE_sum` | Total number of L2 cache write requests over all TCC instances. |
| `TCC_WRITEBACK_sum` | Total number of lines written back to the main memory including writebacks of dirty lines and uncached write/atomic requests, over all TCC instances. |
| `TCC_WRREQ_STALL_max` | Maximum number of cycles a write request is stalled, over all TCC instances. |
| `TCP_ATOMIC_TAGCONFLICT_STALL_CYCLES_sum` | Total number of cycles tagram conflict stalls on an atomic, over all TCP instances. |
| `TCP_GATE_EN1_sum` | Total number of cycles vL1D interface clocks are turned on, over all TCP instances. |
| `TCP_GATE_EN2_sum` | Total number of cycles vL1D core clocks are turned on, over all TCP instances. |
| `TCP_PENDING_STALL_CYCLES_sum` | Total number of cycles vL1D cache is stalled due to data pending from L2 Cache, over all TCP instances. |
| `TCP_READ_TAGCONFLICT_STALL_CYCLES_sum` | Total number of cycles tagram conflict stalls on a read, over all TCP instances. |
| `TCP_TA_TCP_STATE_READ_sum` | Total number of state reads by all TCP instances. |
| `TCP_TCC_ATOMIC_WITH_RET_REQ_sum` | Total number of atomic requests to L2 cache with return, over all TCP instances. |
| `TCP_TCC_ATOMIC_WITHOUT_RET_REQ_sum` | Total number of atomic requests to L2 cache without return, over all TCP instances. |
| `TCP_TCC_CC_READ_REQ_sum` | Total number of CC read requests to L2 cache, over all TCP instances. |
| `TCP_TCC_CC_WRITE_REQ_sum` | Total number of CC write requests to L2 cache, over all TCP instances. |
| `TCP_TCC_CC_ATOMIC_REQ_sum` | Total number of CC atomic requests to L2 cache, over all TCP instances. |
| `TCP_TCC_NC_READ_REQ_sum` | Total number of NC read requests to L2 cache, over all TCP instances. |
| `TCP_TCC_NC_WRITE_REQ_sum` | Total number of NC write requests to L2 cache, over all TCP instances. |
| `TCP_TCC_NC_ATOMIC_REQ_sum` | Total number of NC atomic requests to L2 cache, over all TCP instances. |
| `TCP_TCC_READ_REQ_LATENCY_sum` | Total vL1D to L2 request latency over all wavefronts for reads and atomics with return for all TCP instances. |
| `TCP_TCC_READ_REQ_sum` | Total number of read requests to L2 cache, over all TCP instances. |
| `TCP_TCC_RW_READ_REQ_sum` | Total number of RW read requests to L2 cache, over all TCP instances. |
| `TCP_TCC_RW_WRITE_REQ_sum` | Total number of RW write requests to L2 cache, over all TCP instances. |
| `TCP_TCC_RW_ATOMIC_REQ_sum` | Total number of RW atomic requests to L2 cache, over all TCP instances. |
| `TCP_TCC_UC_READ_REQ_sum` | Total number of UC read requests to L2 cache, over all TCP instances. |
| `TCP_TCC_UC_WRITE_REQ_sum` | Total number of UC write requests to L2 cache, over all TCP instances. |
| `TCP_TCC_UC_ATOMIC_REQ_sum` | Total number of UC atomic requests to L2 cache, over all TCP instances. |
| `TCP_TCC_WRITE_REQ_LATENCY_sum` | Total vL1D to L2 request latency over all wavefronts for writes and atomics without return for all TCP instances. |
| `TCP_TCC_WRITE_REQ_sum` | Total number of write requests to L2 cache, over all TCP instances. |
| `TCP_TCP_LATENCY_sum` | Total wave access latency to vL1D over all wavefronts for all TCP instances. |
| `TCP_TCR_TCP_STALL_CYCLES_sum` | Total number of cycles TCR stalls vL1D, over all TCP instances. |
| `TCP_TD_TCP_STALL_CYCLES_sum` | Total number of cycles TD stalls vL1D, over all TCP instances. |
| `TCP_TOTAL_ACCESSES_sum` | Total number of vL1D accesses, over all TCP instances. |
| `TCP_TOTAL_READ_sum` | Total number of vL1D read accesses, over all TCP instances. |
| `TCP_TOTAL_WRITE_sum` | Total number of vL1D write accesses, over all TCP instances. |
| `TCP_TOTAL_ATOMIC_WITH_RET_sum` | Total number of vL1D atomic requests with return, over all TCP instances. |
| `TCP_TOTAL_ATOMIC_WITHOUT_RET_sum` | Total number of vL1D atomic requests without return, over all TCP instances. |
| `TCP_TOTAL_CACHE_ACCESSES_sum` | Total number of vL1D cache accesses (including hits and misses) by all TCP instances. |
| `TCP_TOTAL_WRITEBACK_INVALIDATES_sum` | Total number of vL1D writebacks and invalidates, over all TCP instances. |
| `TCP_UTCL1_PERMISSION_MISS_sum` | Total number of UTCL1 permission misses by all TCP instances. |
| `TCP_UTCL1_REQUEST_sum` | Total number of address translation requests to UTCL1 by all TCP instances. |
| `TCP_UTCL1_TRANSLATION_MISS_sum` | Total number of UTCL1 translation misses by all TCP instances. |
| `TCP_UTCL1_TRANSLATION_HIT_sum` | Total number of UTCL1 translation hits by all TCP instances. |
| `TCP_VOLATILE_sum` | Total number of L1 volatile pixels/buffers from TA, over all TCP instances. |
| `TCP_WRITE_TAGCONFLICT_STALL_CYCLES_sum` | Total number of cycles tagram conflict stalls on a write, over all TCP instances. |
| `TD_ATOMIC_WAVEFRONT_sum` | Total number of atomic wavefront instructions, over all TD instances. |
| `TD_COALESCABLE_WAVEFRONT_sum` | Total number of coalescable wavefronts according to TA, over all TD instances. |
| `TD_LOAD_WAVEFRONT_sum` | Total number of wavefront instructions (read/write/atomic), over all TD instances. |
| `TD_SPI_STALL_sum` | Total number of cycles TD is stalled by SPI, over all TD instances. |
| `TD_STORE_WAVEFRONT_sum` | Total number of write wavefront instructions, over all TD instances. |
| `TD_TC_STALL_sum` | Total number of cycles TD is stalled waiting for TC data, over all TD instances. |
| `TD_TD_BUSY_sum` | Total number of TD busy cycles while it is processing or waiting for data, over all TD instances. |
| `VALUBusy`         | Percentage of GPU time vector ALU instructions are processed. Value range: 0% (bad) to 100% (optimal). |
| `VALUInsts` | Average number of vector ALU instructions executed per work item (affected by flow control). |
| `VALUUtilization`  | Percentage of active vector ALU threads in a wave. A lower number can mean either more thread divergence in a wave or that the work-group size is not a multiple of 64. Value range: 0% (bad), 100% (ideal - no thread divergence). |
| `VFetchInsts`      | Average number of vector fetch instructions from the video memory executed per work-item (affected by flow control). Excludes FLAT instructions that fetch from video memory.               |
| `VWriteInsts`      | Average number of vector write instructions to the video memory executed per work-item (affected by flow control). Excludes FLAT instructions that write to video memory.                 |
| `Wavefronts` | Total wavefronts. |
| `WRITE_REQ_32B` | Total number of 32-byte effective memory writes. |
| `WriteSize` | Total kilobytes written to the video memory. This is measured with all extra fetches and any cache or memory effects taken into account. |
| `WriteUnitStalled` | Percentage of GPU time the write unit is stalled. Value range: 0% to 100% (bad).      |

## Abbreviations

| Abbreviation | Meaning                                                                           |
|:------------|:--------------------------------------------------------------------------------|
| `ALU`          | Arithmetic Logic Unit                                                             |
| `Arb`          | Arbiter                                                                           |
| `BF16`         | Brain Floating Point - 16 bits                                                    |
| `CC`           | Coherently Cached                                                                 |
| `CP`           | Command Processor                                                                 |
| `CPC`          | Command Processor - Compute                                                       |
| `CPF`          | Command Processor - Fetcher                                                       |
| `CS`           | Compute Shader                                                                    |
| `CSC`          | Compute Shader Controller                                                         |
| `CSn`          | Compute Shader, the n-th pipe                                                     |
| `CU`           | Compute Unit                                                                      |
| `DW`           | 32-bit Data Word, DWORD                                                           |
| `EA`           | Efficiency Arbiter                                                                |
| `F16`          | Half Precision Floating Point                                                     |
| `F32`          | Full Precision Floating Point                                                     |
| `FLAT`         | FLAT instructions allow read/write/atomic access to a generic memory address pointer, which can resolve to any of the following physical memories:<br>.   Global Memory<br>.   Scratch ("private")<br>.   LDS ("shared")<br>.   Invalid - MEM_VIOL TrapStatus |
| `FMA`          | Fused Multiply Add                                                                |
| `GDS`          | Global Data Share                                                                 |
| `GRBM`         | Graphics Register Bus Manager                                                     |
| `HBM`          | High Bandwidth Memory                                                             |
| `Instr`        | Instructions                                                                      |
| `IOP`          | Integer Operation                                                                 |
| `L2`           | Level-2 Cache                                                                     |
| `LDS`          | Local Data Share                                                                  |
| `ME1`          | Micro Engine, running packet processing firmware on CPC                           |
| `MFMA`         | Matrix Fused Multiply Add                                                         |
| `NC`           | Noncoherently Cached                                                              |
| `RW`           | Coherently Cached with Write                                                      |
| `SALU`         | Scalar ALU                                                                        |
| `SGPR`         | Scalar General Purpose Register                                                   |
| `SIMD`         | Single Instruction Multiple Data                                                  |
| `sL1D`         | Scalar Level-1 Data Cache                                                         |
| `SMEM`         | Scalar Memory                                                                     |
| `SPI`          | Shader Processor Input                                                            |
| `SQ`           | Sequencer                                                                         |
| `TA`           | Texture Addressing Unit                                                           |
| `TC`           | Texture Cache                                                                     |
| `TCA`          | Texture Cache Arbiter                                                             |
| `TCC`          | Texture Cache per Channel, known as L2 Cache                                      |
| `TCIU`         | Texture Cache Interface Unit (interface between CP and the memory system) |
| `TCP`          | Texture Cache per Pipe, known as vector L1 Cache                                  |
| `TCR`          | Texture Cache Router                                                              |
| `TD`           | Texture Data Unit                                                                 |
| `UC`           | Uncached                                                                          |
| `UTCL1`        | Unified Translation Cache - Level 1                                               |
| `UTCL2`        | Unified Translation Cache - Level 2                                               |
| `VALU`         | Vector ALU                                                                        |
| `VGPR`         | Vector General Purpose Register                                                   |
| `vL1D`         | Vector Level -1 Data Cache                                                        |
| `VMEM`         | Vector Memory                                                                     |
