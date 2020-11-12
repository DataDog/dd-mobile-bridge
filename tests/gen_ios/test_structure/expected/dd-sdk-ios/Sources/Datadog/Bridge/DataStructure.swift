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
     - someInt: A mandatory int property
     - someFloat: A mandatory float property
     - someString: A mandatory string property
     - someList: A mandatory list property
     - someMap: A mandatory map property
 */
struct DataStructure{
    let someBoolean: Bool,
    let someInt: Int,
    let someFloat: Float,
    let someString: NSString,
    let someList: NSArray,
    let someMap: NSDictionary
}
