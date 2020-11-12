/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.android.bridge

/**
 * A data structure to test data transfer through the bridge
 * @param someBoolean A mandatory boolean property
 * @param someInt A mandatory int property
 * @param someFloat A mandatory float property
 * @param someString A mandatory string property
 * @param someList A mandatory list property
 * @param someMap A mandatory map property
 */
data class DataStructure(
    val someBoolean: Boolean,
    val someInt: Int,
    val someFloat: Float,
    val someString: String,
    val someList: List<Any?>,
    val someMap: Map<String, Any?>
)
