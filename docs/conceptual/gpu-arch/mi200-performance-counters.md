# MI200 performance counters and metrics
<!-- markdownlint-disable no-duplicate-header -->

This document lists and describes the hardware performance counters and the derived metrics available on the AMD Instinct™ MI200 GPU. All hardware performance monitors, and the derived performance metrics are accessible via AMD ROCm™ Profiler tool.

## MI200 performance counters list

```{note}
Preliminary validation of all MI200 performance counters is in progress. Those with “[*]” appended to the names require further evaluation.
```

### Graphics register bus management (GRBM)

#### GRBM counters

| Hardware Counter   | Unit   | Definition |
|--------------------|--------| ------------------------------------------------------|
| `grbm_count`       | Cycles | Free-running GPU clock |
| `grbm_gui_active`  | Cycles | GPU active cycles |
| `grbm_cp_busy`     | Cycles | Any of the command processor (CPC/CPF) blocks are busy. |
| `grbm_spi_busy`    | Cycles | Any of the shader processor input (SPI) are busy in the shader engine(s). |
| `grbm_ta_busy`     | Cycles | Any of the texture addressing unit are busy in the shader engine(s). |
| `grbm_tc_busy`     | Cycles | Any of the texture cache blocks (TCP/TCI/TCA/TCC) are busy. |
| `grbm_cpc_busy`    | Cycles | The command processor - compute (CPC) is busy. |
| `grbm_cpf_busy`    | Cycles | The command processor - fetcher (CPF) is busy. |
| `grbm_utcl2_busy`  | Cycles | The unified translation cache - level 2 (UTCL2) block is busy. |
| `grbm_ea_busy`     | Cycles | The efficiency arbiter (EA) block is busy. |

### Command processor

The command processor counters are further classified into fetcher and compute.

#### Command processor - fetcher (CPF)

##### CPF counters

| Hardware Counter                     | Unit   | Definition                                                   |
|--------------------------------------|--------|--------------------------------------------------------------|
| `cpf_cmp_utcl1_stall_on_translation` | Cycles | One of the compute UTCL1s is stalled waiting on translation. |
| `cpf_cpf_stat_idle[∗]`               | Cycles | CPF idle                                                   |
| `cpf_cpf_stat_stall`                 | Cycles | CPF stall                                                  |
| `cpf_cpf_tciu_busy`                  | Cycles | CPF TCIU interface busy                                    |
| `cpf_cpf_tciu_idle`                  | Cycles | CPF TCIU interface idle                                    |
| `cpf_cpf_tciu_stall[∗]`              | Cycles | CPF TCIU interface is stalled waiting on free tags.        |

#### Command processor - compute (CPC)

##### CPC counters

| Hardware Counter                 | Unit   | Definition                                          |
| ---------------------------------| -------| --------------------------------------------------- |
| `cpc_me1_busy_for_packet_decode` | Cycles | CPC ME1 busy decoding packets                       |
| `cpc_utcl1_stall_on_translation` | Cycles | One of the UTCL1s is stalled waiting on translation |
| `cpc_cpc_stat_busy`              | Cycles | CPC busy                                            |
| `cpc_cpc_stat_idle`              | Cycles | CPC idle                                            |
| `cpc_cpc_stat_stall`             | Cycles | CPC stalled                                         |
| `cpc_cpc_tciu_busy`              | Cycles | CPC TCIU interface busy                             |
| `cpc_cpc_tciu_idle`              | Cycles | CPC TCIU interface idle                             |
| `cpc_cpc_utcl2iu_busy`           | Cycles | CPC UTCL2 interface busy                            |
| `cpc_cpc_utcl2iu_idle`           | Cycles | CPC UTCL2 interface idle                            |
| `cpc_cpc_utcl2iu_stall[∗]`       | Cycles | CPC UTCL2 interface stalled waiting                 |
| `cpc_me1_dci0_spi_busy`          | Cycles | CPC ME1 Processor busy                              |

### Shader processor input (SPI)

#### SPI counters

