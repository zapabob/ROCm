# AMD ROCm™

This repository contains the manifest file for ROCm™ releases, changelogs, and
release information. The file default.xml contains information for all
repositories and the associated commit used to build the current ROCm release.

The default.xml file uses the repo Manifest format.

The develop branch of this repository contains content for the next
ROCm release.

## How to build documentation via Sphinx

```bash
cd docs

pip3 install -r .sphinx/requirements.txt

python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

## Older ROCm™ Releases

For release information for older ROCm™ releases, refer to
[CHANGELOG](./CHANGELOG.md).
