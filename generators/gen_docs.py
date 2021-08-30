#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc

import os
from typing import TextIO
from .gen_utils import *

OUTPUT_FILE = 'API_REFERENCE.md'

HEADER = """# Bridge API Reference

"""


# noinspection PyMethodMayBeStatic
class ReadmeGenerator:

    def __init__(self, output_folder: str):
        self.output_folder = output_folder

    def generate(self, definitions: list):
        output_path = prepare_output_path(self.output_folder, ".", OUTPUT_FILE)

        with open(output_path, 'w') as output:
            output.write(HEADER)

            output.write("## Interfaces\n\n")
            for definition in definitions:
                if definition['type'] == "interface":
                    self._generate_interface(definition, output)

            output.write("## Data structures\n\n")
            for definition in definitions:
                if definition['type'] == "data":
                    self._generate_structure(definition, output)

    def _generate_interface(self, definition: dict, output: TextIO):
        output.write("#### ")
        output.write(definition['name'])
        output.write("\n\n")

        output.write(definition['documentation'])
        output.write("\n\n")

        for method in definition['methods']:
            self._generate_method(method, output)
            pass

    def _generate_method(self, method: dict, output: TextIO):
        params = method["parameters"]

        output.write("- `")
        output.write(method['name'])
        output.write("(")
        for i, param in enumerate(params):
            if i > 0:
                output.write(", ")
            output.write(param['name'] + ": " + param['type'])
        output.write(")`\n\n")

        output.write("    ")
        output.write(method['documentation'])
        output.write("\n\n")

        for param in params:
            output.write("    - `")
            output.write(param['name'])
            output.write("`: ")
            if param.get('optional'):
                output.write("Optional. ")
            output.write(param['documentation'])
            output.write('\n')
        output.write('\n')

    def _generate_structure(self, definition: dict, output: TextIO):
        output.write("#### ")
        output.write(definition['name'])
        output.write("\n\n")

        output.write(definition['documentation'])
        output.write("\n\n")

        for prop in definition['properties']:
            output.write("- `")
            output.write(prop['name'])
            output.write("` (")
            output.write(prop['type'])
            output.write("): ")
            output.write(prop['documentation'])
            output.write("\n")
        output.write("\n")
