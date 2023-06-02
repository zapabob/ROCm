# Installation Prerequisites (Linux)

You must perform the following steps before installing ROCm and check if the
system meets all the requirements to proceed with the installation.

## Confirm the System Has a Supported Linux Distribution Version

The ROCm installation is supported only on specific Linux distributions and
kernel versions.

### Check the Linux Distribution and Kernel Version on Your System

This section discusses obtaining information about the Linux distribution and
kernel version.

#### Linux Distribution Information

Verify the Linux distribution using the following steps:

1. To obtain the Linux distribution information, type the following command on
   your system from the Command Line Interface (CLI):

   ```shell
   uname -m && cat /etc/*release
   ```

2. Confirm that the obtained Linux distribution information matches with those listed in {ref}`supported_distributions`.

   **Example:** Running the command above on an Ubuntu system results in the
   following output:

   ```shell
   x86_64
   DISTRIB_ID=Ubuntu
   DISTRIB_RELEASE=20.04
   DISTRIB_CODENAME=focal
   DISTRIB_DESCRIPTION="Ubuntu 20.04.5 LTS"
   ```

(check-kernel-info)=

#### Kernel Information

Verify the kernel version using the following steps:

1. To check the kernel version of your Linux system, type the following command:

   ```shell
   uname -srmv
   ```

2. Confirm that the obtained kernel version information matches with System
   Requirements.

   **Example:** The output of the command above lists the kernel version in the
   following format:

   ```shell
   Linux 5.15.0-46-generic #44~20.04.5-Ubuntu SMP Fri Jun 24 13:27:29 UTC 2022 x86_64
   ```

### Setting Permissions for Groups

This section provides steps to add any current user to a video group to access
GPU resources.

1. To check the groups in your system, issue the following command:

   ```shell
   groups
   ```

2. Add yourself to the `render` or `video` group using the following instruction:

   ```shell
   sudo usermod -a -G render $LOGNAME
   # OR
   sudo usermod -a -G video $LOGNAME
   ```

3. Use of the video group is recommended for all ROCm-supported operating
   systems.

To add all future users to the `video` and `render` groups by default, run
the following commands:

   ```shell
   echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
   echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
   echo 'EXTRA_GROUPS=render' | sudo tee -a /etc/adduser.conf
   ```
