# Management Tools

:::::{grid} 1 1 3 3
:gutter: 1

:::{grid-item-card} [AMD SMI](https://rocmdocs.amd.com/projects/amdsmi/en/latest/)
GO AMD SMI provides GO binding for [E-SMI In-Band C library](https://github.com/amd/esmi_ib_library.git),
[ROCm SMI Library](https://github.com/RadeonOpenCompute/rocm_smi_lib.git), and any
GO language application that needs to link with these libraries and call the APIs
from the GO application. The GO binding are imported in the
[AMD SMI Exporter](https://github.com/amd/amd_smi_exporter.git) to export information
provided by the AMD E-SMI inband library and the ROCm SMI GPU library to the Prometheus server.

- [Documentation](https://rocmdocs.amd.com/projects/amdsmi/en/latest/)
- [Examples](https://github.com/amd/go_amd_smi#example)

:::

:::{grid-item-card} [ROCm SMI](https://rocmdocs.amd.com/projects/rocmsmi/en/latest/)
This tool acts as a command line interface for manipulating and monitoring the amdgpu kernel, and is intended to replace and deprecate the existing rocm_smi.py CLI tool. It uses Ctypes to call the rocm_smi_lib API.

- [Documentation](https://rocmdocs.amd.com/projects/rocmsmi/en/latest/)
- [Examples](https://github.com/RadeonOpenCompute/rocm_smi_lib/tree/master/python_smi_tools)

:::

:::{grid-item-card} [ROCm Datacenter Tool](https://rocmdocs.amd.com/projects/rdc/en/latest/)
The ROCm™ Data Center Tool simplifies the administration and addresses key infrastructure challenges in AMD GPUs in cluster and datacenter environments.

- [Documentation](https://rocmdocs.amd.com/projects/rdc/en/latest/)
- [Examples](https://github.com/RadeonOpenCompute/rdc/tree/master/example)

:::

:::::
