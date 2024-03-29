/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.DdBridge
import com.datadog.android.bridge.BridgeWithData as SDKBridgeWithData
import com.facebook.react.bridge.Promise
import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.bridge.ReactContextBaseJavaModule
import com.facebook.react.bridge.ReactMethod
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap

/**
 * An interface to test transferring complex types
 */
class BridgeWithData(reactContext: ReactApplicationContext) : ReactContextBaseJavaModule(reactContext) {

    private val nativeInstance: SDKBridgeWithData = DdBridge.getBridgeWithData(reactContext)

    override fun getName(): String = "BridgeWithData"

    /**
     * Empty method, ComplexDataStructure param, returns void
     * @param value A ComplexDataStructure param
     */
    @ReactMethod
    fun setData(value: ReadableMap, promise: Promise) {
        nativeInstance.setData(value.asComplexDataStructure())
        promise.resolve(null)
    }

    /**
     * Empty method, returns ComplexDataStructure
     */
    @ReactMethod
    fun getData(promise: Promise) {
        val result = nativeInstance.getData()
        promise.resolve(result.toReadableMap())
    }

    /**
     * Empty method, optional long param, returns void
     * @param value An optional long param
     */
    @ReactMethod
    fun setTimestamp(value: Double, promise: Promise) {
        nativeInstance.setTimestamp(value.toLong())
        promise.resolve(null)
    }

}
