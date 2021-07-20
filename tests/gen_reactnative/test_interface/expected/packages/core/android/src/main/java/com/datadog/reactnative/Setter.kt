/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.DdBridge
import com.datadog.android.bridge.Setter as SDKSetter
import com.facebook.react.bridge.Promise
import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.bridge.ReactContextBaseJavaModule
import com.facebook.react.bridge.ReactMethod
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap

/**
 * An interface to test setting types
 */
class Setter(reactContext: ReactApplicationContext) : ReactContextBaseJavaModule(reactContext) {

    private val nativeInstance: SDKSetter = DdBridge.getSetter(reactContext)

    override fun getName(): String = "Setter"

    /**
     * Empty method, boolean param, returns void
     * @param value A boolean param
     */
    @ReactMethod
    fun setBoolean(value: Boolean, promise: Promise) {
        nativeInstance.setBoolean(value)
        promise.resolve(null)
    }

    /**
     * Empty method, long param, returns void
     * @param value A long param
     */
    @ReactMethod
    fun setLong(value: Double, promise: Promise) {
        nativeInstance.setLong(value.toLong())
        promise.resolve(null)
    }

    /**
     * Empty method, double param, returns void
     * @param value A double param
     */
    @ReactMethod
    fun setDouble(value: Double, promise: Promise) {
        nativeInstance.setDouble(value)
        promise.resolve(null)
    }

    /**
     * Empty method, string param, returns void
     * @param value A string param
     */
    @ReactMethod
    fun setString(value: String, promise: Promise) {
        nativeInstance.setString(value)
        promise.resolve(null)
    }

    /**
     * Empty method, map param, returns void
     * @param value A map param
     */
    @ReactMethod
    fun setMap(value: ReadableMap, promise: Promise) {
        nativeInstance.setMap(value.toHashMap())
        promise.resolve(null)
    }

    /**
     * Empty method, list param, returns void
     * @param value A list param
     */
    @ReactMethod
    fun setList(value: ReadableArray, promise: Promise) {
        nativeInstance.setList(value.toArrayList())
        promise.resolve(null)
    }

}
