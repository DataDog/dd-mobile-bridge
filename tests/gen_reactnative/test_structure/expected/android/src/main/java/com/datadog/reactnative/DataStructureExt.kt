/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.reactnative

import com.datadog.android.bridge.DataStructure
import com.facebook.react.bridge.ReadableArray
import com.facebook.react.bridge.ReadableMap
import com.facebook.react.bridge.WritableNativeMap

fun ReadableMap.asDataStructure(): DataStructure{
    return DataStructure(
        someBoolean = getBoolean("someBoolean"),
        someInt = getInt("someInt"),
        someFloat = getDouble("someFloat").toFloat(),
        someString = getString("someString").orEmpty(),
        someList = getArray("someList")?.toArrayList()!!,
        someMap = getMap("someMap")?.toHashMap()!!
    )
}

fun DataStructure.toReadableMap(): WritableNativeMap {
    val map = WritableNativeMap()
    map.putBoolean("someBoolean", someBoolean)
    map.putInt("someInt", someInt)
    map.putDouble("someFloat", someFloat.toDouble())
    map.putString("someString", someString)
    map.putArray("someList", someList.toWritableArray())
    map.putMap("someMap", someMap.toWritableMap())
    return map
}
