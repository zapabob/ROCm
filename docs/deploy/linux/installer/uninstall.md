# Installer Script Uninstallation (Linux)

::::{rubric} Uninstalling Single-Version Install
::::

```console shell
sudo amdgpu-install --uninstall
```

```{note}
This command uninstalls all ROCm packages associated with the installed ROCm
release along with the kernel-mode driver.
```

::::{rubric} Uninstalling a Specific ROCm Release
::::

```console shell
sudo amdgpu-install --uninstall --rocmrelease=<release-number>
```

::::{rubric} Uninstalling all ROCm Releases
::::

```console shell
sudo amdgpu-install --uninstall --rocmrelease=all
```
