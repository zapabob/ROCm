# ROCm File Reorganization White Paper

## Introduction

ROCm™ packages have adopted the Linux foundation file system hierarchy standard
to ensure ROCm components follow open source conventions for Linux-based
distributions. Following is the ROCm proposed file structure.

```none
/opt/rocm-<ver>
    | -- bin
         | -- all public binaries
    | -- lib
         | -- lib<soname>.so->lib<soname>.so.major->lib<soname>.so.major.minor.patch
              (public libaries to link with applications)
         | -- <component> 
              | -- architecture dependent libraries and binaries used internally by components
         | -- cmake
              | -- <component>
                   | --<component>.config.cmake
    | -- libexec
         | -- <component> 
              | -- non ISA/architecture independent executables used internally by components
    | -- include
         | -- <component>
              | -- public header files
    | -- share
         | -- html
              | -- <component>
                   | -- html documentation
         | -- info
              | -- <component>
                   | -- info files
         | -- man
              | -- <component>
                   | -- man pages
         | -- doc
              | -- <component>
                   | -- license files
         | -- <component>
              | -- samples
              | -- architecture independent misc files
```

## Changes from earlier ROCm versions

ROCm with the file reorganization is going to have a lean structure. Following
table gives the comparison with new and old folder structure.

```none
 ______________________________________________________
|  New File Structure         |  Old File Structure    |
|_____________________________|________________________|
| /opt/rocm-<ver>             | /opt/rocm-<ver>        |
|     | -- bin                |     | -- bin           |
|     | -- lib                |     | -- lib           |
|          | -- cmake         |     | -- include       |
|     | -- libexec            |     | -- <component_1> |
|     | -- include            |          | -- bin      |
|          | -- <component_1> |          | -- cmake    |
|     | -- share              |          | -- doc      |
|          | -- html          |          | -- lib      |
|          | -- info          |          | -- include  |
|          | -- man           |          | -- samples  |
|          | -- doc           |     | -- <component_n> |
|          | -- <component_1> |          | -- bin      |
|               | -- samples  |          | -- cmake    |
|               | -- ..       |          | -- doc      |
|          | -- <component_n> |          | -- lib      |
|               | -- samples  |          | -- include  |
|               | -- ..       |          | -- samples  |
|______________________________________________________|
```

## ROCm File reorganization transition plan

New file organization for ROCm was first introduced ROCm v5.2 release. Backward
compatibility was in place to make sure users had a chance to change their
applications using ROCm. ROCm has moved header files and libraries to its new
location as indicated in the above structure and included symbolic-link and
wrapper header files in its old location for backward compatibility.

### Wrapper header files

Wrapper header files are placed in the old location (
`/opt/rocm-xxx/<component>/include`) with a warning message to include files
from the new location (/opt/rocm-xxx/include) as shown in the example below.

```cpp
#pragma message "This file is deprecated. Use file from include path /opt/rocm-ver/include/ and prefix with hip."
#include "hip/hip_runtime.h"
```

The depreciation plan for backward compatibility wrapper header files is as
follows

- #pragma message announcing deprecation – ROCm v5.2 release.
- #pragma message changed to #warning – Future release, tentatively ROCm v5.5.
- #warning changed to #error – Future release, tentatively ROCm v5.6.
- Backward compatibility wrappers removed – Future release, tentatively ROCm
v6.0.

### Executable files

Executable files are available in the /opt/rocm-xxx/bin folder. For backward
compatibility, the old library location (`/opt/rocm-xxx/<component>/bin`) has a
soft link to the library at the new location. Soft links will be removed in a
future release, tentatively ROCm v6.0.

```bash
$ ls -l /opt/rocm/hip/bin/
lrwxrwxrwx 1 root root   24 Jan 1 23:32 hipcc -> ../../bin/hipcc
```

### Library files

Library files are available in the `/opt/rocm-xxx/lib` folder. For backward
compatibility, the old library location (`/opt/rocm-xxx/<component>/lib`) has a
soft link to the library at the new location. Soft links will be removed in a
future release, tentatively ROCm v6.0.

```shell
$ ls -l /opt/rocm/hip/lib/
drwxr-xr-x 4 root root 4096 Jan 1 10:45 cmake
lrwxrwxrwx 1 root root   24 Jan 1 23:32 libamdhip64.so -> ../../lib/libamdhip64.so
```

### CMake Config files

All CMake configuration files are available in the
`/opt/rocm-xxx/lib/cmake/<component>` folder. For backward compatibility, the
old CMake locations (`/opt/rocm-xxx/<component>/lib/cmake`) consist of a soft
link to the new CMake config. Soft links will be removed in a future release,
tentatively ROCm v6.0.

```shell
$ ls -l /opt/rocm/hip/lib/cmake/hip/
lrwxrwxrwx 1 root root 42 Jan 1 23:32 hip-config.cmake -> ../../../../lib/cmake/hip/hip-config.cmake
```

## Changes required in applications using ROCm

Applications using ROCm are advised to use the new file paths. As the old files
will be deprecated in a future release. Application have to make sure to include
correct header file and use correct search paths.

1. `#include<header_file.h>` needs to be changed to
`#include <component/header_file.h>`

    For eg: `#include <hip.h>` needs to change
to `#include <hip/hip.h>`

2. Any variable in cmake or makefiles pointing to component folder needs to
changed.

    For eg: `VAR1=/opt/rocm/hip` needs to be changed to `VAR1=/opt/rocm`
    `VAR2=/opt/rocm/hsa` needs to be changed to `VAR2=/opt/rocm`

3. Any reference to `/opt/rocm/<component>/bin` or `/opt/rocm/<component>/lib`
needs to be changed to `/opt/rocm/bin` and `/opt/rocm/lib/` respectively.

## References

ROCm deprecation warning :
<https://docs.amd.com/bundle/ROCm-Release-Notes-v5.4.3/page/Deprecations_and_Warnings.html>

Linux File System Standard : <https://refspecs.linuxfoundation.org/fhs.shtml>
