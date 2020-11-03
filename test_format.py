#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import jsonschema
import os
import sys


def _validate_file(test_file_path, schema, resolver):
    with open(test_file_path) as test_file:
        test_json = json.load(test_file)
        try:
            jsonschema.validate(test_json, schema, resolver=resolver)
            print(" ✔ '" + test_file_path + "' file is valid")
        except jsonschema.exceptions.ValidationError as err:
            print(" ✘ '" + test_file_path + "' file is not valid")
            print(err, file=sys.stderr)


def _validate_project():
    schema_path = 'bridge-schema.json'
    api_path = 'mobile-bridge-api.json'
    test_folder_path = 'tests/format'

    current_path = os.path.abspath(os.path.dirname(__file__))
    test_file_names = [f for f in os.listdir(test_folder_path) if f.endswith(".json")]

    with open(schema_path) as file_object:
        schema = json.load(file_object)
        resolver = jsonschema.RefResolver(base_uri='file://' + current_path + '/', referrer=schema)

        for test_file_name in test_file_names:
            test_file_path = test_folder_path + "/" + test_file_name
            _validate_file(test_file_path, schema, resolver)

        _validate_file(api_path, schema, resolver)


if __name__ == "__main__":
    sys.exit(_validate_project())
