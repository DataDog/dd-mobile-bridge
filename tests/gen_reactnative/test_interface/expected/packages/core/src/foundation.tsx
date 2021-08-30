/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import { NativeModules } from 'react-native';
import { GetterType, SetterType } from './types';

class SetterWrapper implements SetterType {

  private nativeSetter: SetterType = NativeModules.Setter;

  setBoolean(value: boolean): Promise<void> {
    return this.nativeSetter.setBoolean(value);
  }

  setLong(value: number): Promise<void> {
    return this.nativeSetter.setLong(value);
  }

  setDouble(value: number): Promise<void> {
    return this.nativeSetter.setDouble(value);
  }

  setString(value: string): Promise<void> {
    return this.nativeSetter.setString(value);
  }

  setMap(value: object): Promise<void> {
    return this.nativeSetter.setMap(value);
  }

  setList(value: Array<any>): Promise<void> {
    return this.nativeSetter.setList(value);
  }

  setTimestamp(value: number = Date.now()): Promise<void> {
    return this.nativeSetter.setTimestamp(value);
  }

}

const Getter: GetterType = NativeModules.Getter;
const Setter: SetterType = new SetterWrapper();

export { Getter, Setter };
