# ROCm™ Repository Updates
This repository contains the manifest file for ROCm™ releases, changelogs, and release information. The file default.xml contains information for all repositories and the associated commit used to build the current ROCm release.

The default.xml file uses the repo Manifest format.

# ROCm v5.4.1 Release Notes
ROCm v5.4.1 is now released. For ROCm v5.4.1 documentation, refer to https://docs.amd.com.

# ROCm v5.4 Release Notes
ROCm v5.4 is now released. For ROCm v5.4 documentation, refer to https://docs.amd.com.

# ROCm v5.3.3 Release Notes
ROCm v5.3.3 is now released. For ROCm v5.3.3 documentation, refer to https://docs.amd.com.

# ROCm v5.3.2 Release Notes
ROCm v5.3.2 is now released. For ROCm v5.3.2 documentation, refer to https://docs.amd.com.

# ROCm v5.3 Release Notes
ROCm v5.3 is now released. For ROCm v5.3 documentation, refer to https://docs.amd.com.

# ROCm v5.2.3 Release Notes
The ROCm v5.2.3 patch release is now available. The details are listed below. Highlights of this release include enhancements in RCCL version compatibility and minor bug fixes in the HIP Runtime.

Additionally, ROCm releases will return to use of the [ROCm](https://github.com/RadeonOpenCompute/ROCm) repository for version-controlled release notes henceforth.

**NOTE**: This release of ROCm is validated with the AMDGPU release v22.20.1.

All users of the ROCm v5.2.1 release and below are encouraged to upgrade. Refer to https://docs.amd.com for documentation associated with this release.


## Introducing Preview Support for Ubuntu 20.04.5 HWE

Refer to the following article for information on the preview support for Ubuntu 20.04.5 HWE.

https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-22-20


## Changes in This Release

### Ubuntu 18.04 End of Life

Support for Ubuntu 18.04 ends in this release. Future releases of ROCm will not provide prebuilt packages for Ubuntu 18.04.


### HIP and Other Runtimes

#### HIP Runtime

##### Fixes

 - A bug was discovered in the HIP graph capture implementation in the ROCm v5.2.0 release. If the same kernel is called twice (with different argument values) in a graph capture, the implementation only kept the argument values for the second kernel call.

- A bug was introduced in the hiprtc implementation in the ROCm v5.2.0 release. This bug caused the *hiprtcGetLoweredName* call to fail for named expressions with whitespace in it.

**Example:** The named expression ```my_sqrt<complex<double>>``` passed but ```my_sqrt<complex<double>>``` failed.


### ROCm Libraries

#### RCCL

##### Added
- Compatibility with NCCL 2.12.10
- Packages for test and benchmark executables on all supported OSes using CPack
- Adding custom signal handler - opt-in with RCCL_ENABLE_SIGNALHANDLER=1
  - Additional details provided if Binary File Descriptor library (BFD) is pre-installed.
  - Adding experimental support for using multiple ranks per device
    - Requires using a new interface to create communicator (ncclCommInitRankMulti),
        refer to the interface documentation for details.
	  - To avoid potential deadlocks, user might have to set an environment variables increasing
	      the number of hardware queues. For example,

```
    export GPU_MAX_HW_QUEUES=16

```
- Adding support for reusing ports in NET/IB channels
  - Opt-in with NCCL_IB_SOCK_CLIENT_PORT_REUSE=1 and NCCL_IB_SOCK_SERVER_PORT_REUSE=1
    - When "Call to bind failed: Address already in use" error happens in large-scale AlltoAll
        (for example, >=64 MI200 nodes), users are suggested to opt-in either one or both of the options to resolve the massive port usage issue
	  - Avoid using NCCL_IB_SOCK_SERVER_PORT_REUSE when NCCL_NCHANNELS_PER_NET_PEER is tuned >1

##### Removed
- Removed experimental clique-based kernels

### Development Tools
No notable changes in this release for development tools, including the compiler, profiler, and debugger.

### Deployment and Management Tools
No notable changes in this release for deployment and management tools.

## Older ROCm™ Releases
For release information for older ROCm™ releases, refer to [CHANGELOG](CHANGELOG.md).
