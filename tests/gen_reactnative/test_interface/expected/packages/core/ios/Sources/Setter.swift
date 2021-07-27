/*
 * Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.
 * This product includes software developed at Datadog (https://www.datadoghq.com/).
 * Copyright 2016-Present Datadog, Inc.
 */

import Foundation
import DatadogSDKBridge

@objc(Setter)
class RNSetter: NSObject {

    @objc(requiresMainQueueSetup)
    static func requiresMainQueueSetup() -> Bool {
        return false
    }

    let nativeInstance: Setter = Bridge.getSetter()

    @objc(methodQueue)
    let methodQueue: DispatchQueue = sharedQueue

    @objc(setBoolean:withResolver:withRejecter:)
    func setBoolean(value: Bool, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setBoolean(value: value)
        resolve(nil)
    }

    @objc(setLong:withResolver:withRejecter:)
    func setLong(value: Int64, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setLong(value: value)
        resolve(nil)
    }

    @objc(setDouble:withResolver:withRejecter:)
    func setDouble(value: Double, resolve:RCTPromiseResolveBlock, reject:RCTPromiseRejectBlock) -> Void {
        nativeInstance.setDouble(value: value)
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
