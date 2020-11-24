/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

/**
   An interface to test return types
 */
@objc(Getter)
protocol Getter {

    /**
       Empty method, returns void
     */
    func emptyMethod() -> Void

    /**
       Empty method, returns boolean
     */
    func getBoolean() -> Bool

    /**
       Empty method, returns long
     */
    func getLong() -> Int64

    /**
       Empty method, returns double
     */
    func getDouble() -> Double

    /**
       Empty method, returns string
     */
    func getString() -> String

    /**
       Empty method, returns map
     */
    func getMap() -> Dictionary<String, Any?>

    /**
       Empty method, returns list
     */
    func getList() -> Array<Any?>

}
