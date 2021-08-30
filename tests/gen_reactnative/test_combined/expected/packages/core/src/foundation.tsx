/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import { NativeModules } from 'react-native';
import { ComplexDataStructure, NotExposedDataStructure, NotExposedBridgeType, BridgeWithDataType } from './types';

class BridgeWithDataWrapper implements BridgeWithDataType {

  private nativeBridgeWithData: BridgeWithDataType = NativeModules.BridgeWithData;

  setData(value: ComplexDataStructure): Promise<void> {
    return this.nativeBridgeWithData.setData(value);
  }

  getData(): Promise<ComplexDataStructure> {
    return this.nativeBridgeWithData.getData();
  }

  setTimestamp(value: number = Date.now()): Promise<void> {
    return this.nativeBridgeWithData.setTimestamp(value);
  }

}

const NotExposedBridge: NotExposedBridgeType = NativeModules.NotExposedBridge;
const BridgeWithData: BridgeWithDataType = new BridgeWithDataWrapper();

export { ComplexDataStructure, NotExposedDataStructure, NotExposedBridge, BridgeWithData };
