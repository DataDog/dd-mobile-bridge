/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.android.bridge

/**
 * A data structure to test data transfer through the bridge
 * @param someLong A mandatory long property
 * @param someString An optional string property
 * @param someMap A mandatory map property
 */
data class ComplexDataStructure(
    val someLong: Long,
    val someString: String? = null,
    val someMap: Map<String, Any?>
)
