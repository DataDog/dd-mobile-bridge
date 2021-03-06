/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import { NativeModules } from 'react-native';
import { GetterType, SetterType } from './types';

const Getter: GetterType = NativeModules.Getter;
const Setter: SetterType = NativeModules.Setter;

export { Getter, Setter };
