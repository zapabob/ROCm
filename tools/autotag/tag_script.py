#!/usr/bin/env python3
"""Automatically tag and release math libraries with new release of ROCm."""

from dataclasses import dataclass
import dbm
import sys
from typing import List, Optional, TextIO, Union
import xml.etree.ElementTree as ET
import urllib.request
import argparse
from github import Github, NamedUser

from util.release_data import ReleaseDataFactory, ReleaseLib
from util import PROCESSORS, TEMPLATES


def get_token(
    passed_token: Optional[str],
    *,
    token_keys: Optional[Union[str, List[str]]] = None,
) -> str:
    """Get and/or store a token to the database file"""
    with dbm.open("gh_token", "c") as db:
        used_token: Optional[str] = None
        if passed_token is not None and passed_token != "":
            used_token = passed_token
        else:
            used_token_bytes: Optional[bytes] = None
            if isinstance(token_keys, str):
                used_token_bytes = db.get(token_keys, None)
            elif isinstance(token_keys, list):
                for key in token_keys:
                    if db.get(key, None) is not None:
                        used_token_bytes = db[key]
                        break
            if used_token_bytes is None:
                raise ValueError(
                    "No token was passed, and no stored token could be found."
                )
            used_token = used_token_bytes.decode()
            print(f"Using stored token: {used_token}")
        if isinstance(token_keys, str):
            db[token_keys] = used_token
        elif isinstance(token_keys, list):
            db[token_keys[0]] = used_token
    return used_token


@dataclass
class TaggingArgs(argparse.Namespace):
    """Arguments for the tagging script."""

    token: Optional[str] = None
    pr_token: Optional[str] = None
    library: Optional[List[str]] = None
    organization: Optional[str] = None
    manifest_url: Optional[str] = None
    version: str = ""
    release: Optional[bool] = None
    pulls: Optional[bool] = None
    previous: Optional[bool] = None
    _exclude: Optional[List[str]] = None
    github_url: str = "github.com"
    branch: Optional[str] = None
    compile_file: Optional[TextIO] = None

    @property
    def org(self) -> Optional[str]:
        """Alias for the organization."""
        return self.organization

    @org.setter
    def org(self, value: str):
        self.organization = value

    @property
    def exclude(self) -> List[str]:
        """Get the excluded libraries plus defaults."""
        defaults = [
            "AMDMIGraphX",
            "MIOpenGEMM",
            "MIOpenKernels",
            "MIOpenTensile",
            "ROCmValidationSuite",
            "half",
            "hipFORT",
            "rccl-rdma-sharp-plugins",
            "MLSEQA_TestRepo",
        ]
        return defaults + (self._exclude if self._exclude is not None else [])


def parse_args() -> TaggingArgs:
    """Parse arguments."""

    def add_arg_pair(
        parser: argparse.ArgumentParser,
        name: str,
        help_suffix: Optional[str] = None,
    ):
        """Add enable/disable argument pair."""
        group = parser.add_mutually_exclusive_group()
        help_suffix = (name + ".") if help_suffix is None else help_suffix
        group.add_argument(
            f"--do-{name}",
            help=f"Do {help_suffix}",
            action="store_const",
            const=True,
            default=None,
            dest=name,
        )
        group.add_argument(
            f"--no-{name}",
            help=f"Don't do {help_suffix}",
            action="store_const",
            const=False,
            default=None,
            dest=name,
        )

    parser = argparse.ArgumentParser(
        "Create tags and releases for all math libraries for a ROCm release"
    )
    parser.add_argument(
        "-t",
        "--token",
        type=str,
        help="The access token to use to log in to Github",
    )
    parser.add_argument(
        "--pr-token",
        type=str,
        help=(
            "The access token to use for PRs, if different from the other"
            " token"
        ),
    )
    parser.add_argument(
        "-l", "--library", help="A library to release.", action="append"
    )
    parser.add_argument(
        "-x",
        "--exclude",
        dest="_exclude",
        help="A library to exclude from release.",
        action="append",
    )
    parser.add_argument(
        "-o",
        "--org",
        help="The Github org to look for the repos in.",
    )
    add_arg_pair(parser, "release", "the tag & release.")
    add_arg_pair(parser, "pulls", "the pull requests to internal repos.")
    add_arg_pair(parser, "previous", " use previous versions as required.")
    parser.add_argument(
        "--manifest-url",
        help="The url to download the manifest.xml file from.",
    )
    parser.add_argument(
        "--branch", help="A branch to check the changelog from."
    )
    parser.add_argument(
        "--github-url",
        help="The GitHub URL to use for tag & release and pull requests.",
        default="github.com",
    )
    parser.add_argument(
        "--compile_file",
        help="The file to write the compiled release notes to.",
        type=argparse.FileType("w", encoding="utf-8"),
        default=None,
    )
    parser.add_argument(
        "version", help="The ROCm release version to release libraries for."
    )
    args = parser.parse_args(namespace=TaggingArgs())
    if args.pr_token is None:
        args.pr_token = args.token
    return args


