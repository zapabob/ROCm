# Using the LLVM Address Sanitizer (ASAN) on the GPU

The LLVM Address Sanitizer provides a process that allows developers to detect runtime addressing errors in applications and libraries. The detection is achieved using a combination of compiler-added instrumentation and runtime techniques, including function interception and replacement.

Until now, the LLVM Address Sanitizer process was only available for traditional purely CPU applications. However, ROCm has extended this mechanism to additionally allow the detection of some addressing errors on the GPU in heterogeneous applications. Ideally, developers should treat heterogeneous HIP and OpenMP applications exactly like pure CPU applications. However, this simplicity has not been achieved yet.

This document provides documentation on using ROCm Address Sanitizer.
For information about LLVM Address Sanitizer, see [the LLVM documentation](https://clang.llvm.org/docs/AddressSanitizer.html).

## Compile for Address Sanitizer

The address sanitizer process begins by compiling the application of interest with the address sanitizer instrumentation.

Recommendations for doing this are:

* Compile as many application and dependent library sources as possible using an AMD-built clang-based compiler such as `amdclang++`.
* Add the following options to the existing compiler and linker options:
  * `-fsanitize=address` - enables instrumentation
  * `-shared-libsan` - use shared version of runtime
  * `-g` - add debug info for improved reporting
* Explicitly use `xnack+` in the offload architecture option. For example, `--offload-arch=gfx90a:xnack+`
Other architectures are allowed, but their device code will not be instrumented and a warning will be emitted.

It is not an error to compile some files without address sanitizer instrumentation, but doing so reduces the ability of the process to detect addressing errors. However, if the main program "`a.out`" does not directly depend on the Address Sanitizer runtime (`libclang_rt.asan-x86_64.so`) after the build completes (check by running `ldd` (List Dynamic Dependencies) or `readelf`), the application will immediately report an error at runtime as described in the next section.

### About Compilation Time

When `-fsanitize=address` is used, the LLVM compiler adds instrumentation code around every memory operation. This added code must be handled by all of the downstream components of the compiler toolchain and results in increased overall compilation time. This increase is especially evident in the AMDGPU device compiler and has in a few instances raised the compile time to an unacceptable level.

There are a few options if the compile time becomes unacceptable:

* Avoid instrumentation of the files which have the worst compile times. This will reduce the effectiveness of the address sanitizer process.
* Add the option `-fsanitize-recover=address` to the compiles with the worst compile times. This option simplifies the added instrumentation resulting in faster compilation. See below for more information.
* Disable instrumentation on a per-function basis by adding `__attribute__`((no_sanitize("address"))) to functions found to be responsible for the large compile time. Again, this will reduce the effectiveness of the process.

## Use AMD Supplied Address Sanitizer Instrumented Libraries

ROCm releases provide optional packages containing address sanitizer instrumented builds of a subset of those ROCm libraries usually found in `/opt/rocm-<version>/lib`. These optional packages are typically named <library>-asan. However, the instrumented libraries themselves have identical names as the regular uninstrumented libraries and are located in `/opt/rocm-<version>/lib/asan`. It is expected that the subset of address sanitizer instrumented ROCm libraries will be expanded in future releases. They are built using the `amdclang++` and `hipcc` compilers, while some uninstrumented libraries are built with g++. The preexisting build options are used, but, as described above, additional options are used: `-fsanitize=address`, `-shared-libsan` and `-g`.

These additional libraries avoid additional developer effort to locate repositories, identify the correct branch, check out the correct tags, and other efforts needed to build the libraries from the source. And they extend the ability of the process to detect addressing errors into the ROCm libraries themselves.

When adjusting an application build to add instrumentation, linking against these instrumented libraries is unnecessary. For example, any `-L` `/opt/rocm-<version>/lib` compiler options need not be changed. However, the instrumented libraries should be used when the application is run. It is particularly important that the instrumented language runtimes, like `libamdhip64.so` and `librocm-core.so`, are used; otherwise, device invalid access detections may not be reported.

## Running Address Sanitizer Instrumented Applications

### Preparing to Run an Instrumented Application

Here are a few recommendations to consider before running an address sanitizer instrumented heterogeneous application.

* Ensure the Linux kernel running on the system has Heterogeneous Memory Management (HMM) support. A kernel version of 5.6 or higher should be sufficient.
* Ensure XNACK is enabled
  * For `gfx90a` (MI-2X0) or `gfx940` (MI-3X0) use environment `HSA_XNACK = 1`.
  * For `gfx906` (MI-50) or `gfx908` (MI-100) use environment `HSA_XNACK = 1` but also ensure the amdgpu kernel module is loaded with module argument `noretry=0`.  
This requirement is due to the fact that the XNACK setting for these GPUs is system-wide.

* Ensure that the application will use the instrumented libraries when it runs. The output from the shell command `ldd <application name>` can be used to see which libraries will be used.
If the instrumented libraries are not listed by `ldd`, the environment variable `LD_LIBRARY_PATH` may need to be adjusted, or in some cases an `RPATH` compiled into the application may need to be changed and the application recompiled.

* Ensure that the application depends on the address sanitizer runtime. This can be checked by running the command `readelf -d <application name> | grep NEEDED` and verifying that shared library: `libclang_rt.asan-x86_64.so` appears in the output.
If it does not appear, when executed the application will quickly output an address sanitizer error that looks like:

```bash
==3210==ASan runtime does not come first in initial library list; you should either link runtime to your application or manually preload it with LD_PRELOAD.
```

* Ensure that the application `llvm-symbolizer` can be executed, and that it is located in `/opt/rocm-<version>/llvm/bin`. This executable is not strictly required, but if found is used to translate ("symbolize") a host-side instruction address into a more useful function name, file name, and line number (assuming the application has been built to include debug information).

There is an environment variable, `ASAN_OPTIONS` which can be used to adjust the runtime behavior of the ASAN runtime itself. There are more than a hundred "flags" that can be adjusted (see an old list at [flags](https://github.com/google/sanitizers/wiki/AddressSanitizerFlags)) but the default settings are correct and should be used in most cases. It must be noted that these options only affect the host ASAN runtime. The device runtime only currently supports the default settings for the few relevant options.

There are two `ASAN_OPTION` flags of particular note.

* `halt_on_error=0/1 default 1`.  

This tells the ASAN runtime to halt the application immediately after detecting and reporting an addressing error. The default makes sense because the application has entered the realm of undefined behavior. If the developer wishes to have the application continue anyway, this option can be set to zero. However, the application and libraries should then be compiled with the additional option `-fsanitize-recover=address`. Note that the ROCm optional address sanitizer instrumented libraries are not compiled with this option and if an error is detected within one of them, but halt_on_error is set to 0, more undefined behavior will occur.

* `detect_leaks=0/1 default 1`.
This option directs the address sanitizer runtime to enable the [Leak Sanitizer](https://clang.llvm.org/docs/LeakSanitizer.html) (LSAN). Unfortunately, for heterogeneous applications, this default will result in significant output from the leak sanitizer when the application exits due to allocations made by the language runtime which are not considered to be to be leaks. This output can be avoided by adding `detect_leaks=0` to the `ASAN_OPTIONS`, or alternatively by producing an LSAN suppression file (syntax described [here](https://github.com/google/sanitizers/wiki/AddressSanitizerLeakSanitizer)) and activating it with environment variable `LSAN_OPTIONS=suppressions=/path/to/suppression/file`. When using a suppression file, a suppression report is printed by default. The suppression report can be disabled by using the `LSAN_OPTIONS` flag `print_suppressions=0`.

## Runtime Overhead

Running an address sanitizer instrumented application incurs
overheads which may result in unacceptably long runtimes
or failure to run at all.

### Higher Execution Time

Address sanitizer detection works by checking each address at runtime
before the address is actually accessed by a load, store, or atomic
instruction.
This checking involves an additional load to "shadow" memory which
records whether the address is "poisoned" or not, and additional logic
that decides whether to produce an detection report or not.

This extra runtime work can cause the application to slow down by
a factor of three or more, depending on how many memory accesses are
executed.
For heterogeneous applications, the shadow memory must be accessible by all devices
and this can mean that shadow accesses from some devices may be more costly
than non-shadow accesses.

### Higher Memory Use

The address checking described above relies on the compiler to surround
each program variable with a red zone and on address sanitizer
runtime to surround each runtime memory allocation with a red zone and
fill the shadow corresponding to each red zone with poison.
The added memory for the red zones is additional overhead on top
of the 13% overhead for the shadow memory itself.

Applications which consume most one or more available memory pools when
run normally are likely to encounter allocation failures when run with
instrumentation.

## Runtime Reporting

It is not the intention of this document to provide a detailed explanation of all of the types of reports that can be output by the address sanitizer runtime. Instead, the focus is on the differences between the standard reports for CPU issues, and reports for GPU issues.

An invalid address detection report for the CPU always starts with

```bash
==<PID>==ERROR: AddressSanitizer: <problem type> on address <memory address> at pc <pc> bp <bp> sp <sp> <access> of size <N> at <memory address> thread T0
```

and continues with a stack trace for the access, a stack trace for the allocation and deallocation, if relevant, and a dump of the shadow near the <memory address>.

In contrast, an invalid address detection report for the GPU always starts with

```bash
==<PID>==ERROR: AddressSanitizer: <problem type> on amdgpu device <device> at pc <pc> <access> of size <n> in workgroup id (<X>,<Y>,<Z>)
```

Above, `<device>` is the integer device ID, and `(<X>, <Y>, <Z>)` is the ID of the workgroup or block where the invalid address was detected.

While the CPU report include a call stack for the thread attempting the invalid access, the GPU is currently to a call stack of size one, i.e. the (symbolized) of the invalid access, e.g.

```bash
#0 <pc> in <fuction signature> at /path/to/file.hip:<line>:<column>
```

This short call stack is followed by a GPU unique section that looks like

```bash
Thread ids and accessed addresses:
<lid0> <maddr 0> : <lid1> <maddr1> : ...
```

where each `<lid j> <maddr j>` indicates the lane ID and the invalid memory address held by lane `j` of the wavefront attempting the invalid access.

Additionally, reports for invalid GPU accesses to memory allocated by GPU code via `malloc` or new starting with, for example,

```bash
==1234==ERROR: AddressSanitizer: heap-buffer-overflow on amdgpu device 0 at pc 0x7fa9f5c92dcc
```

or

```bash
==5678==ERROR: AddressSanitizer: heap-use-after-free on amdgpu device 3 at pc 0x7f4c10062d74
```

currently may include one or two surprising CPU side tracebacks mentioning :`hostcall`". This is due to how `malloc` and `free` are implemented for GPU code and these call stacks can be ignored.

## Running with `rocgdb`

`rocgdb` can be used to further investigate address sanitizer detected errors, with some preparation.

Currently, the address sanitizer runtime complains when starting `rocgdb` without preparation.

```bash
$ rocgdb my_app
==1122==ASan` runtime does not come first in initial library list; you should either link runtime to your application or manually preload it with LD_PRELOAD.
```

This is solved by setting environment variable `LD_PRELOAD` to the path to the address sanitizer runtime, whose path can be obtained using the command

```bash
amdclang++ -print-file-name=libclang_rt.asan-x86_64.so
```

It is also recommended to set the environment variable `HIP_ENABLE_DEFERRED_LOADING=0` before debugging HIP applications.

After starting `rocgdb` breakpoints can be set on the address sanitizer runtime error reporting entry points of interest. For example, if an address sanitizer error report includes

```bash
WRITE of size 4 in workgroup id (10,0,0)
```

the `rocgdb` command needed to stop the program before the report is printed is

```bash
(gdb) break __asan_report_store4
```

Similarly, the appropriate command for a report including

```bash
READ of size <N> in workgroup ID (1,2,3)
```

is

```bash
(gdb) break __asan_report_load<N>
```

It is possible to set breakpoints on all address sanitizer report functions using these commands:

```bash
$ rocgdb <path to application>
(gdb) start <commmand line arguments>
(gdb) rbreak ^__asan_report
(gdb) c
```

## Using Address Sanitizer with a Short HIP Application (LINK NEEDED HERE)

## Known Issues with Using GPU Sanitizer

* Red zones must have limited size and it is possible for an invalid access to completely miss a red zone and not be detected.

* Lack of detection or false reports can be caused by the runtime not properly maintaining red zone shadows.

* Lack of detection on the GPU might also be due to the implementation not instrumenting accesses to all GPU specific address spaces. For example, in the current implementation accesses to "private" or "stack" variables on the GPU are not instrumented, and accesses to HIP shared variables (also known as "local data store" or "LDS") are also not instrumented.

* It can also be the case that a memory fault is hit for an invalid address even with the instrumentation. This is usually caused by the invalid address being so wild that its shadow address is outside of any memory region, and the fault actually occurs on the access to the shadow address. It is also possible to hit a memory fault for the `NULL` pointer. While address 0 does have a shadow location, it is not poisoned by the runtime.
