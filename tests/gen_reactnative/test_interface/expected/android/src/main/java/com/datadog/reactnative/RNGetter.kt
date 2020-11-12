/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.Getter
import com.facebook.react.bridge.Promise
import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.bridge.ReactContextBaseJavaModule
import com.facebook.react.bridge.ReactMethod
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap

/**
 * An interface to test return types
 */
class RNGetter(reactContext: ReactApplicationContext) : ReactContextBaseJavaModule(reactContext) {

    private val nativeInstance: Getter = Getter(reactContext)

    override fun getName(): String = "Getter"

    /**
     * Empty method, returns void
     */
    @ReactMethod
    fun emptyMethod(promise: Promise) {
        nativeInstance.emptyMethod()
        promise.resolve(null)
    }

    /**
     * Empty method, returns int
     */
    @ReactMethod
    fun getBoolean(promise: Promise) {
                val result = nativeInstance.getBoolean()
        promise.resolve(result)
    }

    /**
     * Empty method, returns int
     */
    @ReactMethod
    fun getInt(promise: Promise) {
                val result = nativeInstance.getInt()
        promise.resolve(result)
    }

    /**
     * Empty method, returns float
     */
    @ReactMethod
    fun getFloat(promise: Promise) {
                val result = nativeInstance.getFloat()
        promise.resolve(result)
    }

    /**
     * Empty method, returns string
     */
    @ReactMethod
    fun getString(promise: Promise) {
                val result = nativeInstance.getString()
        promise.resolve(result)
    }

    /**
     * Empty method, returns map
     */
    @ReactMethod
    fun getMap(promise: Promise) {
                val result = nativeInstance.getMap()
        promise.resolve(result.toWritableMap())
    }

    /**
     * Empty method, returns list
     */
    @ReactMethod
    fun getList(promise: Promise) {
                val result = nativeInstance.getList()
        promise.resolve(result.toWritableArray())
    }

}
