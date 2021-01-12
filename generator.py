#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc


import json
import sys
from argparse import ArgumentParser, Namespace
from typing import Any

PLATFORM_RN = "reactnative"
PLATFORM_AND = "android"
PLATFORM_IOS = "ios"
PLATFORM_DOCS = "docs"

PLATFORMS = [PLATFORM_AND, PLATFORM_IOS, PLATFORM_DOCS, PLATFORM_RN]

def parse_arguments(args: list) -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("-s", "--source", required=True, help="the source Json definition of the API")
    parser.add_argument("-o", "--output", required=False, default=".", help="the output folder")
    parser.add_argument("-p", "--platform", required=True,
                        choices=PLATFORMS,
                        help="the target platform")

    return parser.parse_args(args)


def load_definition_from_path(path: str) -> Any:
    with open(path) as json_file:
        return json.load(json_file)


def load_generator(platform: str, output_folder: str) -> Any:
    if platform == PLATFORM_AND:
        from generators.gen_android import AndroidGenerator
        return AndroidGenerator(output_folder)
    if platform == PLATFORM_IOS:
        from generators.gen_ios import IOSGenerator
        return IOSGenerator(output_folder)
    if platform == PLATFORM_DOCS:
        from generators.gen_docs import ReadmeGenerator
        return ReadmeGenerator(output_folder)
    if platform == PLATFORM_RN:
        from generators.gen_reactnative import RNGenerator
        return RNGenerator(output_folder)
    else:
        raise RuntimeError("Unknown platform " + platform)


def run_generator(platform: str, output_folder: str, definition_path: str) -> int:
    generator = load_generator(platform, output_folder)
    definitions = load_definition_from_path(definition_path)

    if isinstance(definitions, list):
        generator.generate(definitions)
    else:
        raise RuntimeError("Expected definitions to be a list, but was  " + str(type(definitions)))

    return 0


def run_main() -> int:
    cli_args = parse_arguments(sys.argv[1:])
    return run_generator(cli_args.platform, cli_args.output, cli_args.source)


if __name__ == "__main__":
    sys.exit(run_main())
