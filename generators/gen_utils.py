#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc

import os

TYPE_VOID = 'void'
TYPE_BOOL = 'boolean'
TYPE_LONG = 'long'
TYPE_DOUBLE = 'double'
TYPE_STRING = 'string'
TYPE_MAP = 'map'
TYPE_LIST = 'list'

LICENSE_HEADER = """/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

"""


def prepare_output_path(root_folder: str, output_folder: str, file_name: str) -> str:
    output_folder_path = os.path.join(root_folder, output_folder)
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    return os.path.join(output_folder_path, file_name)

def interface_definition_has_optional_params(definition: dict) -> bool:
    for method in definition['methods']:
        for parameter in method['parameters']:
            if parameter.get("optional"):
                return True
    return False
