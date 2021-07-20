/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

/**
 * A data structure to test data transfer through the bridge
 */
export class ComplexDataStructure {
  constructor(
    readonly someLong: number,
    readonly someString: string,
    readonly someMap: object
  ) {}
}

/**
 * A data structure test exclusion
 */
export class NotExposedDataStructure {
  constructor(
    readonly someLong: number,
    readonly someString: string,
    readonly someMap: object
  ) {}
}

/**
 * An interface to test exclusion
 */
export type NotExposedBridgeType = {
  /**
   * Empty method, ComplexDataStructure param, returns void
   * @param value: A ComplexDataStructure param
   */
  setData(value: ComplexDataStructure): Promise<void>;

  /**
   * Empty method, returns ComplexDataStructure
   */
  getData(): Promise<ComplexDataStructure>;

};

/**
 * An interface to test transferring complex types
 */
export type BridgeWithDataType = {
  /**
   * Empty method, ComplexDataStructure param, returns void
   * @param value: A ComplexDataStructure param
   */
  setData(value: ComplexDataStructure): Promise<void>;

  /**
   * Empty method, returns ComplexDataStructure
   */
  getData(): Promise<ComplexDataStructure>;

};

