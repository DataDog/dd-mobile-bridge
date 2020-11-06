#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import difflib
import filecmp
import json
import jsonschema
import os
import shutil
import subprocess
import sys


def _report_file_diff(output_file_path, expected_file_path):
    with open(output_file_path, 'r') as output_file:
        with open(expected_file_path, 'r') as expected_file:
            diff = difflib.unified_diff(
                output_file.readlines(),
                expected_file.readlines(),
                fromfile=output_file_path,
                tofile=expected_file_path,
            )
            for line in diff:
                sys.stdout.write(line)


def _compare_folders(output_dir_path, expected_dir_path):
    comparison = filecmp.dircmp(output_dir_path, expected_dir_path)
    common = sorted(comparison.common)
    expected = sorted(comparison.right_list)
    invalid_count = 0

    if common != expected:
        print("  ✘ Invalid output in " + output_dir_path)
        print("     Missing the following files: " + repr(comparison.right_only))
        print("     Unexpected generated files:  " + repr(comparison.left_only))
        invalid_count += len(comparison.right_only) + len(comparison.left_only)

    diff_files = comparison.diff_files
    if len(diff_files) > 0:
        print("  ✘ Invalid output in " + output_dir_path)
        for subfile in diff_files:
            print("     File " + subfile + " content didn't meet expectations")
            invalid_count = invalid_count + 1
            _report_file_diff(os.path.join(output_dir_path, subfile), os.path.join(expected_dir_path, subfile))

    for subdir in comparison.common_dirs:
        output_subdir = os.path.join(output_dir_path, subdir)
        expected_subdir = os.path.join(expected_dir_path, subdir)
        invalid_count = invalid_count + _compare_folders(output_subdir, expected_subdir)
    return invalid_count


def _validate_generator_case(platform, test_case):
    source_path = "tests/gen_" + platform + "/" + test_case + "/input.json"
    output_dir_path = "tests/gen_" + platform + "/" + test_case + "/output"
    expected_dir_path = "tests/gen_" + platform + "/" + test_case + "/expected"

    # Clear any previous data
    shutil.rmtree(output_dir_path, ignore_errors=True)

    print("… Generating code for " + platform + "/" + test_case)
    cmd_args = ['./generator.py', '-s', source_path, '-o', output_dir_path, '-p', platform]
    result = subprocess.call(cmd_args, shell=False, stdout=subprocess.DEVNULL)
    if result > 0:
        print("✘ generation failed for " + platform + "/" + test_case)
        return

    print("… Verifying generated code for " + platform + "/" + test_case)
    result = _compare_folders(output_dir_path, expected_dir_path)

    if result == 0:
        shutil.rmtree(output_dir_path, ignore_errors=True)
    return result


def _validate_generator(platform):
    test_dir_path = "tests/gen_" + platform + "/"
    test_dir_names = [f for f in os.listdir(test_dir_path)]
    invalid_count = 0
    for test_case in test_dir_names:
        invalid_count = invalid_count + _validate_generator_case(platform, test_case)

    if invalid_count == 0:
        print("✔ All tests are green for platform " + platform)
    else:
        print("✘ There were " + str(invalid_count) + " errors in the tests for platform " + platform)
    return invalid_count


def _validate_project():
    invalid_count = _validate_generator("reactnative")
    return invalid_count


# schema_path = 'bridge-schema.json'
# api_path = 'mobile-bridge-api.json'
# test_folder_path = 'tests/format'
#
# current_path = os.path.abspath(os.path.dirname(__file__))
# test_file_names = [f for f in os.listdir(test_folder_path) if f.endswith(".json")]
#
# with open(schema_path) as file_object:
#     schema = json.load(file_object)
#     resolver = jsonschema.RefResolver(base_uri='file://' + current_path + '/', referrer=schema)
#
#     for test_file_name in test_file_names:
#         test_file_path = test_folder_path + "/" + test_file_name
#         _validate_file(test_file_path, schema, resolver)
#
#     _validate_file(api_path, schema, resolver)


if __name__ == "__main__":
    sys.exit(_validate_project())
