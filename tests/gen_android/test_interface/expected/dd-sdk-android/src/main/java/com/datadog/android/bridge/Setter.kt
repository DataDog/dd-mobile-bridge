/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.android.bridge

import android.content.Context

/**
 * An interface to test setting types
 */
class Setter(context: Context) {

    private val appContext = context.applicationContext

    /**
     * Empty method, boolean param, returns void
     */
    fun setBoolean(value: Boolean): Unit {
        TODO()
    }

    /**
     * Empty method, int param, returns void
     */
    fun setInt(value: Int): Unit {
        TODO()
    }

    /**
     * Empty method, float param, returns void
     */
    fun setFloat(value: Float): Unit {
        TODO()
    }

    /**
     * Empty method, string param, returns void
     */
    fun setString(value: String): Unit {
        TODO()
    }

    /**
     * Empty method, map param, returns void
     */
    fun setMap(value: Map<String, Any?>): Unit {
        TODO()
    }

    /**
     * Empty method, list param, returns void
     */
    fun setList(value: List<Any?>): Unit {
        TODO()
    }

}
