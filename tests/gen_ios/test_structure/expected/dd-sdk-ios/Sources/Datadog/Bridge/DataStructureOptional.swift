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
     - someInt: An optional int property
     - someFloat: An optional float property
     - someString: An optional string property
     - someList: An optional list property
     - someMap: An optional map property
 */
struct DataStructureOptional{
    var someBoolean: Bool? = nil,
    var someInt: Int? = nil,
    var someFloat: Float? = nil,
    var someString: NSString? = nil,
    var someList: NSArray? = nil,
    var someMap: NSDictionary? = nil
}
