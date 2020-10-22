#!/usr/bin/env bash

format='bridge-format.json'
definition='mobile-bridge-api.json'
line='----------------------------------------'

for test in tests/*.json; do
  printf "Validating %s %s " "$test" "${line:${#test}}"
  result=$(python3 validate.py "$test" "$format" 2>&1)
  status=$?
  if [ $status -ne 0 ]
  then
    echo "❌"
    echo "$result"
    exit $status
  else
    echo "✅"
  fi
done


printf "Validating %s %s " "$definition" "${line:${#definition}}"
result=$(python3 validate.py "$test" "$format" 2>&1)
status=$?
if [ $status -ne 0 ]
then
  echo "❌"
  echo "$result"
  exit $status
else
  echo "✅"
fi