/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.android.bridge

/**
 * A data structure to test data transfer with optional properties
 * @param someBoolean An optional boolean property
 * @param someLong An optional long property
 * @param someDouble An optional double property
 * @param someString An optional string property
 * @param someList An optional list property
 * @param someMap An optional map property
 */
data class DataStructureOptional(
    val someBoolean: Boolean? = null,
    val someLong: Long? = null,
    val someDouble: Double? = null,
    val someString: String? = null,
    val someList: List<Any?>? = null,
    val someMap: Map<String, Any?>? = null
)
