#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc


import subprocess
import sys
from argparse import ArgumentParser, Namespace
from tempfile import TemporaryDirectory
from typing import Tuple

import requests
from git import Repo

PLATFORM_AND = "android"
PLATFORM_IOS = "ios"
PLATFORM_RN = "reactnative"

REPOSITORIES = {
    PLATFORM_AND: "dd-bridge-android",
    PLATFORM_IOS: "dd-bridge-ios",
    PLATFORM_RN: "dd-sdk-reactnative"
}


def parse_arguments(args: list) -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("-s", "--source", required=True, help="the source Json definition of the API")
    parser.add_argument("-p", "--platform", required=True,
                        choices=[PLATFORM_AND, PLATFORM_IOS, PLATFORM_RN],
                        help="the target platform")
    parser.add_argument("-v", "--version", required=True, help="the version of the mobile bridge")

    return parser.parse_args(args)


def github_create_pr(repository: str, branch_name: str, base_name: str, version: str, gh_token: str) -> int:
    headers = {
        'authorization': "Bearer " + gh_token,
        'Accept': 'application/vnd.github.v3+json',
    }
    data = '{"body": "This PR has been created automatically by the CI", ' \
           '"title": "Update to version ' + version + '", ' \
                                                      '"base":"' + base_name + '", "head":"' + branch_name + '"}'

    url = "https://api.github.com/repos/DataDog/" + repository + "/pulls"
    response = requests.post(url=url, headers=headers, data=data)
    if response.status_code == 201:
        print("✔ Pull Request created successfully")
        return 0
    else:
        print("✘ pull request failed " + str(response.status_code) + '\n' + response.text)
        return 1


def generate_target_code(platform: str, source_path: str, temp_dir_path: str) -> int:
    cmd_args = ['./generator.py', '-s', source_path, '-o', temp_dir_path, '-p', platform]
    result = subprocess.call(cmd_args, shell=False, stdout=subprocess.DEVNULL)
    return result


def git_clone_repository(repo_name: str, gh_token: str, temp_dir_path: str, branch_name: str) -> Tuple[Repo, str]:
    url = "https://" + gh_token + ":x-oauth-basic@github.com/DataDog/" + repo_name
    repo = Repo.clone_from(url, temp_dir_path)
    base_name = repo.active_branch.name
    repo.git.checkout('HEAD', b=branch_name)
    return repo, base_name


def git_push_changes(repo: Repo, version: str):
    repo.git.add(update=True)
    repo.index.commit("Update generated code from bridge version " + version)
    origin = repo.remote(name="origin")
    repo.git.push("--set-upstream", "--force", origin, repo.head.ref)


def update_dependant(source_path: str, platform: str, version: str, gh_token: str) -> int:
    repo_name = REPOSITORIES[platform]
    branch_name = "generated_" + version
    temp_dir = TemporaryDirectory()
    temp_dir_path = temp_dir.name

    repo, base_name = git_clone_repository(repo_name, gh_token, temp_dir_path, branch_name)

    result = generate_target_code(platform, source_path, temp_dir_path)
    if result > 0:
        print("✘ generation failed for " + platform)
        return result

    if not repo.is_dirty():
        print("∅ Nothing to commit, all is in order…")
        return 0

    git_push_changes(repo, version)

    return github_create_pr(repo_name, branch_name, base_name, version, gh_token)


def run_main() -> int:
    cli_args = parse_arguments(sys.argv[1:])

    # This script expects to have a valid Github Token in a "gh_token" text file
    # The token needs the `repo` permissions, and for now is a PAT
    with open('gh_token', 'r') as f:
        gh_token = f.read().strip()

    return update_dependant(cli_args.source, cli_args.platform, cli_args.version, gh_token)


if __name__ == "__main__":
    sys.exit(run_main())
