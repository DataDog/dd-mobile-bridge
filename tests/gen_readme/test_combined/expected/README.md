# dd-mobile-bridge

JSON description of mobile bridges used by cross-platform or hybrid mobile frameworks (React Native, Xamarin, …)

## Bridge API

### Interfaces

#### BridgeWithData

An interface to test transferring complex types

- `setData(value: ComplexDataStructure)`

    Empty method, ComplexDataStructure param, returns void

    - `value`: A ComplexDataStructure param

- `getData()`

    Empty method, returns ComplexDataStructure


### Data structures

#### ComplexDataStructure

A data structure to test data transfer through the bridge

- `someInt` (int): A mandatory int property
- `someString` (string): An optional string property
- `someMap` (map): A mandatory map property

