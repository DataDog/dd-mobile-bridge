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
   * Empty method, returns boolean
   */
  getBoolean(): Promise<boolean>;

  /**
   * Empty method, returns long
   */
  getLong(): Promise<number>;

  /**
   * Empty method, returns double
   */
  getDouble(): Promise<number>;

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
  getList(): Promise<Array<any>>;

};

/**
 * An interface to test setting types
 */
export type SetterType = {
  /**
   * Empty method, boolean param, returns void
   * @param value: A boolean param
   */
  setBoolean(value: boolean): Promise<void>;

  /**
   * Empty method, long param, returns void
   * @param value: A long param
   */
  setLong(value: number): Promise<void>;

  /**
   * Empty method, double param, returns void
   * @param value: A double param
   */
  setDouble(value: number): Promise<void>;

  /**
   * Empty method, string param, returns void
   * @param value: A string param
   */
  setString(value: string): Promise<void>;

  /**
   * Empty method, map param, returns void
   * @param value: A map param
   */
  setMap(value: object): Promise<void>;

  /**
   * Empty method, list param, returns void
   * @param value: A list param
   */
  setList(value: Array<any>): Promise<void>;

  /**
   * Empty method, optional long param, returns void
   * @param value: An optional long param
   */
  setTimestamp(value?: number): Promise<void>;

};

