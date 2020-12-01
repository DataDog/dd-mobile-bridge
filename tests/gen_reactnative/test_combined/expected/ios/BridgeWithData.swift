/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation
import Datadog

@objc(BridgeWithData)
class RNBridgeWithData: NSObject {

    let nativeInstance: BridgeWithData = Bridge.getBridgeWithData()

    @objc(setData:withResolver:withRejecter:)
    func setData(value: NSDictionary, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setData(value: value.asComplexDataStructure())
        resolve(nil)
    }

    @objc(getDatawithResolver:withRejecter:)
    func getData(resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        let result = nativeInstance.getData()
        resolve(result)
    }

}
