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
interface Getter {

    /**
     * Empty method, returns void
     */
    fun emptyMethod(): Unit

    /**
     * Empty method, returns boolean
     */
    fun getBoolean(): Boolean

    /**
     * Empty method, returns long
     */
    fun getLong(): Long

    /**
     * Empty method, returns double
     */
    fun getDouble(): Double

    /**
     * Empty method, returns string
     */
    fun getString(): String

    /**
     * Empty method, returns map
     */
    fun getMap(): Map<String, Any?>

    /**
     * Empty method, returns list
     */
    fun getList(): List<Any?>

}
