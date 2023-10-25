# Autotag

## Pre-requisites

* Create a GitHub Personal Access Token.
  * Tested with all the read-only permissions, but public_repo, read:project read:user, and repo:status should be enough.
  * Copy the token somewhere safe.
* Configure SSO for this token by authorizing it for the following organizations:
  * ROCm-Developer-Tools
  * RadeonOpenCompute
  * ROCmSoftwarePlatform

## Updating the changelog

* Add or update the release specific notes in `tools/autotag/templates/rocm_changes`
* Ensure the all the repositories have their release specific branch with the updated changelogs.
* Run this for 5.6.0 (change for whatever version you require)
* `GITHUB_ACCESS_TOKEN=my_token_here`

<<<<<<< HEAD
To generate the changelog from 5.0.0 up to and including 5.7.0:

```sh
python3 tag_script.py -t $GITHUB_ACCESS_TOKEN --no-release --no-pulls --do-previous --compile_file ../../CHANGELOG.md --branch release/rocm-rel-5.7 5.7.0
=======
To generate the changelog from 5.0.0 up to and including 5.7.1:

```sh
python3 tag_script.py -t $GITHUB_ACCESS_TOKEN --no-release --no-pulls --do-previous --compile_file ../../CHANGELOG.md --branch release/rocm-rel-5.7 5.7.1
>>>>>>> roc-5.7.x
```

To generate the changelog only for 5.7.1:

```sh
python3 tag_script.py -t $GITHUB_ACCESS_TOKEN --no-release --no-pulls --compile_file ../../CHANGELOG.md --branch release/rocm-rel-5.7 5.7.1
```

### Notes

> If branch cannot be found, edit default.xml at root.
> Sometimes the script doesn't know whether to include or exclude an entry for a specific release. Continue this part by accepting (Y) or rejecting (N) entries.
> The end result should be a newly generated changelog in the project root.
> Compiling the changelog without the `--do-previous`-flag will always think that all libraries are new since no previous version of said library has been parsed.
> Trying to run without a token is possible but GitHub enforces stricter rate limits and is therefore not advised.

* Copy over the first part of the changelog and replace the old release notes in RELEASE.md.

## Adding new libraries/repositories

* Add the name or group of the repository (retrieved in default.xml in the ROCm project root) to: included_names or included_groups to auto_tag.py.
* At the moment of writing, this is only in the 5.6 branch and not the develop branch.
* Re-run the command specified in the steps above.
* Some libraries do not have the changelog for every point release. The tool will give out warnings, but it is okay to ignore them.
