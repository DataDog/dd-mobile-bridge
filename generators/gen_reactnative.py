#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from typing import TextIO

OUTPUT_TS_FOLDER = "src"
OUTPUT_TS_TYPES = "types.tsx"
OUTPUT_TS_INDEX = "index.tsx"

OUTPUT_AND_FOLDER = "android/src/main/java/com/datadog/reactnative"
OUTPUT_AND_PACKAGE = "DdSdkReactNativePackage.kt"
OUTPUT_AND_BRIDGE = "DdSdkBridgeExt.kt"

OUTPUT_IOS_FOLDER = "ios"

TS_TYPES = {
    'void': 'void',
    'boolean': 'boolean',
    'int': 'number',
    'float': 'number',
    'map': 'object',
    'list': 'array',
    'string': 'string'
}

AND_TYPES = {
    'void': 'Unit',
    'boolean': 'Boolean',
    'int': 'Int',
    'float': 'Float',
    'map': 'ReadableMap',
    'list': 'ReadableArray',
    'string': 'String'
}

IOS_TYPES_SWIFT = {
    'void': 'Void',
    'boolean': 'Bool',
    'int': 'Int',
    'float': 'Float',
    'map': 'NSDictionary',
    'list': 'NSArray',
    'string': 'NSString'
}

IOS_TYPES_OBJC = {
    'void': 'void',
    'boolean': 'BOOL',
    'int': 'NSInteger',
    'float': 'float',
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


def _get_ts_type(typename: str) -> str:
    if typename in TS_TYPES:
        return TS_TYPES[typename]
    else:
        return typename


def _get_and_type(typename: str, default: str = None) -> str:
    if typename in AND_TYPES:
        return AND_TYPES[typename]
    elif default:
        return default
    else:
        return typename


def _get_ios_type_swift(typename: str, default: str = None) -> str:
    if typename in IOS_TYPES_SWIFT:
        return IOS_TYPES_SWIFT[typename]
    elif default:
        return default
    else:
        return typename


def _get_ios_type_objc(typename: str, default: str = None) -> str:
    if typename in IOS_TYPES_OBJC:
        return IOS_TYPES_OBJC[typename]
    elif default:
        return default
    else:
        return typename


# noinspection PyMethodMayBeStatic
class RNGenerator:

    def __init__(self, output_folder: str):
        self.output_folder = output_folder

    def generate(self, definitions: list):
        self._generate_ts_index(definitions)
        self._generate_ts_types(definitions)
        self._generate_and_package(definitions)
        self._generate_and_bridge_ext(definitions)
        for definition in definitions:
            if definition['type'] == "interface":
                self._generate_and_implementation(definition)
                self._generate_ios_interface(definition)
                self._generate_ios_swift_implementation(definition)
            elif definition['type'] == "data":
                self._generate_and_data_ext(definition)
                self._generate_ios_struct_ext(definition)

    def _generate_ts_index(self, definitions: list):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_TS_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, OUTPUT_TS_INDEX)
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("import { NativeModules } from 'react-native';\n")

            output.write("import { ")
            for i, definition in enumerate(definitions):
                if i > 0:
                    output.write(", ")
                if definition['type'] == "interface":
                    output.write(definition['name'] + "Type")
                elif definition['type'] == "data":
                    output.write(definition['name'])
            output.write(" }  from './types';\n\n")

            for definition in definitions:
                if definition['type'] == "interface":
                    output.write("const ")
                    output.write(definition['name'])
                    output.write(": ")
                    output.write(definition['name'] + "Type")
                    output.write(" = NativeModules.")
                    output.write(definition['name'])
                    output.write('\n')

            output.write('\n')

            output.write("export { ")
            for i, definition in enumerate(definitions):
                if i > 0:
                    output.write(", ")
                output.write(definition['name'])
            output.write(" };\n")

    def _generate_ts_types(self, definitions: list):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_TS_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, OUTPUT_TS_TYPES)
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            for definition in definitions:
                if definition['type'] == "interface":
                    self._generate_ts_interface(definition, output)
                elif definition['type'] == "data":
                    self._generate_ts_data_class(definition, output)

    def _generate_ts_interface(self, definition: dict, output: TextIO):
        output.write("/**\n")
        output.write(" * " + definition['documentation'] + '\n')
        output.write(" */\n")
        output.write("export type " + definition['name'] + "Type = {\n")

        for method in definition['methods']:
            self._generate_ts_method(method, output)

        output.write("};\n\n")

    def _generate_ts_method(self, method: dict, output: TextIO):
        return_type = method['type']
        params = method['parameters']

        # Documentation
        output.write("  /**\n")
        output.write("   * " + method['documentation'] + '\n')
        for param in params:
            output.write("   * " + param['name'] + ": " + param['documentation'] + '\n')
        output.write("   */\n")

        # Method signature
        output.write("  " + method['name'] + "(")

        for i, param in enumerate(params):
            if i > 0:
                output.write(", ")
            output.write(param['name'])
            output.write(": " + _get_ts_type(param['type']))

        output.write("): ")
        output.write("Promise<")
        output.write(_get_ts_type(return_type))
        output.write(">")
        output.write(";\n\n")

    def _generate_ts_data_class(self, definition: dict, output: TextIO):
        # Documentation
        output.write("/**\n")
        output.write(" * " + definition['documentation'] + '\n')
        output.write(" */\n")

        # Data class structure
        output.write("export class " + definition['name'] + " {\n")

        output.write("  constructor(\n")
        for i, prop in enumerate(definition['properties']):
            if i > 0:
                output.write(",\n")
            output.write("    readonly ")
            output.write(prop['name'] + ": " + _get_ts_type(prop['type']))

        output.write("\n  ) {}\n")
        output.write("};\n\n")

    def _generate_and_implementation(self, definition: dict):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_AND_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, "RN" + definition['name'] + ".kt")
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("package com.datadog.reactnative\n\n")

            output.write("import com.datadog.android.bridge." + definition['name'] + "\n")
            output.write("import com.facebook.react.bridge.Promise\n")
            output.write("import com.facebook.react.bridge.ReactApplicationContext\n")
            output.write("import com.facebook.react.bridge.ReactContextBaseJavaModule\n")
            output.write("import com.facebook.react.bridge.ReactMethod\n")
            output.write("import com.facebook.react.bridge.ReadableArray\n")
            output.write("import com.facebook.react.bridge.ReadableMap\n")
            output.write("\n")

            output.write("/**\n")
            output.write(" * " + definition['documentation'] + '\n')
            output.write(" */\n")

            output.write("class RN" + definition['name'])
            output.write("(reactContext: ReactApplicationContext) : ReactContextBaseJavaModule(reactContext) {\n\n")

            output.write("    private val nativeInstance: ")
            output.write(definition['name'])
            output.write(" = ")
            output.write(definition['name'])
            output.write("(reactContext)\n\n")

            output.write("    override fun getName(): String = \"")
            output.write(definition['name'])
            output.write("\"\n\n")

            for method in definition['methods']:
                self._generate_and_method(method, output)

            output.write("}\n")

    def _generate_and_method(self, method: dict, output: TextIO):
        params = method['parameters']
        return_type = method['type']

        output.write("    /**\n")
        output.write("     * " + method['documentation'] + '\n')
        for param in params:
            output.write("     * @param ")
            output.write(param['name'] + " " + param['documentation'] + '\n')
        output.write("     */\n")

        output.write("    @ReactMethod\n")
        output.write("    fun " + method['name'] + "(")

        for i, param in enumerate(params):
            if i > 0:
                output.write(", ")
            output.write(param['name'] + ": " + _get_and_type(param['type'], "ReadableMap"))
        if len(params) > 0:
            output.write(", ")
        output.write("promise: Promise) {\n")

        output.write("        ")
        if return_type != "void":
            output.write("        val result = ")
        output.write("nativeInstance.")
        output.write(method['name'])
        output.write('(')
        for i, param in enumerate(params):
            if i > 0:
                output.write(", ")
            output.write(param['name'])
            if param['type'] == 'map':
                output.write('.toHashMap()')
            elif param['type'] == 'list':
                output.write('.toArrayList()')
            elif param['type'] not in AND_TYPES:
                output.write('.as')
                output.write(param['type'])
                output.write('()')
        output.write(')\n')

        if return_type == 'void':
            output.write("        promise.resolve(null)\n")
        elif return_type == 'map':
            output.write("        promise.resolve(result.toWritableMap())\n")
        elif return_type == 'list':
            output.write("        promise.resolve(result.toWritableArray())\n")
        elif return_type in ['boolean', 'int', 'float', 'string']:
            output.write("        promise.resolve(result)\n")
        else:
            output.write("        promise.resolve(result.toReadableMap())\n")
        output.write("    }\n\n")

    def _generate_and_bridge_ext(self, definitions: list):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_AND_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, OUTPUT_AND_BRIDGE)
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("package com.datadog.reactnative\n\n")

            output.write("import com.facebook.react.bridge.WritableNativeArray\n")
            output.write("import com.facebook.react.bridge.WritableNativeMap\n")
            output.write("\n")

            output.write("fun List<*>.toWritableArray(): WritableNativeArray {\n")
            output.write("    val list = WritableNativeArray()\n")
            output.write("    forEach {\n")
            output.write("        when (it) {\n")
            output.write("            null -> list.pushNull()\n")
            output.write("            is Int -> list.pushInt(it)\n")
            output.write("            is Float -> list.pushDouble(it.toDouble())\n")
            output.write("            is String -> list.pushString(it)\n")
            output.write("            is List<*> -> list.pushArray(it.toWritableArray())\n")
            output.write("            is Map<*, *> -> list.pushMap(it.toWritableMap())\n")
            output.write("            else -> TODO()\n")
            output.write("        }\n")
            output.write("    }\n")
            output.write("    return list\n")
            output.write("}\n\n")

            output.write("fun Map<*, *>.toWritableMap(): WritableNativeMap {\n")
            output.write("    val map = WritableNativeMap()\n")
            output.write("    forEach { (k, v) ->\n")
            output.write("        val key = (k as? String) ?: k.toString()\n")
            output.write("        when (v) {\n")
            output.write("            null -> map.putNull(key)\n")
            output.write("            is Int -> map.putInt(key, v)\n")
            output.write("            is Float -> map.putDouble(key, v.toDouble())\n")
            output.write("            is Double -> map.putDouble(key, v)\n")
            output.write("            is String -> map.putString(key, v)\n")
            output.write("            is List<*> -> map.putArray(key, v.toWritableArray())\n")
            output.write("            is Map<*, *> -> map.putMap(key, v.toWritableMap())\n")
            output.write("            else -> TODO()\n")
            output.write("        }\n")
            output.write("    }\n")
            output.write("    return map\n")
            output.write("}\n")

            for definition in definitions:
                if definition['type'] == "data":
                    pass

    def _generate_and_data_ext(self, definition: dict):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_AND_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, "RN" + definition['name'] + ".kt")
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("package com.datadog.reactnative\n\n")

            output.write("import com.datadog.android.bridge." + definition['name'] + "\n")
            output.write("import com.facebook.react.bridge.ReadableArray\n")
            output.write("import com.facebook.react.bridge.ReadableMap\n")
            output.write("import com.facebook.react.bridge.WritableNativeMap\n")

            self._generate_and_data_ext_from_map(definition, output)
            self._generate_and_data_ext_to_map(definition, output)

    def _generate_and_data_ext_from_map(self, definition: dict, output: TextIO):
        output.write("\n")
        output.write("fun ReadableMap.as")
        output.write(definition['name'])
        output.write("(): ")
        output.write(definition['name'])
        output.write("{\n")

        output.write("    return ")
        output.write(definition['name'])
        output.write("(\n")
        for i, prop in enumerate(definition['properties']):
            if i > 0:
                output.write(",\n")
            property_name = prop['name']
            property_type = prop['type']
            property_mandatory = prop['mandatory']
            output.write("        ")
            output.write(property_name)
            output.write(" = ")
            if property_type == "string":
                output.write("getString(\"")
                output.write(property_name)
                output.write("\")")
                if property_mandatory:
                    output.write(".orEmpty()")
            elif property_type == "boolean":
                output.write("getBoolean(\"")
                output.write(property_name)
                output.write("\")")
            elif property_type == "int":
                output.write("getInt(\"")
                output.write(property_name)
                output.write("\")")
            elif property_type == "double":
                output.write("getDouble(\"")
                output.write(property_name)
                output.write("\")")
            elif property_type == "float":
                output.write("getDouble(\"")
                output.write(property_name)
                output.write("\").toFloat()")
            elif property_type == "list":
                output.write("getArray(\"")
                output.write(property_name)
                output.write("\")?.toArrayList()")
                if property_mandatory:
                    output.write("!!")
            elif property_type == "map":
                output.write("getMap(\"")
                output.write(property_name)
                output.write("\")?.toHashMap()")
                if property_mandatory:
                    output.write("!!")
            else:
                output.write("getMap(\"")
                output.write(property_name)
                output.write("\")?.as")
                output.write(property_type)
                output.write("()")
                if property_mandatory:
                    output.write("!!")
        output.write("\n    )\n")

        output.write("}\n")

    def _generate_and_data_ext_to_map(self, definition: dict, output: TextIO):
        output.write("\n")
        output.write("fun ")
        output.write(definition['name'])
        output.write(".toReadableMap(): WritableNativeMap {\n")
        output.write("    val map = WritableNativeMap()\n")

        for prop in definition['properties']:
            property_name = prop['name']
            property_type = prop['type']
            property_mandatory = prop['mandatory']
            output.write("    ")
            if not property_mandatory:
                output.write("if (")
                output.write(property_name)
                output.write(" != null) ")

            if property_type == "string":
                output.write("map.putString(\"")
                output.write(property_name)
                output.write("\", ")
                output.write(property_name)
                output.write(")")
            elif property_type == "boolean":
                output.write("map.putBoolean(\"")
                output.write(property_name)
                output.write("\", ")
                output.write(property_name)
                output.write(")")
            elif property_type == "int":
                output.write("map.putInt(\"")
                output.write(property_name)
                output.write("\", ")
                output.write(property_name)
                output.write(")")
            elif property_type == "double":
                output.write("map.putDouble(\"")
                output.write(property_name)
                output.write("\", ")
                output.write(property_name)
                output.write(")")
            elif property_type == "float":
                output.write("map.putDouble(\"")
                output.write(property_name)
                output.write("\", ")
                output.write(property_name)
                output.write(".toDouble())")
            elif property_type == "list":
                output.write("map.putArray(\"")
                output.write(property_name)
                output.write("\", ")
                output.write(property_name)
                output.write(".toWritableArray())")
            elif property_type == "map":
                output.write("map.putMap(\"")
                output.write(property_name)
                output.write("\", ")
                output.write(property_name)
                output.write(".toWritableMap())")
            else:
                output.write("map.putMap(\"")
                output.write(property_name)
                output.write("\", ")
                output.write(property_name)
                output.write(".toReadableMap())")
            output.write("\n")
        output.write("    return map\n")
        output.write("}\n")

    def _generate_and_package(self, definitions: list):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_AND_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, OUTPUT_AND_PACKAGE)
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("package com.datadog.reactnative\n\n")
            output.write("import com.facebook.react.ReactPackage\n")
            output.write("import com.facebook.react.bridge.NativeModule\n")
            output.write("import com.facebook.react.bridge.ReactApplicationContext\n")
            output.write("import com.facebook.react.uimanager.ViewManager\n\n")

            output.write("class DdSdkReactNativePackage : ReactPackage {\n\n")

            output.write("    override fun createViewManagers(\n")
            output.write("        reactContext: ReactApplicationContext\n")
            output.write("    ): List<ViewManager<*, *>> {\n")
            output.write("        return emptyList()\n")
            output.write("    }\n\n")

            output.write("    override fun createNativeModules(\n")
            output.write("        reactContext: ReactApplicationContext\n")
            output.write("    ): List<NativeModule> {\n")
            output.write("        return listOf(\n")

            i = 0
            for definition in definitions:
                if definition['type'] == "interface":
                    if i > 0:
                        output.write(",\n")
                    i = i + 1
                    output.write("            RN" + definition['name'] + "(reactContext)")

            output.write("\n        )\n")
            output.write("    }\n")

            output.write("}\n")

    def _generate_ios_interface(self, definition: dict):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_IOS_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, definition['name'] + ".m")
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("#import <React/RCTBridgeModule.h>\n\n")
            output.write("@interface RCT_EXTERN_MODULE(")
            output.write(definition['name'])
            output.write(", NSObject)\n\n")

            for method in definition['methods']:
                self._generate_ios_method(method, output)

            output.write("@end\n")

    def _generate_ios_method(self, method: dict, output: TextIO):
        params = method['parameters']

        output.write("RCT_EXTERN_METHOD(")
        output.write(method['name'])

        for i, param in enumerate(params):
            if i > 0:
                output.write("\n                 with")
                output.write(param['name'].capitalize())
            output.write(":(" + _get_ios_type_objc(param['type'], "NSDictionary") + ")" + param['name'])

        output.write("\n                 withResolver:(RCTPromiseResolveBlock)resolve")
        output.write("\n                 withRejecter:(RCTPromiseRejectBlock)reject")
        output.write(")\n\n")

    def _generate_ios_swift_implementation(self, definition: dict):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_IOS_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, definition['name'] + ".swift")
        print("writing to " + output_path)
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("import Foundation\n\n")
            output.write("@objc(" + definition['name'] + ")\n")
            output.write("class RN" + definition['name'] + ": NSObject {\n\n")
            output.write("    let nativeInstance = " + definition['name'] + "()\n\n")

            for method in definition['methods']:
                self._generate_ios_swift_method(method, output)

            output.write("}\n")

    def _generate_ios_swift_method(self, method: dict, output: TextIO):
        params = method['parameters']
        return_type = method['type']

        output.write("    @objc(")
        output.write(method['name'])
        for i, param in enumerate(params):
            if i > 0:
                output.write("with")
                output.write(param['name'].capitalize())
            output.write(":")
        output.write("withResolver:withRejecter:)\n")
        output.write("    func " + method['name'] + "(")

        for i, param in enumerate(params):
            if i > 0:
                output.write(", ")
            output.write(param['name'] + ": " + _get_ios_type_swift(param['type'], "NSDictionary"))
        if len(params) > 0:
            output.write(", ")
        output.write("resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock)")
        output.write(" -> Void {\n")

        output.write("        ")
        if return_type != "void":
            output.write("let result = ")
        output.write("nativeInstance.")
        output.write(method['name'])
        output.write('(')
        for i, param in enumerate(params):
            if i > 0:
                output.write(", ")
            output.write(param['name'])
            output.write(": ")
            output.write(param['name'])
            if param['type'] not in AND_TYPES:
                output.write('.as')
                output.write(param['type'])
                output.write('()')
        output.write(')\n')

        if return_type == 'void':
            output.write("        resolve(nil)\n")
        else:
            output.write("        resolve(result)\n")
        # TODO convert inner types to Maps/Lists
        output.write("    }\n\n")

    def _generate_ios_struct_ext(self, definition: dict):
        output_folder_path = os.path.join(self.output_folder, OUTPUT_IOS_FOLDER)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        output_path = os.path.join(output_folder_path, "RN" + definition['name'] + ".swift")
        with open(output_path, 'w') as output:
            output.write(LICENSE_HEADER)
            output.write("import Foundation\n\n")

            output.write("extension NSDictionary {\n\n")

            self._generate_ios_struct_ext_from_dict(definition, output)

            output.write("}\n")

    def _generate_ios_struct_ext_from_dict(self, definition: dict, output: TextIO):
        output.write("    func as")
        output.write(definition['name'])
        output.write("() -> ")
        output.write(definition['name'])
        output.write(" {\n")

        for prop in definition['properties']:
            output.write("        let ")
            output.write(prop['name'])
            output.write(" = ")
            output.write("object(forKey: \"")
            output.write(prop['name'])
            output.write("\") as? ")
            output.write(_get_ios_type_swift(prop['type']))
            output.write("\n")

        output.write("        return ")
        output.write(definition['name'])
        output.write("(\n")
        for i, prop in enumerate(definition['properties']):
            if i > 0:
                output.write(",\n")
            property_name = prop['name']
            property_type = prop['type']
            property_mandatory = prop['mandatory']
            output.write("            ")
            output.write(property_name)
            output.write(": ")

            if property_mandatory:
                output.write("(")
                output.write(property_name)
                output.write(" != nil) ? ")
                output.write(property_name)
                output.write("! : ")
                if property_type == "string":
                    output.write("NSString()")
                elif property_type == "boolean":
                    output.write("false")
                elif property_type == "int":
                    output.write("0")
                elif property_type == "float":
                    output.write("0.0")
                elif property_type == "list":
                    output.write("NSArray()")
                elif property_type == "map":
                    output.write("NSDictionary()")

            else:
                output.write(property_name)

            # TODO map object to known type

        output.write("\n        )\n")

        output.write("    }\n")
