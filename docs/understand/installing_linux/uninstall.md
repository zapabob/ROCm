## Uninstallation

ROCm may be uninstalled by removing its packages and unregistering the repo:

::::{tab-set}
:::{tab-item} Ubuntu
:sync: ubuntu

```console shell
sudo apt autoremove rocm-core rocm-hip-libraries
```

:::

:::{tab-item} Red Hat Enterprise Linux
:sync: RHEL

```console shell
sudo yum autoremove rocm-core rocm-hip-libraries
```

:::

:::{tab-item} SUSE Linux Enterprise Server 15
:sync: SLES15

```console shell
sudo zypper rm -u rocm-core rocm-hip-libraries
```

:::
::::