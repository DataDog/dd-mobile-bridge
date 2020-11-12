/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

@objc(Getter)
class RNGetter: NSObject {

    let nativeInstance = Getter()

    @objc(emptyMethodwithResolver:withRejecter:)
    func emptyMethod(resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.emptyMethod()
        resolve(nil)
    }

    @objc(getBooleanwithResolver:withRejecter:)
    func getBoolean(resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        let result = nativeInstance.getBoolean()
        resolve(result)
    }

    @objc(getIntwithResolver:withRejecter:)
    func getInt(resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        let result = nativeInstance.getInt()
        resolve(result)
    }

    @objc(getFloatwithResolver:withRejecter:)
    func getFloat(resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        let result = nativeInstance.getFloat()
        resolve(result)
    }

    @objc(getStringwithResolver:withRejecter:)
    func getString(resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        let result = nativeInstance.getString()
        resolve(result)
    }

    @objc(getMapwithResolver:withRejecter:)
    func getMap(resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        let result = nativeInstance.getMap()
        resolve(result)
    }

    @objc(getListwithResolver:withRejecter:)
    func getList(resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        let result = nativeInstance.getList()
        resolve(result)
    }

}