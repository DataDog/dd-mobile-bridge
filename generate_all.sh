#!/bin/sh

echo "Generating Readme"
./generator.py -s mobile-bridge-api.json -p readme -o .

echo "Generating Android code"
./generator.py -s mobile-bridge-api.json -p android -o ../dd-bridge-android/

echo "Generating iOS code"
./generator.py -s mobile-bridge-api.json -p ios -o ../dd-bridge-ios/

echo "Generating React Native code"
./generator.py -s mobile-bridge-api.json -p reactnative -o ../dd-sdk-reactnative/

