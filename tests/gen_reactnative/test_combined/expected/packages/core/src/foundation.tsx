/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import { NativeModules } from 'react-native';
import { ComplexDataStructure, NotExposedDataStructure, NotExposedBridgeType, BridgeWithDataType } from './types';

const NotExposedBridge: NotExposedBridgeType = NativeModules.NotExposedBridge;
const BridgeWithData: BridgeWithDataType = NativeModules.BridgeWithData;

export { ComplexDataStructure, NotExposedDataStructure, NotExposedBridge, BridgeWithData };
