# Compiler Reference Guide

## Introduction to Compiler Reference Guide

ROCmCC is a Clang/LLVM-based compiler. It is optimized for high-performance
computing on AMD GPUs and CPUs and supports various heterogeneous programming
models such as HIP, OpenMP, and OpenCL.

ROCmCC is made available via two packages: `rocm-llvm` and `rocm-llvm-alt`.
The differences are listed in [the table below](rocm-llvm-vs-alt).

:::{table} Differences between `rocm-llvm` and `rocm-llvm-alt`
:name: rocm-llvm-vs-alt
| **`rocm-llvm`**                                     | **`rocm-llvm-alt`**                                                                                                             |
|:---------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| Installed by default when ROCm™ itself is installed | An optional package                                                                                                             |
| Provides an open-source compiler                    | Provides an additional closed-source compiler for users interested in additional CPU optimizations not available in `rocm-llvm` |
:::

For more details, see:

- AMD GPU usage: [llvm.org/docs/AMDGPUUsage.html](https://llvm.org/docs/AMDGPUUsage.html)
- Releases and source: <https://github.com/RadeonOpenCompute/llvm-project>

### ROCm Compiler Interfaces

ROCm currently provides two compiler interfaces for compiling HIP programs:

- `/opt/rocm/bin/hipcc`
- `/opt/rocm/bin/amdclang++`

Both leverage the same LLVM compiler technology with the AMD GCN GPU support;
however, they offer a slightly different user experience. The `hipcc` command-line
interface aims to provide a more familiar user interface to users who are
experienced in CUDA but relatively new to the ROCm/HIP development environment.
On the other hand, `amdclang++` provides a user interface identical to the clang++
compiler. It is more suitable for experienced developers who want to directly
interact with the clang compiler and gain full control of their application’s
build process.

The major differences between `hipcc` and `amdclang++` are listed below:

::::{table} Differences between `hipcc` and `amdclang++`
:name: hipcc-vs-amdclang
| *                                  | **`hipcc`**                                                                                                              | **`amdclang++`** |
|:----------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| Compiling HIP source files         | Treats all source files as HIP language source files                                                                     | Enables the HIP language support for files with the `.hip` extension or through the `-x hip` compiler option |
| Detecting GPU architecture         | Auto-detects the GPUs available on the system and generates code for those devices when no GPU architecture is specified | Has AMD GCN gfx803 as the default GPU architecture. The `--offload-arch` compiler option may be used to target other GPU architectures |
| Finding a HIP installation         | Finds the HIP installation based on its own location and its knowledge about the ROCm directory structure                | First looks for HIP under the same parent directory as its own LLVM directory and then falls back on `/opt/rocm`. Users can use the `--rocm-path` option to instruct the compiler to use HIP from the specified ROCm installation. |
| Linking to the HIP runtime library | Is configured to automatically link to the HIP runtime from the detected HIP installation                                | Requires the `--hip-link` flag to be specified to link to the HIP runtime. Alternatively, users can use the `-l<dir> -lamdhip64` option to link to a HIP runtime library. |
| Device function inlining           | Inlines all GPU device functions, which provide greater performance and compatibility for codes that contain file scoped or device function scoped `__shared__` variables. However, it may increase compile time. | Relies on inlining heuristics to control inlining. Users experiencing performance or compilation issues with code using file scoped or device function scoped `__shared__` variables could try `-mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false` to work around the issue. There are plans to address these issues with future compiler improvements. |
| Source code location               | <https://github.com/ROCm-Developer-Tools/HIPCC>                                                                          | <https://github.com/RadeonOpenCompute/llvm-project> |
::::

## Compiler Options and Features

This chapter discusses compiler options and features.

### AMD GPU Compilation

This section outlines commonly used compiler flags for `hipcc` and `amdclang++`.
:::{option} -x hip
  Compiles the source file as a HIP program.
:::

:::{option} -fopenmp
  Enables the OpenMP support.
:::

:::{option} -fopenmp-targets=<gpu>
  Enables the OpenMP target offload support of the specified GPU architecture.

  :gpu: The GPU architecture. E.g. gfx908.
:::

:::{option} --gpu-max-threads-per-block=<value>:
  Sets the default limit of threads per block. Also referred to as the launch bounds.

  :value: The default maximum amount of threads per block.
:::

:::{option} -munsafe-fp-atomics
  Enables unsafe floating point atomic instructions (AMDGPU only).
:::

:::{option} -ffast-math
  Allows aggressive, lossy floating-point optimizations.
:::

:::{option} -mwavefrontsize64, -mno-wavefrontsize64
  Sets wavefront size to be 64 or 32 on RDNA architectures.
:::

:::{option} -mcumode
  Switches between CU and WGP modes on RDNA architectures.
:::

:::{option} --offload-arch=<gpu>
  HIP offloading target ID. May be specified more than once.

  :gpu: The a device architecture followed by target ID features
    delimited by a colon. Each target ID feature is a predefined
    string followed by a plus or minus sign (e.g. `gfx908:xnack+:sramecc-`).
:::

:::{option} -g
  Generates source-level debug information.
:::

:::{option} -fgpu-rdc, -fno-gpu-rdc
  Generates relocatable device code, also known as separate compilation mode.
:::

### AMD Optimizations for Zen Architectures

The CPU compiler optimizations described in this chapter originate from the AMD
Optimizing C/C++ Compiler (AOCC) compiler. They are available in ROCmCC if the
optional `rocm-llvm-alt` package is installed. The user’s interaction with the
compiler does not change once `rocm-llvm-alt` is installed. The user should use
the same compiler entry point, provided AMD provides high-performance compiler
optimizations for Zen-based processors in AOCC.

For more information, refer to
[https://www.amd.com/en/developer/aocc.html](https://www.amd.com/en/developer/aocc.html).

#### `-famd-opt`

Enables a default set of AMD proprietary optimizations for the AMD Zen CPU
architectures.

`-fno-amd-opt` disables the AMD proprietary optimizations.

The `-famd-opt` flag is useful when a user wants to build with the proprietary
optimization compiler and not have to depend on setting any of the other
proprietary optimization flags.

:::{note}
`-famd-opt` can be used in addition to the other proprietary CPU optimization
flags. The table of optimizations below implicitly enables the invocation of the
AMD proprietary optimizations compiler, whereas the `-famd-opt` flag requires
this to be handled explicitly.
:::

#### `-fstruct-layout=[1,2,3,4,5,6,7]`

Analyzes the whole program to determine if the structures in the code can be
peeled and the pointer or integer fields in the structure can be compressed. If
feasible, this optimization transforms the code to enable these improvements.
This transformation is likely to improve cache utilization and memory bandwidth.
It is expected to improve the scalability of programs executed on multiple cores.

This is effective only under `-flto`, as the whole program analysis is required
to perform this optimization. Users can choose different levels of
aggressiveness with which this optimization can be applied to the application,
with 1 being the least aggressive and 7 being the most aggressive level.

:::{table} -fstruct-layout Values and Their Effects
| `-fstruct-layout` value | Structure peeling | Pointer size after selective compression of self-referential pointers in structures, wherever safe | Type of structure fields eligible for compression | Whether compression performed under safety check |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 1 | Enabled | NA | NA | NA |
| 2 | Enabled | 32-bit | NA | NA |
| 3 | Enabled | 16-bit | NA | NA |
| 4 | Enabled | 32-bit | Integer | Yes |
| 5 | Enabled | 16-bit | Integer | Yes |
| 6 | Enabled | 32-bit | 64-bit signed int or unsigned int. Users must ensure that the values assigned to 64-bit signed int fields are in range -(2^31 - 1) to +(2^31 - 1) and 64-bit unsigned int fields are in the range 0 to +(2^31 - 1). Otherwise, you may obtain incorrect results. | No. Users must ensure the safety based on the program compiled. |
| 7 | Enabled | 16-bit | 64-bit signed int or unsigned int. Users must ensure that the values assigned to 64-bit signed int fields are in range -(2^31 - 1) to +(2^31 - 1) and 64-bit unsigned int fields are in the range 0 to +(2^31 - 1). Otherwise, you may obtain incorrect results. | No. Users must ensure the safety based on the program compiled. |
:::

#### `-fitodcalls`

Promotes indirect-to-direct calls by placing conditional calls. Application or
benchmarks that have a small and deterministic set of target functions for
function pointers passed as call parameters benefit from this optimization.
Indirect-to-direct call promotion transforms the code to use all possible
determined targets under runtime checks and falls back to the original code for
all the other cases. Runtime checks are introduced by the compiler for each of
these possible function pointer targets followed by direct calls to the targets.

This is a link time optimization, which is invoked as `-flto -fitodcalls`

#### `-fitodcallsbyclone`

Performs value specialization for functions with function pointers passed as an
argument. It does this specialization by generating a clone of the function. The
cloning of the function happens in the call chain as needed, to allow conversion
of indirect function call to direct call.

This complements `-fitodcalls` optimization and is also a link time
optimization, which is invoked as `-flto -fitodcallsbyclone`.

#### `-fremap-arrays`

Transforms the data layout of a single dimensional array to provide better cache
locality. This optimization is effective only under `-flto`, as the whole program
needs to be analyzed to perform this optimization, which can be invoked as
`-flto -fremap-arrays`.

#### `-finline-aggressive`

Enables improved inlining capability through better heuristics. This
optimization is more effective when used with `-flto`, as the whole program
analysis is required to perform this optimization, which can be invoked as
`-flto -finline-aggressive`.

#### `-fnt-store (non-temporal store)`

Generates a non-temporal store instruction for array accesses in a loop with a
large trip count.

#### `-fnt-store=aggressive`

This is an experimental option to generate non-temporal store instruction for
array accesses in a loop, whose iteration count cannot be determined at compile
time. In this case, the compiler assumes the iteration count to be huge.

#### Optimizations Through Driver `-mllvm <options>`

The following optimization options must be invoked through driver
`-mllvm <options>`:

##### `-enable-partial-unswitch`

Enables partial loop unswitching, which is an enhancement to the existing loop
unswitching optimization in LLVM. Partial loop unswitching hoists a condition
inside a loop from a path for which the execution condition remains invariant,
whereas the original loop unswitching works for a condition that is completely
loop invariant. The condition inside the loop gets hoisted out from the
invariant path, and the original loop is retained for the path where the
condition is variant.

##### `-aggressive-loop-unswitch`

Experimental option that enables aggressive loop unswitching heuristic
(including `-enable-partial-unswitch`) based on the usage of the branch
conditional values. Loop unswitching leads to code bloat. Code bloat can be
minimized if the hoisted condition is executed more often. This heuristic
prioritizes the conditions based on the number of times they are used within the
loop. The heuristic can be controlled with the following options:

- `-unswitch-identical-branches-min-count=<n>`
  - Enables unswitching of a loop with respect to a branch conditional value
    (B), where B appears in at least `<n>` compares in the loop. This option is
    enabled with `-aggressive-loop-unswitch`. The default value is 3.

  **Usage:** `-mllvm -aggressive-loop-unswitch -mllvm -unswitch-identical-branches-min-count=<n>`

  Where, `n` is a positive integer and lower value of `<n>` facilitates more
  unswitching.
- `-unswitch-identical-branches-max-count=<n>`
  - Enables unswitching of a loop with respect to a branch conditional value
    (B), where B appears in at most `<n>` compares in the loop. This option is
    enabled with `-aggressive-loop-unswitch`. The default value is 6.

  **Usage:** `-mllvm -aggressive-loop-unswitch -mllvm -unswitch-identical-branches-max-count=<n>`

  Where, `n` is a positive integer and higher value of `<n>` facilitates more unswitching.

   :::{note}
   These options may facilitate more unswitching under some workloads. Since
   loop-unswitching inherently leads to code bloat, facilitating more
   unswitching may significantly increase the code size. Hence, it may also lead
   to longer compilation times.
   :::

##### `-enable-strided-vectorization`

Enables strided memory vectorization as an enhancement to the interleaved
vectorization framework present in LLVM. It enables the effective use of gather
and scatter kind of instruction patterns. This flag must be used along with the
interleave vectorization flag.

##### `-enable-epilog-vectorization`

Enables vectorization of epilog-iterations as an enhancement to existing
vectorization framework. This enables generation of an additional epilog vector
loop version for the remainder iterations of the original vector loop. The
vector size or factor of the original loop should be large enough to allow an
effective epilog vectorization of the remaining iterations. This optimization
takes place only when the original vector loop is vectorized with a vector width
or factor of 16. This vectorization width of 16 may be overwritten by
`-min-width-epilog-vectorization` command-line option.

##### `-enable-redundant-movs`

Removes any redundant `mov` operations including redundant loads from memory and
stores to memory. This can be invoked using
`-Wl,-plugin-opt=-enable-redundant-movs`.

##### `-merge-constant`

Attempts to promote frequently occurring constants to registers. The aim is to
reduce the size of the instruction encoding for instructions using constants and
obtain a performance improvement.

##### `-function-specialize`

Optimizes the functions with compile time constant formal arguments.

##### `-lv-function-specialization`

Generates specialized function versions when the loops inside function are
vectorizable and the arguments are not aliased with each other.

##### `-enable-vectorize-compares`

Enables vectorization on certain loops with conditional breaks assuming the
memory accesses are safely bound within the page boundary.

##### `-inline-recursion=[1,2,3,4]`

Enables inlining for recursive functions based on heuristics where the
aggressiveness of heuristics increases with the level (1-4). The default level
is 2. Higher levels may lead to code bloat due to expansion of recursive
functions at call sites.

:::{table} -inline-recursion Level and Their Effects
| `-inline-recursion` **value** | **Inline depth of heuristics used to enable inlining for recursive functions** |
|:-----------------------------:|:------------------------------------------------------------------------------:|
| 1                             | 1                                                                              |
| 2                             | 1                                                                              |
| 3                             | 1                                                                              |
| 4                             | 10                                                                             |
:::

This is more effective with `-flto` as the whole program needs to be analyzed to
perform this optimization, which can be invoked as
`-flto -inline-recursion=[1,2,3,4]`.

##### `-reduce-array-computations=[1,2,3]`

Performs array data flow analysis and optimizes the unused array computations.

:::{table} -reduce-array-computations Values and Their Effects
| -reduce-array-computations value | Array elements eligible for elimination of computations |
| -------------------------------- | --------------------------- |
| 1                                | Unused                      |
| 2                                | Zero valued                 |
| 3                                | Both unused and zero valued |
:::

This optimization is effective with `-flto` as the whole program needs to be
analyzed to perform this optimization, which can be invoked as
`-flto -reduce-array-computations=[1,2,3]`.

##### `-global-vectorize-slp={true,false}`

Vectorizes the straight-line code inside a basic block with data reordering
vector operations. This option is set to **true** by default.

##### `-region-vectorize`

Experimental flag for enabling vectorization on certain loops with complex
control flow, which the normal vectorizer cannot handle.

This optimization is effective with `-flto` as the whole program needs to be
analyzed to perform this optimization, which can be invoked as
`-flto -region-vectorize`.

##### `-enable-x86-prefetching`

Enables the generation of x86 prefetch instruction for the memory references
inside a loop or inside an innermost loop of a loop nest to prefetch the second
dimension of multidimensional array/memory references in the innermost loop of a
loop nest. This is an experimental pass; its profitability is being improved.

##### `-suppress-fmas`

Identifies the reduction patterns on FMA and suppresses the FMA generation, as
it is not profitable on the reduction patterns.

##### `-enable-icm-vrp`

Enables estimation of the virtual register pressure before performing loop
invariant code motion. This estimation is used to control the number of loop
invariants that will be hoisted during the loop invariant code motion.

##### `-loop-splitting`

Enables splitting of loops into multiple loops to eliminate the branches, which
compare the loop induction with an invariant or constant expression. This option
is enabled under `-O3` by default. To disable this optimization, use
`-loop-splitting=false`.

##### `-enable-ipo-loop-split`

Enables splitting of loops into multiple loops to eliminate the branches, which
compares the loop induction with a constant expression. This constant expression
can be derived through inter-procedural analysis. This option is enabled under
`-O3` by default. To disable this optimization, use
`-enable-ipo-loop-split=false`.

##### `-compute-interchange-order`

Enables heuristic for finding the best possible interchange order for a loop
nest. To enable this option, use `-enable-loopinterchange`. This option is set
to **false** by default.

**Usage:**

```bash
-mllvm -enable-loopinterchange -mllvm -compute-interchange-order
```

##### `-convert-pow-exp-to-int={true,false}`

Converts the call to floating point exponent version of pow to its integer
exponent version if the floating-point exponent can be converted to integer.
This option is set to **true** by default.

##### `-do-lock-reordering={none,normal,aggressive}`

Reorders the control predicates in increasing order of complexity from outer
predicate to inner when it is safe. The **normal** mode reorders simple
expressions, while the **aggressive** mode reorders predicates involving
function calls if no side effects are determined. This option is set to
**normal** by default.

##### `-fuse-tile-inner-loop`

Enables fusion of adjacent tiled loops as a part of loop tiling transformation.
This option is set to false by default.

##### `-Hz,1,0x1 [Fortran]`

Helps to preserve array index information for array access expressions which get
linearized in the compiler front end. The preserved information is used by the
compiler optimization phase in performing optimizations such as loop
transformations. It is recommended that any user who is using optimizations
such as loop transformations and other optimizations requiring de-linearized
index expressions should use the Hz option. This option has no impact on any
other aspects of the Flang front end.

### Inline ASM Statements

Inline assembly (ASM) statements allow a developer to include assembly
instructions directly in either host or device code. While the ROCm compiler
supports ASM statements, their use is not recommended for the following reasons:

- The compiler's ability to produce both correct code and to optimize
  surrounding code is impeded.
- The compiler does not parse the content of the ASM statements and so
  cannot "see" its contents.
- The compiler must make conservative assumptions in an effort to retain
  correctness.
- The conservative assumptions may yield code that, on the whole, is less
  performant compared to code without ASM statements. It is possible that a
  syntactically correct ASM statement may cause incorrect runtime behavior.
- ASM statements are often ASIC-specific; code containing them is less portable
  and adds a maintenance burden to the developer if different ASICs are
  targeted.
- Writing correct ASM statements is often difficult; we strongly recommend
  thorough testing of any use of ASM statements.

:::{note}
For developers who choose to include ASM statements in the code, AMD is
interested in understanding the use case and appreciates feedback at
[https://github.com/RadeonOpenCompute/ROCm/issues](https://github.com/RadeonOpenCompute/ROCm/issues)
:::

### Miscellaneous OpenMP Compiler Features

This section discusses features that have been added or enhanced in the OpenMP
compiler.

#### Offload-arch Tool

An LLVM library and tool that is used to query the execution capability of the
current system as well as to query requirements of a binary file. It is used by
OpenMP device runtime to ensure compatibility of an image with the current
system while loading it. It is compatible with target ID support and multi-image
fat binary support.

**Usage:**

```bash
offload-arch [Options] [Optional lookup-value]
```

When used without an option, offload-arch prints the value of the first offload
arch found in the underlying system. This can be used by various clang
front ends. For example, to compile for OpenMP offloading on your current system,
invoke clang with the following command:

```bash
clang -fopenmp -fopenmp-targets=`offload-arch` foo.c
```

If an optional lookup-value is specified, offload-arch will check if the value
is either a valid offload-arch or a codename and look up requested additional
information.

The following command provides all the information for offload-arch gfx906:

```bash
offload-arch gfx906 -v
```

The options are listed below:

:::{program} offload-arch
:::{option} -h
  Prints the help message.
:::

:::{option} -a
  Prints values for all devices. Do not stop at the first device found.
:::

:::{option} -m
  Prints device code name (often found in `pci.ids` file).
:::

:::{option} -n
  Prints numeric `pci-id`.
:::

:::{option} -t
   Prints clang offload triple to use for the offload arch.
:::

:::{option} -v
  Verbose. Implies: `-a -m -n -t`. For: all devices, prints codename, numeric value, and triple.
:::

:::{option} -f <file>
   Prints offload requirements including offload-arch for each compiled offload image built into an application binary file.
:::

:::{option} -c
  Prints offload capabilities of the underlying system. This option is used by the language runtime to select an image when multiple images are available. A capability must exist for each requirement of the selected image.
:::

There are symbolic link aliases `amdgpu-offload-arch` and `nvidia-arch` for
`offload-arch`. These aliases return 1 if no AMD GCN GPU or CUDA GPU is found.
These aliases are useful in determining whether architecture-specific tests
should be run or to conditionally load architecture-specific software.

#### Command-Line Simplification Using `offload-arch` Flag

Legacy mechanism of specifying offloading target for OpenMP involves using three
flags, `-fopenmp-targets`, `-Xopenmp-target`, and `-march`. The first two flags
take a target triple (like `amdgcn-amd-amdhsa` or `nvptx64-nvidia-cuda`), while
the last flag takes device name (like `gfx908` or `sm_70`) as input.
Alternatively, users of ROCmCC compiler can use the flag `—offload-arch` for a
combined effect of the above three flags.

**Example:**

```bash
# Legacy mechanism
clang -fopenmp -target x86_64-linux-gnu \
-fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa \
-march=gfx906 helloworld.c -o helloworld
```

**Example:**

```bash
# Using offload-arch flag
clang -fopenmp -target x86_64-linux-gnu \
--offload-arch=gfx906 helloworld.c -o helloworld.
```

To ensure backward compatibility, both styles are supported. This option is
compatible with target ID support and multi-image fat binaries.

#### Target ID Support for OpenMP

The ROCmCC compiler supports specification of target features along with the GPU
name while specifying a target offload device in the command line, using
`-march` or `--offload-arch` options. The compiled image in such cases is
specialized for a given configuration of device and target features (target ID).

**Example:**

```bash
# compiling for a gfx908 device with XNACK paging support turned ON
clang -fopenmp -target x86_64-linux-gnu \
-fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa \
-march=gfx908:xnack+ helloworld.c -o helloworld
```

**Example:**

```bash
# compiling for a gfx908 device with SRAMECC support turned OFF
clang -fopenmp -target x86_64-linux-gnu \
-fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa \
-march=gfx908:sramecc- helloworld.c -o helloworld
```

**Example:**

```bash
# compiling for a gfx908 device with SRAMECC support turned ON and XNACK paging support turned OFF
clang -fopenmp -target x86_64-linux-gnu \
-fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa \
-march=gfx908:sramecc+:xnack- helloworld.c -o helloworld
```

The target ID specified on the command line is passed to the clang driver using
`target-feature` flag, to the LLVM optimizer and back end using `-mattr` flag, and
to linker using `-plugin-opt=-mattr` flag. This feature is compatible with
offload-arch command-line option and multi-image binaries for multiple
architectures.

#### Multi-image Fat Binary for OpenMP

The ROCmCC compiler is enhanced to generate binaries that can contain
heterogenous images. This heterogeneity could be in terms of:

- Images of different architectures, like AMD GCN and NVPTX
- Images of same architectures but for different GPUs, like gfx906 and gfx908
- Images of same architecture and same GPU but for different target features,
  like `gfx908:xnack+` and `gfx908:xnack-`

An appropriate image is selected by the OpenMP device runtime for execution
depending on the capability of the current system. This feature is compatible
with target ID support and offload-arch command-line options and uses
offload-arch tool to determine capability of the current system.

**Example:**

```bash
clang -fopenmp -target x86_64-linux-gnu \
-fopenmp-targets=amdgcn-amd-amdhsa,amdgcn-amd-amdhsa \
-Xopenmp-target=amdgcn-amd-amdhsa -march=gfx906 \
-Xopenmp-target=amdgcn-amd-amdhsa -march=gfx908 \
helloworld.c -o helloworld
```

**Example:**

```bash
clang -fopenmp -target x86_64-linux-gnu \
--offload-arch=gfx906 \
--offload-arch=gfx908 \
helloworld.c -o helloworld
```

**Example:**

```bash
clang -fopenmp -target x86_64-linux-gnu \
-fopenmp-targets=amdgcn-amd-amdhsa,amdgcn-amd-amdhsa,amdgcn-amd-amdhsa,amdgcn-amd-amdhsa \
-Xopenmp-target=amdgcn-amd-amdhsa -march=gfx908:sramecc+:xnack+ \
-Xopenmp-target=amdgcn-amd-amdhsa -march=gfx908:sramecc-:xnack+ \
-Xopenmp-target=amdgcn-amd-amdhsa -march=gfx908:sramecc+:xnack- \
-Xopenmp-target=amdgcn-amd-amdhsa -march=gfx908:sramecc-:xnack- \
helloworld.c -o helloworld
```

The ROCmCC compiler creates an instance of toolchain for each unique combination
of target triple and the target GPU (along with the associated target features).
`clang-offload-wrapper` tool is modified to insert a new structure
`__tgt_image_info` along with each image in the binary. Device runtime is also
modified to query this structure to identify a compatible image based on the
capability of the current system.

#### Unified Shared Memory (USM)

The following OpenMP pragma is available on MI200, and it must be executed with
`xnack+` support.

```cpp
omp requires unified_shared_memory
```

For more details on USM refer to the {ref}`openmp_usm` section of the OpenMP
Guide.

### Support Status of Other Clang Options

The following table lists the other Clang options and their support status.

<!-- spellcheck-disable -->

:::{table} Clang Options
:name: clang-options
:widths: auto
:align: center

| **Option**                               | **Support Status** | **Description**                                                                                                                |
|------------------------------------------|:------------------:|--------------------------------------------------------------------------------------------------------------------------------|
| `-###`                                   | Supported          | Prints (but does not run) the commands to run for this compilation                                                             |
| `--analyzer-output <value>`              | Supported          | "Static analyzer report output format (`html|plist|plist-multi-file|plist-html|sarif|text`)"                                   |
| `--analyze`                              | Supported          | Runs the static analyzer                                                                                                       |
| `-arcmt-migrate-emit-errors`             | Unsupported        | Emits ARC errors even if the migrator can fix them                                                                             |
| `-arcmt-migrate-report-output  <value>`  | Unsupported        | Output path for the plist report                                                                                               |
| `-byteswapio`                            | Supported          | Swaps byte-order for unformatted input/output                                                                                  |
| `-B <dir>`                               | Supported          | Adds `<dir>` to search path for binaries and object files used implicitly                                                      |
| `-CC`                                    | Supported          | Includes comments from within the macros in the preprocessed output                                                            |
| `-cl-denorms-are-zero`                   | Supported          | OpenCL only. Allows denormals to be flushed to zero                                                                            |
| `-cl-fast-relaxed-math`                  | Supported          | OpenCL only. Sets `-cl-finite-math-only` and `-cl-unsafe-math-optimizations` and defines `__FAST_RELAXED_MATH__`               |
| `-cl-finite-math-only`                   | Supported          | OpenCL only. Allows floating-point optimizations that assume arguments and results are not `NaN`s or `+-Inf`                   |
| `-cl-fp32-correctly-rounded-divide-sqrt` | Supported          | OpenCL only. Specifies that single-precision floating-point divide and `sqrt` used in the program source are correctly rounded |
| `-cl-kernel-arg-info`                    | Supported          | OpenCL only. Generates kernel argument metadata                                                                                |
| `-cl-mad-enable`                         | Supported          | OpenCL only. Allows use of less precise MAD computations in the generated binary                                               |
| `-cl-no-signed-zeros`                    | Supported          | OpenCL only. Allows use of less precise no-signed-zeros computations in the generated binary                                   |
| `-cl-opt-disable`                        | Supported          | OpenCL only. Disables all optimizations. By default, optimizations are enabled.                                                |
| `-cl-single-precision-constant`          | Supported          | OpenCL only. Treats double-precision floating-point constant as single precision constant                                      |
| `-cl-std= <value>`                       | Supported          | OpenCL language standard to compile for                                                                                        |
| `-cl-strict-aliasing`                    | Supported          | OpenCL only. This option is added for compatibility with OpenCL 1.0.                                                           |
| `-cl-uniform-work-group-size`            | Supported          | OpenCL only. Defines the global work-size to be a multiple of the work-group size specified for `clEnqueueNDRangeKernel`       |
| `-cl-unsafe-math-optimizations`          | Supported          | OpenCL only. Allows unsafe floating-point optimizations. Also implies `-cl-no-signed-zeros` and `-cl-mad-enable`               |
| `--config <value>`                       | Supported          | Specifies configuration file                                                                                                   |
| `--cuda-compile-host-device`             | Supported          | Compiles CUDA code for both host and device (default). Has no effect on non-CUDA compilations                                  |
| `--cuda-device-only`                     | Supported          | Compiles CUDA code for device only                                                                                             |
| `--cuda-host-only`                       | Supported          | Compiles CUDA code for host only. Has no effect on non-CUDA compilations                                                       |
| `--cuda-include-ptx=<value>`             | Unsupported        | Includes PTX for the following GPU architecture (e.g. `sm_35`) or "all." May be specified more than once                       |
| `--cuda-noopt-device-debug`              | Unsupported        | Enables device-side debug info generation. Disables ptxas optimizations                                                        |
| `--cuda-path-ignore-env`                 | Unsupported        | Ignores environment variables to detect CUDA installation                                                                      |
| `--cuda-path=<value>`                    | Unsupported        | CUDA installation path                                                                                                         |
| `-cxx-isystem <directory>`               | Supported          | Adds a directory to the C++ SYSTEM include search path                                                                         |
| `-C`                                     | Supported          | Includes comments in the preprocessed output                                                                                   |
| `-c`                                     | Supported          | Runs only preprocess, compile, and assemble steps                                                                              |
| `-dD`                                    | Supported          | Prints macro definitions in `-E` mode in addition to the normal output                                                         |
| `-dependency-dot <value>`                | Supported          | Writes DOT-formatted header dependencies to the specified filename                                                             |
| `-dependency-file <value>`               | Supported          | Writes dependency output to the specified filename (or `-`)                                                                    |
| `-dI`                                    | Supported          | Prints include directives in `-E` mode in addition to the normal output                                                        |
| `-dM`                                    | Supported          | Prints macro definitions in `-E` mode instead of the normal output                                                             |
| `-dsym-dir <dir>`                        | Unsupported        | Outputs dSYMs (if any) to the specified directory                                                                              |
| `-D <macro>`                             | Supported          | `=<value>`. Defines  `<macro>` to  `<value>` (or `1` if  `<value>` omitted)                                                    |
| `-emit-ast`                              | Supported          | Emits Clang AST files for source inputs                                                                                        |
| `-emit-interface-stubs`                  | Supported          | Generates interface stub files                                                                                                 |
| `-emit-llvm`                             | Supported          | Uses the LLVM representation for assembler and object files                                                                    |
| `-emit-merged-ifs`                       | Supported          | Generates interface stub files and emits merged text not binary                                                                |
| `--emit-static-lib`                      | Supported          | Enables linker job to emit a static library                                                                                    |
| `-enable-trivial-auto-var-init-zero-knowing-it-will-be-removed-from-clang` | Supported | Declares enabling trivial automatic variable initialization to zero for benchmarking purpose with the knowledge that it will eventually be removed |
| `-E`                                     | Supported          | Runs the preprocessor only                                                                                                     |
| `-fAAPCSBitfieldLoad`                    | Unsupported        | Follows the AAPCS standard where all volatile bit-field writes generate at least one load (ARM only)                           |
| `-faddrsig`                              | Supported          | Emits an address-significance table                                                                                            |
| `-faligned-allocation`                   | Supported          | Enables C++17 aligned allocation functions                                                                                     |
| `-fallow-editor-placeholders`            | Supported          | Treats editor placeholders as valid source code                                                                                |
| `-fallow-fortran-gnu-ext`                | Supported          | Allows Fortran GNU extensions                                                                                                  |
| `-fansi-escape-codes`                    | Supported          | Uses ANSI escape codes for diagnostics                                                                                         |
| `-fapple-kext`                           | Unsupported        | Uses Apple's kernel extensions ABI                                                                                             |
| `-fapple-link-rtlib`                     | Unsupported        | Forces linking of the clang built-ins runtime library                                                                          |
 |-fapple-pragma-pack|Unsupported|Enables Apple gcc-compatible #pragma pack handling|
 |-fapplication-extension|Unsupported|Restricts code to those available for App Extensions|
 |-fbackslash|Supported|Treats backslash as C-style escape character|
 |-fbasic-block-sections= \<value\>|Supported|"Places each function's basic blocks in unique sections (ELF Only) : all \| labels \| none \| list= \<file\>"|
 |-fblocks|Supported|Enables the 'blocks' language feature|
 |-fborland-extensions|Unsupported|Accepts non-standard constructs supported by the Borland compile|
 |-fbuild-session-file= \<file\>|Supported|Uses the last modification time of  \<file\> as the build session timestamp|
 |-fbuild-session-timestamp= \<time since Epoch in seconds\>|Supported|Specifies starting time of the current build session|
 |-fbuiltin-module-map|Unsupported|Loads the Clang built-ins module map file|
 |-fcall-saved-x10|Unsupported|Makes the x10 register call-saved (AArch64 only)|
 |-fcall-saved-x11|Unsupported|Makes the x11 register call-saved (AArch64 only)|
 |-fcall-saved-x12|Unsupported|Makes the x12 register call-saved (AArch64 only)|
 |-fcall-saved-x13|Unsupported|Makes the x13 register call-saved (AArch64 only)|
 |-fcall-saved-x14|Unsupported|Makes the x14 register call-saved (AArch64 only)|
 |-fcall-saved-x15|Unsupported|Makes the x15 register call-saved (AArch64 only)|
 |-fcall-saved-x18|Unsupported|Makes the x18 register call-saved (AArch64 only)|
 |-fcall-saved-x8|Unsupported|Makes the x8 register call-saved (AArch64 only)|
 |-fcall-saved-x9|Unsupported|Makes the x9 register call-saved (AArch64 only)|
 |-fcf-protection= \<value\>|Unsupported|Specifies the instrument control-flow architecture protection using options: return, branch, full, none|
 |-fcf-protection|Unsupported|Enables cf-protection in 'full' mode|
 |-fchar8_t|Supported|Enables C++ built-in type char8_t|
 |-fclang-abi-compat= \<version\>|Supported|Attempts to match the ABI of Clang  \<version\>|
 |-fcolor-diagnostics|Supported|Enables colors in diagnostics|
 |-fcomment-block-commands= \<arg\>|Supported|Treats each comma-separated argument in  \<arg\> as a documentation comment block command|
 |-fcommon|Supported|Places uninitialized global variables in a common block|
 |-fcomplete-member-pointers|Supported|Requires member pointer base types to be complete if they are significant under the Microsoft ABI|
 |-fconvergent-functions|Supported|Assumes functions to be convergent|
 |-fcoroutines-ts|Supported|Enables support for the C++ Coroutines TS|
 |-fcoverage-mapping|Unsupported|Generates coverage mapping to enable code coverage analysis|
 |-fcs-profile-generate= \<directory\>|Unsupported|Generates instrumented code to collect context-sensitive execution counts into  \<directory\>/default.profraw (overridden by LLVM_PROFILE_FILE env var)|
 |-fcs-profile-generate|Unsupported|Generates instrumented code to collect context-sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)|
 |-fcuda-approx-transcendentals|Unsupported|Uses approximate transcendental functions|
 |-fcuda-flush-denormals-to-zero|Supported|Flushes denormal floating-point values to zero in CUDA device mode|
 |-fcuda-short-ptr|Unsupported|Uses 32-bit pointers for accessing const/local/shared address spaces|
 |-fcxx-exceptions|Supported|Enables C++ exceptions|
 |-fdata-sections|Supported|Places each data in its section|
 |-fdebug-compilation-dir  \<value\>|Supported|Specifies the compilation directory for embedding the debug info|
 |-fdebug-default-version= \<value\>|Supported|Specifies the default DWARF version to use, if a -g option caused DWARF debug info to be produced|
 |-fdebug-info-for-profiling|Supported|Emits extra debug info to make the sample profile more accurate|
 |-fdebug-macro|Supported|Emits macro debug information|
 |-fdebug-prefix-map= \<value\>|Supported|Remaps file source paths in debug info|
 |-fdebug-ranges-base-address|Supported|Uses DWARF base address selection entries in .debug ranges|
 |-fdebug-types-section|Supported|Places debug types in their section (ELF only)|
 |-fdeclspec|Supported|Allows __declspec as a keyword|
 |-fdelayed-template-parsing|Supported|Parses templated function definitions at the end of the translation unit|
 |-fdelete-null-pointer-checks|Supported|Treats usage of null pointers as undefined behavior (default)|
 |-fdiagnostics-absolute-paths|Supported|Prints absolute paths in diagnostics|
 |-fdiagnostics-hotness-threshold= \<number\>|Unsupported|Prevents optimization remarks from being output if they do not have at least the specified number of profile count|
 |-fdiagnostics-parseable-fixits|Supported|Prints fix-its in machine parseable form|
 |-fdiagnostics-print-source-range-info|Supported|Prints source range spans in numeric form|
 |-fdiagnostics-show-hotness|Unsupported|Enables profile hotness information in diagnostic line|
 |-fdiagnostics-show-note-include-stack|Supported|Displays include stacks for diagnostic notes|
 |-fdiagnostics-show-option|Supported|Prints option name with mappable diagnostics|
 |-fdiagnostics-show-template-tree|Supported|Prints a template comparison tree for differing templates|
 |-fdigraphs|Supported|Enables alternative token representations ' \<:', ':\>', ' \<%', '%\>', '%:', '%:%:' (default)|
 |-fdiscard-value-names|Supported|Discards value names in LLVM IR|
 |-fdollars-in-identifiers|Supported|Allows "$" in identifiers|
 |-fdouble-square-bracket-attributes|Supported|Enables '[[]]' attributes in all C and C++ language modes|
 |-fdwarf-exceptions|Unsupported|Uses DWARF style exceptions|
 |-feliminate-unused-debug-types|Supported|Eliminates debug info for defined but unused types|
 |-fembed-bitcode-marker|Supported|Embeds placeholder LLVM IR data as a marker|
 |-fembed-bitcode= \<option\>|Supported|Embeds LLVM bitcode (option: off, all, bitcode, marker)|
 |-fembed-bitcode|Supported|Embeds LLVM IR bitcode as data|
 |-femit-all-decls|Supported|Emits all declarations, even if unused|
 |-femulated-tls|Supported|Uses emutls functions to access thread_local variables|
 |-fenable-matrix|Supported|Enables matrix data type and related built-in functions|
 |-fexceptions|Supported|Enables support for exception handling|
 |-fexperimental-new-constant-interpreter|Supported|Enables the experimental new constant interpreter|
 |-fexperimental-new-pass-manager|Supported|Enables an experimental new pass manager in LLVM|
 |-fexperimental-relative-c++-abi-vtables|Supported|Uses the experimental C++ class ABI for classes with virtual tables|
 |-fexperimental-strict-floating-point|Supported|Enables experimental strict floating point in LLVM|
 |-ffast-math|Supported|Allows aggressive, lossy floating-point optimizations|
 |-ffile-prefix-map= \<value\>|Supported|Remaps file source paths in debug info and predefined preprocessor macros|
 |-ffine-grained-bitfield-accesses|Supported|Uses separate accesses for consecutive bitfield runs with legal widths and alignments|
 |-ffixed-form|Supported|Enables fixed-form format for Fortran|
 |-ffixed-point|Supported|Enables fixed point types|
 |-ffixed-r19|Unsupported|Reserves the r19 register (Hexagon only)|
 |-ffixed-r9|Unsupported|Reserves the r9 register (ARM only)|
 |-ffixed-x10|Unsupported|Reserves the x10 register (AArch64/RISC-V only)|
 |-ffixed-x11|Unsupported|Reserves the x11 register (AArch64/RISC-V only)|
 |-ffixed-x12|Unsupported|Reserves the x12 register (AArch64/RISC-V only)|
 |-ffixed-x13|Unsupported|Reserves the x13 register (AArch64/RISC-V only)|
 |-ffixed-x14|Unsupported|Reserves the x14 register (AArch64/RISC-V only)|
 |-ffixed-x15|Unsupported|Reserves the x15 register (AArch64/RISC-V only)|
 |-ffixed-x16|Unsupported|Reserves the x16 register (AArch64/RISC-V only)|
 |-ffixed-x17|Unsupported|Reserves the x17 register (AArch64/RISC-V only)|
 |-ffixed-x18|Unsupported|Reserves the x18 register (AArch64/RISC-V only)|
 |-ffixed-x19|Unsupported|Reserves the x19 register (AArch64/RISC-V only)|
 |-ffixed-x1|Unsupported|Reserves the x1 register (AArch64/RISC-V only)|
 |-ffixed-x20|Unsupported|Reserves the x20 register (AArch64/RISC-V only)|
 |-ffixed-x21|Unsupported|Reserves the x21 register (AArch64/RISC-V only)|
 |-ffixed-x22|Unsupported|Reserves the x22 register (AArch64/RISC-V only)|
 |-ffixed-x23|Unsupported|Reserves the x23 register (AArch64/RISC-V only)|
 |-ffixed-x24|Unsupported|Reserves the x24 register (AArch64/RISC-V only)|
 |-ffixed-x25|Unsupported|Reserves the x25 register (AArch64/RISC-V only)|
 |-ffixed-x26|Unsupported|Reserves the x26 register (AArch64/RISC-V only)|
 |-ffixed-x27|Unsupported|Reserves the x27 register (AArch64/RISC-V only)|
 |-ffixed-x28|Unsupported|Reserves the x28 register (AArch64/RISC-V only)|
 |-ffixed-x29|Unsupported|Reserves the x29 register (AArch64/RISC-V only)|
 |-ffixed-x2|Unsupported|Reserves the x2 register (AArch64/RISC-V only)|
 |-ffixed-x30|Unsupported|Reserves the x30 register (AArch64/RISC-V only)|
 |-ffixed-x31|Unsupported|Reserves the x31 register (AArch64/RISC-V only)|
 |-ffixed-x3|Unsupported|Reserves the x3 register (AArch64/RISC-V only)|
 |-ffixed-x4|Unsupported|Reserves the x4 register (AArch64/RISC-V only)|
 |-ffixed-x5|Unsupported|Reserves the x5 register (AArch64/RISC-V only)|
 |-ffixed-x6|Unsupported|Reserves the x6 register (AArch64/RISC-V only)|
 |-ffixed-x7|Unsupported|Reserves the x7 register (AArch64/RISC-V only)|
 |-ffixed-x8|Unsupported|Reserves the x8 register (AArch64/RISC-V only)|
 |-ffixed-x9|Unsupported|Reserves the x9 register (AArch64/RISC-V only)|
 |-fforce-dwarf-frame|Supported|Mandatorily emits a debug frame section|
 |-fforce-emit-vtables|Supported|Emits more virtual tables to improve devirtualization|
 |-fforce-enable-int128|Supported|Enables support for int128_t type|
 |-ffp-contract= \<value\>|Supported|Forms fused FP ops (e.g. FMAs): fast (everywhere) \ on (according to FP_CONTRACT pragma) \ off (never fuse). Default is "fast" for CUDA/HIP and "on" for others.|
 |-ffp-exception-behavior= \<value\>|Supported|Specifies the exception behavior of floating-point operations|
 |-ffp-model= \<value\>|Supported|Controls the semantics of floating-point calculations|
 |-ffree-form|Supported|Enables free-form format for Fortran|
 |-ffreestanding|Supported|Asserts the compilation to take place in a freestanding environment|
 |-ffunc-args-alias|Supported|Allows the function arguments aliases (equivalent to ansi alias)|
 |-ffunction-sections|Supported|Places each function in its section|
 |-fglobal-isel|Supported|Enables the global instruction selector|
 |-fgnu-keywords|Supported|Allows GNU-extension keywords regardless of a language standard|
 |-fgnu-runtime|Unsupported|Generates output compatible with the standard GNU Objective-C runtime|
 |-fgnu89-inline|Unsupported|Uses the gnu89 inline semantics|
 |-fgnuc-version= \<value\>|Supported|Sets various macros to claim compatibility with the given GCC version (default is 4.2.1)|
 |-fgpu-allow-device-init|Supported|Allows device-side init function in HIP|
 |-fgpu-rdc|Supported|Generates relocatable device code, also known as separate compilation mode|
 |-fhip-new-launch-api|Supported|Uses new kernel launching API for HIP|
 |-fignore-exceptions|Supported|Enables support for ignoring exception handling constructs|
 |-fimplicit-module-maps|Unsupported|Implicitly searches the file system for module map files|
 |-finline-functions|Supported|Inlines suitable functions|
 |-finline-hint-functions|Supported|Inlines functions that are (explicitly or implicitly) marked inline|
 |-finstrument-function-entry-bare|Unsupported|Allows instrument function entry only after inlining, without arguments to the instrumentation call|
 |-finstrument-functions-after-inlining|Unsupported|Similar to -finstrument-functions option but inserts the calls after inlining|
 |-finstrument-functions|Unsupported|Generates calls to instrument function entry and exit|
 |-fintegrated-as|Supported|Enables the integrated assembler|
 |-fintegrated-cc1|Supported|Runs cc1 in-process|
 |-fjump-tables|Supported|Uses jump tables for lowering switches|
 |-fkeep-static-consts|Supported|Keeps static const variables if unused|
 |-flax-vector-conversions= \<value\>|Supported|Enables implicit vector bit-casts|
 |-flto-jobs= \<value\>|Unsupported|Controls the backend parallelism of -flto=thin (A default value of 0 means the number of threads will be derived from the number of CPUs detected.)|
 |-flto= \<value\>|Unsupported|Sets LTO mode to either "full" or "thin"|
 |-flto|Unsupported|Enables LTO in "full" mode|
 |-fmacro-prefix-map= \<value\>|Supported|Remaps file source paths in predefined preprocessor macros|
 |-fmath-errno|Supported|Requires math functions to indicate errors by setting errno|
 |-fmax-tokens= \<value\>|Supported|Specifies max total number of preprocessed tokens for -Wmax-tokens|
 |-fmax-type-align= \<value\>|Supported|Specifies the maximum alignment to enforce on pointers lacking an explicit alignment|
 |-fmemory-profile|Supported|Enables heap memory profiling|
 |-fmerge-all-constants|Supported|Allows merging of constants|
 |-fmessage-length= \<value\>|Supported|Formats message diagnostics to fit within N columns|
 |-fmodule-file=[ \<name\>=] \<file\>|Unsupported|Specifies the mapping of module name to precompiled module file. Loads a module file if name is omitted|
 |-fmodule-map-file= \<file\>|Unsupported|Loads the specified module map file|
 |-fmodule-name= \<name\>|Unsupported|Specifies the name of the module to build|
 |-fmodules-cache-path= \<directory\>|Unsupported|Specifies the module cache path|
 |-fmodules-decluse|Unsupported|Asserts declaration of modules used within a module|
 |-fmodules-disable-diagnostic-validation|Unsupported|Disables validation of the diagnostic options when loading the module|
 |-fmodules-ignore-macro= \<value\>|Unsupported|Ignores the definition of the specified macro when building and loading modules|
 |-fmodules-prune-after= \<seconds\>|Unsupported|Specifies the interval (in seconds) after which a module file is to be considered unused|
 |-fmodules-prune-interval= \<seconds\>|Unsupported|Specifies the interval (in seconds) between attempts to prune the module cache|
 |-fmodules-search-all|Unsupported|Searches even non-imported modules to resolve references|
 |-fmodules-strict-decluse|Unsupported|Similar to -fmodules-decluse option but requires all headers to be in the modules|
 |-fmodules-ts|Unsupported|Enables support for the C++ Modules TS|
 |-fmodules-user-build-path  \<directory\>|Unsupported|Specifies the module user build path|
 |-fmodules-validate-input-files-content|Supported|Validates PCM input files based on content if mtime differs|
 |-fmodules-validate-once-per-build-session|Unsupported|Prohibits verification of input files for the modules if the module has been successfully validated or loaded during the current build session|
 |-fmodules-validate-system-headers|Supported|Validates the system headers that a module depends on when loading the module|
 |-fmodules|Unsupported|Enables the "modules" language feature|
 |-fms-compatibility-version= \<value\>|Supported|Specifies the dot-separated value representing the Microsoft compiler version number to report in _MSC_VER (0 = do not define it (default))|
 |-fms-compatibility|Supported|Enables full Microsoft Visual C++ compatibility|
 |-fms-extensions|Supported|Accepts some non-standard constructs supported by the Microsoft compiler|
 |-fmsc-version= \<value\>|Supported|Specifies the Microsoft compiler version number to report in _MSC_VER (0 = do not define it (default))|
 |-fnew-alignment= \<align\>|Supported|Specifies the largest alignment guaranteed by "::operator new(size_t)"|
 |-fno-addrsig|Supported|Prohibits emitting an address-significance table|
 |-fno-allow-fortran-gnu-ext|Supported|Allows Fortran GNU extensions|
 |-fno-assume-sane-operator-new|Supported|Prohibits the assumption that C++'s global operator new cannot alias any pointer|
 |-fno-autolink|Supported|Disables generation of linker directives for automatic library linking|
 |-fno-backslash|Supported|Allows treatment of backslash like any other character in character strings|
 |-fno-builtin- \<value\>|Supported|Disables implicit built-in knowledge of a specific function|
 |-fno-builtin|Supported|Disables implicit built-in knowledge of functions|
 |-fno-c++-static-destructors|Supported|Disables C++ static destructor registration|
 |-fno-char8_t|Supported|Disables C++ built-in type char8_t|
 |-fno-color-diagnostics|Supported|Disables colors in diagnostics|
 |-fno-common|Supported|Compiles common globals like normal definitions|
 |-fno-complete-member-pointers|Supported|Eliminates the requirement for the member pointer base types to be complete if they would be significant under the Microsoft ABI|
 |-fno-constant-cfstrings|Supported|Disables creation of CodeFoundation-type constant strings|
 |-fno-coverage-mapping|Supported|Disables code coverage analysis|
 |-fno-crash-diagnostics|Supported|Disables auto-generation of preprocessed source files and a script for reproduction during a Clang crash|
 |-fno-cuda-approx-transcendentals|Unsupported|Eliminates the usage of approximate transcendental functions|
 |-fno-debug-macro|Supported|Prohibits emitting the macro debug information|
 |-fno-declspec|Unsupported|Disallows declspec as a keyword|
 |-fno-delayed-template-parsing|Supported|Disables delayed template parsing|
 |-fno-delete-null-pointer-checks|Supported|Prohibits the treatment of null pointers as undefined behavior|
 |-fno-diagnostics-fixit-info|Supported|Prohibits including fixit information in diagnostics|
 |-fno-digraphs|Supported|Disallows alternative token representations " \<:', ':\>', ' \<%', '%\>', '%:', '%:%:"|
 |-fno-discard-value-names|Supported|Prohibits discarding value names in LLVM IR|
 |-fno-dollars-in-identifiers|Supported|Disallows '$' in identifiers|
 |-fno-double-square-bracket-attributes|Supported|Disables '[[]]' attributes in all C and C++ language modes|
 |-fno-elide-constructors|Supported|Disables C++ copy constructor elision|
 |-fno-elide-type|Supported|Prohibits eliding types when printing diagnostics|
 |-fno-eliminate-unused-debug-types|Supported|Emits debug info for defined but unused types|
 |-fno-exceptions|Supported|Disables support for exception handling|
 |-fno-experimental-new-pass-manager|Supported|Disables an experimental new pass manager in LLVM|
 |-fno-experimental-relative-c++-abi-vtables|Supported|Prohibits using the experimental C++ class ABI for classes with virtual tables|
 |-fno-fine-grained-bitfield-accesses|Supported|Allows using large-integer access for consecutive bitfield runs|
 |-fno-fixed-form|Supported|Disables fixed-form format for Fortran|
 |-fno-fixed-point|Supported|Disables fixed point types|
 |-fno-force-enable-int128|Supported|Disables support for int128_t type|
 |-fno-fortran-main|Supported|Prohibits linking in Fortran main|
 |-fno-free-form|Supported|Disables free-form format for Fortran|
 |-fno-func-args-alias|Supported|Allows the function argument alias (equivalent to ansi alias)|
 |-fno-global-isel|Supported|Disables the global instruction selector|
 |-fno-gnu-inline-asm|Supported|Disables GNU style inline asm|
 |-fno-gpu-allow-device-init|Supported|Disallows device-side init function in HIP|
 |-fno-hip-new-launch-api|Supported|Disallows new kernel launching API for HIP|
 |-fno-integrated-as|Supported|Disables the integrated assembler|
 |-fno-integrated-cc1|Supported|Spawns a separate process for each cc1|
 |-fno-jump-tables|Supported|Disallows jump tables for lowering switches|
 |-fno-keep-static-consts|Supported|Prohibits keeping static const variables if unused|
 |-fno-lto|Supported|Disables LTO mode (default)|
 |-fno-memory-profile|Supported|Disables heap memory profiling|
 |-fno-merge-all-constants|Supported|Disallows merging of constants|
 |-fno-no-access-control|Supported|Disables C++ access control|
 |-fno-objc-infer-related-result-type|Supported|Prohibits inferring Objective-C related result type based on the method family|
 |-fno-operator-names|Supported|Disallows treatment of C++ operator name keywords as synonyms for operators|
 |-fno-pch-codegen|Supported|Disallows code-generation for uses of the PCH that assumes building an explicit object file for the PCH|
 |-fno-pch-debuginfo|Supported|Prohibits generation of debug info for types in an object file built from this PCH or elsewhere|
 |-fno-plt|Supported|Asserts usage of GOT indirection instead of PLT to make external function calls (x86 only)|
 |-fno-preserve-as-comments|Supported|Prohibits preserving comments in inline assembly|
 |-fno-profile-generate|Supported|Disables generation of profile instrumentation|
 |-fno-profile-instr-generate|Supported|Disables generation of profile instrumentation|
 |-fno-profile-instr-use|Supported|Disables usage of instrumentation data for profile-guided optimization|
 |-fno-register-global-dtors-with-atexit|Supported|Disallows usage of atexit or __cxa_atexit to register global destructors|
 |-fno-rtlib-add-rpath|Supported|Prohibits adding -rpath with architecture-specific resource directory to the linker flags|
 |-fno-rtti-data|Supported|Disables generation of RTTI data|
 |-fno-rtti|Supported|Disables generation of rtti information|
 |-fno-sanitize-address-poison-custom-array-cookie|Supported on Host only|Disables poisoning of array cookies when using custom operator new[] in AddressSanitizer|
 |-fno-sanitize-address-use-after-scope|Supported on Host only|Disables use-after-scope detection in AddressSanitizer|
 |-fno-sanitize-address-use-odr-indicator|Supported on Host only|Disables ODR indicator globals|
 |-fno-sanitize-blacklist|Supported on Host only|Prohibits using blacklist file for sanitizers|
 |-fno-sanitize-cfi-canonical-jump-tables|Supported on Host only|Prohibits making the jump table addresses canonical in the symbol table|
 |-fno-sanitize-cfi-cross-dso|Supported on Host only|Disables control flow integrity (CFI) checks for cross-DSO calls|
 |-fno-sanitize-coverage= \<value\>|Supported on Host only|Disables specified features of coverage instrumentation for Sanitizers|
 |-fno-sanitize-memory-track-origins|Supported on Host only|Disables origins tracking in MemorySanitizer|
 |-fno-sanitize-memory-use-after-dtor|Supported on Host only|Disables use-after-destroy detection in MemorySanitizer|
 |-fno-sanitize-recover= \<value\>|Supported on Host only|Disables recovery for specified sanitizers|
 |-fno-sanitize-stats|Supported on Host only|Disables sanitizer statistics gathering|
 |-fno-sanitize-thread-atomics|Supported on Host only|Disables atomic operations instrumentation in ThreadSanitizer|
 |-fno-sanitize-thread-func-entry-exit|Supported on Host only|Disables function entry/exit instrumentation in ThreadSanitizer|
 |-fno-sanitize-thread-memory-access|Supported on Host only|Disables memory access instrumentation in ThreadSanitizer|
 |-fno-sanitize-trap= \<value\>|Supported on Host only|Disables trapping for specified sanitizers|
 |-fno-sanitize-trap|Supported on Host only|Disables trapping for all sanitizers|
 |-fno-short-wchar|Supported|Forces wchar_t to be an unsigned int|
 |-fno-show-column|Supported|Prohibits including column number on diagnostics|
 |-fno-show-source-location|Supported|Prohibits including source location information with diagnostics|
 |-fno-signed-char|Supported|char is unsigned|
 |-fno-signed-zeros|Supported|Allows optimizations that ignore the sign of floating point zeros|
 |-fno-spell-checking|Supported|Disables spell-check|
 |-fno-split-machine-functions|Supported|Disables late function splitting using profile information (x86 ELF)|
 |-fno-stack-clash-protection|Supported|Disables stack clash protection|
 |-fno-stack-protector|Supported|Disables the use of stack protectors|
 |-fno-standalone-debug|Supported|Limits debug information produced to reduce size of debug binary|
 |-fno-strict-float-cast-overflow|Supported|Relaxes language rules and tries to match the behavior of the target's native float-to-int conversion instructions|
 |-fno-strict-return|Supported|Prohibits treating the control flow paths that fall off the end of a non-void function as unreachable|
 |-fno-sycl|Unsupported|Disables SYCL kernels compilation for device|
 |-fno-temp-file|Supported|Asserts direct creation of compilation output files. This may lead to incorrect incremental builds if the compiler crashes.|
 |-fno-threadsafe-statics|Supported|Prohibits emitting code to make initialization of local statics thread safe|
 |-fno-trigraphs|Supported|Prohibits processing trigraph sequences|
 |-fno-unique-section-names|Supported|Prohibits the usage of unique names for text and data sections|
 |-fno-unroll-loops|Supported|Turns off the loop unroller|
 |-fno-use-cxa-atexit|Supported|Prohibits the usage of __cxa_atexit for calling destructors|
 |-fno-use-flang-math-libs|Supported|Asserts the usage of Flang internal runtime math library instead of LLVM math intrinsics|
 |-fno-use-init-array|Supported|Asserts the usage of .ctors/.dtors instead of .init_array/.fini_array|
 |-fno-visibility-inlines-hidden-static-local-var|Supported|Disables -fvisibility-inlines-hidden-static-local-var (This is the default on non-darwin targets.)|
 |-fno-xray-function-index|Unsupported|Allows omitting function index section at the expense of single-function patching performance|
 |-fno-zero-initialized-in-bss|Supported|Prohibits placing zero initialized data in BSS|
 |-fobjc-arc-exceptions|Unsupported|Asserts using EH-safe code when synthesizing retains and releases in -fobjc-arc|
 |-fobjc-arc|Unsupported|Synthesizes retain and release calls for Objective-C pointers|
 |-fobjc-exceptions|Unsupported|Enables Objective-C exceptions|
 |-fobjc-runtime= \<value\>|Unsupported|Specifies the target Objective-C runtime kind and version|
 |-fobjc-weak|Unsupported|Enables ARC-style weak references in Objective-C|
 |-fopenmp-simd|Unsupported|Emits OpenMP code only for SIMD-based constructs|
 |-fopenmp-targets= \<value\>|Unsupported|Specifies a comma-separated list of triples OpenMP offloading targets to be supported|
 |-fopenmp|Unsupported|Parses OpenMP pragmas and generates parallel code|
 |-foptimization-record-file= \<file\>|Supported|Specifies the output name of the file containing the optimization remarks. Implies -fsave-optimization-record. On Darwin platforms, this cannot be used with multiple -arch  \<arch\> options.|
 |-foptimization-record-passes= \<regex\>|Supported|Exclusively allows the inclusion of passes that match a specified regular expression in the generated optimization record (By default, include all passes.)|
 |-forder-file-instrumentation|Supported|Generates instrumented code to collect order file into default.profraw file (overridden by '=' form of option or LLVM_PROFILE_FILE env var)|
 |-fpack-struct= \<value\>|Unsupported|Specifies the default maximum struct packing alignment|
 |-fpascal-strings|Supported|Recognizes and constructs Pascal-style string literals|
 |-fpass-plugin= \<dsopath\>|Supported|Loads pass plugin from a dynamic shared object file (only with new pass manager)|
 |-fpatchable-function-entry= \<N,M\>|Supported|Generates M NOPs before function entry and N-M NOPs after function entry|
 |-fpcc-struct-return|Unsupported|Overrides the default ABI to return all structs on the stack|
 |-fpch-codegen|Supported|Generates code for using this PCH that assumes building an explicit object file for the PCH|
 |-fpch-debuginfo|Supported|Generates debug info for types exclusively in an object file built from this PCH|
 |-fpch-instantiate-templates|Supported|Instantiates templates already while building a PCH|
 |-fpch-validate-input-files-content|Supported|Validates PCH input files based on the content if mtime differs|
 |-fplugin= \<dsopath\>|Supported|Loads the named plugin (dynamic shared object)|
 |-fprebuilt-module-path= \<directory\>|Unsupported|Specifies the prebuilt module path|
 |-fprofile-exclude-files= \<value\>|Unsupported|Exclusively instruments those functions from files where names do not match all the regexes separated by a semicolon|
 |-fprofile-filter-files= \<value\>|Unsupported|Exclusively instruments those functions from files where names match any regex separated by a semicolon|
 |-fprofile-generate= \<directory\>|Unsupported|Generates instrumented code to collect execution counts into  \<directory\>/default.profraw (overridden by LLVM_PROFILE_FILE env var)|
 |-fprofile-generate|Unsupported|Generates instrumented code to collect execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)|
 |-fprofile-instr-generate= \<file\>|Unsupported|Generates instrumented code to collect execution counts into  \<file\> (overridden by LLVM_PROFILE_FILE env var)|
 |-fprofile-instr-generate|Unsupported|Generates instrumented code to collect execution counts into default.profraw file (overridden by '=' form of option or LLVM_PROFILE_FILE env var)|
 |-fprofile-instr-use= \<value\>|Unsupported|Uses instrumentation data for profile-guided optimization|
 |-fprofile-remapping-file= \<file\>|Unsupported|Uses the remappings described in  \<file\> to match the profile data against the names in the program|
 |-fprofile-sample-accurate|Unsupported|Specifies that the sample profile is accurate|
 |-fprofile-sample-use= \<value\>|Unsupported|Enables sample-based profile-guided optimizations|
 |-fprofile-use= \<pathname\>|Unsupported|Uses instrumentation data for profile-guided optimization. If pathname is a directory, it reads from  \<pathname\>/default.profdata. Otherwise, it reads from file  \<pathname\>.|
 |-freciprocal-math|Supported|Allows division operations to be reassociated|
 |-freg-struct-return|Unsupported|Overrides the default ABI to return small structs in registers|
 |-fregister-global-dtors-with-atexit|Supported|Uses atexit or __cxa_atexit to register global destructors|
 |-frelaxed-template-template-args|Supported|Enables C++17 relaxed template argument matching|
 |-freroll-loops|Supported|Turns on loop reroller|
 |-fropi|Unsupported|Generates read-only position independent code (ARM only)|
 |-frtlib-add-rpath|Supported|Adds -rpath with architecture-specific resource directory to the linker flags|
 |-frwpi|Unsupported|Generates read-write position-independent code (ARM only)|
 |-fsanitize-address-field-padding= \<value\>|Supported on Host only|Specifies the level of field padding for AddressSanitizer|
 |-fsanitize-address-globals-dead-stripping|Supported on Host only|Enables linker dead stripping of globals in AddressSanitizer|
 |-fsanitize-address-poison-custom-array-cookie|Supported on Host only|Enables poisoning of array cookies when using custom operator new[] in AddressSanitizer|
 |-fsanitize-address-use-after-scope|Supported on Host only|Enables use-after-scope detection in AddressSanitizer|
 |-fsanitize-address-use-odr-indicator|Supported on Host only|Enables ODR indicator globals to avoid false ODR violation reports in partially sanitized programs at the cost of an increase in binary size|
 |-fsanitize-blacklist= \<value\>|Supported on Host only|Specifies the path to blacklisted files for sanitizers|
 |-fsanitize-cfi-canonical-jump-tables|Supported on Host only|Makes the jump table addresses canonical in the symbol table|
 |-fsanitize-cfi-cross-dso|Supported on Host only|Enables control flow integrity (CFI) checks for cross-DSO calls|
 |-fsanitize-cfi-icall-generalize-pointers|Supported on Host only|Generalizes pointers in CFI indirect call type signature checks|
 |-fsanitize-coverage-allowlist= \<value\>|Supported on Host only|Restricts sanitizer coverage instrumentation exclusively to modules and functions that match the provided special case list, except the blocked ones|
 |-fsanitize-coverage-blacklist= \<value\>|Supported on Host only|Deprecated; use -fsanitize-coverage-blocklist= instead.|
 |-fsanitize-coverage-blocklist= \<value\>|Supported on Host only|Disables sanitizer coverage instrumentation for modules and functions that match the provided special case list, even the allowed ones|
 |-fsanitize-coverage-whitelist= \<value\>|Supported on Host only|Deprecated; use -fsanitize-coverage-allowlist= instead.|
 |-fsanitize-coverage= \<value\>|Supported on Host only|Specifies the type of coverage instrumentation for Sanitizers|
 |-fsanitize-hwaddress-abi= \<value\>|Supported on Host only|Selects the HWAddressSanitizer ABI to target (interceptor or platform, default interceptor). This option is currently unused.|
 |-fsanitize-memory-track-origins= \<value\>|Supported on Host only|Enables origins tracking in MemorySanitizer|
 |-fsanitize-memory-track-origins|Supported on Host only|Enables origins tracking in MemorySanitizer|
 |-fsanitize-memory-use-after-dtor|Supported on Host only|Enables use-after-destroy detection in MemorySanitizer|
 |-fsanitize-recover= \<value\>|Supported on Host only|Enables recovery for specified sanitizers|
 |-fsanitize-stats|Supported on Host only|Enables sanitizer statistics gathering|
 |-fsanitize-system-blacklist= \<value\>|Supported on Host only|Specifies the path to system blacklist files for sanitizers|
 |-fsanitize-thread-atomics|Supported on Host only|Enables atomic operations instrumentation in ThreadSanitizer (default)|
 |-fsanitize-thread-func-entry-exit|Supported on Host only|Enables function entry/exit instrumentation in ThreadSanitizer (default)|
 |-fsanitize-thread-memory-access|Supported on Host only|Enables memory access instrumentation in ThreadSanitizer (default)|
 |-fsanitize-trap= \<value\>|Supported on Host only|Enables trapping for specified sanitizers|
 |-fsanitize-trap|Supported on Host only|Enables trapping for all sanitizers|
 |-fsanitize-undefined-strip-path-components= \<number\>|Supported on Host only|Strips (or keeps only, if negative) the given number of path components when emitting check metadata|
 |-fsanitize= \<check\>|Supported on Host only|Turns on runtime checks for various forms of undefined or suspicious behavior. See user manual for available checks.|
 |-fsave-optimization-record= \<format\>|Supported|Generates an optimization record file in the specified format|
 |-fsave-optimization-record|Supported|Generates a YAML optimization record file|
 |-fseh-exceptions|Supported|Uses SEH style exceptions|
 |-fshort-enums|Supported|Allocates to an enum type only as many bytes as it needs for the declared range of possible values|
 |-fshort-wchar|Unsupported|Forces wchar_t to be a short unsigned int|
 |-fshow-overloads= \<value\>|Supported|Specifies which overload candidates are shown when overload resolution fails. Values = best\all; default value = "all"|
 |-fsigned-char|Supported|Asserts that the char is signed|
 |-fsized-deallocation|Supported|Enables C++14 sized global deallocation functions|
 |-fsjlj-exceptions|Supported|Uses SjLj style exceptions|
 |-fslp-vectorize|Supported|Enables the superword-level parallelism vectorization passes|
 |-fsplit-dwarf-inlining|Unsupported|Provides minimal debug info in the object/executable to facilitate online symbolication/stack traces in the absence of .dwo/.dwp files when using Split DWARF|
 |-fsplit-lto-unit|Unsupported|Enables splitting of the LTO unit|
 |-fsplit-machine-functions|Supported|Enables late function splitting using profile information (x86 ELF)|
 |-fstack-clash-protection|Supported|Enables stack clash protection|
 |-fstack-protector-all|Unsupported|Enables stack protectors for all functions|
 |-fstack-protector-strong|Unsupported|Enables stack protectors for some functions vulnerable to stack smashing. Compared to -fstack-protector, this uses a stronger heuristic that includes functions containing arrays of any size (and any type), as well as any calls to allocate or the taking of an address from a local variable.|
 |-fstack-protector|Unsupported|Enables stack protectors for some functions vulnerable to stack smashing. This uses a loose heuristic that considers the functions to be vulnerable if they contain a char (or 8bit integer) array or constant-size calls to alloca, which are of greater size than ssp-buffer-size (default: 8 bytes). All variable-size calls to alloca are considered vulnerable. A function with a stack protector has a guard value added to the stack frame that is checked on function exit. The guard value must be positioned in the stack frame such that a buffer overflow from a vulnerable variable will overwrite the guard value before overwriting the function's return address. The reference stack guard value is stored in a global variable.|
 |-fstack-size-section|Supported|Emits section containing metadata on function stack sizes|
 |-fstandalone-debug|Supported|Emits full debug info for all types used by the program|
 |-fstrict-enums|Supported|Enables optimizations based on the strict definition of an enum's value range|
 |-fstrict-float-cast-overflow|Supported|Assumes the overflowing float-to-int casts to be undefined (default)|
 |-fstrict-vtable-pointers|Supported|Enables optimizations based on the strict rules for overwriting polymorphic C++ objects|
 |-fsycl|Unsupported|Enables SYCL kernels compilation for device|
 |-fsystem-module|u|Builds this module as a system module. Only used with -emit-module|
 |-fthin-link-bitcode= \<value\>|Supported|Writes minimized bitcode to  \<file\> for the ThinLTO thin link only|
 |-fthinlto-index= \<value\>|Unsupported|Performs ThinLTO import using the provided function summary index|
 |-ftime-trace-granularity= \<value\>|Supported|Specifies the minimum time granularity (in microseconds) traced by time profiler|
 |-ftime-trace|Supported|Turns on time profiler. Generates JSON file based on output filename|
 |-ftrap-function= \<value\>|Unsupported|Issues call to specified function rather than a trap instruction|
 |-ftrapv-handler= \<function name\>|Unsupported|Specifies the function to be called on overflow|
 |-ftrapv|Unsupported|Traps on integer overflow|
 |-ftrigraphs|Supported|Processes trigraph sequences|
 |-ftrivial-auto-var-init-stop-after= \<value\>|Supported|Stops initializing trivial automatic stack variables after the specified number of instances|
 |-ftrivial-auto-var-init= \<value\>|Supported|Initializes trivial automatic stack variables. Values: uninitialized (default) / pattern|
 |-funique-basic-block-section-names|Supported|Uses unique names for basic block sections (ELF only)|
 |-funique-internal-linkage-names|Supported|Makes the Internal Linkage Symbol names unique by appending the MD5 hash of the module path|
 |-funroll-loops|Supported|Turns on loop unroller|
 |-fuse-flang-math-libs|Supported|Uses Flang internal runtime math library instead of LLVM math intrinsics|
 |-fuse-line-directives|Supported|Uses #line in preprocessed output|
 |-fvalidate-ast-input-files-content|Supported|Computes and stores the hash of input files used to build an AST. Files with mismatching mtimes are considered valid if both have identical contents.|
 |-fveclib= \<value\>|Unsupported|Uses the given vector functions library|
 |-fvectorize|Unsupported|Enables the loop vectorization passes|
 |-fverbose-asm|Supported|Generates verbose assembly output|
 |-fvirtual-function-elimination|Supported|Enables dead virtual function elimination optimization. Requires -flto=full|
 |-fvisibility-global-new-delete-hidden|Supported|Marks the visibility of global C++ operators "new" and "delete" as hidden|
 |-fvisibility-inlines-hidden-static-local-var|Supported|Marks the visibility of static variables in inline C++ member functions as hidden by default when -fvisibility-inlines-hidden is enabled|
 |-fvisibility-inlines-hidden|Supported|Marks the visibility of inline C++ member functions as hidden by default|
 |-fvisibility-ms-compat|Supported|Marks the visibility of global types as default and global functions and variables as hidden by default|
 |-fvisibility= \<value\>|Supported|Sets the default symbol visibility for all global declarations to the specified value|
 |-fwasm-exceptions|Unsupported|Uses WebAssembly style exceptions|
 |-fwhole-program-vtables|Unsupported|Enables whole program vtable optimization. Requires -flto|
 |-fwrapv|Supported|Treats signed integer overflow as two's complement|
 |-fwritable-strings|Supported|Stores string literals as writable data|
 |-fxray-always-emit-customevents|Unsupported|Mandates emitting __xray_customevent(...) calls even if the containing function is not always instrumented|
 |-fxray-always-emit-typedevents|Unsupported|Mandates emitting __xray_typedevent(...) calls even if the containing function is not always instrumented|
 |-fxray-always-instrument=  \<value\>|Unsupported|Deprecated: Specifies the filename defining the whitelist for imbuing the "always instrument" XRay attribute|
 |-fxray-attr-list=  \<value\>|Unsupported|Specifies the filename defining the list of functions/types for imbuing XRay attributes|
 |-fxray-ignore-loops|Unsupported|Prohibits instrumenting functions with loops unless they also meet the minimum function size|
 |-fxray-instruction-threshold=  \<value\>|Unsupported|Sets the minimum function size to instrument with Xray|
 |-fxray-instrumentation-bundle=  \<value\>|Unsupported|Specifies which XRay instrumentation points to emit. Values: all/ none/ function-entry/ function-exit/ function/ custom. Default is "all," and "function" includes both "function-entry" and "function-exit."|
 |-fxray-instrument|Unsupported|Generates XRay instrumentation sleds on function entry and exit|
 |-fxray-link-deps|Unsupported|Informs Clang to add the link dependencies for XRay|
 |-fxray-modes=  \<value\>|Unsupported|Specifies the list of modes to link in by default into the XRay instrumented binaries|
 |-fxray-never-instrument=  \<value\>|Unsupported|Deprecated: Specifies the filename defining the whitelist for imbuing the "never instrument" XRay attribute|
 |-fzvector|Supported|Enables System z vector language extension|
 |-F  \<value\>|Unsupported|Adds directory to the framework include search path|
 |--gcc-toolchain= \<value\>|Supported|Uses the gcc toolchain at the given directory|
 |-gcodeview-ghash|Supported|Emits type record hashes in a .debug$H section|
 |-gcodeview|Supported|Generates code view debug information|
 |-gdwarf-2|Supported|Generates source-level debug information with dwarf version 2|
 |-gdwarf-3|Supported|Generates source-level debug information with dwarf version 3|
 |-gdwarf-4|Supported|Generates source-level debug information with dwarf version 4|
 |-gdwarf-5|Supported|Generates source-level debug information with dwarf version 5|
 |-gdwarf|Supported|Generates source-level debug information with the default DWARF version|
 |-gembed-source|Supported|Embeds source text in DWARF debug sections|
 |-gline-directives-only|Supported|Emits debug line info directives only.|
 |-gline-tables-only|Supported|Emits debug line number tables only.|
 |-gmodules|Supported|Generates debug info with external references to clang modules or precompiled headers|
 |-gno-embed-source|Supported|Restores the default behavior of not embedding the source text in DWARF debug sections|
 |-gno-inline-line-tables|Supported|Prohibits emitting inline line tables|
 |--gpu-max-threads-per-block= \<value\>|Supported|Specifies the default max threads per block for kernel launch bounds for HIP|
 |-gsplit-dwarf= \<value\>|Supported|Sets DWARF fission mode to values: "split"/ "single"|
 |-gz= \<value\>|Supported|Specifies DWARF debug section's compression type|
 |-gz|Supported|Shows DWARF debug section"s compression type|
 |-G  \<size\>|Unsupported|Puts objects of maximum  \<size\> bytes into small data section (MIPS / Hexagon)|
 |-g|Supported|Generates source-level debug information|
 |--help-hidden|Supported|Displays help for hidden options|
 |-help|Supported|Displays available options|
 |--hip-device-lib= \<value\>|Supported|Specifies the HIP device library|
 |--hip-link|Supported|Links clang-offload-bundler bundles for HIP|
 |--hip-version= \<value\>|Supported|Allows specification of HIP version in the format: major/minor/patch|
 |-H|Supported|Shows header "includes" and nesting depth|
 |-I-|Supported|Restricts all prior -I flags to double-quoted inclusion and removes the current directory from include path|
 |-ibuiltininc|Supported|Enables built-in #include directories even when -nostdinc is used before or after -ibuiltininc. Using -nobuiltininc after the option disables it|
 |-idirafter  \<value\>|Supported|Adds the directory to AFTER include search path|
 |-iframeworkwithsysroot  \<directory\>|Unsupported|Adds the directory to SYSTEM framework search path; absolute paths are relative to -isysroot|
 |-iframework  \<value\>|Unsupported|Adds the directory to SYSTEM framework search path|
 |-imacros  \<file\>|Supported|Specifies the file containing macros to be included before parsing|
 |-include-pch  \<file\>|Supported|Includes the specified precompiled header file|
 |-include  \<file\>|Supported|Includes the specified file before parsing|
 |-index-header-map|Supported|Makes the next included directory (-I or -F) an indexer header map|
 |-iprefix  \<dir\>|Supported|Sets the -iwithprefix/-iwithprefixbefore prefix|
 |-iquote  \<directory\>|Supported|Adds the directory to QUOTE include search path|
 |-isysroot  \<dir\>|Supported|Sets the system root directory (usually /)|
 |-isystem-after  \<directory\>|Supported|Adds the directory to end of the SYSTEM include search path|
 |-isystem  \<directory\>|Supported|Adds the directory to SYSTEM include search path|
 |-ivfsoverlay  \<value\>|Supported|Overlays the virtual filesystem described by the specified file over the real file system|
 |-iwithprefixbefore  \<dir\>|Supported|Sets the directory to include search path with prefix|
 |-iwithprefix  \<dir\>|Supported|Sets the directory to SYSTEM include search path with prefix|
 |-iwithsysroot  \<directory\>|Supported|Adds directory to SYSTEM include search path; absolute paths are relative to -isysroot|
 |-I  \<dir\>|Supported|Adds directory to include search path. If there are multiple -I options, these directories are searched in the order they are given before the standard system directories are searched. If the same directory is in the SYSTEM include search paths, for example, if also specified with -isystem, the -I option is ignored.|
 |--libomptarget-nvptx-path= \<value\>|Unsupported|Specifies path to libomptarget-nvptx libraries|
 |-L  \<dir\>|Supported|Adds directory to library search path|
 |-mabicalls|Unsupported|Enables SVR4-style position-independent code (Mips only)|
 |-maix-struct-return|Unsupported|Returns all structs in memory (PPC32 only)|
 |-malign-branch-boundary= \<value\>|Supported|Specifies the boundary's size to align branches|
 |-malign-branch= \<value\>|Supported|Specifies the types of branches to align|
 |-malign-double|Supported|Aligns doubles to two words in structs (x86 only)|
 |-Mallocatable= \<value\>|Unsupported|Provides semantics for assignments to allocatables. Value: F03/ F95.|
 |-mbackchain|Unsupported|Links stack frames through backchain on System Z|
 |-mbranch-protection= \<value\>|Unsupported|Enforces targets of indirect branches and function returns|
 |-mbranches-within-32B-boundaries|Supported|Aligns selected branches (fused, jcc, jmp) within 32-byte boundary|
 |-mcmodel=medany|Unsupported|Equivalent to -mcmodel=medium, compatible with RISC-V gcc|
 |-mcmodel=medlow|Unsupported|Equivalent to -mcmodel=small, compatible with RISC-V gcc|
 |-mcmse|Unsupported|Allows use of CMSE (Armv8-M Security Extensions)|
 |-mcode-object-v3|Supported|Legacy option to specify code object ABI V2 (-mnocode-object-v3) or V3 (-mcode-object-v3) (AMDGPU only)|
 |-mcode-object-version= \<version\>|Supported|Specifies code object ABI version. Default value: 4. (AMDGPU only).|
 |-mcrc|Unsupported|Allows use of CRC instructions (ARM/Mips only)|
 |-mcumode|Supported|Specifies CU (-mcumode) or WGP (-mno-cumode) wavefront execution mode (AMDGPU only)|
 |-mdouble= \<value\>|Supported|Forces double to be 32 bits or 64 bits|
 |-MD|Supported|Writes a depfile containing user and system headers|
 |-meabi  \<value\>|Supported|Sets EABI type. Value: 4/ 5/ gnu. Default depends on triple|
 |-membedded-data|Unsupported|Places constants in the .rodata section instead of the .sdata section even if they meet the -G  \<size\> threshold (MIPS)|
 |-menable-experimental-extensions|Unsupported|Enables usage of experimental RISC-V extensions.|
 |-mexec-model= \<value\>|Unsupported|Specifies the execution model (WebAssembly only)|
 |-mexecute-only|Unsupported|Disallows generation of data access to code sections (ARM only)|
 |-mextern-sdata|Unsupported|Assumes externally defined data to be in the small data if it meets the -G  \<size\> threshold (MIPS)|
 |-mfentry|Unsupported|Inserts calls to fentry at function entry (x86/SystemZ only)|
 |-mfix-cortex-a53-835769|Unsupported|Workaround Cortex-A53 erratum 835769 (AArch64 only)|
 |0|Unsupported|Asserts usage of 32-bit floating point registers (MIPS only)|
 |0|Unsupported|Asserts usage of 64-bit floating point registers (MIPS only)|
 |-MF  \<file\>|Supported|Writes depfile output from -MMD, -MD, -MM, or -M to  \<file\>|
 |-mgeneral-regs-only|Unsupported|Generates code that exclusively uses the general-purpose registers (AArch64 only)|
 |-mglobal-merge|Supported|Enables merging of globals|
 |-mgpopt|Unsupported|Allows using GP relative accesses for symbols known to be in a small data section (MIPS)|
 |-MG|Supported|Adds missing headers to depfile|
 |-mharden-sls= \<value\>|Unsupported|Sets straight-line speculation hardening scope|
 |-mhvx-length= \<value\>|Unsupported|Sets Hexagon Vector Length|
 |-mhvx= \<value\>|Unsupported|Sets Hexagon Vector eXtensions|
 |-mhvx|Unsupported|Enables Hexagon Vector eXtensions|
 |-miamcu|Unsupported|Allows using Intel MCU ABI|
 |--migrate|Unsupported|Runs the migrator|
 |-mincremental-linker-compatible|Supported|(integrated-as) Emits an object file that can be used with an incremental linker|
 |-mindirect-jump= \<value\>|Unsupported|Changes indirect jump instructions to inhibit speculation|
 |-Minform= \<value\>|Supported|Sets error level of messages to display|
 |-mios-version-min= \<value\>|Unsupported|Sets iOS deployment target|
 |-MJ  \<value\>|Unsupported|Writes a compilation database entry per input|
 |-mllvm  \<value\>|Supported|Specifies additional arguments to forward to LLVM's option processing|
 |-mlocal-sdata|Unsupported|Extends the -G behavior to object local data (MIPS)|
 |-mlong-calls|Supported|Generates branches with extended addressability, usually via indirect jumps|
 |-mlong-double-128|Supported on Host only|Forces long double to be 128 bits|
 |-mlong-double-64|Supported|Forces long double to be 64 bits|
 |-mlong-double-80|Supported on Host only|Forces long double to be 80 bits, padded to 128 bits for storage|
 |-mlvi-cfi|Supported on Host only|Enables only control-flow mitigations for Load Value Injection (LVI)|
 |-mlvi-hardening|Supported on Host only|Enables all mitigations for Load Value Injection (LVI)|
 |-mmacosx-version-min= \<value\>|Unsupported|Sets Mac OS X deployment target|
 |-mmadd4|Supported|Enables the generation of 4-operand madd.s, madd.d, and related instructions|
 |-mmark-bti-property|Unsupported|Adds .note.gnu.property with BTI to assembly files (AArch64 only)|
 |-MMD|Supported|Writes a depfile containing user headers|
 |-mmemops|Supported|Enables generation of memop instructions|
 |-mms-bitfields|Unsupported|Sets the default structure layout to be compatible with the Microsoft compiler standard|
 |-mmsa|Unsupported|Enables MSA ASE (MIPS only)|
 |-mmt|Unsupported|Enables MT ASE (MIPS only)|
 |-MM|Supported|Similar to -MMD but also implies -E and writes to stdout by default|
 |-mno-abicalls|Unsupported|Disables SVR4-style position-independent code (Mips only)|
 |-mno-crc|Unsupported|Disallows use of CRC instructions (MIPS only)|
 |-mno-embedded-data|Unsupported|Prohibits placing constants in the .rodata section instead of the .sdata if they meet the -G  \<size\> threshold (MIPS)|
 |-mno-execute-only|Unsupported|Allows generation of data access to code sections (ARM only)|
 |-mno-extern-sdata|Unsupported|Prohibits assuming the externally defined data to be in the small data if it meets the -G  \<size\> threshold (MIPS)|
 |-mno-fix-cortex-a53-835769|Unsupported|Disallows workaround Cortex-A53 erratum 835769 (AArch64 only)|
 |-mno-global-merge|Supported|Disables merging of globals|
 |-mno-gpopt|Unsupported|Prohibits using GP relative accesses for symbols known to be in a small data section (MIPS)|
 |-mno-hvx|Unsupported|Disables Hexagon Vector eXtensions.|
 |-mno-implicit-float|Supported|Prohibits generating implicit floating-point instructions|
 |-mno-incremental-linker-compatible|Supported|(integrated-as) Emits an object file that cannot be used with an incremental linker|
 |-mno-local-sdata|Unsupported|Prohibits extending the -G behavior to object local data (MIPS)|
 |-mno-long-calls|Supported|Restores the default behavior of not generating long calls|
 |-mno-lvi-cfi|Supported on Host only|Disables control-flow mitigations for Load Value Injection (LVI)|
 |-mno-lvi-hardening|Supported on Host only|Disables mitigations for Load Value Injection (LVI)|
 |-mno-madd4|Supported|Disables the generation of 4-operand madd.s, madd.d, and related instructions|
 |-mno-memops|Supported|Disables the generation of memop instructions|
 |-mno-movt|Supported|Disallows usage of movt/movw pairs (ARM only)|
 |-mno-ms-bitfields|Supported|Prohibits setting the default structure layout to be compatible with the Microsoft compiler standard|
 |-mno-msa|Unsupported|Disables MSA ASE (MIPS only)|
 |-mno-mt|Unsupported|Disables MT ASE (MIPS only)|
 |-mno-neg-immediates|Supported|Disallows converting instructions with negative immediates to their negation or inversion|
 |-mno-nvj|Supported|Disables generation of new-value jumps|
 |-mno-nvs|Supported|Disables generation of new-value stores|
 |-mno-outline|Unsupported|Disables function outlining (AArch64 only)|
 |-mno-packets|Supported|Disables generation of instruction packets|
 |-mno-relax|Supported|Disables linker relaxation|
 |-mno-restrict-it|Unsupported|Allows generation of deprecated IT blocks for ARMv8. It is off by default for ARMv8 Thumb mode|
 |-mno-save-restore|Unsupported|Disables usage of library calls for save and restore|
 |-mno-seses|Unsupported|Disables speculative execution side-effect suppression (SESES)|
 |-mno-stack-arg-probe|Supported|Disables stack probes which are enabled by default|
 |-mno-tls-direct-seg-refs|Supported|Disables direct TLS access through segment registers|
 |-mno-unaligned-access|Unsupported|Forces all memory accesses to be aligned (AArch32/AArch64 only)|
 |-mno-wavefrontsize64|Supported|Asserts wavefront size to 32 (AMDGPU only)|
 |-mnocrc|Unsupported|Disallows usage of CRC instructions (ARM only)|
 |-mnop-mcount|Supported|Generates `mcount`/`__fentry__` calls as nops. To activate, they need to be patched in|
 |-mnvj|Supported|Enables generation of new-value jumps|
 |-mnvs|Supported|Enables generation of new-value stores|
 |-module-dependency-dir  \<value\>|Unsupported|Specifies directory for dumping module dependencies|
 |-module-file-info|Unsupported|Provides information about a particular module file|
 |-momit-leaf-frame-pointer|Supported|Omits frame pointer setup for leaf functions|
 |-moutline|Unsupported|Enables function outlining (AArch64 only)|
 |-mpacked-stack|Unsupported|Asserts the usage of packed stack layout (SystemZ only)|
 |-mpackets|Supported|Enables generation of instruction packets|
 |-mpad-max-prefix-size= \<value\>|Supported|Specifies maximum number of prefixes to use for padding|
 |-mpie-copy-relocations|Supported|Asserts the usage of copy relocations support for PIE builds|
 |-mprefer-vector-width= \<value\>|Unsupported|Specifies preferred vector width for auto-vectorization. Default value: "none," which allows target specific decisions.|
 |-MP|Supported|Creates phony target for each dependency (other than the main file)|
 |-mqdsp6-compat|Unsupported|Enables hexagon-qdsp6 backward compatibility|
 |-MQ  \<value\>|Supported|Specifies the name of the main file output to quote in depfile|
 |-mrecord-mcount|Supported|Generates a __mcount_loc section entry for each fentry call|
 |-mrelax-all|Supported|(integrated-as) Relaxes all machine instructions|
 |-mrelax|Supported|Enables linker relaxation|
 |-mrestrict-it|Unsupported|Disallows generation of deprecated IT blocks for ARMv8. It is on by default for ARMv8 Thumb mode.|
 |-mrtd|Unsupported|Makes StdCall calling the default convention|
 |-msave-restore|Unsupported|Enables using library calls for save and restore|
 |-mseses|Unsupported|Enables speculative execution side effect suppression (SESES). Includes LVI control flow integrity mitigations.|
 |-msign-return-address= \<value\>|Unsupported|Specifies the return address signing scope|
 |-msmall-data-limit= \<value\>|Supported|Puts global and static data smaller than the specified limit into a special section|
 |-msoft-float|Supported|Uses software floating point|
 |-msram-ecc|Supported|Legacy option to specify SRAM ECC mode (AMDGPU only). Should use --offload-arch with sramecc+ instead.|
 |-mstack-alignment= \<value\>|Unsupported|Sets the stack alignment|
 |-mstack-arg-probe|Unsupported|Enables stack probes|
 |-mstack-probe-size= \<value\>|Unsupported|Sets the stack probe size|
 |-mstackrealign|Unsupported|Forces realign the stack at entry on every function|
 |-msve-vector-bits= \<value\>|Unsupported|Specifies the size in bits of an SVE vector register. Defaults to the vector length agnostic value of "scalable" (AArch64 only).|
 |-msvr4-struct-return|Unsupported|Returns small structs in registers (PPC32 only)|
 |-mthread-model  \<value\>|Supported|Specifies the thread model to use. Value: posix/single. Default: posix.|
 |-mtls-direct-seg-refs|Supported|Enables direct TLS access through segment registers (default)|
 |-mtls-size= \<value\>|Unsupported|Specifies the bit size of immediate TLS offsets (AArch64 ELF only). Value: 12 (for 4KB) \ 24 (for 16MB, default) \ 32 (for 4GB) \ 48 (for 256TB, needs -mcmodel=large).|
 |-mtp= \<value\>|Unsupported|Specifies the thread pointer access method. Value: AArch32/AArch64 only|
 |-mtune= \<value\>|Supported on Host only|Supported on X86 only. Otherwise accepted for compatibility with GCC.|
 |-MT  \<value\>|Unsupported|Specifies the name of main file output in depfile|
 |-munaligned-access|Unsupported|Allows memory accesses to be unaligned (AArch32/AArch64 only)|
 |-MV|Supported|Uses NMake/Jom format for the depfile|
 |-mwavefrontsize64|Supported|Asserts wavefront size of 64 (AMDGPU only)|
 |-mxnack|Supported|Legacy option to specify XNACK mode (AMDGPU only). Use --offload-arch with :xnack+ instead.|
 |-M|Supported|Similar to -MD but also implies -E and writes to stdout by default|
 |--no-cuda-include-ptx= \<value\>|Supported|Prohibits including PTX for the specified GPU architecture (e.g. sm_35) or "all". May be specified more than once.|
 |--no-cuda-version-check|Supported|Disallows erroring out if the detected version of the CUDA install is too low for the requested CUDA GPU architecture|
 |-no-flang-libs|Supported|Prohibits linking against Flang libraries|
 |--no-offload-arch= \<value\>|Supported|Removes CUDA/HIP offloading device architecture (e.g. sm_35, gfx906) from the list of devices to compile for. "all" resets the list to its default value|
 |--no-system-header-prefix= \<prefix\>|Supported|Assumes no system header for all #include paths starting with the given  \<prefix\>|
 |-nobuiltininc|Supported|Disables built-in #include directories|
 |-nogpuinc|Supported|Prohibits adding CUDA/HIP include paths and includes default CUDA/HIP wrapper header files|
 |-nogpulib|Supported|Prohibits linking device library for CUDA/HIP device compilation|
 |-nostdinc++|Unsupported|Disables standard #include directories for the C++ standard library|
 |-ObjC++|Unsupported|Treats source input files as Objective-C++ inputs|
 |-objcmt-atomic-property|Unsupported|Enables migration to "atomic" properties|
 |-objcmt-migrate-all|Unsupported|Enables migration to modern ObjC|
 |-objcmt-migrate-annotation|Unsupported|Enables migration to property and method annotations|
 |-objcmt-migrate-designated-init|Unsupported|Enables migration to infer NS_DESIGNATED_INITIALIZER for initializer methods|
 |-objcmt-migrate-instancetype|Unsupported|Enables migration to infer instancetype for method result type|
 |-objcmt-migrate-literals|Unsupported|Enables migration to modern ObjC literals|
 |-objcmt-migrate-ns-macros|Unsupported|Enables migration to NS_ENUM/NS_OPTIONS macros|
 |-objcmt-migrate-property-dot-syntax|Unsupported|Enables migration of setter/getter messages to property-dot syntax|
 |-objcmt-migrate-property|Unsupported|Enables migration to modern ObjC property|
 |-objcmt-migrate-protocol-conformance|Unsupported|Enables migration to add protocol conformance on classes|
 |-objcmt-migrate-readonly-property|Unsupported|Enables migration to modern ObjC readonly property|
 |-objcmt-migrate-readwrite-property|Unsupported|Enables migration to modern ObjC readwrite property|
 |-objcmt-migrate-subscripting|Unsupported|Enables migration to modern ObjC subscripting|
 |-objcmt-ns-nonatomic-iosonly|Unsupported|Enables migration to use NS_NONATOMIC_IOSONLY macro for setting property's "atomic" attribute|
 |-objcmt-returns-innerpointer-property|Unsupported|Enables migration to annotate property with NS_RETURNS_INNER_POINTER|
 |-objcmt-whitelist-dir-path= \<value\>|Unsupported|Modifies exclusively the files with the filename present in the given directory|
 |-ObjC|Unsupported|Treats source input files as Objective-C inputs|
 |--offload-arch= \<value\>|Supported|Specifies CUDA offloading device architecture (e.g. sm_35), or HIP offloading target ID in the form of a device architecture followed by target ID features delimited by a colon. Each target ID feature is a predefined string followed by a plus or minus sign (e.g. gfx908:xnack+:sramecc-). May be specified more than once.|
 |-o  \<file\>|Supported|Writes output to the given  \<file\>|
 |-parallel-jobs= \<value\>|Supported|Specifies the number of parallel jobs allowed|
 |-pg|Supported|Enables mcount instrumentation|
 |-pipe|Supported|Asserts using pipes between commands, when possible.|
 |--precompile|Supported|Only precompiles the input|
 |-print-effective-triple|Supported|Prints the effective target triple|
 |-print-file-name= \<file\>|Supported|Prints the full library path of the given  \<file\>|
 |-print-ivar-layout|Unsupported|Enables Objective-C Ivar layout bitmap print trace|
 |-print-libgcc-file-name|Supported|"Prints the library path for the currently used compiler runtime library (""libgcc.a"" or ""libclang_rt.builtins.*.a"")"|
 |-print-prog-name= \<name\>|Supported|Prints the full program path of the given  \<name\>|
 |-print-resource-dir|Supported|Prints the resource directory pathname|
 |-print-search-dirs|Supported|Prints the paths used for finding libraries and programs|
 |-print-supported-cpus|Supported|Prints the supported CPU models for the given target. If target is not specified, it prints the supported CPUs for the default target.|
 |-print-target-triple|Supported|Prints the normalized target triple|
 |-print-targets|Supported|Prints the registered targets|
 |-pthread|Supported|Supports POSIX threads in the generated code|
 |--ptxas-path= \<value\>|Unsupported|Specifies the path to ptxas (used for compiling CUDA code)|
 |-P|Supported|Disables linemarker output in -E mode|
 |-Qn|Supported|Prohibits emitting metadata containing compiler name and version|
 |-Qunused-arguments|Supported|Prohibits emitting warning for unused driver arguments|
 |-Qy|Supported|Emits metadata containing compiler name and version|
 |-relocatable-pch|Supported|Allows to build a relocatable precompiled header|
 |-rewrite-legacy-objc|Unsupported|Rewrites Legacy Objective-C source to C++|
 |-rewrite-objc|Unsupported|Rewrites Objective-C source to C++|
 |--rocm-device-lib-path= \<value\>|Supported|Specifies ROCm device library path. Alternative to rocm-path|
 |--rocm-path= \<value\>|Supported|Specifies ROCm installation path that is used for finding and automatically linking required bitcode libraries|
 |-Rpass-analysis= \<value\>|Supported|Reports transformation analysis by optimization passes whose names match the given POSIX regular expression|
 |-Rpass-missed= \<value\>|Supported|Reports missed transformations by optimization passes whose names match the given POSIX regular expression|
 |-Rpass= \<value\>|Supported|Reports transformations by optimization passes whose names match the given POSIX regular expression|
 |-rtlib= \<value\>|Unsupported|Specifies the compiler runtime library to be used|
 |-R \<remark\>|Unsupported|Enables the specified remark|
 |-save-stats= \<value\>|Supported|Saves llvm statistics|
 |-save-stats|Supported|Saves llvm statistics|
 |-save-temps= \<value\>|Supported|Saves intermediate compilation results|
 |-save-temps|Supported|Saves intermediate compilation results|
 |-serialize-diagnostics=  \<value\>|Supported|Serializes compiler diagnostics to the specified file|
 |-shared-libsan|Unsupported|Dynamically links the sanitizer runtime|
 |-static-flang-libs|Supported|Asserts linking using static Flang libraries|
 |-static-libsan|Unsupported|Statically links the sanitizer runtime|
 |-static-openmp|Supported|Asserts using the static host OpenMP runtime while linking|
 |-std= \<value\>|Supported|Specifies the language standard to compile for.|
 |-stdlib++-isystem  \<directory\>|Supported|Specifies the directory to be used as the C++ standard library include path|
 |-stdlib= \<value\>|Supported|Specifies the C++ standard library to be used|
 |-sycl-std= \<value\>|Unsupported|Specifies the SYCL language standard to compile for|
 |--system-header-prefix= \<prefix\>|Supported|Assumes all #include paths starting with the given  \<prefix\> to include a system header|
 |-S|Supported|Runs only preprocess and compilation steps|
 |--target= \<value\>|Supported|Generates code for the given target|
 |-Tbss  \<addr\>|Supported|Sets the starting address of BSS to the given  \<addr\>|
 |-Tdata  \<addr\>|Supported|Sets the starting address of DATA to the given  \<addr\>|
 |-time|Supported|Times individual commands|
 |-traditional-cpp|Unsupported|Enables some traditional CPP emulation|
 |-trigraphs|Supported|Processes trigraph sequences|
 |-Ttext  \<addr\>|Supported|Sets starting address of TEXT to the given  \<addr\>|
 |-T \ \<script\\>|Unsupported|Specifies the given. \ \<script\\> as linker script|
 |-undef|Supported|undefs all system defines|
 |-unwindlib= \<value\>|Supported|Specifies the unwind library to be used|
 |-U  \<macro\>|Supported|Undefines the given  \<macro\>|
 |--verify-debug-info|Supported|Verifies the binary representation of the debug output|
 |-verify-pch|Unsupported|Loads and verifies if a precompiled header file is stale|
 |--version|Supported|Prints version information|
 |-v|Supported|Shows commands to be run, and uses verbose output|
 |-Wa, \<arg\>|Supported|Passes the comma-separated arguments in the given  \<arg\> to the assembler|
 |-Wdeprecated|Supported|Enables warnings for deprecated constructs and defines_DEPRECATED|
 |-Wl, \<arg\>|Supported|Passes comma-separated arguments in  \<arg\> to the linker.|
 |-working-directory  \<value\>|Supported|Resolves file paths relative to the specified directory|
 |-Wp, \<arg\>|Supported|Passes comma-separated arguments in  \<arg\> to the preprocessor|
 |-W \<warning\>|Supported|Enables the specified warning|
 |-w|Supported|Suppresses all warnings|
 |-Xanalyzer  \<arg\>|Supported|Passes  \<arg\> to the static analyzer|
 |-Xarch_device  \<arg\>|Supported|Passes  \<arg\> to the CUDA/HIP device compilation|
 |-Xarch_host  \<arg\>|Supported|Passes  \<arg\> to the CUDA/HIP host compilation|
 |-Xassembler  \<arg\>|Supported|Passes  \<arg\> to the assembler|
 |-Xclang  \<arg\>|Supported|Passes  \<arg\> to the clang compiler|
 |-Xcuda-fatbinary  \<arg\>|Supported|Passes  \<arg\> to fatbinary invocation|
 |-Xcuda-ptxas  \<arg\>|Supported|Passes  \<arg\> to the ptxas assembler|
 |-Xlinker  \<arg\>|Supported|Passes  \<arg\> to the linker|
 |-Xopenmp-target= \<triple\>  \<arg\>|Supported|Passes  \<arg\> to the target offloading toolchain identified by  \<triple\>|
 |-Xopenmp-target  \<arg\>|Supported|Passes  \<arg\> to the target offloading toolchain|
 |-Xpreprocessor  \<arg\>|Supported|Passes  \<arg\> to the preprocessor|
 |-x  \<language\>|Supported|Assumes subsequent input files to have the given type  \<language\>|
 |-z  \<arg\>|Supported|Passes -z  \<arg\> to the linker|
:::
<!-- spellcheck-enable -->
