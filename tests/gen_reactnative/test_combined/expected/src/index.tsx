/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import { NativeModules } from 'react-native';
import { ComplexDataStructure, BridgeWithDataType } from './types';

console.log("index.tsx was re-generated; make sure you include any missing code")

const BridgeWithData: BridgeWithDataType = NativeModules.BridgeWithData;

export { ComplexDataStructure, BridgeWithData };
