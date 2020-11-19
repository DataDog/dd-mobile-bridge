#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import sys
from argparse import ArgumentParser, Namespace
from typing import Any

PLATFORM_RN = "reactnative"
PLATFORM_AND = "android"
PLATFORM_IOS = "ios"
PLATFORM_README = "readme"


def parse_arguments(args: list) -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("-s", "--source", required=True, help="the source Json definition of the API")
    parser.add_argument("-o", "--output", required=False, default=".", help="the output folder")
    parser.add_argument("-p", "--platform", required=True,
                        choices=[PLATFORM_AND, PLATFORM_IOS, PLATFORM_README, PLATFORM_RN],
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
    if platform == PLATFORM_README:
        from generators.gen_readme import ReadmeGenerator
        return ReadmeGenerator(output_folder)
    if platform == PLATFORM_RN:
        from generators.gen_reactnative import RNGenerator
        return RNGenerator(output_folder)
    else:
        raise RuntimeError("Unknown platform " + platform)


def run_main() -> int:
    cli_args = parse_arguments(sys.argv[1:])

    generator = load_generator(cli_args.platform, cli_args.output)
    definitions = load_definition_from_path(cli_args.source)

    if isinstance(definitions, list):
        generator.generate(definitions)
    else:
        raise RuntimeError("Expected definitions to be a list, but was  " + str(type(definitions)))

    return 0


if __name__ == "__main__":
    sys.exit(run_main())