| Hardware Counter             | Unit        | Definition                                                   |
| :----------------------------| :-----------| -----------------------------------------------------------: |
| `spi_csn_busy`                 | Cycles      | Number of clocks with outstanding waves                      |
| `spi_csn_window_valid`         | Cycles      | Clock count enabled by perfcounter_start event               |
| `spi_csn_num_threadgroups`     | Workgroups  | Total number of dispatched workgroups                        |
| `spi_csn_wave`                 | Wavefronts  | Total number of dispatched wavefronts                        |
| `spi_ra_req_no_alloc`          | Cycles      | Arb cycles with requests but no allocation (need to multiply this value by 4) |
|`spi_ra_req_no_alloc_csn`       | Cycles      | Arb cycles with CSn req and no CSn alloc (need to multiply this value by 4) |
| `spi_ra_res_stall_csn`         | Cycles      | Arb cycles with CSn req and no CSn fits (need to multiply this value by 4) |
| `spi_ra_tmp_stall_csn[∗]`      | Cycles      | Cycles where CSn wants to req but does not fit in temp space |
| `spi_ra_wave_simd_full_csn`    | SIMD-cycles | Sum of SIMD where WAVE cannot take csn wave when not fits    |
| `spi_ra_vgpr_simd_full_csn[∗]` | SIMD-cycles | Sum of SIMD where VGPR cannot take csn wave when not fits    |
| `spi_ra_sgpr_simd_full_csn[∗]` | SIMD-cycles | Sum of SIMD where SGPR cannot take csn wave when not fits    |
| `spi_ra_lds_cu_full_csn`       | CUs         | Sum of CU where LDS cannot take csn wave when not fits       |
| `spi_ra_bar_cu_full_csn[∗]`    | CUs         | Sum of CU where BARRIER cannot take csn wave when not fits   |
| `spi_ra_bulky_cu_full_csn[∗]`  | CUs         | Sum of CU where BULKY cannot take csn wave when not fits     |
| `spi_ra_tglim_cu_full_csn[∗]`  | Cycles      | Cycles where csn wants to req but all CUs are at tg_limit    |
| `spi_ra_wvlim_cu_full_csn[∗]`  | Cycles      | Number of clocks csn is stalled due to WAVE LIMIT            |
| `spi_vwc_csc_wr`               | Cycles      | Number of clocks to write CSC waves to VGPRs (need to multiply this value by 4) |
| `spi_swc_csc_wr`               | Cycles      | Number of clocks to write CSC waves to SGPRs (need to multiply this value by 4) |

### Compute unit

The compute unit counters are further classified into instruction mix, MFMA operation counters, level counters, wavefront counters, wavefront cycle counters, local data share counters, and others.

#### Instruction mix

| Hardware Counter        | Unit   | Definition                                                               |
| :-----------------------| :-----:| -----------------------------------------------------------------------: |
| `sq_insts`                | Instr | Number of instructions issued                                             |
| `sq_insts_valu`           | Instr | Number of VALU instructions issued, including MFMA                        |
| `sq_insts_valu_add_f16`   | Instr | Number of VALU F16 Add instructions issued                                |
| `sq_insts_valu_mul_f16`   | Instr | Number of VALU F16 Multiply instructions issued                           |
| `sq_insts_valu_fma_f16`   | Instr | Number of VALU F16 FMA instructions issued                                |
| `sq_insts_valu_trans_f16` | Instr | Number of VALU F16 Transcendental instructions issued                     |
| `sq_insts_valu_add_f32`   | Instr | Number of VALU F32 Add instructions issued                                |
| `sq_insts_valu_mul_f32`   | Instr | Number of VALU F32 Multiply instructions issued                           |
| `sq_insts_valu_fma_f32`   | Instr | Number of VALU F32 FMA instructions issued                                |
| `sq_insts_valu_trans_f32` | Instr | Number of VALU F32 Transcendental instructions issued                     |
| `sq_insts_valu_add_f64`   | Instr | Number of VALU F64 Add instructions issued                                |
| `sq_insts_valu_mul_f64`   | Instr | Number of VALU F64 Multiply instructions issued                           |
| `sq_insts_valu_fma_f64`   | Instr | Number of VALU F64 FMA instructions issued                                |
| `sq_insts_valu_trans_f64` | Instr | Number of VALU F64 Transcendental instructions issued                     |
| `sq_insts_valu_int32`     | Instr | Number of VALU 32-bit integer instructions issued (signed or unsigned)    |
| `sq_insts_valu_int64`     | Instr | Number of VALU 64-bit integer instructions issued (signed or unsigned)    |
| `sq_insts_valu_cvt`       | Instr | Number of VALU Conversion instructions issued                             |
| `sq_insts_valu_mfma_i8`   | Instr | Number of 8-bit Integer MFMA instructions issued                          |
| `sq_insts_valu_mfma_f16`  | Instr | Number of F16 MFMA instructions issued                                    |
| `sq_insts_valu_mfma_bf16` | Instr | Number of BF16 MFMA instructions issued                                   |
| `sq_insts_valu_mfma_f32`  | Instr | Number of F32 MFMA instructions issued                                    |
| `sq_insts_valu_mfma_f64`  | Instr | Number of F64 MFMA instructions issued                                    |
| `sq_insts_mfma`           | Instr | Number of MFMA instructions issued                                        |
| `sq_insts_vmem_wr`        | Instr | Number of VMEM write instructions issued                                  |
| `sq_insts_vmem_rd`        | Instr | Number of VMEM read instructions issued                                   |
| `sq_insts_vmem`           | Instr | Number of VMEM instructions issued, including both FLAT and buffer instructions |
| `sq_insts_salu`           | Instr | Number of SALU instructions issued                                        |
| `sq_insts_smem`           | Instr | Number of SMEM instructions issued                                        |
| `sq_insts_smem_norm`      | Instr | Number of SMEM instructions issued to normalize to match `smem_level`. Used in measuring SMEM latency |
| `sq_insts_flat`           | Instr | Number of FLAT instructions issued                                        |
| `sq_insts_flat_lds_only`  | Instr | Number of FLAT instructions issued that read/write only from/to LDS       |
| `sq_insts_lds`            | Instr | Number of LDS instructions issued                                         |
| `sq_insts_gds`            | Instr | Number of GDS instructions issued                                         |
| `sq_insts_exp_gds`        | Instr | Number of EXP and GDS instructions excluding skipped export instructions issued |
| `sq_insts_branch`         | Instr | Number of Branch instructions issued                                      |
| `sq_insts_sendmsg`        | Instr | Number of SENDMSG instructions including s_endpgm issued                  |
| `sq_insts_vskipped[∗]`    | Instr | Number of VSkipped instructions issued                                    |

