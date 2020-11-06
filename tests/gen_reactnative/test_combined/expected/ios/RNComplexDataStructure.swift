/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

extension NSDictionary {

    func asComplexDataStructure() -> ComplexDataStructure {
        let someInt = object(forKey: "someInt") as? NSInteger
        let someString = object(forKey: "someString") as? NSString
        let someMap = object(forKey: "someMap") as? NSDictionary
        return ComplexDataStructure(
            someInt: (someInt != nil) ? someInt! : 0,
            someString: someString,
            someMap: (someMap != nil) ? someMap! : NSDictionary()
        )
    }
}
