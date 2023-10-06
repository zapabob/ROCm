# Introduction to Spack

Spack is a package management tool designed to support multiple versions and configurations of software on a wide variety of platforms and environments. It was designed for large supercomputing centers, where many users and application teams share common installations of software on clusters with exotic architectures, using libraries that do not have a standard ABI. Spack is non-destructive: installing a new version does not break existing installations, so many configurations can coexist on the same system.

Most importantly, Spack is *simple*. It offers a simple *spec* syntax so that users can specify versions and configuration options concisely. Spack is also simple for package authors: package files are written in pure Python, and specs allow package authors to maintain a single file for many different builds of the same package. Below link can be referred for more generic information on Spack.

Reference: <https://spack-tutorial.readthedocs.io/en/latest/>

## ROCM packages in Spack

| **Component**             | **Spack Package Name** |
|---------------------------|------------------------|
| **rocm-cmake**            | rocm-cmake             |
| **thunk**                 | hsakmt-roct            |
| **rocm-smi-lib**          | rocm-smi-lib           |
| **hsa**                   | hsa-rocr-dev           |
| **lightning**             | llvm-amdgpu            |
| **devicelibs**            | rocm-device-libs       |
| **comgr**                 | comgr                  |
| **rocclr (vdi)**          | hip-rocclr             |
| **hipify_clang**          | hipify-clang           |
| **hip (hip_in_vdi)**      | hip                    |
| **ocl (opencl_on_vdi )**  | rocm-opencl            |
| **rocminfo**              | rocminfo               |
| **clang-ocl**             | rocm-clang-ocl         |
| **rccl**                  | rccl                   |
| **atmi**                  | atmi                   |
| **rocm_debug_agent**      | rocm-debug-agent       |
| **rocm_bandwidth_test**   | rocm-bandwidth-test    |
| **rocprofiler**           | rocprofiler-dev        |
| **roctracer-dev-api**     | roctracer-dev-api      |
| **roctracer**             | roctracer-dev          |
| **dbgapi**                | rocm-dbgapi            |
| **rocm-gdb**              | rocm-gdb               |
| **openmp-extras**         | rocm-openmp-extras     |
| **rocBLAS**               | rocblas                |
| **hipBLAS**               | hipblas                |
| **rocFFT**                | rocfft                 |
| **rocRAND**               | rocrand                |
| **rocSPARSE**             | rocsparse              |
| **hipSPARSE**             | hipsparse              |
| **rocALUTION**            | rocalution             |
| **rocSOLVER**             | rocsolver              |
| **rocPRIM**               | rocprim                |
| **rocThrust**             | rocthrust              |
| **hipCUB**                | hipcub                 |
| **hipfort**               | hipfort                |
| **ROCmValidationSuite**   | rocm-validation-suite  |
| **MIOpenGEMM**            | miopengemm             |
| **MIOpen(Hip variant)**   | miopen-hip             |
| **MIOpen(opencl)**        | miopen-opencl          |
| **MIVisionX**             | mivisionx              |
| **AMDMIGraphX**           | migraphx               |
| **rocm-tensile**          | rocm-tensile           |
| **hipfft**                | hipfft                 |
| **RDC**                   | rdc                    |
| **hipsolver**             | hipsolver              |
| **mlirmiopen**            | mlirmiopen             |

Install all prerequisites before performing the SPACK installation.

::::{tab-set}
:::{tab-item} Ubuntu
:sync: Ubuntu

```shell
# Install some essential utilities:
apt-get update
apt-get install make patch bash tar gzip unzip bzip2 file gnupg2 git gawk
apt-get update -y
apt-get install -y xz-utils
apt-get build-essential
apt-get install vim
# Install Python:
apt-get install python3
apt-get upgrade python3-pip
# Install Compilers:
apt-get install gcc
apt-get install gfortran
```

:::
:::{tab-item} SLES
:sync: SLES

```shell
# Install some essential utilities:
zypper update
zypper install make patch bash tar gzip unzip bzip xz file gnupg2 git awk
zypper in -t pattern
zypper install vim
# Install Python:
zypper install python3
zypper install python3-pip
# Install Compilers:
zypper install gcc
zypper install gcc-fortran
zypper install gcc-c++
```

:::
:::{tab-item} CentOS
:sync: CentOS

```shell
# Install some essential utilities:
yum update
yum install make
yum install patch bash tar yum install gzip unzip bzip2 xz file gnupg2 git gawk
yum group install "Development Tools"
yum install vim
# Install Python:
yum install python3
pip3 install --upgrade pip 
# Install compilers:
yum install gcc
yum install gcc-gfortran
yum install gcc-c++
```

