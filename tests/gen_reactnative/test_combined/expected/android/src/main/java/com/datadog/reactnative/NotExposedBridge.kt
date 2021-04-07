/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.DdBridge
import com.datadog.android.bridge.NotExposedBridge as SDKNotExposedBridge
import com.facebook.react.bridge.Promise
import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.bridge.ReactContextBaseJavaModule
import com.facebook.react.bridge.ReactMethod
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap

/**
 * An interface to test exclusion
 */
class NotExposedBridge(reactContext: ReactApplicationContext) : ReactContextBaseJavaModule(reactContext) {

    private val nativeInstance: SDKNotExposedBridge = DdBridge.getNotExposedBridge(reactContext)

    override fun getName(): String = "NotExposedBridge"

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

}
