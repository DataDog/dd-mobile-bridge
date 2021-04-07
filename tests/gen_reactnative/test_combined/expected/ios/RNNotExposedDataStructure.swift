/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation
import DatadogSDKBridge

extension NSDictionary {

    func asNotExposedDataStructure() -> NotExposedDataStructure {
        let someLong = object(forKey: "someLong") as? Int64
        let someString = object(forKey: "someString") as? NSString
        let someMap = object(forKey: "someMap") as? NSDictionary
        return NotExposedDataStructure(
            someLong: (someLong != nil) ? someLong! : 0,
            someString: someString,
            someMap: (someMap != nil) ? someMap! : NSDictionary()
        )
    }
}
