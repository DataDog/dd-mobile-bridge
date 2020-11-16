#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from .gen_utils import *

OUTPUT_AND_FOLDER = os.path.join("dd-sdk-android", "src", "main", "java", "com", "datadog", "android", "bridge")

AND_TYPES = {
    TYPE_VOID: 'Unit',
    TYPE_BOOL: 'Boolean',
    TYPE_INT: 'Int',
    TYPE_FLOAT: 'Float',
    TYPE_MAP: 'Map<String, Any?>',
    TYPE_LIST: 'List<Any?>',
    TYPE_STRING: 'String'
}


def _get_and_type(typename: str, default: str = None) -> str:
    if typename in AND_TYPES:
        return AND_TYPES[typename]
    elif default:
        return default
    else:
        return typename


class AndroidGenerator:

    def __init__(self, output_folder: str):
        self.output_folder = output_folder

    def generate(self, definitions: list):
        for definition in definitions:
            if definition['type'] == "interface":
                self._generate_and_interface(definition)
            elif definition['type'] == "data":
                self._generate_and_data(definition)

    def _generate_and_interface(self, definition: dict):
        file_name = definition['name'] + ".kt"
        output_path = prepare_output_path(self.output_folder, OUTPUT_AND_FOLDER, file_name)
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("package com.datadog.android.bridge\n\n")

            output.write("import android.content.Context\n")
            output.write("\n")

            if "documentation" in definition:
                output.write("/**\n")
                output.write(" * " + definition['documentation'] + '\n')
                output.write(" */\n")

            output.write("interface " + definition['name'] + " {\n\n")

            for method in definition['methods']:
                if 'documentation' in method:
                    output.write("    /**\n")
                    output.write("     * " + method['documentation'] + '\n')
                    output.write("     */\n")

                output.write("    fun " + method['name'] + "(")

                for i, param in enumerate(method['parameters']):
                    if i > 0:
                        output.write(", ")
                    output.write(param['name'] + ": " + _get_and_type(param['type']))
                output.write("): ")
                output.write(_get_and_type(method['type']))
                output.write("\n\n")

            output.write("}\n")

    def _generate_and_data(self, definition: dict):
        file_name = definition['name'] + ".kt"
        output_path = prepare_output_path(self.output_folder, OUTPUT_AND_FOLDER, file_name)
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("package com.datadog.android.bridge\n\n")

            # Documentation
            output.write("/**\n")
            output.write(" * " + definition['documentation'] + '\n')
            for prop in definition['properties']:
                output.write(" * @param ")
                output.write(prop['name'])
                output.write(" ")
                output.write(prop['documentation'])
                output.write("\n")
            output.write(" */\n")

            output.write("data class ")
            output.write(definition['name'])
            output.write("(\n")
            for i, prop in enumerate(definition['properties']):
                if i > 0:
                    output.write(",\n")
                property_name = prop['name']
                property_type = prop['type']
                property_mandatory = prop['mandatory']
                output.write("    val ")
                output.write(property_name)
                output.write(": ")
                output.write(_get_and_type(property_type))
                if not property_mandatory:
                    output.write("? = null")

            output.write("\n)\n")
