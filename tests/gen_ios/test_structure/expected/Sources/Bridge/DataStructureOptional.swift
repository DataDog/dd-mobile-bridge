/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

/**
 A data structure to test data transfer with optional properties
 - Parameters:
     - someBoolean: An optional boolean property
     - someLong: An optional long property
     - someDouble: An optional double property
     - someString: An optional string property
     - someList: An optional list property
     - someMap: An optional map property
 */
@objc(DataStructureOptional)
public class DataStructureOptional: NSObject{
    public var someBoolean: Bool? = nil
    public var someLong: Int64? = nil
    public var someDouble: Double? = nil
    public var someString: NSString? = nil
    public var someList: NSArray? = nil
    public var someMap: NSDictionary? = nil

    public init(
        someBoolean: Bool?,
        someLong: Int64?,
        someDouble: Double?,
        someString: NSString?,
        someList: NSArray?,
        someMap: NSDictionary?
    ) {
        self.someBoolean = someBoolean
        self.someLong = someLong
        self.someDouble = someDouble
        self.someString = someString
        self.someList = someList
        self.someMap = someMap
    }
}