#### MFMA operation counters

| Hardware Counter             | Unit  | Definition                                      |
| :----------------------------| :-----| ----------------------------------------------: |
| `sq_insts_valu_mfma_mops_I8`   | IOP   | Number of 8-bit integer MFMA ops in unit of 512 |
| `sq_insts_valu_mfma_mops_F16`  | FLOP  | Number of F16 floating MFMA ops in unit of 512  |
| `sq_insts_valu_mfma_mops_BF16` | FLOP  | Number of BF16 floating MFMA ops in unit of 512 |
| `sq_insts_valu_mfma_mops_F32`  | FLOP  | Number of F32 floating MFMA ops in unit of 512  |
| `sq_insts_valu_mfma_mops_F64`  | FLOP  | Number of F64 floating MFMA ops in unit of 512  |

#### Level counters

| Hardware Counter    | Unit  | Definition                             |
| :-------------------| :-----| -------------------------------------: |
| `sq_accum_prev`       | Count | Accumulated counter sample value where accumulation takes place once every  four cycles |
| `sq_accum_prev_hires` | Count | Accumulated counter sample value where accumulation takes place once every cycle |
| `sq_level_waves`      | Waves | Number of inflight waves               |
| `sq_insts_level_vmem` | Instr | Number of inflight VMEM instructions   |
| `sq_insts_level_smem` | Instr | Number of inflight SMEM instructions   |
| `sq_insts_level_lds`  | Instr | Number of inflight LDS instructions    |
| `sq_ifetch_level`     | Instr | Number of inflight instruction fetches |

#### Wavefront counters

| Hardware Counter     | Unit  | Definition                                                        |
| :--------------------| :-----| ----------------------------------------------------------------: |
| `sq_waves`             | Waves | Number of wavefronts dispatch to SQs, including both new and restored wavefronts |
| `sq_waves_saved[∗]`    | Waves | Number of context-saved wavefronts                                |
| `sq_waves_restored[∗]` | Waves | Number of context-restored wavefronts                             |
| `sq_waves_eq_64`       | Waves | Number of wavefronts with exactly 64 active threads sent to SQs   |
| `sq_waves_lt_64`       | Waves | Number of wavefronts with less than 64 active threads sent to SQs |
| `sq_waves_lt_48`       | Waves | Number of wavefronts with less than 48 active threads sent to SQs |
| `sq_waves_lt_32`       | Waves | Number of wavefronts with less than 32 active threads sent to SQs |
| `sq_waves_lt_16`       | Waves | Number of wavefronts with less than 16 active threads sent to SQs |

#### Wavefront cycle counters

