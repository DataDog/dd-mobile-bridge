/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.Setter
import com.facebook.react.bridge.Promise
import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.bridge.ReactContextBaseJavaModule
import com.facebook.react.bridge.ReactMethod
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap

/**
 * An interface to test setting types
 */
class RNSetter(reactContext: ReactApplicationContext) : ReactContextBaseJavaModule(reactContext) {

    private val nativeInstance: Setter = Setter(reactContext)

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
     * Empty method, int param, returns void
     * @param value An int param
     */
    @ReactMethod
    fun setInt(value: Int, promise: Promise) {
        nativeInstance.setInt(value)
        promise.resolve(null)
    }

    /**
     * Empty method, float param, returns void
     * @param value A float param
     */
    @ReactMethod
    fun setFloat(value: Float, promise: Promise) {
        nativeInstance.setFloat(value)
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
