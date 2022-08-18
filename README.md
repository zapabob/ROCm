# ROCm™ v5.2.3
This repository contains the manifest file for ROCm™ releases, changelogs and release information. The file default.xml contains information all the repositories and the associated commit use to build the current ROCm release. The default.xml file uses the repo Manifest format.

# Release Notes
The ROCm v5.2.3 patch release is now available. The details are listed below. Highlights of this release include a bump in RCCL version compatibility and minor bug fixes in the HIP Runtime. Additionally, ROCm releases will return to use of the 
[ROCm](https://github.com/RadeonOpenCompute/ROCm) repository for version controlled release notes henceforth. This 
release of ROCm is validated with the AMDGPU release 22.20.1.

All users of the ROCm v5.2.1 release and below are encouraged to upgrade. Refer to https://docs.amd.com for all documentation associated with this release. 


## All Components
### Ubuntu 18.04 End of Life Announcement
ROCm v5.2.3 is the last release to support Ubuntu 18.04. Future releases of ROCm will not provide prebuilt packages for Ubuntu 18.04. 

## HIP and Other Runtimes

### HIP Runtime

#### Fixes
 - Fixed a bug discovered in the HIP graph capture implementation in the ROCm v5.2.0 release. If the same kernel is called twice
 (with different argument values) in a graph capture, the implementation was only keeping the argument values for 
 the second kernel call.
 - Fixed a bug introduced in the hiprtc implementation in the ROCm v5.2.0 release. This bug caused the *hiprtcGetLoweredName* call failed
 for named expressions with a whitespace in it. 

    **Example:** The named expression ```my_sqrt<complex<double>>``` passed but ```my_sqrt<complex< double>>``` failed. 

## ROCm Libraries

### RCCL

#### Added
- Compatibility with NCCL 2.12.10
- Packages for test and benchmark executables on all supported OSes using CPack.
- Adding custom signal handler - opt-in with RCCL_ENABLE_SIGNALHANDLER=1
  - Additional details provided if Binary File Descriptor library (BFD) is pre-installed
- Adding experimental support for using multiple ranks per device
  - Requires using a new interface to create communicator (ncclCommInitRankMulti), please
    refer to the interface documentation for details.
  - To avoid potential deadlocks, user might have to set an environment variables increasing
    the number of hardware queues (e.g. export GPU_MAX_HW_QUEUES=16)
- Adding support for reusing ports in NET/IB channels
  - Opt-in with NCCL_IB_SOCK_CLIENT_PORT_REUSE=1 and NCCL_IB_SOCK_SERVER_PORT_REUSE=1
  - When "Call to bind failed : Address already in use" error happens in large-scale AlltoAll
    (e.g., >=64 MI200 nodes), users are suggested to opt-in either one or both of the options
    to resolve the massive port usage issue
  - Avoid using NCCL_IB_SOCK_SERVER_PORT_REUSE when NCCL_NCHANNELS_PER_NET_PEER is tuned >1
#### Removed
- Removed experimental clique-based kernels

## Development Tools
No notable changes in this release for our development tools including the compiler, profiler and debugger.

## Deployment and Management Tools
No notable changes in this release for our deployment and management tools.

# Older ROCm™ Releases
For release information for older ROCm™ releases, please visit the [CHANGELOG](CHANGELOG.md).

