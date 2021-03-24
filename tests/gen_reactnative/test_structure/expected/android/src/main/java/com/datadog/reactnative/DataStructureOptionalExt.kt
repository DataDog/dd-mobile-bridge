/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.DataStructureOptional
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap
import com.facebook.react.bridge.WritableNativeMap

fun ReadableMap.asDataStructureOptional(): DataStructureOptional {
    return DataStructureOptional(
        someBoolean = getBoolean("someBoolean"),
        someLong = getDouble("someLong").toLong(),
        someDouble = getDouble("someDouble"),
        someString = getString("someString"),
        someList = getArray("someList")?.toArrayList(),
        someMap = getMap("someMap")?.toHashMap()
    )
}

fun DataStructureOptional.toReadableMap(): WritableNativeMap {
    val map = WritableNativeMap()
    someBoolean?.let{ map.putBoolean("someBoolean", it) }
    someLong?.let{ map.putDouble("someLong", it.toDouble()) }
    someDouble?.let{ map.putDouble("someDouble", it) }
    someString?.let{ map.putString("someString", it) }
    someList?.let{ map.putArray("someList", it.toWritableArray()) }
    someMap?.let{ map.putMap("someMap", it.toWritableMap()) }
    return map
}
