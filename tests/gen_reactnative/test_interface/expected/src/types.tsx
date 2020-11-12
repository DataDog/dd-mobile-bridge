/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

/**
 * An interface to test return types
 */
export type GetterType = {
  /**
   * Empty method, returns void
   */
  emptyMethod(): Promise<void>;

  /**
   * Empty method, returns int
   */
  getBoolean(): Promise<boolean>;

  /**
   * Empty method, returns int
   */
  getInt(): Promise<number>;

  /**
   * Empty method, returns float
   */
  getFloat(): Promise<number>;

  /**
   * Empty method, returns string
   */
  getString(): Promise<string>;

  /**
   * Empty method, returns map
   */
  getMap(): Promise<object>;

  /**
   * Empty method, returns list
   */
  getList(): Promise<array>;

};

/**
 * An interface to test setting types
 */
export type SetterType = {
  /**
   * Empty method, boolean param, returns void
   * value: A boolean param
   */
  setBoolean(value: boolean): Promise<void>;

  /**
   * Empty method, int param, returns void
   * value: An int param
   */
  setInt(value: number): Promise<void>;

  /**
   * Empty method, float param, returns void
   * value: A float param
   */
  setFloat(value: number): Promise<void>;

  /**
   * Empty method, string param, returns void
   * value: A string param
   */
  setString(value: string): Promise<void>;

  /**
   * Empty method, map param, returns void
   * value: A map param
   */
  setMap(value: object): Promise<void>;

  /**
   * Empty method, list param, returns void
   * value: A list param
   */
  setList(value: array): Promise<void>;

};

