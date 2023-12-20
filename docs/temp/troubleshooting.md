# Troubleshooting

**Q: What do I do if I get this error when trying to run PyTorch:**

```bash
hipErrorNoBinaryForGPU: Unable to find code object for all current devices!
```

Ans: The error denotes that the installation of PyTorch and/or other
dependencies or libraries do not support the current GPU.

**Workaround:**

To implement a workaround, follow these steps:

1. Confirm that the hardware supports the ROCm stack. Refer to
{ref}`linux-support` and {ref}`windows-support`.

2. Determine the gfx target.

    ```bash
    rocminfo | grep gfx
    ```

3. Check if PyTorch is compiled with the correct gfx target.

    ```bash
    TORCHDIR=$( dirname $( python3 -c 'import torch; print(torch.__file__)' ) )
    roc-obj-ls -v $TORCHDIR/lib/libtorch_hip.so # check for gfx target
    ```

:::{note}
    Recompile PyTorch with the right gfx target if compiling from the source if
    the hardware is not supported. For wheels or Docker installation, contact
    ROCm support [^ROCm_issues].
:::

**Q: Why am I unable to access Docker or GPU in user accounts?**

Ans: Ensure that the user is added to docker, video, and render Linux groups as
described in the ROCm Installation Guide at {ref}`linux_group_permissions`.

**Q: Can I install PyTorch directly on bare metal?**

Ans: Bare-metal installation of PyTorch is supported through wheels. Refer to
Option 2: Install PyTorch Using Wheels Package. See {doc}`PyTorch for ROCm<rocm-install-on-linux:pytorch-install>` for more information.

**Q: How do I profile PyTorch workloads?**

Ans: Use the PyTorch Profiler to profile GPU kernels on ROCm.