| Hardware Counter         | Unit    | Definition                                                            |
| :------------------------| :-------| --------------------------------------------------------------------: |
| `sq_cycles`                | Cycles  | Free-running  SQ clocks                                               |
| `sq_busy_cycles`           | Cycles  | Number of cycles while SQ reports it to be busy                       |
| `sq_busy_cu_cycles`        | Qcycles | Number of quad cycles each CU is busy                                 |
| `sq_valu_mfma_busy_cycles` | Cycles  | Number of cycles the MFMA ALU is busy                                 |
| `sq_wave_cycles`           | Qcycles | Number of quad cycles spent by waves in the CUs                       |
| `sq_wait_any`              | Qcycles | Number of quad cycles spent waiting for anything                      |
| `sq_wait_inst_any`         | Qcycles | Number of quad cycles spent waiting for an issued instruction         |
| `sq_active_inst_any`       | Qcycles | Number of quad cycles spent by each wave to work on an instruction    |
| `sq_active_inst_vmem`      | Qcycles | Number of quad cycles spent by each wave to work on a non-FLAT VMEM instruction |
| `sq_active_inst_lds`       | Qcycles | Number of quad cycles spent by each wave to work on an LDS instruction |
| `sq_active_inst_valu`      | Qcycles | Number of quad cycles spent by each wave to work on a VALU instruction |
| `sq_active_inst_sca`       | Qcycles | Number of quad cycles spent by each wave to work on an SCA instruction |
| `sq_active_inst_exp_gds`   | Qcycles | Number of quad cycles spent by each wave to work on EXP or GDS instruction |
| `sq_active_inst_misc`      | Qcycles | Number of quad cycles spent by each wave to work on an MISC instruction, including branch and sendmsg |
| `sq_active_inst_flat`      | Qcycles | Number of quad cycles spent by each wave to work on a FLAT instruction |
| `sq_inst_cycles_vmem_wr`   | Qcycles | Number of quad cycles  spent to send addr and cmd data for VMEM write instructions, including both FLAT and buffer |
| `sq_inst_cycles_vmem_rd`   | Qcycles | Number of quad cycles  spent to send addr and cmd data for VMEM read instructions, including both FLAT and buffer |
| `sq_inst_cycles_smem`      | Qcycles | Number of quad cycles  spent to execute scalar memory reads           |
| `sq_inst_cycles_salu`      | Cycles  | Number of cycles spent to execute non-memory read scalar operations   |
| `sq_thread_cycles_valu`    | Cycles  | Number of thread cycles spent to execute VALU operations              |

#### Local data share

| Hardware Counter           | Unit   | Definition                                                |
| :--------------------------| :------| --------------------------------------------------------: |
| `sq_lds_atomic_return`       | Cycles | Number of atomic return cycles in LDS                     |
| `sq_lds_bank_conflict`       | Cycles | Number of cycles LDS is stalled by bank conflicts         |
| `sq_lds_addr_conflict[∗]`    | Cycles | Number of cycles LDS is stalled by address conflicts      |
| `sq_lds_unaligned_stalls[∗]` | Cycles | Number of cycles LDS is stalled processing flat unaligned load/store ops |
| `sq_lds_mem_violations[∗]`   | Count  | Number of threads that have a memory violation in the LDS |

#### Miscellaneous

##### Local data share

| Hardware Counter | Unit    | Definition                                                |
| :----------------| :-------| --------------------------------------------------------: |
| `sq_ifetch`        | Count   | Number of fetch requests from L1I cache, in 32-byte width |
| `sq_items`         | Threads | Number of valid threads                                   |

### L1I and sL1D caches

#### L1I and sL1D caches

| Hardware Counter             | Unit   | Definition                                                        |
| :----------------------------| :------| ----------------------------------------------------------------: |
| `sqc_icache_req`               | Req    | Number of L1I cache requests                                      |
| `sqc_icache_hits`              | Count  | Number of L1I cache lookup-hits                                   |
| `sqc_icache_misses`            | Count  | Number of L1I cache non-duplicate lookup-misses                   |
| `sqc_icache_misses_duplicate`  | Count  | Number of d L1I cache duplicate lookup misses  whose previous lookup miss on the same cache line is not fulfilled yet |
| `sqc_dcache_req`               | Req    | Number of sL1D cache requests                                       |
| `sqc_dcache_input_valid_readb` | Cycles | Number of cycles while SQ input is valid but sL1D cache is not ready |
| `sqc_dcache_hits`              | Count  | Number of sL1D cache lookup-hits                                  |
| `sqc_dcache_misses`            | Count  | Number of sL1D non-duplicate lookup-misses                        |
| `sqc_dcache_misses_duplicate`  | Count  | Number of sL1D duplicate lookup-misses                            |
| `sqc_dcache_req_read_1`        | Req    | Number of read requests in a single 32-bit data word, DWORD (DW)  |
| `sqc_dcache_req_read_2`        | Req    | Number of read requests in 2 DW                                   |
| `sqc_dcache_req_read_4`        | Req    | Number of read requests in 4 DW                                   |
| `sqc_dcache_req_read_8`        | Req    | Number of read requests in 8 DW                                   |
| `sqc_dcache_req_read_16`       | Req    | Number of read requests in 16 DW                                  |
| `sqc_dcache_atomic[∗]`         | Req    | Number of atomic requests                                         |
| `sqc_tc_req`                   | Req    | Number of L2 cache requests that were issued by instruction and constant caches |
| `sqc_tc_inst_req`              | Req    | Number of instruction cache line requests to L2 cache             |
| `sqc_tc_data_read_req`         | Req    | Number of data read requests to the L2 cache                      |
| `sqc_tc_data_write_req[∗]`     | Req    | Number of data write requests to the L2 cache                     |
| `sqc_tc_data_atomic_req[∗]`    | Req    | Number of data atomic requests to the L2 cache                    |
| `sqc_tc_stall[∗]`              | Cycles | Number of cycles while the valid requests to L2 cache are stalled |

