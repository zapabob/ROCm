# Autotag

## How to use

The tag script can simply be invoked by passing it as a python script:

```sh
python3 tag_script.py --help
```

To generate the changelog from 5.0.0 up to and including 5.4.3:

```sh
python3 tag_script.py -t <GITHUB_TOKEN> --no-release --no-pulls --do-previous --compile_file ../../CHANGELOG.md --branch release/rocm-rel-5.4 5.4.3
```

> **Note**
>
> Compiling the changelog without the `--do-previous`-flag will always think that all libraries are new since no previous version of said library has been parsed.

Trying to run without a token is possible but GitHub enforces stricter rate limits and is therefore not advised.
