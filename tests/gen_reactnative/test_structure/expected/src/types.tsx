/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

/**
 * A data structure to test data transfer through the bridge
 */
export class DataStructure {
  constructor(
    readonly someBoolean: boolean,
    readonly someLong: number,
    readonly someDouble: number,
    readonly someString: string,
    readonly someList: array,
    readonly someMap: object
  ) {}
}

/**
 * A data structure to test data transfer with optional properties
 */
export class DataStructureOptional {
  constructor(
    readonly someBoolean: boolean,
    readonly someLong: number,
    readonly someDouble: number,
    readonly someString: string,
    readonly someList: array,
    readonly someMap: object
  ) {}
}

