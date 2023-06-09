# Quick Start (Linux)

## Add Repositories

::::::{tab-set}
:::::{tab-item} Ubuntu
:sync: ubuntu

::::{rubric} 1. Download and convert the package signing key
::::

```shell
# Make the directory if it doesn't exist yet.
# This location is recommended by the distribution maintainers.
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
# Download the key, convert the signing-key to a full
# keyring required by apt and store in the keyring directory
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | \
    gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null
```

::::{rubric} 2. Add the repositories
::::

::::{tab-set}
:::{tab-item} Ubuntu 20.04
:sync: ubuntu-20.04

```shell
# Kernel driver repository for focal
sudo tee /etc/apt/sources.list.d/amdgpu.list <<'EOF'
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/latest/ubuntu focal main
EOF
# ROCm repository for focal
sudo tee /etc/apt/sources.list.d/rocm.list <<'EOF'
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/debian focal main
EOF
```

:::
:::{tab-item} Ubuntu 22.04
:sync: ubuntu-22.04

```shell
# Kernel driver repository for jammy
sudo tee /etc/apt/sources.list.d/amdgpu.list <<'EOF'
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/latest/ubuntu jammy main
EOF
# ROCm repository for jammy
sudo tee /etc/apt/sources.list.d/rocm.list <<'EOF'
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/debian jammy main
EOF
# Prefer packages from the rocm repository over system packages
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
```

:::
::::

::::{rubric} 3. Update the list of packages
::::

```shell
sudo apt update
```

:::::

:::::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

::::{rubric} 1. Add the repositories
::::

::::{tab-set}
:::{tab-item} RHEL 8.6
:sync: RHEL-8.6

```shell
# Add the amdgpu module repository for RHEL 8.6
sudo tee /etc/yum.repos.d/amdgpu.repo <<'EOF'
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/latest/rhel/8.6/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
# Add the rocm repository for RHEL 8
sudo tee /etc/yum.repos.d/rocm.repo <<'EOF'
[rocm]
name=rocm
baseurl=https://repo.radeon.com/rocm/rhel8/latest/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
```

:::

:::{tab-item} RHEL 8.7
:sync: RHEL-8.7

```shell
# Add the amdgpu module repository for RHEL 8.7
sudo tee /etc/yum.repos.d/amdgpu.repo <<'EOF'
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/latest/rhel/8.7/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
# Add the rocm repository for RHEL 8
sudo tee /etc/yum.repos.d/rocm.repo <<'EOF'
[rocm]
name=rocm
baseurl=https://repo.radeon.com/rocm/rhel8/latest/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
```

:::

:::{tab-item} RHEL 9.1
:sync: RHEL-9.1

```shell
# Add the amdgpu module repository for RHEL 9.1
sudo tee /etc/yum.repos.d/amdgpu.repo <<'EOF'
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/latest/rhel/9.1/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
# Add the rocm repository for RHEL 9
sudo tee /etc/yum.repos.d/rocm.repo <<'EOF'
[rocm]
name=rocm
baseurl=https://repo.radeon.com/rocm/rhel9/latest/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
```

:::
::::

::::{rubric} 2. Clean cached files from enabled repositories
::::

```shell
sudo yum clean all
```

:::::

:::::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

::::{rubric} 1. Add the repositories
::::

::::{tab-set}
:::{tab-item} SLES 15 SP4
:sync: SLES15-SP4

```shell

# Add the amdgpu module repository for SLES 15.4
sudo tee /etc/zypp/repos.d/amdgpu.repo <<'EOF'
[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/latest/sle/15.4/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
# Add the rocm repository for SLES
sudo tee /etc/zypp/repos.d/rocm.repo <<'EOF'
[rocm]
name=rocm
baseurl=https://repo.radeon.com/rocm/zyp/zypper
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
```

:::
::::

::::{rubric} 2. Update the new repository
::::

```shell
sudo zypper ref
```

:::::
::::::

## Install Drivers

Install the `amdgpu-dkms` kernel module, aka driver, on your system.

::::{tab-set}

:::{tab-item} Ubuntu
:sync: ubuntu

```shell
sudo apt install amdgpu-dkms
```

:::

:::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

```shell
sudo yum install amdgpu-dkms
```

:::

:::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

```shell
sudo zypper install amdgpu-dkms
```

:::

::::

## Install ROCm Runtimes

Install the `rocm-hip-libraries` meta-package. This contains dependencies for most
common ROCm applications.

::::{tab-set}
:::{tab-item} Ubuntu
:sync: ubuntu

```console shell
sudo apt install rocm-hip-libraries
```

:::

:::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

```console shell
sudo yum install rocm-hip-libraries
```

:::

:::{tab-item} SUSE Linux Enterprise Server
:sync: SLES

```console shell
sudo zypper install rocm-hip-libraries
```

:::
::::

## Reboot the system

Loading the new driver requires a reboot of the system.

```shell
sudo reboot
```
