#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc

import os
import sys
from git import Repo
from generator import run_generator, PLATFORM_DOCS
from generators.gen_docs import OUTPUT_FILE

DOCS_PATH = OUTPUT_FILE
DEFINITION_PATH = 'mobile-bridge-api.json'


def _validate_docs():
    current_path = os.path.abspath(os.path.dirname(__file__))
    run_generator(PLATFORM_DOCS, current_path, DEFINITION_PATH)

    repo = Repo(current_path)
    head_commit = repo.head.commit
    diff_index = head_commit.diff(None)

    for change_type in diff_index.change_type:
        for diff in diff_index.iter_change_type(change_type):
            if diff.a_path == DOCS_PATH or diff.b_path == DOCS_PATH:
                print(" ✘ " + DOCS_PATH + " doesn't match the mobile bridge definition. "
                      "Make sure you update it before submitting your PR.")
                return 1
    print(" ✔ " + DOCS_PATH + " matches the mobile bridge definition.")
    return 0


if __name__ == "__main__":
    sys.exit(_validate_docs())
