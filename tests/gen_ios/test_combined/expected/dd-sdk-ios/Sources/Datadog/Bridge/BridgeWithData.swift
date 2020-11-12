/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

/**
   An interface to test transferring complex types
 */
@objc(BridgeWithData)
class BridgeWithData: NSObject {

    /**
       Empty method, ComplexDataStructure param, returns void
     */
    func setData(value: ComplexDataStructure) -> Void {
        // TODO
    }

    /**
       Empty method, returns ComplexDataStructure
     */
    func getData() -> ComplexDataStructure {
        // TODO
    }

}
