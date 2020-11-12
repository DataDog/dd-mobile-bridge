/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation

@objc(Setter)
class RNSetter: NSObject {

    let nativeInstance = Setter()

    @objc(setBoolean:withResolver:withRejecter:)
    func setBoolean(value: Bool, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setBoolean(value: value)
        resolve(nil)
    }

    @objc(setInt:withResolver:withRejecter:)
    func setInt(value: NSInteger, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setInt(value: value)
        resolve(nil)
    }

    @objc(setFloat:withResolver:withRejecter:)
    func setFloat(value: Float, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setFloat(value: value)
        resolve(nil)
    }

    @objc(setString:withResolver:withRejecter:)
    func setString(value: NSString, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setString(value: value)
        resolve(nil)
    }

    @objc(setMap:withResolver:withRejecter:)
    func setMap(value: NSDictionary, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setMap(value: value)
        resolve(nil)
    }

    @objc(setList:withResolver:withRejecter:)
    func setList(value: NSArray, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setList(value: value)
        resolve(nil)
    }

}
