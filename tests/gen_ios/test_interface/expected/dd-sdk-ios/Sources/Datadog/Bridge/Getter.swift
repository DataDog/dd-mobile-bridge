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
       Empty method, returns int
     */
    func getBoolean() -> Bool

    /**
       Empty method, returns int
     */
    func getInt() -> Int

    /**
       Empty method, returns float
     */
    func getFloat() -> Float

    /**
       Empty method, returns string
     */
    func getString() -> NSString

    /**
       Empty method, returns map
     */
    func getMap() -> NSDictionary

    /**
       Empty method, returns list
     */
    func getList() -> NSArray

}