def run_tagging():
    """Run the tagging/releasing process on each specified library."""
    args = parse_args()

    if args.manifest_url is None:
        manifest_url = (
            "https://github.com/RadeonOpenCompute/ROCm/raw/develop/default.xml"
        )
    else:
        manifest_url = args.manifest_url
    manifest_path, _ = urllib.request.urlretrieve(manifest_url, "manifest.xml")
    manifest_tree = ET.parse(manifest_path).getroot()

    gh_args = {
        "login_or_token": get_token(
            args.token, token_keys=["gh_token", "token"]
        )
    }
    pr_args = {"login_or_token": get_token(args.token, token_keys="pr_token")}

    if args.github_url != "github.com":
        gh_args["base_url"] = pr_args[
            "base_url"
        ] = f"https://{args.github_url}/api/v3"

    data_factory = ReleaseDataFactory(
        args.org, args.version, Github(**gh_args), Github(**pr_args)
    )

    remote_map = {
        "rocmswplatform": "ROCmSoftwarePlatform",
        "rocmswplatform-internal": "ROCmSoftwarePlatform",
        "amdgpuopenlib": "GPUOpen-ProfessionalCompute-Libraries",
        "radeonopencompute": "RadeonOpenCompute",
        "radeonopencompute-internal": "RadeonOpenCompute"
    }

    libraries: list[ReleaseLib] = []

    for entry in manifest_tree.findall(".*[@groups='mathlibs']"):
        if (
            args.library is None or entry.get("name") in args.library
        ) and entry.get("name") not in args.exclude:
            library_data = data_factory.create_data(
                entry.get("name", ""),
                entry.get("revision", ""),
                org=remote_map[entry.get("remote", "")],
            )

            if args.branch is not None:
                library_data.commit = library_data.repo.get_branch(
                    args.branch
                ).commit.sha
            libraries.append(library_data)

    failed: list[str] = []
    for data in libraries:
        try:
            print(f"{data.name} commit revision = {data.commit}")
            print(
                "Commit Link: "
                f"https://github.com/{data.qualified_repo}/commit/{data.commit}"
            )

            if not PROCESSORS[data.name](
                data, TEMPLATES[data.name], args.previous
            ):
                failed.append(data.name)
                continue

            if args.compile_file is not None:
                print("# " + data.repo.name, file=args.compile_file)
                print(file=args.compile_file)
                print(data.notes, file=args.compile_file)
            data.do_release(args.release)
            pr = data.do_create_pull(args.pulls, pr_args["login_or_token"])
            if pr is not None:
                if isinstance(data_factory.gh.get_user(), NamedUser.NamedUser):
                    pr.create_review_request([data_factory.gh.get_user().name])
        except Exception as err:
            print(f"Encountered error tagging {data.name}: {err}")
    if failed:
        print("Error processing the following libraries:", file=sys.stderr)
        for lib in failed:
            print("\t" + lib, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    run_tagging()
