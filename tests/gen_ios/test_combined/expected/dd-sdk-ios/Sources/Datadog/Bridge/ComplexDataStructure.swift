/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

/**
 A data structure to test data transfer through the bridge
 - Parameters:
     - someLong: A mandatory long property
     - someString: An optional string property
     - someMap: A mandatory map property
 */
struct ComplexDataStructure{
    let someLong: Int64
    var someString: String? = nil
    let someMap: Dictionary<String, Any?>
}