### Vector L1 cache subsystem

The vector L1 cache subsystem counters are further classified into texture addressing unit, texture data unit, vector L1D cache, and texture cache arbiter.

#### Texture addressing unit

##### Texture addressing unit counters

| Hardware Counter                 | Unit   | Definition                                        |
| :--------------------------------| :------| ------------------------------------------------: |
| `ta_ta_busy`                       | Cycles | texture addressing unit busy cycles                                    |
| `ta_total_wavefronts`              | Instr  | Number of wavefront instructions                  |
| `ta_buffer_wavefronts`             | Instr  | Number of buffer wavefront instructions           |
| `ta_buffer_read_wavefronts`        | Instr  | Number of buffer read wavefront instructions      |
| `ta_buffer_write_wavefronts`       | Instr  | Number of buffer write wavefront instructions     |
| `ta_buffer_atomic_wavefronts[∗]`   | Instr  | Number of buffer atomic wavefront instructions    |
| `ta_buffer_total_cycles`           | Cycles | Number of buffer cycles, including read and write |
| `ta_buffer_coalesced_read_cycles`  | Cycles | Number of coalesced buffer read cycles            |
| `ta_buffer_coalesced_write_cycles` | Cycles | Number of coalesced buffer write cycles           |
| `ta_addr_stalled_by_tc`            | Cycles | Number of cycles texture addressing unit address is stalled by TCP     |
| `ta_data_stalled_by_tc`            | Cycles | Number of cycles texture addressing unit data is stalled by TCP        |
| `ta_addr_stalled_by_td_cycles[∗]`  | Cycles | Number of cycles texture addressing unit address is stalled by TD      |
| `ta_flat_wavefronts`               | Instr  | Number of flat wavefront instructions             |
| `ta_flat_read_wavefronts`          | Instr  | Number of flat read wavefront instructions        |
| `ta_flat_write_wavefronts`         | Instr  | Number of flat write wavefront instructions       |
| `ta_flat_atomic_wavefronts`        | Instr  | Number of flat atomic wavefront instructions      |

#### Texture data unit

##### Texture data unit counters

| Hardware Counter         | Unit  | Definition                                           |
| :------------------------| :-----| ---------------------------------------------------: |
| `td_td_busy`               | Cycle | TD busy cycles                                       |
| `td_tc_stall`              | Cycle | Number of cycles TD is stalled by TCP                |
| `td_spi_stall[∗]`          | Cycle | Number of cycles TD is stalled by SPI                |
| `td_load_wavefront`        | Instr | Number of wavefront instructions (read/write/atomic) |
| `td_store_wavefront`       | Instr | Number of write wavefront instructions               |
| `td_atomic_wavefront`      | Instr | Number of atomic wavefront instructions              |
| `td_coalescable_wavefront` | Instr | Number of coalescable instructions                   |

#### Vector L1D cache

