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
struct DataStructureOptional{
    var someBoolean: Bool? = nil
    var someLong: Int64? = nil
    var someDouble: Double? = nil
    var someString: String? = nil
    var someList: Array<Any?>? = nil
    var someMap: Dictionary<String, Any?>? = nil
}
