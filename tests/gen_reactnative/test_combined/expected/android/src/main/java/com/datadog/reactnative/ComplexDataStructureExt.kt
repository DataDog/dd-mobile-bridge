/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.ComplexDataStructure
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap
import com.facebook.react.bridge.WritableNativeMap

fun ReadableMap.asComplexDataStructure(): ComplexDataStructure{
    return ComplexDataStructure(
        someLong = getDouble("someLong").toLong(),
        someString = getString("someString"),
        someMap = getMap("someMap")?.toHashMap()!!
    )
}

fun ComplexDataStructure.toReadableMap(): WritableNativeMap {
    val map = WritableNativeMap()
    map.putDouble("someLong", someLong.toDouble())
    if (someString != null) map.putString("someString", someString)
    map.putMap("someMap", someMap.toWritableMap())
    return map
}
