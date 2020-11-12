/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.android.bridge

import android.content.Context

/**
 * An interface to test transferring complex types
 */
class BridgeWithData(context: Context) {

    private val appContext = context.applicationContext

    /**
     * Empty method, ComplexDataStructure param, returns void
     */
    fun setData(value: ComplexDataStructure): Unit {
        TODO()
    }

    /**
     * Empty method, returns ComplexDataStructure
     */
    fun getData(): ComplexDataStructure {
        TODO()
    }

}
