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
interface Setter {

    /**
     * Empty method, boolean param, returns void
     */
    fun setBoolean(value: Boolean): Unit

    /**
     * Empty method, long param, returns void
     */
    fun setLong(value: Long): Unit

    /**
     * Empty method, double param, returns void
     */
    fun setDouble(value: Double): Unit

    /**
     * Empty method, string param, returns void
     */
    fun setString(value: String): Unit

    /**
     * Empty method, map param, returns void
     */
    fun setMap(value: Map<String, Any?>): Unit

    /**
     * Empty method, list param, returns void
     */
    fun setList(value: List<Any?>): Unit

}