| Hardware Counter                    | Unit   | Definition                                                  |
| :-----------------------------------| :------| ----------------------------------------------------------: |
| `tcp_gate_en1`                        | Cycles | Number of cycles/ vL1D interface clocks are turned on    |
| `tcp_gate_en2`                        | Cycles | Number of cycles vL1D core clocks are turned on           |
| `tcp_td_tcp_stall_cycles`             | Cycles | Number of cycles TD stalls vL1D                           |
| `tcp_tcr_tcp_stall_cycles`            | Cycles | Number of cycles TCR stalls vL1D                           |
| `tcp_read_tagconflict_stall_cycles`   | Cycles | Number of cycles tagram conflict stalls on a read          |
| `tcp_write_tagconflict_stall_cycles`  | Cycles | Number of cycles tagram conflict stalls on a write         |
| `tcp_atomic_tagconflict_stall_cycles` | Cycles | Number of cycles tagram conflict stalls on an atomic       |
| `tcp_pending_stall_cycles`            | Cycles | Number of cycles vL1D cache is stalled due to data pending from L2 cache |
| `tcp_ta_tcp_state_read`               | Req    | Number of wavefront instruction requests to vL1D           |
| `tcp_volatile[∗]`                     | Req    | Number of L1 volatile pixels/buffers from texture addressing unit               |
| `tcp_total_accesses`                  | Req    | Number of vL1D accesses                                    |
| `tcp_total_read`                      | Req    | Number of vL1D read accesses                               |
| `tcp_total_write`                     | Req    | Number of vL1D write accesses                              |
| `tcp_total_atomic_with_ret`           | Req    | Number of vL1D atomic with return                          |
| `tcp_total_atomic_without_ret`        | Req    | Number of vL1D atomic without return                       |
| `tcp_total_writeback_invalidates`     | Count  | Number of vL1D writebacks and Invalidates                  |
| `tcp_utcl1_request`                   | Req    | Number of address translation requests to UTCL1            |
| `tcp_utcl1_translation_hit`           | Req    | Number of UTCL1 translation hits                            |
| `tcp_utcl1_translation_miss`          | Req    | Number of UTCL1 translation misses                          |
| `tcp_utcl1_persmission_miss`          | Req    | Number of UTCL1 permission misses                           |
| `tcp_total_cache_accesses`            | Req    | Number of vL1D cache accesses                               |
| `tcp_tcp_latency`                     | Cycles | Accumulated wave access latency to vL1D over all wavefronts |
| `tcp_tcc_read_req_latency`            | Cycles | Accumulated vL1D-L2 request latency over all wavefronts for reads and atomics with return |
| `tcp_tcc_write_req_latency`           | Cycles | Accumulated vL1D-L2 request latency over all wavefronts for writes and atomics without return |
| `tcp_tcc_read_req`                    | Req    | Number of read requests to L2 cache                        |
| `tcp_tcc_write_req`                   | Req    | Number of write requests to L2 cache                       |
| `tcp_tcc_atomic_with_ret_req`         | Req    | Number of atomic requests to L2 cache with return          |
| `tcp_tcc_atomic_without_ret_req`      | Req    | Number of atomic requests to L2 cache without return       |
| `tcp_tcc_nc_read_req`                 | Req    | Number of NC read requests to L2 cache                     |
| `tcp_tcc_uc_read_req`                 | Req    | Number of UC read requests to L2 cache                     |
| `tcp_tcc_cc_read_req`                 | Req    | Number of CC read requests to L2 cache                     |
| `tcp_tcc_rw_read_req`                 | Req    | Number of RW read requests to L2 cache                     |
| `tcp_tcc_nc_write_req`                | Req    | Number of NC write requests to L2 cache                    |
| `tcp_tcc_uc_write_req`                | Req    | Number of UC write requests to L2 cache                    |
| `tcp_tcc_cc_write_req`                | Req    | Number of CC write requests to L2 cache                    |
| `tcp_tcc_rw_write_req`                | Req    | Number of RW write requests to L2 cache                    |
| `tcp_tcc_nc_atomic_req`               | Req    | Number of NC atomic requests to L2 cache                   |
| `tcp_tcc_uc_atomic_req`               | Req    | Number of UC atomic requests to L2 cache                   |
| `tcp_tcc_cc_atomic_req`               | Req    | Number of CC atomic requests to L2 cache                   |
| `tcp_tcc_rw_atomic_req`               | Req    | Number of RW atomic requests to L2 cache                   |

#### Texture cache arbiter (TCA)

| Hardware Counter | Unit   | Definition                                  |
| :----------------| :------| ------------------------------------------: |
| `tca_cycle`        | Cycles | TCA cycles                                  |
| `tca_busy`         | Cycles | Number of cycles  TCA has a pending request |

### L2 cache access

#### L2 cache access counters

