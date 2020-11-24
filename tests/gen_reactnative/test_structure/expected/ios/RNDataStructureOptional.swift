/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

extension NSDictionary {

    func asDataStructureOptional() -> DataStructureOptional {
        let someBoolean = object(forKey: "someBoolean") as? Bool
        let someLong = object(forKey: "someLong") as? Int64
        let someDouble = object(forKey: "someDouble") as? Double
        let someString = object(forKey: "someString") as? NSString
        let someList = object(forKey: "someList") as? NSArray
        let someMap = object(forKey: "someMap") as? NSDictionary
        return DataStructureOptional(
            someBoolean: someBoolean,
            someLong: someLong,
            someDouble: someDouble,
            someString: someString,
            someList: someList,
            someMap: someMap
        )
    }
}
