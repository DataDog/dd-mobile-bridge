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

#### DdLogs

The entry point to use Datadog's Logs feature.

- `debug(message: string, context: map)`

    Send a log with level debug.

    - `message`: The message to send.
    - `context`: The additional context to send.

- `info(message: string, context: map)`

    Send a log with level info.

    - `message`: The message to send.
    - `context`: The additional context to send.

- `warn(message: string, context: map)`

    Send a log with level warn.

    - `message`: The message to send.
    - `context`: The additional context to send.

- `error(message: string, context: map)`

    Send a log with level error.

    - `message`: The message to send.
    - `context`: The additional context to send.

#### DdTrace

The entry point to use Datadog's Trace feature.

- `startSpan(operation: string, timestampMs: long, context: map)`

    Start a span, and returns a unique identifier for the span.

    - `operation`: The operation name of the span.
    - `timestampMs`: The timestamp when the operation started (in milliseconds).
    - `context`: The additional context to send.

- `finishSpan(spanId: string, timestampMs: long, context: map)`

    Finish a started span.

    - `spanId`: The unique identifier of the span.
    - `timestampMs`: The timestamp when the operation stopped (in milliseconds).
    - `context`: The additional context to send.

#### DdRum

The entry point to use Datadog's RUM feature.

- `startView(key: string, name: string, timestampMs: long, context: map)`

    Start tracking a RUM View.

    - `key`: The view unique key identifier.
    - `name`: The view name.
    - `timestampMs`: The timestamp when the view started (in milliseconds).
    - `context`: The additional context to send.

- `stopView(key: string, timestampMs: long, context: map)`

    Stop tracking a RUM View.

    - `key`: The view unique key identifier.
    - `timestampMs`: The timestamp when the view stopped (in milliseconds).
    - `context`: The additional context to send.

- `startAction(type: string, name: string, timestampMs: long, context: map)`

    Start tracking a RUM Action.

    - `type`: The action type (tap, scroll, swipe, click, custom).
    - `name`: The action name.
    - `timestampMs`: The timestamp when the action started (in milliseconds).
    - `context`: The additional context to send.

- `stopAction(timestampMs: long, context: map)`

    Stop tracking the ongoing RUM Action.

    - `timestampMs`: The timestamp when the action stopped (in milliseconds).
    - `context`: The additional context to send.

- `addAction(type: string, name: string, timestampMs: long, context: map)`

    Add a RUM Action.

    - `type`: The action type (tap, scroll, swipe, click, custom).
    - `name`: The action name.
    - `timestampMs`: The timestamp when the action occurred (in milliseconds).
    - `context`: The additional context to send.

- `startResource(key: string, method: string, url: string, timestampMs: long, context: map)`

    Start tracking a RUM Resource.

    - `key`: The resource unique key identifier.
    - `method`: The resource method (GET, POST, …).
    - `url`: The resource url.
    - `timestampMs`: The timestamp when the resource started (in milliseconds).
    - `context`: The additional context to send.

- `stopResource(key: string, statusCode: long, kind: string, timestampMs: long, context: map)`

    Stop tracking a RUM Resource.

    - `key`: The resource unique key identifier.
    - `statusCode`: The resource status code.
    - `kind`: The resource's kind (xhr, document, image, css, font, …).
    - `timestampMs`: The timestamp when the resource stopped (in milliseconds).
    - `context`: The additional context to send.

- `addError(message: string, source: string, stacktrace: string, timestampMs: long, context: map)`

    Add a RUM Error.

    - `message`: The error message.
    - `source`: The error source (network, source, console, logger, …).
    - `stacktrace`: The error stacktrace.
    - `timestampMs`: The timestamp when the error occurred (in milliseconds).
    - `context`: The additional context to send.

## Data structures

#### DdSdkConfiguration

A configuration object to initialize Datadog's features.

- `clientToken` (string): A valid Datadog client token.
- `env` (string): The application’s environment, for example: prod, pre-prod, staging, etc.
- `applicationId` (string): The RUM application ID.
- `sampleRate` (double): The sample rate (between 0 and 100) of RUM sessions kept.