| Hardware Counter                 | Unit   | Definition                                                     |
| :--------------------------------| :------| -------------------------------------------------------------: |
| `tcc_cycle`                        |Cycle   | L2 cache free-running clocks                                  |
| `tcc_busy`                         |Cycle   | L2 cache busy cycles                                          |
| `tcc_req`                          |Req     | Number of L2 cache requests                                   |
| `tcc_streaming_req[∗]`             |Req     | Number of L2 cache streaming requests                         |
| `tcc_NC_req`                       |Req     | Number of NC requests                                         |
| `tcc_UC_req`                       |Req     | Number of UC requests                                         |
| `tcc_CC_req`                       |Req     | Number of CC requests                                         |
| `tcc_RW_req`                       |Req     | Number of RW requests                                         |
| `tcc_probe`                        |Req     | Number of L2 cache probe requests                             |
| `tcc_probe_all[∗]`                 |Req     | Number of external probe requests with EA_TCC_preq_all== 1    |
| `tcc_read_req`                     |Req     | Number of L2 cache read requests                              |
| `tcc_write_req`                    |Req     | Number of L2 cache write requests                             |
| `tcc_atomic_req`                   |Req     | Number of L2 cache atomic requests                            |
| `tcc_hit`                          |Req     | Number of L2 cache lookup-hits                                |
| `tcc_miss`                         |Req     | Number of L2 cache lookup-misses                              |
| `tcc_writeback`                    |Req     | Number of lines written back to main memory, including writebacks of dirty lines and uncached write/atomic requests |
| `tcc_ea_wrreq`                     |Req     | Total number of 32-byte and 64-byte write requests to EA      |
| `tcc_ea_wrreq_64B`                 |Req     | Total number of 64-byte write requests to EA                  |
| `tcc_ea_wr_uncached_32B`           |Req     | Number of 32-byte write/atomic going over the TC_EA_wrreq interface due to uncached traffic. Note that CC mtypes can produce uncached requests, and those are included in this. A 64-byte request is counted as 2. |
| `tcc_ea_wrreq_stall`               | Cycles | Number of cycles a write request was stalled                  |
| `tcc_ea_wrreq_io_credit_stall[∗]`  | Cycles | Number of cycles an EA write request runs out of IO credits   |
| `tcc_ea_wrreq_gmi_credit_stall[∗]` | Cycles | Number of cycles an EA write request runs out of GMI credits  |
| `tcc_ea_wrreq_dram_credit_stall`   | Cycles | Number of cycles an EA write request runs out of DRAM credits |
| `tcc_too_many_ea_wrreqs_stall[∗]`  | Cycles | Number of cycles the L2 cache reaches maximum number of pending EA write requests |
| `tcc_ea_wrreq_level`               | Req    | Accumulated number of L2 cache-EA write requests in flight    |
| `tcc_ea_atomic`                    | Req    | Number of 32-byte and 64-byte atomic requests to EA           |
| `tcc_ea_atomic_level`              | Req    | Accumulated number of L2 cache-EA atomic requests in flight   |
| `tcc_ea_rdreq`                     | Req    | Total number of 32-byte and 64-byte read requests to EA       |
| `tcc_ea_rdreq_32B`                 | Req    | Total number of 32-byte read requests to EA                   |
| `tcc_ea_rd_uncached_32B`           | Req    | Number of 32-byte L2 cache-EA read due to uncached traffic. A 64-byte request is counted as 2. |
| `tcc_ea_rdreq_io_credit_stall[∗]`  | Cycles | Number of cycles read request interface runs out of IO credits  |
| `tcc_ea_rdreq_gmi_credit_stall[∗]` | Cycles | Number of cycles read request interface runs out of GMI credits |
| `tcc_ea_rdreq_dram_credit_stall`   | Cycles | Number of cycles read request interface runs out of DRAM credits |
| `tcc_ea_rdreq_level`               | Req    | Accumulated number of L2 cache-EA read requests in flight     |
| `tcc_ea_rdreq_dram`                | Req    | Number of 32-byte and 64-byte read requests to HBM            |
| `tcc_ea_wrreq_dram`                | Req    | Number of 32-byte and 64-byte write requests to HBM           |
| `tcc_tag_stall`                    | Cycles | Number of cycles the normal request pipeline in the tag was stalled for any reason |
| `tcc_normal_writeback`             | Req    | Number of L2 cache normal writeback                           |
| `tcc_all_tc_op_wb_writeback[∗]`    | Req    | Number of instruction-triggered writeback requests            |
| `tcc_normal_evict`                 | Req    | Number of L2 cache normal evictions                           |
| `tcc_all_tc_op_inv_evict[∗]`       | Req    | Number of instruction-triggered eviction requests             |

## MI200 derived metrics list

### Derived metrics on MI200 GPUs

