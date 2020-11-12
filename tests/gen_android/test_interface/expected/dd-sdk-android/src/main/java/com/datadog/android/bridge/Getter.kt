/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

package com.datadog.android.bridge

import android.content.Context

/**
 * An interface to test return types
 */
class Getter(context: Context) {

    private val appContext = context.applicationContext

    /**
     * Empty method, returns void
     */
    fun emptyMethod(): Unit {
        TODO()
    }

    /**
     * Empty method, returns int
     */
    fun getBoolean(): Boolean {
        TODO()
    }

    /**
     * Empty method, returns int
     */
    fun getInt(): Int {
        TODO()
    }

    /**
     * Empty method, returns float
     */
    fun getFloat(): Float {
        TODO()
    }

    /**
     * Empty method, returns string
     */
    fun getString(): String {
        TODO()
    }

    /**
     * Empty method, returns map
     */
    fun getMap(): Map<String, Any?> {
        TODO()
    }

    /**
     * Empty method, returns list
     */
    fun getList(): List<Any?> {
        TODO()
    }

}
