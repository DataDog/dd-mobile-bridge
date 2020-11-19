#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from git import Repo
from generator import run_generator, PLATFORM_README

readme_path = 'README.md'
definition_path = 'mobile-bridge-api.json'


def _validate_readme():
    current_path = os.path.abspath(os.path.dirname(__file__))
    run_generator(PLATFORM_README, current_path, definition_path)

    repo = Repo(current_path)
    head_commit = repo.head.commit
    diff_index = head_commit.diff(None)

    for change_type in diff_index.change_type:
        for diff in diff_index.iter_change_type(change_type):
            if diff.a_path == readme_path or diff.b_path == readme_path:
                print(" ✘ README.md doesn't match the mobile bridge definition. "
                      "Make sure you update it before submitting your PR.")
                return 1
    print(" ✔ README.md matches the mobile bridge definition.")
    return 0


if __name__ == "__main__":
    sys.exit(_validate_readme())
