# Installation with install script

Prior to beginning, please ensure you have the [prerequisites](../prerequisites)
installed.

## Download the Installer Script

To download and install the `amdgpu-install` script on the system, use the
following commands based on your distribution.

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.5.1/ubuntu/focal/amdgpu-install_5.5.50501-1_all.deb
sudo apt install ./amdgpu-install_5.5.50501-1_all.deb
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.5.1/ubuntu/jammy/amdgpu-install_5.5.50501-1_all.deb
sudo apt install ./amdgpu-install_5.5.50501-1_all.deb
```

:::
::::
:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{tab-set}
:::{tab-item} RHEL 8.6
:sync: RHEL-8.6
:sync: RHEL-8

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.5.1/rhel/8.6/amdgpu-install-5.5.50501-1.el8.noarch.rpm
```

:::
:::{tab-item} RHEL 8.7
:sync: RHEL-8.7
:sync: RHEL-8

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.5.1/rhel/8.7/amdgpu-install-5.5.50501-1.el8.noarch.rpm
```

:::
:::{tab-item} RHEL 9.1
:sync: RHEL-9.1
:sync: RHEL-9

```shell
sudo yum install https://repo.radeon.com/amdgpu-install/5.5.1/rhel/9.1/amdgpu-install-5.5.50501-1.el8.noarch.rpm
```

:::
::::
:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

::::{tab-set}
:::{tab-item} Service Pack 4
:sync: SLES15-SP4

```shell
sudo zypper --no-gpg-checks install https://repo.radeon.com/amdgpu-install/5.5.1/sle/15.4/amdgpu-install-5.5.50501-1.noarch.rpm
```

:::
::::
:::::
::::::

## Use cases

Instead of installing individual applications or libraries the installer script
groups packages into specific use cases, matching typical workflows and runtimes.

To display a list of available use cases execute the command:

```shell
sudo amdgpu-install --list-usecase
```

The available use-cases will be printed in a format similar to the example
output below.

```none
If --usecase option is not present, the default selection is "graphics,opencl,hip"

Available use cases:
rocm(for users and developers requiring full ROCm stack)
- OpenCL (ROCr/KFD based) runtime
- HIP runtimes
- Machine learning framework
- All ROCm libraries and applications
- ROCm Compiler and device libraries
- ROCr runtime and thunk
lrt(for users of applications requiring ROCm runtime)
- ROCm Compiler and device libraries
- ROCr runtime and thunk
opencl(for users of applications requiring OpenCL on Vega or
later products)
- ROCr based OpenCL
- ROCm Language runtime

openclsdk (for application developers requiring ROCr based OpenCL)
- ROCr based OpenCL
- ROCm Language runtime
- development and SDK files for ROCr based OpenCL

hip(for users of HIP runtime on AMD products)
- HIP runtimes
hiplibsdk (for application developers requiring HIP on AMD products)
- HIP runtimes
- ROCm math libraries
- HIP development libraries
```

To install use cases specific to your requirements, use the installer
`amdgpu-install` as follows:

- To install a single use case add it with the `--usecase` option:

  ```shell
  sudo amdgpu-install --usecase=rocm
  ```

- For multiple use cases separate them with commas:

  ```shell
  sudo amdgpu-install --usecase=hiplibsdk,rocm
  ```

## Single-version ROCm Installation

By default (without the `--rocmrelease` option)
the installer script will install packages in the single-version layout.

## Multi-version ROCm Installation

For the multi-version ROCm installation you must use the installer script from
the latest release of ROCm that you wish to install.

**Example:** If you want to install ROCm releases 5.3.3 and 5.5.1
simultaneously, you are required to download the installer from the latest ROCm
release v5.5.1.

### Add Required Repositories

You must add the ROCm repositories manually for all ROCm releases
you want to install except the latest one. The `amdgpu-install` script
automatically adds the required repositories for the latest release.

Run the following commands based on your distribution to add the repositories:

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
for ver in 5.3.3 5.4.3; do
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver focal main" | sudo tee /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
for ver in 5.3.3 5.4.3; do
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver jammy main" | sudo tee /etc/apt/sources.list.d/rocm.list
done
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```

:::
::::
:::::
:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{tab-set}
:::{tab-item} RHEL 8
:sync: RHEL-8

```shell
for ver in 5.3.3 5.4.3; do
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[ROCm-$ver]
name=ROCm$ver
baseurl=https://repo.radeon.com/rocm/rhel8/$ver/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo yum clean all
```

:::
:::{tab-item} RHEL 9
:sync: RHEL-9

```shell
for ver in 5.3.3 5.4.3; do
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[ROCm-$ver]
name=ROCm$ver
baseurl=https://repo.radeon.com/rocm/rhel9/$ver/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo yum clean all
```

:::
::::
:::::
:::::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

```shell
for ver in 5.3.3 5.4.3; do
sudo tee --append /etc/zypp/repos.d/rocm.repo <<EOF
name=rocm
baseurl=https://repo.radeon.com/rocm/$ver/sle/15.4/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo zypper ref
```

:::::
::::::

### Install packages

Use the installer script as given below:

```none
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-1>
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-2>
sudo amdgpu-install --usecase=rocm --rocmrelease=<release-number-3>
```

Following are examples of ROCm multi-version installation. The kernel-mode
driver, associated with the ROCm release v5.5.1, will be installed as its latest
release in the list.

```none
sudo amdgpu-install --usecase=rocm --rocmrelease=5.3.3
sudo amdgpu-install --usecase=rocm --rocmrelease=5.5.1
```

## Additional options

### Unattended installation

Adding `-y` as a parameter to `amdgpu-install` skips user prompts (for
automation). Example: `amdgpu-install -y --usecase=rocm`

### Skipping kernel mode driver installation

The installer script tries to install the kernel mode driver along with the
requested use cases. This might be unnecessary as in the case of docker
containers or you may wish to keep a specific version when using multi-version
installation, and not have the last installed version overwrite the kernel mode
driver.

To skip the installation of the kernel-mode driver add the `--no-dkms` option
when calling the installer script.
