/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.DdBridge
import com.datadog.android.bridge.Getter as SDKGetter
import com.facebook.react.bridge.Promise
import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.bridge.ReactContextBaseJavaModule
import com.facebook.react.bridge.ReactMethod
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap

/**
 * An interface to test return types
 */
class Getter(reactContext: ReactApplicationContext) : ReactContextBaseJavaModule(reactContext) {

    private val nativeInstance: SDKGetter = DdBridge.getGetter(reactContext)

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
     * Empty method, returns boolean
     */
    @ReactMethod
    fun getBoolean(promise: Promise) {
        val result = nativeInstance.getBoolean()
        promise.resolve(result)
    }

    /**
     * Empty method, returns long
     */
    @ReactMethod
    fun getLong(promise: Promise) {
        val result = nativeInstance.getLong()
        promise.resolve(result.toDouble())
    }

    /**
     * Empty method, returns double
     */
    @ReactMethod
    fun getDouble(promise: Promise) {
        val result = nativeInstance.getDouble()
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