:::
::::

## Steps to build ROCm Components using Spack

## Clone Spack project

Clone the Spack project from github in order to use the spack package manager.

git clone <https://github.com/spack/spack>

## Initialize Spack

The script setup-env.sh will initialize spack environment.

\$ cd spack

\$ . share/spack/setup-env.sh

Spack commands will be available once the above steps are executed successfully.

spack help will list the commands available.

root@[ixt-rack-104:/spack\#](http://ixt-rack-104/spack) spack help

## Using Spack to install ROCm components  

## rocm-cmake  

Below command will install the default variants and latest version of rocm-cmake.

spack install rocm-cmake

In order to install a specific version of rocm-cmake below format can be used.

spack install rocm-cmake@\<version number\>

Example:

spack install rocm-cmake@5.2.0

## Using info  

info** command will display basic information of the package. It shows the Preferred, Safe and Deprecated versions and different Variants available.

It also shows the Dependencies with other packages. as shown below.

spack info mivisionx

Example:

root@[ixt-rack-104:/spack\#](http://ixt-rack-104/spack) spack info mivisionx  
CMakePackage: mivisionx  
  
Description:  
 MIVisionX toolkit is a set of comprehensive computer vision and machine  
 intelligence libraries, utilities, and applications bundled into a  
 single toolkit.  
  
Homepage: <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX>  
  
Preferred version:  
 5.3.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.3.0.tar.gz>  
  
Safe versions:  
 5.3.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.3.0.tar.gz>  
 5.2.3 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.2.3.tar.gz>  
 5.2.1 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.2.1.tar.gz>  
 5.2.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.2.0.tar.gz>  
 5.1.3 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.1.3.tar.gz>  
 5.1.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.1.0.tar.gz>  
 5.0.2 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.0.2.tar.gz>  
 5.0.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-5.0.0.tar.gz>  
 4.5.2 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-4.5.2.tar.gz>  
 4.5.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-4.5.0.tar.gz>  
  
Deprecated versions:  
 4.3.1 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-4.3.1.tar.gz>  
 4.3.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-4.3.0.tar.gz>  
 4.2.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-4.2.0.tar.gz>  
 4.1.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-4.1.0.tar.gz>  
 4.0.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-4.0.0.tar.gz>  
 3.10.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-3.10.0.tar.gz>  
 3.9.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-3.9.0.tar.gz>  
 3.8.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-3.8.0.tar.gz>  
 3.7.0 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/rocm-3.7.0.tar.gz>  
 1.7 <https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/archive/1.7.tar.gz>  
  
Variants:  
 Name [Default] When Allowed values Description  
 ==================== ==== ==================== ==================================  
  
 build_type [Release] -- Release, Debug, CMake build type  
 RelWithDebInfo  
 hip [on] -- on, off Use HIP as backend  
 ipo [off] -- on, off CMake interprocedural optimization  
 opencl [off] -- on, off Use OPENCL as the backend  
  
Build Dependencies:  
 cmake ffmpeg libjpeg-turbo miopen-hip miopen-opencl miopengemm opencv openssl protobuf rocm-cmake rocm-opencl  
  
Link Dependencies:  
 miopen-hip miopen-opencl miopengemm openssl rocm-opencl  
  
Run Dependencies:  
 None  
  
root@[ixt-rack-104:/spack\#](http://ixt-rack-104/spack)

## Installing variants for ROCm components  

Variants listed above indicates that mivisionx package is built with **build_type=Release,** backend **hip**  and without backend **opencl** by default.  
But it also supports build_type=**Debug** and **RelWithDebInfo** , with **opencl** and without **hip** as backend.

Example:

spack install mivisionx build_type=Debug (Backend will be hip since it is the default one)  
spack install mivisionx+opencl build_type=Debug (Backend will be opencl and hip will be disabled as per the conflict defined in recipe)

## spack spec command

In order to display the dependency tree spack spec command can be used with the same format.

## Example

root@[ixt-rack-104:/spack\#](http://ixt-rack-104/spack) spack spec mivisionx  
Input spec  
\--------------------------------  
mivisionx  
  
Concretized  
\--------------------------------  
mivisionx@5.3.0%gcc@9.4.0+hip\~ipo\~opencl build_type=Release arch=linux-ubuntu20.04-skylake_avx512  
  
## Creating environment  

You can create an environment with all the components of required version, install them collectively and work in the environment.

1\. In the root folder make a folder to create a .yaml file with which we can create an environment.

* mkdir /localscratch
* cd /localscratch
* vi sample.yaml

2.Add all the required components on sample.yaml file, as shown below,

* spack:
* concretization: separately
* packages:
* all:
* compiler: [gcc@8.5.0]
* specs:
* \- matrix:
* \- ['%gcc@8.5.0\^cmake@3.19.7']
* \- [rocm-cmake@5.3.2, rocm-dbgapi@5.3.2, rocm-debug-agent@5.3.2, rocm-gdb@5.3.2,
* rocminfo@5.3.2, rocm-opencl@5.3.2, rocm-smi-lib@5.3.2, rocm-tensile@5.3.2, rocm-validation-suite@4.3.1,
* rocprim@5.3.2, rocprofiler-dev@5.3.2, rocrand@5.3.2, rocsolver@5.3.2, rocsparse@5.3.2,
* rocthrust@5.3.2, roctracer-dev@5.3.2]
* view: true

3\. Once you got .yaml file, using it create an environment as shown below,

* spack env create -d /localscratch/MyEnvironment /localscratch/sample.yaml

4\. Activate the created environment as shown below,

* spack env activate /localscratch/MyEnvironment

5.Before installing all components using next step, verify whether versions mentioned for all components are desired or not as shown below,

* spack find - this command will list out all components been in the environment (and 0 installed )

6.Install all the components in the .yaml after activating the environment as shown below by entering the created environment.

* cd /localscratch/MyEnvironment
* spack install -j 50

7.Check all the components installation are successful or not.

* spack find

8.If any modification is done to the .yaml file, to reflect those changes one needs to deactivate the existing environment and create a new one again using steps 3 and 4.

* To deactivate use below command,
* spack env deactivate

## Create and apply patch for a package before installation

Spack will install rocm packages after pulling the source code from git hub and building locally.  
In order to build a component with any modification in source code we would need to generate a patch and apply before the build phase by making changes in the spack recipe of the corresponding package.

Below the procedure to generate a patch and build with the changes.

1.**Stage the source code**

spack stage hip@5.2.0 (This will pull the 5.2.0 release version source code of hip and display the path to spack-src directory where entire source code is available)  
  
root@[ixt-rack-104:/spack\#](http://ixt-rack-104/spack) spack stage hip@5.2.0  
==\> Fetching <https://github.com/ROCm-Developer-Tools/HIP/archive/rocm-5.2.0.tar.gz>  
==\> Fetching <https://github.com/ROCm-Developer-Tools/hipamd/archive/rocm-5.2.0.tar.gz>  
==\> Fetching <https://github.com/ROCm-Developer-Tools/ROCclr/archive/rocm-5.2.0.tar.gz>  
==\> Moving resource stage  
 source: /tmp/root/spack-stage/resource-hipamd-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src/  
 destination: /tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src/hipamd  
==\> Moving resource stage  
 source: /tmp/root/spack-stage/resource-opencl-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src/  
 destination: /tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src/opencl  
==\> Moving resource stage  
 source: /tmp/root/spack-stage/resource-rocclr-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src/  
 destination: /tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src/rocclr  
==\> Staged hip in /tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7

2\. **Change directory to spack-src inside the staged directory**

root@[ixt-rack-104:/spack\#cd /tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7](http://ixt-rack-104/spack)  
root@[ixt-rack-104:/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7\#](http://ixt-rack-104/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7) cd spack-src/

3\. **Creates a new Git repository**

root@[ixt-rack-104:/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src\#](http://ixt-rack-104/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src) git init

4\. **Add the entire directory to the repository**

root@[ixt-rack-104:/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src\#](http://ixt-rack-104/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src) git add .

5\. **Make the required changes in the source code**

root@[ixt-rack-104:/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src\#](http://ixt-rack-104/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src) vi hipamd/CMakeLists.txt (Make required changes in the source code)

6\. **Generate the patch using "git diff" command**

root@[ixt-rack-104:/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src\#](http://ixt-rack-104/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src) git diff \> /spack/var/spack/repos/builtin/packages/hip/0001-modifications.patch

7\. **Update the recipe with the patch file name and conditions to apply**

root@[ixt-rack-104:/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src\#](http://ixt-rack-104/tmp/root/spack-stage/spack-stage-hip-5.2.0-wzo5y6ysvmadyb5mvffr35galb6vjxb7/spack-src) spack edit hip  
  
Provide the patch file name and the conditions for the patch to be applied in the hip recipe as below,  
  
patch("0001-modifications.patch", when="@5.2.0")

Spack will apply 0001-modifications.patch on the 5.2.0 release code before starting the build for hip.

**Note**: After each modification we need to make sure the recipe is also updated. If there is no change in the recipe do touch /spack/var/spack/repos/builtin/packages/hip/package.py

**Note:** Spack latest release is 5.5.1