| Derived Metric   | Description                                                                            |
| :----------------| -------------------------------------------------------------------------------------: |
| `VFetchInsts`      | The average number of vector fetch instructions from the video memory executed per work-item (affected by flow control). Excludes FLAT instructions that fetch from video memory               |
| `VWriteInsts`      | The average number of vector write instructions to the video memory executed per work-item (affected by flow control). Excludes FLAT instructions that write to video memory                 |
| `FlatVMemInsts`    | The average number of FLAT instructions that read from or write to the video memory executed per work item (affected by flow control). Includes FLAT instructions that read from or write to scratch |
| `LDSInsts`         | The average number of LDS read/write instructions executed per work item (affected by flow control). Excludes FLAT instructions that read from or write to LDS |
| `FlatLDSInsts`     | The average number of FLAT instructions that read or write to LDS executed per work item (affected by flow control) |
| `VALUUtilization`  | The percentage of active vector ALU threads in a wave. A lower number can mean either more thread divergence in a wave or that the work-group size is not a multiple of 64. Value range: 0% (bad), 100% (ideal - no thread divergence) |
| `VALUBusy`         | The percentage of GPU time vector ALU instructions are processed. Value range: 0% (bad) to 100% (optimal) |
| `SALUBusy`         | The percentage of GPU time scalar ALU instructions are processed. Value range: 0% (bad) to 100% (optimal) |
| `MemWrites32B`     | The total number of effective 32B write transactions to the memory                      |
| `L2CacheHit`       | The percentage of fetch, write, atomic, and other instructions that hit the data in L2 cache. Value range: 0% (no hit) to 100% (optimal) |
| `MemUnitStalled`   | The percentage of GPU time the memory unit is stalled. Try reducing the number or size of fetches and writes if possible. Value range: 0% (optimal) to 100% (bad) |
| `WriteUnitStalled` | The percentage of GPU time the write unit is stalled. Value range: 0% to 100% (bad)      |
| `LDSBankConflict`  | The percentage of GPU time LDS is stalled by bank conflicts. Value range: 0% (optimal) to 100% (bad) |

## Abbreviations

### MI200 abbreviations

| Abbreviation | Meaning                                                                           |
| :------------| --------------------------------------------------------------------------------: |
| `ALU`          | Arithmetic logic unit |
| `Arb`          | Arbiter |
| `BF16`        | Brain floating point – 16 |
| `CC`           | Coherently cached |
| `CP`           | Command processor |
| `CPC`         | Command processor – compute |
| `CPF`         | Command processor – fetcher |
| `CS`           | Compute shader |
| `CSC`         | Compute shader controller |
| `CSn`          | Compute Shader, the n-th pipe |
| `CU`           | Compute unit |
| `DW`           | 32-bit data word, DWORD |
| `EA`           | Efficiency arbiter |
| `F16`          | Half-precision floating point |
| `FLAT`       | FLAT instructions allow read/write/atomic access to a generic memory address pointer, which can resolve to any of the following physical memories:<br>•   Global Memory<br>•   Scratch (“private”)<br>•   LDS (“shared”)<br>•   Invalid – MEM_VIOL TrapStatus |
| `FMA`          | Fused multiply-add |
| `GDS`          | Global data share |
| `GRBM`         | Graphics register bus manager |
| `HBM`          | High bandwidth memory |
| `Instr`        | Instructions |
| `IOP`          | Integer operation |
| `L2`           | Level-2 cache |
| `LDS`          | Local data share |
| `ME1`          | Micro-engine, running packet processing firmware on CPC |
| `MFMA`         | Matrix fused multiply-add |
| `NC`           | Noncoherently cached |
| `RW`           | Coherently cached with write |
| `SALU`         | Scalar ALU |
| `SGPR`         | Scalar GPR |
| `SIMD`         | Single instruction multiple data |
| `sL1D`         | Scalar Level-1 data cache |
| `SMEM`         | Scalar memory |
| `SPI`          | Shader processor input |
| `SQ`           | Sequencer |
| `TA`           | Texture addressing unit |
| `TC`           | Texture cache |
| `TCA`          | Texture cache arbiter |
| `TCC`          | Texture cache per channel, known as L2 cache |
| `TCIU`         | Texture cache interface unit, command processor’s interface to memory system |
| `TCP`          | Texture cache per pipe, known as vector L1 cache |
| `TCR`          | Texture cache router |
| `TD`           | Texture data unit |
| `UC`           | Uncached |
| `UTCL1`        | Unified translation cache – level 1 |
| `UTCL2`        | Unified translation cache – level 2 |
| `VALU`         | Vector ALU |
| `VGPR`         | Vector GPR |
| `vL1D`         | Vector level 1 data cache |
| `VMEM`         | Vector memory |
