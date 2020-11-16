/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

/**
   An interface to test setting types
 */
@objc(Setter)
protocol Setter {

    /**
       Empty method, boolean param, returns void
     */
    func setBoolean(value: Bool) -> Void

    /**
       Empty method, int param, returns void
     */
    func setInt(value: Int) -> Void

    /**
       Empty method, float param, returns void
     */
    func setFloat(value: Float) -> Void

    /**
       Empty method, string param, returns void
     */
    func setString(value: String) -> Void

    /**
       Empty method, map param, returns void
     */
    func setMap(value: Dictionary<String, Any?>) -> Void

    /**
       Empty method, list param, returns void
     */
    func setList(value: Array<Any?>) -> Void

}
