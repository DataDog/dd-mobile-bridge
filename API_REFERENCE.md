# Bridge API Reference

## Interfaces

#### DdSdk

The entry point to initialize Datadog's features.

- `initialize(configuration: DdSdkConfiguration)`

    Initializes Datadog's features.

    - `configuration`: The configuration to use.

- `setAttributes(attributes: map)`

    Sets the global context (set of attributes) attached with all future Logs, Spans and RUM events.

    - `attributes`: The global context attributes.

- `setUser(user: map)`

    Set the user information.

    - `user`: The user object (use builtin attributes: 'id', 'email', 'name', and/or any custom attribute).

- `setTrackingConsent(trackingConsent: string)`

    Set the tracking consent regarding the data collection.

    - `trackingConsent`: Consent, which can take one of the following values: 'pending', 'granted', 'not_granted'.

#### DdLogs

The entry point to use Datadog's Logs feature.

- `debug(message: string, context: map)`

    Send a log with level debug.

    - `message`: The message to send.
    - `context`: Optional. The additional context to send.

- `info(message: string, context: map)`

    Send a log with level info.

    - `message`: The message to send.
    - `context`: Optional. The additional context to send.

- `warn(message: string, context: map)`

    Send a log with level warn.

    - `message`: The message to send.
    - `context`: Optional. The additional context to send.

- `error(message: string, context: map)`

    Send a log with level error.

    - `message`: The message to send.
    - `context`: Optional. The additional context to send.

#### DdTrace

The entry point to use Datadog's Trace feature.

- `startSpan(operation: string, context: map, timestampMs: long)`

    Start a span, and returns a unique identifier for the span.

    - `operation`: The operation name of the span.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the operation started (in milliseconds). If not provided, current timestamp will be used.

- `finishSpan(spanId: string, context: map, timestampMs: long)`

    Finish a started span.

    - `spanId`: The unique identifier of the span.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the operation stopped (in milliseconds). If not provided, current timestamp will be used.

#### DdRum

The entry point to use Datadog's RUM feature.

- `startView(key: string, name: string, context: map, timestampMs: long)`

    Start tracking a RUM View.

    - `key`: The view unique key identifier.
    - `name`: The view name.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the view started (in milliseconds). If not provided, current timestamp will be used.

- `stopView(key: string, context: map, timestampMs: long)`

    Stop tracking a RUM View.

    - `key`: The view unique key identifier.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the view stopped (in milliseconds). If not provided, current timestamp will be used.

- `startAction(type: string, name: string, context: map, timestampMs: long)`

    Start tracking a RUM Action.

    - `type`: The action type (tap, scroll, swipe, click, custom).
    - `name`: The action name.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the action started (in milliseconds). If not provided, current timestamp will be used.

- `stopAction(context: map, timestampMs: long)`

    Stop tracking the ongoing RUM Action.

    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the action stopped (in milliseconds). If not provided, current timestamp will be used.

- `addAction(type: string, name: string, context: map, timestampMs: long)`

    Add a RUM Action.

    - `type`: The action type (tap, scroll, swipe, click, custom).
    - `name`: The action name.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the action occurred (in milliseconds). If not provided, current timestamp will be used.

- `startResource(key: string, method: string, url: string, context: map, timestampMs: long)`

    Start tracking a RUM Resource.

    - `key`: The resource unique key identifier.
    - `method`: The resource method (GET, POST, …).
    - `url`: The resource url.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the resource started (in milliseconds). If not provided, current timestamp will be used.

- `stopResource(key: string, statusCode: long, kind: string, size: long, context: map, timestampMs: long)`

    Stop tracking a RUM Resource.

    - `key`: The resource unique key identifier.
    - `statusCode`: The resource status code.
    - `kind`: The resource's kind (xhr, document, image, css, font, …).
    - `size`: Optional. The resource size in bytes.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the resource stopped (in milliseconds). If not provided, current timestamp will be used.

- `addError(message: string, source: string, stacktrace: string, context: map, timestampMs: long)`

    Add a RUM Error.

    - `message`: The error message.
    - `source`: The error source (network, source, console, logger, …).
    - `stacktrace`: The error stacktrace.
    - `context`: Optional. The additional context to send.
    - `timestampMs`: Optional. The timestamp when the error occurred (in milliseconds). If not provided, current timestamp will be used.

- `addTiming(name: string)`

    Adds a specific timing in the active View. The timing duration will be computed as the difference between the time the View was started and the time this function was called.

    - `name`: The name of the new custom timing attribute. Timings can be nested up to 8 levels deep. Names using more than 8 levels will be sanitized by SDK.

## Data structures

#### DdSdkConfiguration

A configuration object to initialize Datadog's features.

- `clientToken` (string): A valid Datadog client token.
- `env` (string): The application’s environment, for example: prod, pre-prod, staging, etc.
- `applicationId` (string): The RUM application ID.
- `nativeCrashReportEnabled` (boolean): Whether the SDK should track native (pure iOS or pure Android) crashes (default is false).
- `sampleRate` (double): The sample rate (between 0 and 100) of RUM sessions kept.
- `site` (string): The Datadog site of your organization (can be 'US1', 'US1_FED', 'US3', 'US5', or 'EU1', default is 'US1').
- `trackingConsent` (string): Consent, which can take one of the following values: 'pending', 'granted', 'not_granted'.
- `additionalConfig` (map): Additional configuration parameters.

