#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

OUTPUT_IOS_FOLDER = os.path.join("dd-sdk-ios", "Sources", "Datadog", "Bridge")

IOS_TYPES_SWIFT = {
    'void': 'Void',
    'boolean': 'Bool',
    'int': 'Int',
    'float': 'Float',
    'map': 'NSDictionary',
    'list': 'NSArray',
    'string': 'NSString'
}

LICENSE_HEADER = """/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

"""


def _get_ios_type_swift(typename: str, default: str = None) -> str:
    if typename in IOS_TYPES_SWIFT:
        return IOS_TYPES_SWIFT[typename]
    elif default:
        return default
    else:
        return typename


class IOSGenerator:

    def __init__(self, output_folder: str):
        self.output_folder = output_folder

    def generate(self, definitions: list):
        for definition in definitions:
            if definition['type'] == "interface":
                self._generate_ios_interface(definition)
            elif definition['type'] == "data":
                self._generate_ios_data(definition)

    def _generate_ios_interface(self, definition: dict):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_IOS_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, definition['name'] + ".swift")
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("import Foundation\n\n")

            if "documentation" in definition:
                output.write("/**\n")
                output.write("   " + definition['documentation'] + '\n')
                output.write(" */\n")

            output.write("@objc(" + definition['name'] + ")\n")
            output.write("protocol " + definition['name'] + " {\n\n")

            for method in definition['methods']:
                if 'documentation' in method:
                    output.write("    /**\n")
                    output.write("       " + method['documentation'] + '\n')
                    output.write("     */\n")

                output.write("    func " + method['name'] + "(")

                for i, param in enumerate(method['parameters']):
                    if i > 0:
                        output.write(", ")
                    output.write(param['name'] + ": " + _get_ios_type_swift(param['type']))
                output.write(") -> ")
                output.write(_get_ios_type_swift(method['type']))
                output.write("\n\n")

            output.write("}\n")

    def _generate_ios_data(self, definition: dict):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_IOS_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, definition['name'] + ".swift")
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("import Foundation\n\n")

            # Documentation
            output.write("/**\n")
            output.write(" " + definition['documentation'] + '\n')
            if len(definition['properties']):
                output.write(" - Parameters:\n")
                for prop in definition['properties']:
                    output.write("     - ")
                    output.write(prop['name'])
                    output.write(": ")
                    output.write(prop['documentation'])
                    output.write("\n")
            output.write(" */\n")

            output.write("struct ")
            output.write(definition['name'])
            output.write("{\n")
            for i, prop in enumerate(definition['properties']):
                if i > 0:
                    output.write(",\n")
                property_name = prop['name']
                property_type = prop['type']
                property_mandatory = prop['mandatory']
                if property_mandatory:
                    output.write("    let ")
                else:
                    output.write("    var ")
                output.write(property_name)
                output.write(": ")
                output.write(_get_ios_type_swift(property_type))
                if not property_mandatory:
                    output.write("? = nil")

            output.write("\n}\n")
