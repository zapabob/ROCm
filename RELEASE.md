# Release notes
<!-- Disable lints since this is an auto-generated file.    -->
<!-- markdownlint-disable blanks-around-headers             -->
<!-- markdownlint-disable no-duplicate-header               -->
<!-- markdownlint-disable no-blanks-blockquote              -->
<!-- markdownlint-disable ul-indent                         -->
<!-- markdownlint-disable no-trailing-spaces                -->

<!-- spellcheck-disable -->

This page contains the release notes for AMD ROCm Software.

-------------------

## ROCm 6.0.1


### Library changes in ROCM 6.0.1

| Library | Version |
|---------|---------|
| AMDMIGraphX | [2.8](https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-6.0.1) |
| hipBLAS | [2.0.0](https://github.com/ROCm/hipBLAS/releases/tag/rocm-6.0.1) |
| hipCUB | [3.0.0](https://github.com/ROCm/hipCUB/releases/tag/rocm-6.0.1) |
| hipFFT | [1.0.13](https://github.com/ROCm/hipFFT/releases/tag/rocm-6.0.1) |
| hipRAND | [2.10.17](https://github.com/ROCm/hipRAND/releases/tag/rocm-6.0.1) |
| hipSOLVER | [2.0.0](https://github.com/ROCm/hipSOLVER/releases/tag/rocm-6.0.1) |
| hipSPARSE | [3.0.0](https://github.com/ROCm/hipSPARSE/releases/tag/rocm-6.0.1) |
| hipSPARSELt |  ⇒ [0.1.0](https://github.com/ROCm/hipSPARSELt/releases/tag/rocm-6.0.1) |
| hipTensor | [1.1.0](https://github.com/ROCm/hipTensor/releases/tag/rocm-6.0.1) |
| MIOpen | [2.19.0](https://github.com/ROCm/MIOpen/releases/tag/rocm-6.0.1) |
| rccl | [2.15.5](https://github.com/ROCm/rccl/releases/tag/rocm-6.0.1) |
| rocALUTION | [3.0.3](https://github.com/ROCm/rocALUTION/releases/tag/rocm-6.0.1) |
| rocBLAS | [4.0.0](https://github.com/ROCm/rocBLAS/releases/tag/rocm-6.0.1) |
| rocFFT | [1.0.25](https://github.com/ROCm/rocFFT/releases/tag/rocm-6.0.1) |
| rocm-cmake | [0.11.0](https://github.com/ROCm/rocm-cmake/releases/tag/rocm-6.0.1) |
| rocPRIM | [3.0.0](https://github.com/ROCm/rocPRIM/releases/tag/rocm-6.0.1) |
| rocRAND | [2.10.17](https://github.com/ROCm/rocRAND/releases/tag/rocm-6.0.1) |
| rocSOLVER | [3.24.0](https://github.com/ROCm/rocSOLVER/releases/tag/rocm-6.0.1) |
| rocSPARSE | [3.0.2](https://github.com/ROCm/rocSPARSE/releases/tag/rocm-6.0.1) |
| rocThrust | [3.0.0](https://github.com/ROCm/rocThrust/releases/tag/rocm-6.0.1) |
| rocWMMA | [1.3.0](https://github.com/ROCm/rocWMMA/releases/tag/rocm-6.0.1) |
| Tensile | [4.39.0](https://github.com/ROCm/Tensile/releases/tag/rocm-6.0.1) |

#### hipSPARSELt 0.1.0

hipSPARSELt 0.1.0 for ROCm 6.0.1

##### Added

- Enable hipSPARSELt APIs
- Support platform: gfx940, gfx941, gfx942 
- Support problem type: fp16, bf16, int8
- Support activation: relu, gelu, abs, sigmod, tanh
- Support gelu scaling
- Support bias vector
- Support batched computation (single sparse x multiple dense, multiple sparse x single dense)
- Support cuSPARSELt v0.4 backend
- Integreate with tensilelite kernel generator
- Add Gtest: hipsparselt-test
- Add benchmarking tool: hipsparselt-bench
- Add sample app: example_spmm_strided_batched, example_prune, example_compress
