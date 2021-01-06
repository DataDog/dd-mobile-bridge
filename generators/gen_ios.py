#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc

import os
from .gen_utils import *

OUTPUT_IOS_FOLDER = os.path.join("Sources", "Bridge")

IOS_TYPES_SWIFT = {
    TYPE_VOID: 'Void',
    TYPE_BOOL: 'Bool',
    TYPE_LONG: 'Int64',
    TYPE_DOUBLE: 'Double',
    TYPE_MAP: 'NSDictionary',
    TYPE_LIST: 'NSArray',
    TYPE_STRING: 'NSString'
}


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
        file_name = definition['name'] + ".swift"
        output_path = prepare_output_path(self.output_folder, OUTPUT_IOS_FOLDER, file_name)
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("import Foundation\n\n")

            if "documentation" in definition:
                output.write("/**\n")
                output.write("   " + definition['documentation'] + '\n')
                output.write(" */\n")

            output.write("@objc(" + definition['name'] + ")\n")
            output.write("public protocol " + definition['name'] + " {\n")

            method_signatures = map(self._ios_method_signature, definition['methods'])
            output.write("\n".join(method_signatures))
            output.write("}\n")

    def _ios_method_signature(self, method):
        output = ""
        if 'documentation' in method:
            output += "    /**\n"
            output += "       " + method['documentation'] + '\n'
            output += "     */\n"

        output += "    func " + method['name'] + "("

        for i, param in enumerate(method['parameters']):
            if i > 0:
                output += ", "

            output += param['name'] + ": " + _get_ios_type_swift(param['type'])

        output += ")"

        method_type = _get_ios_type_swift(method['type'])
        if method_type is not IOS_TYPES_SWIFT[TYPE_VOID]:
            output += " -> "
            output += _get_ios_type_swift(method_type)

        output += "\n"
        return output

    def _generate_ios_data(self, definition: dict):
        file_name = definition['name'] + ".swift"
        output_path = prepare_output_path(self.output_folder, OUTPUT_IOS_FOLDER, file_name)
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

            output.write("@objc(")
            output.write(definition['name'])
            output.write(")\n")
            output.write("public class ")
            output.write(definition['name'])
            output.write(": NSObject {\n")
            for i, prop in enumerate(definition['properties']):
                if i > 0:
                    output.write("\n")
                property_name = prop['name']
                property_type = prop['type']
                property_mandatory = prop['mandatory']
                output.write("    public var ")
                output.write(property_name)
                output.write(": ")
                output.write(_get_ios_type_swift(property_type))
                if property_mandatory:
                    if property_type == TYPE_BOOL:
                        output.write(" = false")
                    elif property_type == TYPE_LONG:
                        output.write(" = 0")
                    elif property_type == TYPE_DOUBLE:
                        output.write(" = 0.0")
                    elif property_type == TYPE_STRING:
                        output.write(" = \"\"")
                    elif property_type == TYPE_MAP:
                        output.write(" = NSDictionary()")
                    elif property_type == TYPE_LIST:
                        output.write(" = NSArray()")
                else:
                    output.write("? = nil")

            output.write("\n\n    public init(")
            for i, prop in enumerate(definition['properties']):
                if i > 0:
                    output.write(",")
                property_name = prop['name']
                property_type = prop['type']
                property_mandatory = prop['mandatory']
                output.write("\n        ")
                output.write(property_name)
                output.write(": ")
                output.write(_get_ios_type_swift(property_type))
                if not property_mandatory:
                    output.write("?")

            output.write("\n    ) {\n")
            for prop in definition['properties']:
                property_name = prop['name']
                output.write("        self.")
                output.write(property_name)
                output.write(" = ")
                output.write(property_name)
                output.write("\n")
            output.write("    }\n")

            output.write("}\n")
