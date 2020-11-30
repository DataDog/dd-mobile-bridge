/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

/**
 A data structure to test data transfer through the bridge
 - Parameters:
     - someBoolean: A mandatory boolean property
     - someLong: A mandatory long property
     - someDouble: A mandatory double property
     - someString: A mandatory string property
     - someList: A mandatory list property
     - someMap: A mandatory map property
 */
@objc(DataStructure)
public class DataStructure: NSObject{
    public var someBoolean: Bool = false
    public var someLong: Int64 = 0
    public var someDouble: Double = 0.0
    public var someString: NSString = ""
    public var someList: NSArray = NSArray()
    public var someMap: NSDictionary = NSDictionary()

    public init(
        someBoolean: Bool,
        someLong: Int64,
        someDouble: Double,
        someString: NSString,
        someList: NSArray,
        someMap: NSDictionary
    ) {
        self.someBoolean = someBoolean
        self.someLong = someLong
        self.someDouble = someDouble
        self.someString = someString
        self.someList = someList
        self.someMap = someMap
    }
}
