/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.android.bridge

/**
 * A data structure to test data transfer with optional properties
 * @param someBoolean An optional boolean property
 * @param someInt An optional int property
 * @param someFloat An optional float property
 * @param someString An optional string property
 * @param someList An optional list property
 * @param someMap An optional map property
 */
data class DataStructureOptional(
    val someBoolean: Boolean? = null,
    val someInt: Int? = null,
    val someFloat: Float? = null,
    val someString: String? = null,
    val someList: List<Any?>? = null,
    val someMap: Map<String, Any?>? = null
)
